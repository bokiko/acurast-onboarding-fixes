# Troubleshooting by observed error

Read these fixes directly in GitHub. USB/tool errors apply to an authorized setup using the [documented toolchain](../tools/README.md). No computer installation is required to read this guide. For the phone-only QR route, use [Start here](start-here.md).

Always select the intended device explicitly. Stop after a failed prerequisite instead of running the remaining commands. The [checklist](checklist.md) gives the order these checks belong in.

| Observation | Meaning / next check | Tested action or next step |
| --- | --- | --- |
| No device in `adb devices -l` | Cable, USB port, debugging, or Core lockdown | Before onboarding, use a data cable and enable debugging. After pairing, inspect phone and Hub before assuming failure. |
| `unauthorized` | Computer has not been authorized | Unlock phone and accept its USB debugging prompt. |
| `INSTALL_FAILED_USER_RESTRICTED` | OS rejected installation | Inspect phone prompt. Xiaomi manual File Manager installation worked, but did not fix owner permissions. |
| `INJECT_EVENTS` denied | Remote input restriction | On tested Xiaomi, enable extra USB debugging security setting on phone. |
| `Calling identity is not authorized` from `dpm` | Management permission restriction | Extra Xiaomi USB security permission resolved our instance. This error is not proof of a Xiaomi cause on every phone. |
| `already some accounts on the device` | Android rejects owner provisioning in current account state | Remove setup accounts through Settings, verify zero accounts, retry. |
| Existing device owner | Device already managed | Do not overwrite/remove an unrelated administrator. Resolve through its existing management process. |
| APK installed but no pairing | Installation is only one stage | Check device owner, Core version, QR validity and typed extras. Below 1.27.1 see the `Manager: not set` row. |
| **Overview screen shows `Manager: not set`** | **Pairing is incomplete** | **Check the installed version first. On our Android 17 test, 1.26.0 failed here silently and 1.27.1 succeeded. See [version notes](downloads.md).** |
| `Processor` row populated but `Manager` empty | Not a partial success | The processor key is generated locally regardless of pairing. Read the `Manager` row, not the `Processor` row. |
| Chain error about inability to pay fees | Check whether a manager is set; this accompanied incomplete pairing in our sessions | Diagnose pairing first. Do **not** fund the processor as a fix. If already paired, inspect the actual error. |
| Helper rejects schema or launch API | Different payload or Android interface | Stop. Do not strip signature fields or improvise an intent; report redacted versions/error. |
| Activity launch result `0` | Android accepted the activity start | Check disclaimer and Hub. It is not a network success signal. |
| Activity launch result `101` | Task is pinned in lock-task mode | Nothing will start until lock task is cleared. Inspect the pinned task before assuming Core is broken. |
| `am force-stop` has no effect | Core is device owner | Expected. Ownership cannot be worked around; see [recovery boundaries](recovery.md). |
| `pm clear` refused with `SecurityException` | Core is an active device admin | No verified ordinary ownership undo. Do not attempt to remove the admin to get around it. |
| USB vanishes during Core launch | Observed Core lockdown behavior | Inspect phone, read/accept disclaimer if shown, verify Hub status. |
| Phone sits on the disclaimer screen | Pairing applied but is not complete | The owner must accept within the QR's validity window. An expired payload needs a fresh QR. |
| Hub still offline | Pairing or connectivity may be incomplete | Check phone's actual message, internet, correct Hub wallet and QR expiry. Do not repeatedly provision blindly. |
| QR expired | Pairing authorization window ended | Generate a fresh Hub QR; never modify its timestamp or signature. |
| Modified/unlocked firmware | Requirements may not be met | Read [recovery boundaries](recovery.md), not a generic flash recipe. |

## Android 16 and newer device-owner failure

On Android 16 and newer, Core's welcome-screen QR provisioning has been observed downloading the app and then
aborting, with *"Getting your device ready for work"* followed by *"Something went wrong. Contact your IT team"*
and only a Reset button. Recorded on Samsung One UI 8 and on a Pixel running Android 17.

Egress was verified clean in our sessions; that does not establish the cause of every similar error. This observed failure is
tracked upstream as [acurast-processor-update#112](https://github.com/Acurast/acurast-processor-update/issues/112),
open since 2026-08-03 with zero comments when checked on 2026-09-17.

**Repeated factory resets did not fix this observed failure.** Diagnose the blocker before another reset.

What remains available, in rough order of safety:

- **Processor Lite** on that phone. Lite does not need device owner, so this failure does not apply to it. It is a
  different product from Core, not a workaround for it.
- **Another eligible phone**, while recognizing that Android version alone does not guarantee successful onboarding.
- **The community USB route**, with the documented toolchain and phone checks — see
  [USB method](usb-onboarding.md). It registers device owner through ADB rather than the QR provisioning path that
  fails here, which is why it can succeed where the QR route does not.
- **Changing the phone's Android version** is model-specific work with real brick risk from anti-rollback, and this
  guide provides no flashing recipe. Read [recovery boundaries](recovery.md) and get manufacturer-specific guidance
  before any such attempt.

## The fee error means pairing, not funding

This heading describes our incomplete-onboarding observation, not every possible fee error on an already-paired processor.

A processor that is not yet paired can report a chain error stating it cannot pay a transaction fee. The wording invites an obvious and wrong conclusion.

Do not send tokens to the processor address as an onboarding fix. In our observation a working, paired processor on this network held no balance of its own at all, so an empty processor balance is normal rather than the fault. The error appears because an unpaired processor has no manager associated with it yet, and the calls it is attempting are not the one that carries the pairing.

Check the Manager row. If it is not set, pairing is incomplete. If a manager is present, investigate the actual network/app error instead of assuming the same cause. Do not fund the processor to fix this onboarding symptom.

The helper's transport check does not verify the QR signature, eligibility, network health, or reward status. Keep diagnostics limited to the failing stage. Never attach full `dumpsys account`, logcat, or a QR payload publicly without inspecting and redacting it.

## Android too old

Our Huawei Mate 20 Pro on Android 10 rejected the tested Core APK with INSTALL_FAILED_OLDER_SDK. The inspected Core 1.27.1 manifest requires API 30 to install, while Acurast's published eligibility requirement is Android 12+. Installation eligibility is not proof of supported operation. Do not bypass the requirement or infer that every phone of this model is permanently impossible to use. [Field record](sources.md#field-observations).
