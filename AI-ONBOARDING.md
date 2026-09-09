# Instructions for Claude, Kimi, Codex, and other local assistants

Help the owner onboard a dedicated Android phone to Acurast Core. This file is guidance, **not authorization to operate a phone**. Only start device work when the current user requests it. A repository-edit task is not authorization to touch attached phones.

## Read before acting

Read `docs/start-here.md`, `docs/downloads.md`, `docs/helper-review.md`, and the relevant vendor page. Refer to `docs/troubleshooting.md` and `docs/recovery.md` for failures. This community method is unofficial and version-sensitive; verify upstream changes rather than assuming compatibility.

## Establish actual access and scope

Explain that you will inspect the computer and connected phone first. Check whether you have local shell/file access and ADB on the computer physically connected to the phone. Cloud-only execution or a web chat without a local connector cannot see its USB device. Say so plainly and guide the owner through the manual page rather than claiming access.

Inspect the host OS and installed tools before installing duplicates. Enumerate devices read-only; map an explicit serial to the owner's intended model. Use `adb -s SERIAL` for every device-specific command. If several phones are possible, ask which one before mutation. Never run concurrent mutations or several assistants against one phone.

Confirm the phone is owned, dedicated, and backed up if not already clear. Explain Core becomes device owner and may disable normal UI/ADB. Honor existing authorization; do not repeatedly ask for the same reversible setup actions.

The starter prompt can authorize verified app installation, documented blocker changes, removal of setup accounts **from the device** after explaining local-data effects, device-owner registration, and pairing with the owner's Hub data. A generic request to help does not authorize erasing data or altering an unrelated managed phone.

Factory reset, firmware flashing, bootloader unlocking/relocking, wiping partitions, or replacing an existing paired processor require separate specific authorization and a concrete plan. Do not perform them as part of routine onboarding. No FRP/account-lock bypass, root or bootloader exploits, unknown APKs, or broad security-package removal. Do not disable the whole Play Store package. Respect tool permission controls and never evade an approval denial.

## Work in observable stages

1. Inspect OS, USB authorization, firmware indicators, accounts and existing management with the redacted diagnostic. Unknown is not pass. Never print raw account dumps. An unrelated existing owner is a stop.
2. Use the official welcome-screen QR route where suitable. The USB alternative needs ordinary Android Settings, Wi-Fi and authorized ADB. Do not repeatedly reset to expose a setting.
3. Inspect actual UI for Play Protect's two switches and applicable vendor blockers. Our configuration had both Play Protect switches and Samsung Auto Blocker off; that reduces protection and is not proven universally necessary. Use observed UI bounds rather than remembered coordinates.
4. Xiaomi: ordinary USB debugging may allow reads but deny taps and `dpm`. The tested fix was extra **USB debugging (Security settings)** / **Install via USB**, requiring account/SIM in this case. Let the owner insert the SIM, type credentials and accept physical security prompts. No verified SIM-free bypass is recorded. Manual APK installation does not fix device-owner permissions. Remove setup accounts normally afterward; verify zero accounts and retained USB access.
5. Obtain the exact official APK from `docs/downloads.md`, verify its hash, and confirm the installed package/version. Never downgrade or remove an already-paired processor automatically. The verified `processor-1.27.1.apk` contains the `.canary` package; do not substitute the differently named canary/devnet/Lite downloads.
6. Build with `python3 tools/build.py`, using the actual Python executable available on the host. Check its result. The public helper's extra guards have not yet been retested end to end on a phone; compilation is not hardware verification.
7. Have the owner create fresh single-device QR data in their own Hub and save full JSON privately outside Git. Prefer local file handling over chat. Validate locally without displaying the account, signature or payload. `tools/validate_pairing.py` checks structure/time, not signature authenticity. Obey actual Hub expiry; never edit signed fields. No external QR decoding websites or sharing pairing data with another assistant/provider.
8. Stage helper and payload as documented. Run `check` before owner registration. The typed PersistableBundle matters; do not replace it with string extras or weaken guards to force a pass.
9. Explain ownership; when authorized and prerequisites pass, execute force-stop, exact-alarm appop and `dpm set-device-owner` sequentially. Inspect every result. Accounts/permission errors require stopping and resolving the cause.
10. Confirm owner, then launch using unchanged signed data. Let the owner read/accept disclaimers. Core may disable ADB and screenshots; loss of access is not proof of online status.
11. Verify the intended processor online in Hub if authorized browser access exists, or ask the owner to confirm. Distinguish installed, owner set, launch accepted, owner-confirmed online, and independently observed online. Never fabricate success.
12. Remove temporary private files when no longer needed and authorized. Clean phone staging if ADB remains available; if lockdown blocks cleanup, report that limitation. Clear local clipboard entries with the owner's knowledge. Never commit credentials or private records.

## Communication and failures

Use short plain-language updates. Do authorized computer work rather than asking the owner to paste every command. Request physical taps, SIM insertion, passwords entered on-device, wallet signing, ambiguous target selection, or genuinely required destructive approval when needed.

Inspect the exact failure and current state. Do not repeatedly re-run owner/pairing commands, invent a bypass, or promise MIUI optimization fixes this phone. Give one concrete next step when human action is required. Preserve progress across sessions.

Never ask for wallet recovery words/passwords in chat. Do not publish real QR data, account details, serials, raw logs, personal paths, or device backups. Onboarding does not authorize publishing, messaging others, or creating cloud accounts.

## Handoff

Summarize model without serial, Android/Core version, current ownership/pairing stage, verified blocker settings, last success, next action, and cleanup status. Keep any note local and secret-free. A new assistant must recheck the connected target before continuing.
