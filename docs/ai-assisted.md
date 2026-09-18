# Let an AI assistant help with USB setup

Read this guide in your browser. You do not need to download or clone it. Actual USB setup uses computer tools and installs Core on your phone.

**Validation status:** the revised helper has not yet completed a spare-phone test. The procedure stops before ownership until that test is recorded. See [helper review](helper-review.md).

## 1. Open the assistant you use

Use a local assistant with command access on the computer connected to the phone. It starts by reading the same public guide pages you can read, then checks the computer and, when authorized, the phone. A browser-only chat can explain the [manual USB commands](usb-onboarding.md), but cannot run them on your computer.

## 2. Paste this into its chat box

This is a message to your assistant, not a Terminal or PowerShell command. Read it before pasting.

```text
Read this public guide and its linked instructions directly from GitHub:
https://github.com/bokiko/acurast-onboarding-fixes/blob/main/AI-ONBOARDING.md

Help me set up my own dedicated Android phone for Acurast Core using the
community USB procedure. First establish your local access, the available
tools, the intended phone, and the guide's current validation status.
Explain missing tools, official sources, and proposed changes before setup.
You may prepare the documented pinned toolchain within the setup I authorize.
Do not clone the repository just to read it or invent an installer.

Follow the checklist in order. Stop at failed prerequisites and the release
validation gate. A separate spare-phone test requires specific authorization.
Do not reset, flash, change the bootloader, or replace an existing paired
processor without a separate plan and my specific approval.

Keep pairing data in a private local file read directly by the validator and
helper. Never print it, open it into chat, or upload it. Never ask for wallet
recovery words, private keys, passwords, or QR data in chat.

Explain my next action simply. I handle credentials, wallet approvals, and
phone confirmations. Do not claim completion until the intended processor
is confirmed online in my Acurast Hub.
```

If the assistant cannot browse, paste the public instructions without private data. For a review branch, use that branch's instruction link; the example above intentionally targets the published main branch.

## 3. Keep control of the setup

The guide grants no access. The assistant's own permissions determine what it can read or change. These written boundaries are not a technical barrier against mistakes. Review the concrete plan before authorizing it; a reset or firmware change needs separate approval.

You enter credentials on the phone or in the official wallet, approve physical prompts, and read Core's disclaimer yourself.

When ready, open your own [Acurast Hub](https://hub.acurast.com/), select the intended wallet, generate fresh pairing data, and save **Copy QR Data** to a private local file. Do not paste it in chat or a terminal command. Use a local editor without cloud sync or AI extensions; save plain UTF-8 text. The assistant receives the path, never the contents. Keep the file outside the repository, shared folders, and cloud backups. Protect it as described in the [USB procedure](usb-onboarding.md#private-pairing-file).

The helper reads the file directly. Do not let the assistant print it, attach it, capture the clipboard, or take screenshots of the QR. Clear the clipboard after saving. Clipboard history, editor recovery files, and backups are additional private copies to manage.

Core may disconnect USB before staged files can be removed. The assistant should report what was deleted and what could not be checked. Deletion is not a promise of secure erasure.

## 4. Your part

1. Keep the intended phone connected, unlocked, powered, and on Wi-Fi.
2. Authorize the trusted computer's USB debugging prompt when instructed.
3. Handle account removal, credentials, and any required SIM on the phone.
4. Generate the fresh Hub payload only when preflight is ready.
5. Read and accept the disclaimer if you agree, before pairing expires.
6. Confirm the intended processor online in your Hub.

## 5. If it gets stuck

Say: **“Stop repeating the failed command. Read the troubleshooting page and tell me the blocker, the last successful step, and one next action.”**

Use only one assistant to operate a phone. Keep handoffs free of secrets. Without a computer, see the [official route](official-route.md); it may still encounter the recorded Android 16/17 QR failure.
