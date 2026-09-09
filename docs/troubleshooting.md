# Troubleshooting by observed error

Read these fixes directly in GitHub. USB/tool errors apply only if you or an authorized local assistant already have those tools. No computer installation is required to read this guide. For the phone-only QR route, use [Start here](start-here.md).

Always select the intended device explicitly. Stop after a failed prerequisite instead of running the remaining commands.

| Observation | Meaning / next check | Tested action or next step |
| --- | --- | --- |
| No device in `adb devices -l` | Cable, USB port, debugging, or Core lockdown | Before onboarding, use a data cable and enable debugging. After pairing, inspect phone and Hub before assuming failure. |
| `unauthorized` | Computer has not been authorized | Unlock phone and accept its USB debugging prompt. |
| `INSTALL_FAILED_USER_RESTRICTED` | OS rejected installation | Inspect phone prompt. Xiaomi manual File Manager installation worked, but did not fix owner permissions. |
| `INJECT_EVENTS` denied | Remote input restriction | On tested Xiaomi, enable extra USB debugging security setting on phone. |
| `Calling identity is not authorized` from `dpm` | Management permission restriction | Extra Xiaomi USB security permission resolved our instance. This error is not proof of a Xiaomi cause on every phone. |
| `already some accounts on the device` | Android rejects owner provisioning in current account state | Remove setup accounts through Settings, verify zero accounts, retry. |
| Existing device owner | Device already managed | Do not overwrite/remove an unrelated administrator. Resolve through its existing management process. |
| APK installed but no pairing | Installation is only one stage | Check device owner, correct Core package/version, QR validity and typed extras. |
| Helper rejects schema or launch API | Different payload or Android interface | Stop. Do not strip signature fields or improvise an intent; report redacted versions/error. |
| Activity launch result `0` | Android accepted the activity start | Check disclaimer and Hub. It is not a network success signal. |
| USB vanishes during Core launch | Observed Core lockdown behavior | Inspect phone, read/accept disclaimer if shown, verify Hub status. |
| Hub still offline | Pairing or connectivity may be incomplete | Check phone's actual message, internet, correct Hub wallet and QR expiry. Do not repeatedly provision blindly. |
| QR expired | Pairing authorization window ended | Generate a fresh Hub QR; never modify its timestamp or signature. |
| Modified/unlocked firmware | Requirements may not be met | Read [recovery boundaries](recovery.md), not a generic flash recipe. |

The helper's transport check does not verify the QR signature, eligibility, network health, or reward status. Keep diagnostics limited to the failing stage. Never attach full `dumpsys account`, logcat, or a QR payload publicly without inspecting and redacting it.
