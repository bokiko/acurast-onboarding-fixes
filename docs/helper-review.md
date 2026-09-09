# Technical helper review

Maintainer review of the original community method, recorded 2026-09-09. Not an independent audit or an official Acurast API.

The original local helper preserved the Hub's five signed string extras in a typed PersistableBundle, parcel-roundtripped them, and launched Core's MainActivity through Android shell. Inspection of Core 1.27.1's parser informed that mechanism. Original field sessions succeeded, as recorded in the README.

The [source retained for online review](../tools/CoreProvision.java) adds mode, size, schema, admin-component, timestamp-window and launch-interface checks. It was compiled successfully before this repo became a browser-first guide. Those added checks have **not** been rerun through a complete spare-phone onboarding.

Reading the source in GitHub does not execute it. This guide no longer includes a local build/install workflow. An assistant may read the source, but must not download, generate or execute a helper under the no-download starter prompt.

## Limits

- Transport/schema checks do not authenticate a signature or prove the intended wallet. Obtain data from the owner's own Hub.
- The recorded four-hour window is not a timeless protocol guarantee; actual Hub expiry controls.
- Hidden Android APIs and Core's parser can change. Do not weaken checks to force compatibility.
- Ownership changes and launching are separate; failures do not automatically undo device ownership.
- Staged private data is not automatically removed; Core may disconnect ADB before cleanup.
- Host build/test success is not a new phone or network test.
