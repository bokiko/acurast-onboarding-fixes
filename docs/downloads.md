# App version and provenance notes

**This page is a reference, not a download step. Nothing is automatically installed by opening it.** The normal phone onboarding flow obtains the Acurast app separately; this repository does not supply an APK or installer.

Our recorded working app was **Core 1.27.1, version code 136**, package `com.acurast.attested.executor.canary`.

The installed file's SHA-256 matched the official release's `processor-1.27.1.apk` asset:

```text
7bb39cf9f6922c4c67f1b9b5a38303ba8a93b0ce195586613da7707b69a6744c
```

That comparison was checked on 2026-09-09. The [official release page](https://github.com/Acurast/acurast-processor-update/releases/tag/processor-1.27.1) is a provenance reference, not a requirement to download a file to your computer. Despite the package suffix, the matching asset was not the separately named canary, devnet, or Lite file.

## Why the Hub's URL and the working version differ

Our Hub advanced field showed a 1.26.0 URL while we used 1.27.1. An earlier version of this page recorded that we had not established why. We since have, on one device.

On a Pixel 9 Pro Fold running Android 17 (2026-09-12), Core **1.26.0** accepted a USB-delivered provisioning intent and started normally, but never applied the pairing. The phone showed its ordinary overview screen with `Manager: not set`, no error was displayed, and the activity launch reported success. Upgrading the same phone in place to **1.27.1**, with the device-owner registration and the pairing data otherwise unchanged, applied the pairing immediately and advanced to the disclaimer screen.

This is a single observation on a single model and Android version. It does not establish the exact cause inside the app, nor that every build below 1.27.1 behaves this way, nor that every build above it does not. It is enough to justify a practical rule: **for the USB route, install 1.27.1 or newer and do not rely on the version named in the QR.** The [checklist](checklist.md) treats a lower version as a stop condition.

The phone-only [welcome-screen route](start-here.md) is a different mechanism — Android's own provisioning subsystem installs the app from that URL and delivers the pairing itself — and this observation says nothing about it.

## The QR's signature checksum is not a file hash

The QR carries a `SIGNATURE_CHECKSUM` field. It is the base64url-encoded SHA-256 of the app's **signing certificate**, not of the APK file. Two consequences matter in practice:

- It stays the same across app versions signed by the same key. We confirmed the 1.26.0 and 1.27.1 assets carry the identical certificate checksum, so a QR generated against one validates the other. Repointing the Hub's advanced APK URL at a newer build does not invalidate the QR.
- It cannot be checked with `keytool -printcert -jarfile`. These releases carry no v1 (JAR) signature, so that command returns nothing at all rather than an error. The certificate has to be read from the APK signing block instead.

Treat a checksum that does not match as a stop condition and re-obtain the app from official sources.

The field results apply to 1.27.1, not every future version, and are not a recommendation to downgrade an existing processor.
