# Verified APK and version choice

For the recorded sessions the working APK was **Core 1.27.1, version code 136**, package `com.acurast.attested.executor.canary`.

- [Official release page](https://github.com/Acurast/acurast-processor-update/releases/tag/processor-1.27.1)
- [Exact official asset: processor-1.27.1.apk](https://github.com/Acurast/acurast-processor-update/releases/download/processor-1.27.1/processor-1.27.1.apk)
- SHA-256: `7bb39cf9f6922c4c67f1b9b5a38303ba8a93b0ce195586613da7707b69a6744c`

Checked on 2026-09-09 against the official GitHub release asset metadata. The APK used during onboarding has exactly this hash. Despite the package suffix, the matching asset is **processor-1.27.1.apk**, not the separately published `-canary.apk`, `-devnet.apk`, or Lite asset. Do not substitute by filename guesswork.

```sh
curl --fail --location --output processor-1.27.1.apk \
  https://github.com/Acurast/acurast-processor-update/releases/download/processor-1.27.1/processor-1.27.1.apk
python3 -c 'import hashlib,pathlib; p=pathlib.Path("processor-1.27.1.apk"); assert hashlib.sha256(p.read_bytes()).hexdigest()=="7bb39cf9f6922c4c67f1b9b5a38303ba8a93b0ce195586613da7707b69a6744c", "APK hash mismatch"; print("APK hash matches")'
```

Run outside this checkout; APKs are ignored by Git. With Android SDK Build Tools available, also run `apksigner verify --print-certs processor-1.27.1.apk`. A successful signature check alone does not identify the publisher. The field APK's signing certificate digest matched the Hub QR's admin-signature checksum. For the pinned asset, the full-file hash above identifies the exact verified file.

## Why the QR showed 1.26.0

Our Hub advanced field pointed to an official 1.26.0 URL while the APK we actually installed was 1.27.1. We did not determine why that field differed, and do not claim all Hubs default to 1.26.0. Successful results apply to 1.27.1. The USB helper forwards pairing extras; it does **not** download the QR's APK URL.

This is a reproducibility pin, not a recommendation to downgrade or a statement that 1.27.1 is the latest release. Before using another version, verify its official source, package, signer and pairing behavior; this helper's field results do not cover it.
