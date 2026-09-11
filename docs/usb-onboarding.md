# Community USB method: what it requires

**This is a technical explanation you can read in GitHub, not a download or an automatic setup script.** For the self-service route that needs no computer tools, use [Start here](start-here.md). An [AI assistant](ai-assisted.md) can inspect an existing local setup and explain whether this alternative is available.

Work through the [preflight, gates and stop conditions](checklist.md) alongside this page. That page gives the order and the points where you must stop and check; this one explains what the route is and what it needs.

## Two rules before anything else

**Install Core 1.27.1 or newer.** The version named in the QR's advanced field may be older — ours said 1.26.0. On a Pixel 9 Pro Fold running Android 17, 1.26.0 accepted the provisioning intent and then silently discarded the pairing, showing no error anywhere. The same phone paired immediately on 1.27.1. See [version notes](downloads.md).

**Registering the device owner is a one-way door.** Afterwards `am force-stop` has no effect, `pm clear` is refused, and the active admin cannot be removed from a computer. There is no second attempt: a pairing that fails after that point costs a factory reset. Everything that can be verified beforehand must be verified beforehand.

## The stages observed in our sessions

1. Identify the correct phone with already-installed ADB, check firmware indicators, and confirm no competing management.
2. Resolve vendor USB restrictions and remove setup accounts from the phone normally.
3. Verify the official Core app's provenance and installed version, and confirm it is 1.27.1 or newer. The recorded working file was Core 1.27.1 (136); see [version notes](downloads.md).
4. Prepare the owner's fresh single-device Hub pairing data privately.
5. Use a reviewed local helper to construct the typed Android provisioning bundle and check transport compatibility.
6. Re-confirm the preflight conditions, then register Core as device owner and deliver the unchanged signed pairing data. Registering the owner starts Core, so treat the app's state as unknown and check it rather than assuming.
7. Confirm on the phone that the pairing applied before going further, have the owner accept the disclaimer inside the QR's window, then verify the intended processor in Hub.

Stage 7 is the one most easily skipped. A phone that shows its ordinary overview screen with `Manager: not set` has not paired, regardless of what the launch reported. Read the `Manager` row: the `Processor` row fills in from a locally generated key whether or not pairing succeeded.

## Why there is no one-line pairing command here

Our original helper placed five Hub strings—account, accountType, timestamp, signature and type—inside an Android **PersistableBundle** under `android.app.extra.PROVISIONING_ADMIN_EXTRAS_BUNDLE`. It launched Core's `MainActivity` with `android.app.action.PROVISIONING_SUCCESSFUL` using Android shell.

Ordinary `am start --es` string extras are not equivalent to that bundle. APK installation and `dpm set-device-owner` alone do not complete Hub pairing. We will not offer an incomplete command sequence as if it did.

The [helper source](../tools/CoreProvision.java) is available to **read online** for technical review. This browser-first guide does not tell readers to download, compile, or run it. If an assistant does not already have suitable reviewed local tools, it must explain that prerequisite and stop the USB route rather than fetch or invent a helper silently. Any later request to obtain or create tools is a separate decision outside this no-download-computer workflow.

## Required checks before an authorized USB attempt

- Existing local ADB access, explicit target serial and version/provenance checks.
- Installed Core version 1.27.1 or newer, confirmed on the phone rather than assumed from the QR.
- Dedicated, backed-up phone; no unrelated device owner; account state actually inspected.
- Xiaomi's additional USB security permission when required. An APK installed manually does not grant it.
- Fresh QR from the intended Hub wallet, private handling, actual expiry respected. No timestamp/signature edits or public QR decoder.
- Typed-bundle check before ownership. Transport success is not signature authentication.
- Owner registration explicitly successful before pairing, followed by a phone-side check that the pairing applied, then Hub verification.
- The owner available to accept the disclaimer before the payload expires. Pairing that is applied but never accepted still ends as a failed onboarding.

Core may disable debugging during lockdown. Staged private files may remain if ADB disappears; do not promise automatic cleanup. [Review limits](helper-review.md) and [recovery boundaries](recovery.md) explain the remaining caveats.
