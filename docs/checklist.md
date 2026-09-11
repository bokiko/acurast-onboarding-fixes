# Preflight, gates and stop conditions

**Read this page in GitHub. It installs nothing and changes no phone by itself.** It is the operational companion to the [USB method](usb-onboarding.md): that page explains what the route requires, this one gives the order to do it in and the points where you must stop and check.

This page assumes the prerequisites on the USB page are already met — existing reviewed local tooling, an explicit target serial, and the owner's authorization. If you are setting up your own phone without a computer, use [Start here](start-here.md) instead; none of this applies to the welcome-screen QR route.

Two rules decide whether the attempt succeeds. Everything else on this page exists to enforce them.

## Rule 1 — install 1.27.1 or newer

The Hub QR's advanced field may name an older build. Ours named `processor-1.26.0` while our working sessions used 1.27.1.

On a Pixel 9 Pro Fold running Android 17 (2026-09-12), Core 1.26.0 accepted the provisioning intent, started normally, and **never applied the pairing**. No error appeared on the phone, in the app, or in the launch result. The same phone, same device-owner state and same pairing data succeeded immediately after upgrading to 1.27.1. See [version notes](downloads.md) for what this does and does not establish.

Treat a version below 1.27.1 as a stop condition, not a preference.

## Rule 2 — device owner is a one-way door

Registering Core as device owner cannot be undone from a computer. After that point, on our Android 17 test:

- `am force-stop` is accepted but does not stop Core
- `pm clear` is refused with a `SecurityException` about `CLEAR_APP_USER_DATA`
- `dpm remove-active-admin` is refused

There is no retry. A pairing that fails after this point costs a factory reset. Do every check that can be done beforehand, beforehand.

## Preflight — still reversible

At this stage Core is installed but not device owner, so `pm clear` and uninstall still work. Mistakes here are cheap. Confirm each line before continuing.

| Check | Expected | If not |
| --- | --- | --- |
| Correct phone selected by explicit serial | one intended device | Stop. Never operate two phones at once. |
| Core version | 1.27.1 or newer | Install the newer build before going further (Rule 1). |
| Accounts on the phone | zero | Remove setup accounts through Settings, then re-check. |
| Existing device owner | none | Do not overwrite another administrator. Stop. |
| Bootloader / verified boot | locked / verified | Requirements may not be met; see [recovery boundaries](recovery.md). |
| Pairing data | fresh, from the owner's own Hub, unexpired | Generate a new QR. Never edit timestamp or signature. |
| Reviewed helper's own check step | reports the typed bundle and all five fields | Stop. Do not improvise an intent or strip fields. |

Core exits immediately if it is started before it owns the device, so do not read "the app closed by itself" at this stage as a failure.

## Gate A — the last reversible point

Immediately before registering the device owner, re-confirm: Core is not running, accounts are still zero, no device owner is set, the version is still 1.27.1 or newer, and the pairing data has not expired.

Re-check rather than trust an earlier result. Installing, clearing or restarting anything can change these, and this is the last moment a mistake is cheap.

## Gate B — did the pairing actually apply?

Check the phone within a minute of delivering the pairing. This is the check whose absence caused our failed attempt.

| Phone shows | Meaning | Action |
| --- | --- | --- |
| A disclaimer / final-step screen | pairing applied | Hand the phone to the owner to read and accept |
| The ordinary overview screen with **Manager: not set** | pairing was discarded | Stop. Do not re-deliver blindly; see [troubleshooting](troubleshooting.md) |

**`Manager: not set` is the single most useful failure signal in this whole route.** A populated *Processor* row does not mean pairing worked — the processor key is generated locally regardless. Read the *Manager* row.

An activity launch result of `0` means Android accepted the start. It is not evidence that Core used the data.

## Gate C — is it online?

Two things still have to happen after Gate B, and neither is automatic.

**The owner must accept the disclaimer inside the QR's validity window.** Pairing is not complete until they do. We lost one otherwise-successful attempt because the phone sat on the acceptance screen until the payload expired. Tell the owner this before handing the phone over.

**Confirm in the Hub, not from the phone's screen.** ADB normally disappears during Core's lockdown; that is expected behavior and is not evidence of success or failure. Verify the intended processor appears and reports in the owner's authorized Hub session.

## Stop conditions

Stop and report rather than retrying if any of these occur:

- Core version is below 1.27.1
- Any Gate A line fails
- Gate B shows `Manager: not set`
- The phone reports a chain error about paying fees (see [troubleshooting](troubleshooting.md) — this means pairing did not happen and is never fixed by sending funds)
- The same action has failed twice with the same result

Repeating a failed provisioning step does not make it succeed, and after Rule 2 applies it removes the option of a clean retry.
