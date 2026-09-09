# Let Claude, Kimi, or Codex help

**You can give your assistant a link to this guide. There is no guide download, ZIP extraction, project installation, or code-editing step.**

An assistant with access to your computer can handle much of the technical work. You still handle phone passwords, physical confirmations, SIM insertion if required, and wallet approvals. A browser-only chat can coach you, but cannot automatically reach a USB phone.

## 1. Open the assistant you already use

Open your existing Claude, Kimi, or Codex app/session. For direct phone work, use a local session on the computer your phone is connected to, with command access you approve. You do not need all three assistants.

If you do not already have a suitable assistant, use [the manual phone walkthrough](start-here.md). This guide does not ask you to install an AI app or computer software.

## 2. Paste this into its chat box

This is an ordinary message to the AI, **not a command for Terminal or PowerShell**:

```text
Read this instruction file directly from GitHub:
https://github.com/bokiko/acurast-core-onboarding-guide/blob/main/AI-ONBOARDING.md
Then read the guide pages it references, also directly from GitHub.

Help me set up my own dedicated Android phone for Acurast Core, not Lite.
I am not a coder. Explain the next action simply and do the computer work only where
your existing tools and my permission allow it.

Do not download or clone this repository, download helper files, install computer tools,
or run installer scripts. First check whether you can access this computer and its
connected phone using tools that are already available. If you cannot, say so.

Identify the correct phone, check its current state, and explain any proposed change
before asking me to authorize phone setup. Never reset, flash firmware, unlock/relock
the bootloader, or replace an existing paired processor without specific approval.

Do not ask for passwords or wallet recovery words in chat. Keep pairing data private.
Do not claim completion until the intended phone is confirmed online in my Acurast Hub.
```

If the assistant cannot read GitHub, open [AI-ONBOARDING.md](../AI-ONBOARDING.md) in this browser, select its text and paste it into the conversation. No file download is needed. Do not paste a real QR or account credentials along with it.

## 3. What a helpful assistant should do

It should first establish whether it has local access, which phone is connected, and what tools already exist. If it needs ADB or another program that is missing, it should explain that limitation and offer the manual QR route. It must not silently install software to make its plan work.

Once you authorize a concrete phone setup plan, it can carry out the supported steps with available tools and inspect the results. If a setting needs your tap, it should give you the exact menu path. It should not make you run a long list of unexplained commands.

A phone app installation is a separate action: Acurast must be installed on the phone to run. Reading this repo does not install it. The assistant must explain any required transfer or installation rather than promise that all setup is download-free.

## 4. Your part

1. Keep the intended phone connected, unlocked and on Wi-Fi.
2. Accept its USB debugging prompt if using an authorized local USB method.
3. Enter passwords on the phone or in the official wallet, never into chat.
4. Open your own [Acurast Hub](https://hub.acurast.com/), connect the intended wallet, and generate fresh QR data only when needed.
5. Read and accept the phone's disclaimer if you agree.
6. Confirm that the new processor is online in your Hub.

For the normal QR route, simply point the phone's setup scanner at the computer's QR. For an advanced USB route, let the assistant explain how an already-available reviewed tool handles private pairing data; do not upload it to an online QR decoder or public issue.

## 5. If it gets stuck

Say: **“Stop repeating the failed command. Read this guide's troubleshooting page and tell me the exact blocker, the last successful step, and one next action.”**

When switching assistants, request a short handoff without secrets. The next assistant should recheck which phone is connected. Use only one assistant to change a phone at a time.

**Reading this guide makes no changes to your computer or phone.** Actions taken by you or your assistant are separate, explicit steps.
