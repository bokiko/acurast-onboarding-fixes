# Tools

## Read-only diagnosis

```sh
python3 tools/diagnose.py --serial YOUR_DEVICE_SERIAL
```

Needs Python 3 and ADB on PATH. Reads a small allowlist of properties, counts accounts without printing identifiers, summarizes management state, Core version and exact-alarm appop. Errors/timeouts become unknown. It does not contact the Hub or prove eligibility. It can read private account output into process memory to count it, but does not save or print that raw output.

## Pairing schema check

```sh
python3 tools/validate_pairing.py /absolute/private/path/to/provisioning.json
```

Checks JSON size, duplicate keys, expected admin component, five nonempty string extras, recorded account/type, and timestamp window. No network or signature verification. A structurally valid malicious payload can pass; obtain the JSON from your own Hub session and verify the intended wallet.

## Build the Android helper

First-time users: use [Start here](../docs/start-here.md) for download links, installer choices, and exactly where to paste commands.

Requires **JDK 17** (`java` and `javac` available in the terminal), Python 3, and internet for the first build. Run from the repo root:

```sh
python3 tools/build.py
```

The script downloads hash-pinned dependencies from Maven Central and Google's Android Maven repository into ignored `build/deps`, compiles source, and runs D8 to produce `build/helper.zip`. Downloads happen only if absent, and cached hashes are checked too. No phone is contacted. Dependency URLs and SHA-256 hashes are in `tools/build.py`.

The old Android Maven JAR is a compile-time stub only, not an Android runtime or claimed device requirement. APIs newer than those stubs are reached reflectively; `org.json` and Android classes are supplied by the phone at runtime. Only our class is dexed into the helper. No third-party JAR or APK is redistributed.

See [USB instructions](../docs/usb-onboarding.md) for `check` and `launch`. Both require exactly a payload path and mode. The hardcoded package/component intentionally constrain this helper to the recorded Core setup. Never alter it to target a different administrator without a new review.

## Validation and limits

```sh
python3 -m unittest discover -s tests
```

Host tests use synthetic data and cover malformed, expired/future, duplicate, oversize, and wrong-component inputs. They do not run Android or authenticate signatures. Build success is not a device test. See [helper review](../docs/helper-review.md).
