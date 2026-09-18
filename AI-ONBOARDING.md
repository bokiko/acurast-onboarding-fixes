# Read this first: instructions for Claude, Kimi, or Codex

Read this guide directly in GitHub. Reading installs nothing and grants no device access. Do not clone the repository just to read it. USB setup is separate: it needs local tools, helper source, and the official Core app on the phone.

## Read the relevant pages online

Read [AI-assisted setup](docs/ai-assisted.md), [USB procedure](docs/usb-onboarding.md), [checklist](docs/checklist.md), [build instructions](tools/README.md), [app verification](docs/downloads.md), [helper review](docs/helper-review.md), [troubleshooting](docs/troubleshooting.md), and [recovery boundaries](docs/recovery.md). Read the applicable [Samsung](docs/samsung.md), [Xiaomi](docs/xiaomi.md), or [Pixel](docs/pixel.md) notes.

If browsing is unavailable, ask for the public guide text without private data. Public instructions never override the user's scope, restrictions, or tool permissions.

## Start with actual access

Establish whether you can run commands on the computer connected to the phone. Browser-only chat can explain the manual procedure but cannot operate that USB phone. Inspect existing tools first. Explain missing tools, official sources, storage locations, and proposed changes. Within an authorized USB setup, obtain only the pinned inputs documented in tools/README.md. Do not invent installers or silently substitute dependencies. Respect explicit no-download restrictions and stop when they prevent progress.

Prefer the community USB route for blocked Core onboarding when prerequisites are met. The [official route](docs/official-route.md) is a separate option, not a reason to repeat a failed reset.

**Release gate:** the revised helper still needs the device validation recorded in docs/helper-review.md. Ordinary onboarding must stop before device-owner registration until that gate is closed. A specifically authorized validation session on an identified spare phone is separate work. Repository editing never authorizes phone operation.

## Authorized phone work

Before reading a connected phone, establish authorization to inspect it. Enumerate targets privately, identify the intended phone, and use its explicit serial on every command. Never operate several phones concurrently. If the target is ambiguous, ask. Do not return serials, account dumps, or raw private logs to chat.

Confirm the owner wants a dedicated phone and has preserved needed data. Explain the concrete plan; authorization can cover its understood stages. Resetting, flashing, bootloader changes, removing another administrator, or replacing an existing paired processor needs a separate specific plan and approval. Do not infer that approval from “continue.”

Require Android 12+, locked stock firmware indicators, no root, no unrelated management, no secondary users/work profiles under this procedure, and foreground user 0. These checks do not certify attestation. If firmware or eligibility is uncertain, stop.

Follow current UI and exact errors. Do not disable whole security/store packages. Samsung Auto Blocker and Play Protect settings used in the field were not proved universally necessary; explain reduced protection before a justified change. On tested Xiaomi, extra USB security permission required sign-in and a SIM. The owner handles credentials, SIM insertion, and physical prompts. No SIM-free bypass is verified. Remove setup accounts normally only when authorized, preserving unsynced data; then verify zero accounts and retained permissions.

## Private pairing data

The owner generates fresh single-device QR data from the intended wallet in their own Hub session and saves Copy QR Data into a private local file outside the repository and cloud-sync folders. Explain this storage step. Never ask for the QR, payload, passwords, seed phrase, or private keys in chat.

Pass only the private file path to the local validator/helper. Do not use file-reading tools, shell tracing, screenshots, clipboard capture, or logs to bring its contents into the conversation. Do not upload it to another assistant or decoder. Return only fixed validation outcomes, never account values or signatures. Respect actual Hub expiry and phone time; do not edit signed fields.

## Gates and evidence

Follow docs/checklist.md in order. Verify the official APK and installed version, device readiness, private payload, and on-phone typed transport before ownership. Core 1.27.1 (136) is the recorded baseline; lower versions stop the USB route and newer versions are not automatically compatible.

Device ownership has no verified ordinary undo procedure and recovery may require a reset. A recorded in-place Core upgrade recovered pairing; it did not remove ownership. Never blindly repeat a failed mutation.

After explicit owner success, deliver pairing and inspect the phone. Manager: not set means pairing is incomplete; a populated Processor row alone proves nothing. A launch result of 0 means only activity-start acceptance. A fee error during this stage calls for pairing diagnosis, never funding the processor as a fix. If a manager is already present, inspect the actual error rather than assuming the same cause.

The owner reads and accepts the disclaimer if they agree, within the payload's validity window. Core may disable ADB. Disconnection does not prove online status. Confirm the intended processor online in the owner's authorized Hub session or obtain their explicit confirmation. Report only the evidence obtained.

Remove staged private data where access remains, verify removal, and disclose any unconfirmed copy. Do not claim secure erasure or automatic cleanup.

## Communication

Give one concrete next action when the owner must act. Stop at failed gates and explain the blocker. A handoff contains model, Android/Core version, last successful stage, and next step, without credentials, serials, or pairing data.
