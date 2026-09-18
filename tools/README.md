# Build the community pairing helper

Reading this page installs nothing. In an authorized USB setup, you or your assistant may obtain the specific files below and build the helper locally. No repository clone, automatic installer, root access, or phone access is needed to build it.

**Status:** host build and host tests are recorded in [helper review](../docs/helper-review.md#release-validation). The revised helper still needs an authorized spare-phone test before ordinary onboarding. Follow the [USB procedure](../docs/usb-onboarding.md) and [checklist](../docs/checklist.md); do not jump from a successful build to device ownership.

## Supported build recipe

This recipe was checked on macOS Apple Silicon with Temurin JDK 17.0.18+8 and Python 3.14.3. Use the existing macOS curl, shasum, tar, and unzip utilities. Python is required for private-file validation; if absent, obtain it through the [official Python downloads](https://www.python.org/downloads/macos/) and verify its installer provenance before installation. No pip packages are needed. Other host platforms need separately verified archives and instructions; do not reuse macOS binaries or claim Windows/Linux validation.

Review Google's [Android SDK terms](https://developer.android.com/studio/terms) and the JDK's license before using their archives. No license is silently accepted by a script here.

| Input | Pinned version | Official source |
| --- | --- | --- |
| JDK | Temurin 17.0.18+8, macOS aarch64 | [Adoptium release](https://github.com/adoptium/temurin17-binaries/releases/tag/jdk-17.0.18%2B8) |
| Android API library | Platform 35, revision 2 | [Google archive](https://dl.google.com/android/repository/platform-35_r02.zip) |
| D8 and APK verification tools | Build Tools 35.0.0, macOS | [Google archive](https://dl.google.com/android/repository/build-tools_r35_macosx.zip) |
| ADB | Platform Tools 35.0.2, macOS | [Google archive](https://dl.google.com/android/repository/platform-tools_r35.0.2-darwin.zip) |

The archive hashes are pinned in [build-inputs.sha256](build-inputs.sha256). Google's platform/build-tools archive SHA-1 values were also checked against its [repository metadata](https://dl.google.com/android/repository/repository2-3.xml); the JDK SHA-256 matched Adoptium metadata. SHA-256 values here identify the downloaded bytes, not an independent security audit.

## Obtain and verify inputs

Create a new local build folder outside shared/cloud-sync folders. Set `CORE_WORK` to its absolute path. Keep pairing data in a different private directory. Work in a normal user account, not as root.

This recipe pins source revision [aba76f02ef40d929abfe4053a8b59c5d6d8542e3](https://github.com/bokiko/acurast-onboarding-fixes/tree/aba76f02ef40d929abfe4053a8b59c5d6d8542e3/tools). Read its source and checksum files on GitHub before downloading. Use the same revision for all files; do not substitute a moving branch URL. A repository checksum detects changed bytes, but cannot protect against a malicious revision you chose to trust.

```sh
CORE_REV=aba76f02ef40d929abfe4053a8b59c5d6d8542e3
```

From the new folder, download these files without executing downloaded content. Run one command at a time; stop on an error.

```sh
cd "$CORE_WORK"
curl --fail --location --proto '=https' --proto-redir '=https' "https://raw.githubusercontent.com/bokiko/acurast-onboarding-fixes/$CORE_REV/tools/CoreProvision.java" -o CoreProvision.java
curl --fail --location --proto '=https' --proto-redir '=https' "https://raw.githubusercontent.com/bokiko/acurast-onboarding-fixes/$CORE_REV/tools/check-payload.py" -o check-payload.py
curl --fail --location --proto '=https' --proto-redir '=https' "https://raw.githubusercontent.com/bokiko/acurast-onboarding-fixes/$CORE_REV/tools/source.sha256" -o source.sha256
curl --fail --location --proto '=https' --proto-redir '=https' "https://raw.githubusercontent.com/bokiko/acurast-onboarding-fixes/$CORE_REV/tools/build-inputs.sha256" -o build-inputs.sha256
shasum -a 256 -c source.sha256
```

The files must match the checksums you reviewed on GitHub. Then obtain the tool archives:

```sh
curl --fail --location --proto '=https' --proto-redir '=https' 'https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.18%2B8/OpenJDK17U-jdk_aarch64_mac_hotspot_17.0.18_8.tar.gz' -o jdk.tar.gz
curl --fail --location --proto '=https' --proto-redir '=https' https://dl.google.com/android/repository/platform-35_r02.zip -o platform-35_r02.zip
curl --fail --location --proto '=https' --proto-redir '=https' https://dl.google.com/android/repository/build-tools_r35_macosx.zip -o build-tools_r35_macosx.zip
curl --fail --location --proto '=https' --proto-redir '=https' https://dl.google.com/android/repository/platform-tools_r35.0.2-darwin.zip -o platform-tools_r35.0.2-darwin.zip
shasum -a 256 -c build-inputs.sha256
```

Every entry must report OK. Only after all hashes match:

```sh
mkdir jdk sdk classes
tar -xzf jdk.tar.gz -C jdk
unzip -q platform-35_r02.zip -d sdk
unzip -q build-tools_r35_macosx.zip -d sdk
unzip -q platform-tools_r35.0.2-darwin.zip -d sdk
CORE_JAVA="$CORE_WORK/jdk/jdk-17.0.18+8/Contents/Home"
CORE_ANDROID="$CORE_WORK/sdk/android-35/android.jar"
CORE_D8="$CORE_WORK/sdk/android-15/lib/d8.jar"
CORE_ADB="$CORE_WORK/sdk/platform-tools/adb"
"$CORE_JAVA/bin/java" -version
```

The build-tools archive's directory is named **android-15**, despite its package revision being **35.0.0**. Confirm sdk/android-15/source.properties says Pkg.Revision=35.0.0 and sdk/android-35/source.properties says API 35 / revision 2. Do not rename a different version to make the path match.

## Compile and dex

```sh
"$CORE_JAVA/bin/javac" --release 8 -encoding UTF-8   -cp "$CORE_ANDROID" -d "$CORE_WORK/classes" "$CORE_WORK/CoreProvision.java"

"$CORE_JAVA/bin/java" -cp "$CORE_D8" com.android.tools.r8.D8   --release --min-api 31 --lib "$CORE_ANDROID"   --output "$CORE_WORK/helper.zip"   "$CORE_WORK/classes/CoreProvision.class"   "$CORE_WORK/classes/CoreProvision\$Failure.class"

unzip -l "$CORE_WORK/helper.zip"
shasum -a 256 "$CORE_WORK/helper.zip"
```

The archive must contain only classes.dex. The nested Failure class must be included. Record the source revision, tool versions, and resulting helper digest in the local setup record. No private data belongs in that record.

The complete Android SDK jar provides org.json for compilation; Android supplies it at runtime. Do not dex the SDK jar or add the historical json.jar to the phone helper. D8 produces Android bytecode; running this class with an ordinary desktop JVM is not a phone transport test. See [D8 documentation](https://developer.android.com/tools/d8).

Continue with [official APK verification](../docs/downloads.md), then [USB preflight](../docs/usb-onboarding.md). The helper only transfers pairing. It neither installs Core nor registers ownership.

## Maintainer host tests

Host tests use synthetic payloads only. The optional test dependency is [org.json 20240303](https://repo.maven.apache.org/maven2/org/json/json/20240303/json-20240303.jar), SHA-256:

```text
3cf6cd6892e32e2b4c1c39e0f52f5248a2f5b37646fdfbb79a66b46b618414ed
```

Verify that digest before using it. It is a desktop test dependency, not an Android runtime implementation or part of helper.zip. From an existing maintainer checkout, with the variables above and CORE_JSON pointing to that verified jar:

```sh
python3 -m unittest discover -s tools/tests -p 'test_*.py'
mkdir -p "$CORE_WORK/test-classes"
"$CORE_JAVA/bin/javac" --release 8   -cp "$CORE_WORK/classes:$CORE_JSON:$CORE_ANDROID"   -d "$CORE_WORK/test-classes" tools/tests/CoreProvisionTest.java
"$CORE_JAVA/bin/java"   -cp "$CORE_WORK/test-classes:$CORE_WORK/classes:$CORE_JSON:$CORE_ANDROID"   CoreProvisionTest
```

These tests cover validation, error handling, overload selection, and launch-result/user guards. They do not establish Android parcel behavior, hidden API access, device management permission, Hub signature validity, or successful pairing.

## Fixed helper errors

| Code | Meaning |
| --- | --- |
| E_USAGE | Expected a private file path and check or launch mode |
| E_SIZE | Input exceeded 64 KiB |
| E_JSON / E_ADMIN / E_SCHEMA / E_PAIRING_TYPE | Payload structure or supported component/type does not match |
| E_TIMESTAMP / E_WINDOW | Local timestamp syntax or sanity bound failed; check actual Hub expiry separately |
| E_USER | Not shell UID 2000 on foreground user 0 |
| E_BUNDLE_TYPE / E_ROUNDTRIP | Typed transport failed |
| E_LAUNCH_API | Expected hidden launch signature missing or ambiguous |
| E_LAUNCH_RESULT | Android did not return the sole accepted result, 0 |
| E_RUNTIME | Other runtime/read/reflection error; inspect locally without exposing input |

Do not weaken a check to make an error disappear. Any launch error is a stop, including one after ownership. The helper does not roll back device ownership.
