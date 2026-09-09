# App version and provenance notes

**This page is a reference, not a download step. Nothing is automatically installed by opening it.** The normal phone onboarding flow obtains the Acurast app separately; this repository does not supply an APK or installer.

Our recorded working app was **Core 1.27.1, version code 136**, package `com.acurast.attested.executor.canary`.

The installed file's SHA-256 matched the official release's `processor-1.27.1.apk` asset:

```text
7bb39cf9f6922c4c67f1b9b5a38303ba8a93b0ce195586613da7707b69a6744c
```

That comparison was checked on 2026-09-09. The [official release page](https://github.com/Acurast/acurast-processor-update/releases/tag/processor-1.27.1) is a provenance reference, not a requirement to download a file to your computer. Despite the package suffix, the matching asset was not the separately named canary, devnet, or Lite file.

Our Hub advanced field showed a 1.26.0 URL while we used 1.27.1. We did not establish why. The field results apply to 1.27.1, not every future version, and are not a recommendation to downgrade an existing processor.
