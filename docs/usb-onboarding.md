# Community USB method: what it requires

**This is a technical explanation you can read in GitHub, not a download or an automatic setup script.** For the self-service route that needs no computer tools, use [Start here](start-here.md). An [AI assistant](ai-assisted.md) can inspect an existing local setup and explain whether this alternative is available.

## The stages observed in our sessions

1. Identify the correct phone with already-installed ADB, check firmware indicators, and confirm no competing management.
2. Resolve vendor USB restrictions and remove setup accounts from the phone normally.
3. Verify the official Core app's provenance and installed version. The recorded file was Core 1.27.1 (136); see [version notes](downloads.md).
4. Prepare the owner's fresh single-device Hub pairing data privately.
5. Use a reviewed local helper to construct the typed Android provisioning bundle and check transport compatibility.
6. Register Core as device owner, then deliver the unchanged signed pairing data.
7. Complete the phone's prompts and verify the intended processor online in Hub.

## Why there is no one-line pairing command here

Our original helper placed five Hub strings—account, accountType, timestamp, signature and type—inside an Android **PersistableBundle** under `android.app.extra.PROVISIONING_ADMIN_EXTRAS_BUNDLE`. It launched Core's `MainActivity` with `android.app.action.PROVISIONING_SUCCESSFUL` using Android shell.

Ordinary `am start --es` string extras are not equivalent to that bundle. APK installation and `dpm set-device-owner` alone do not complete Hub pairing. We will not offer an incomplete command sequence as if it did.

The [helper source](../tools/CoreProvision.java) is available to **read online** for technical review. This browser-first guide does not tell readers to download, compile, or run it. If an assistant does not already have suitable reviewed local tools, it must explain that prerequisite and stop the USB route rather than fetch or invent a helper silently. Any later request to obtain or create tools is a separate decision outside this no-download-computer workflow.

## Required checks before an authorized USB attempt

- Existing local ADB access, explicit target serial and version/provenance checks.
- Dedicated, backed-up phone; no unrelated device owner; account state actually inspected.
- Xiaomi's additional USB security permission when required. An APK installed manually does not grant it.
- Fresh QR from the intended Hub wallet, private handling, actual expiry respected. No timestamp/signature edits or public QR decoder.
- Typed-bundle check before ownership. Transport success is not signature authentication.
- Owner registration explicitly successful before pairing, followed by phone/Hub verification.

Core may disable debugging during lockdown. Staged private files may remain if ADB disappears; do not promise automatic cleanup. [Review limits](helper-review.md) and [recovery boundaries](recovery.md) explain the remaining caveats.
