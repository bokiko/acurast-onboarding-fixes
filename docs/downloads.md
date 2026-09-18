# App version and provenance notes

**Opening this page installs nothing.** Authorized USB setup downloads the official APK to the computer for verification and installation. This repository does not distribute an APK.

Our recorded working app was **Core 1.27.1, version code 136**, package `com.acurast.attested.executor.canary`.

The installed file's SHA-256 matched the official release's `processor-1.27.1.apk` asset:

```text
7bb39cf9f6922c4c67f1b9b5a38303ba8a93b0ce195586613da7707b69a6744c
```

That comparison was checked on 2026-09-09. The [official release page](https://github.com/Acurast/acurast-processor-update/releases/tag/processor-1.27.1) is the source for an authorized USB download. Despite the package suffix, the matching asset was not the separately named canary, devnet, or Lite file.

## Why the Hub's URL and the working version differ

Our Hub advanced field showed a 1.26.0 URL while we used 1.27.1. An earlier version of this page recorded that we had not established why. We since have, on one device.

On a Pixel 9 Pro Fold running Android 17 (2026-09-12), Core **1.26.0** accepted a USB-delivered provisioning intent and started normally, but never applied the pairing. The phone showed its ordinary overview screen with `Manager: not set`, no error was displayed, and the activity launch reported success. Upgrading the same phone in place to **1.27.1**, with the device-owner registration and the pairing data otherwise unchanged, applied the pairing immediately and advanced to the disclaimer screen.

This is a single observation on a single model and Android version. It does not establish the exact cause inside the app, nor that every build below 1.27.1 behaves this way, nor that every build above it does not. It is enough to justify a practical rule: **for the USB route, install 1.27.1 or newer and do not rely on the version named in the QR.** The [checklist](checklist.md) treats a lower version as a stop condition.

The phone-only [welcome-screen route](start-here.md) is a different mechanism — Android's own provisioning subsystem installs the app from that URL and delivers the pairing itself — and this observation says nothing about it.

## The QR's signature checksum is not a file hash

The QR carries a `SIGNATURE_CHECKSUM` field. It is the base64url-encoded SHA-256 of the app's **signing certificate**, not of the APK file. Two consequences matter in practice:

- It stays the same across app versions signed by the same key. We confirmed the 1.26.0 and 1.27.1 assets carry the identical certificate checksum, so that certificate check can accept either file. This does not authenticate the Hub pairing signature or prove compatibility with another build.
- It cannot be checked with `keytool -printcert -jarfile`. These releases carry no v1 (JAR) signature, so that command returns nothing at all rather than an error. The certificate has to be read from the APK signing block instead.

Treat a checksum that does not match as a stop condition and re-obtain the app from official sources.

The field results apply to 1.27.1, not every future version, and are not a recommendation to downgrade an existing processor.

## Verify before installation

For the baseline, obtain processor-1.27.1.apk from the linked official release and save it in the build folder as processor-1.27.1.apk. Do not use the separately named canary, devnet, or Lite assets. Set CORE_WORK and CORE_JAVA as described in [build instructions](../tools/README.md).

```sh
shasum -a 256 "$CORE_WORK/processor-1.27.1.apk"
"$CORE_JAVA/bin/java" -jar "$CORE_WORK/sdk/android-15/lib/apksigner.jar" verify --verbose --print-certs "$CORE_WORK/processor-1.27.1.apk"
"$CORE_WORK/sdk/android-15/aapt2" dump badging "$CORE_WORK/processor-1.27.1.apk"
```

Require the exact file hash above, successful signature verification, package com.acurast.attested.executor.canary, versionName 1.27.1, versionCode 136, and the inspected SDK requirement. The recorded minSdk is 30 (Android 11); this does not change the guide's Android 12+ eligibility requirement. Apple Silicon may need Apple's Rosetta to run the SDK's Intel native aapt2 binary; do not silently install it or skip the manifest check. Stop and explain the missing prerequisite.

The verified baseline signer-certificate SHA-256 digest is `ec70c2a4e072a0f586552a68357b23697c9d45f1e1257a8c4d29a25ac4982433` (rechecked 2026-09-18). This is different from the APK file hash.

Use apksigner's public signer-certificate SHA-256 digest with the private [payload validator](../tools/check-payload.py). It compares the QR's certificate checksum locally, without exposing the QR. It does not verify the five fields' Hub signature. Confirm the installed app's package, version, signer, and identity after installation as well. For a pre-existing installation, inspect it before proposing any change.

For another Core release, establish its own official digest and compatibility. Never apply the 1.27.1 hash to another APK or re-sign an official release. [Android apksigner reference](https://developer.android.com/tools/apksigner).
