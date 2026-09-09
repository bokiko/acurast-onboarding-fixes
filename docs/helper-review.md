# Helper review and validation limits

Maintainer implementation review, 2026-09-09. This is not an independent security audit or Acurast endorsement.

## Mechanism inspected

The original working helper constructed `android.app.extra.PROVISIONING_ADMIN_EXTRAS_BUNDLE` as a **PersistableBundle**, carrying the Hub's original string values. It addressed Core's `MainActivity` with `android.app.action.PROVISIONING_SUCCESSFUL` using `app_process` as Android shell. Local inspection of Core 1.27.1's pairing parser showed this bundle type was expected. The five recorded values are account, accountType, timestamp, signature, and type.

A normal `am start --es` string extra is not the same bundle. The helper does not invent or sign pairing data, and its parcel roundtrip only checks transport preservation.

## Public-source changes

Compared with the field helper, the published source rejects unknown modes, oversized payload files, wrong admin component, unexpected/missing/empty fields, unrecorded account/pairing types, and timestamps outside the recorded window. It checks every parameter type of the hidden activity-launch interface before either check or launch. Exceptions are summarized without dumping private JSON values. The local Python validator additionally rejects duplicate JSON keys.

The activity target and transport mechanism are unchanged. Host tests and compilation succeeded during publication. **The hardened public source has not been exercised end to end on a spare Android phone.** Field successes refer to the original helper, not a fresh test of these added guards. No independent reader reproduction is claimed.

## Unresolved limits

- The helper does not authenticate signatures, check chain/network state, or confirm the intended wallet. Core must validate pairing; the user must obtain data from their own Hub.
- Four hours reflects the observed Hub window, not a timeless protocol guarantee. Obey the actual Hub expiry even if a local check passes.
- The hidden Android API and Core component may change. A different schema/version requires review, not deleting validation until it runs.
- Readiness, package provenance, and ownership are prerequisites checked separately. Launching is deliberately manual.
- Staged pairing JSON is not automatically removed. ADB lockdown can prevent later deletion. Host files and clipboard also require cleanup.
- Device-owner changes may need a reset to undo; a launch failure does not automatically undo ownership.

Release artifacts contain source only. Compiled helpers, dependency downloads, APKs, real device records, and signed payloads stay out of Git.
