<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;height=200&amp;section=header&amp;text=Acurast%20Onboarding%20Fixes&amp;fontSize=42&amp;fontColor=ffffff&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=Phone%20blocked%20during%20setup%3F%20Start%20here.&amp;descAlignY=58&amp;descAlign=50" alt="Acurast Onboarding Fixes — Phone blocked during setup? Start here." width="100%" />
</p>

<!-- Badge images are stored in this repository; the decorative waves use an external service. -->
<p align="center">
  <a href="docs/ai-assisted.md"><img src="https://github.com/bokiko/acurast-onboarding-fixes/raw/refs/heads/main/docs/assets/guide.png" width="158" height="28" alt="Read the live guide" /></a>
  <a href="https://x.com/bokiko"><img src="https://github.com/bokiko/acurast-onboarding-fixes/raw/refs/heads/main/docs/assets/x.png" width="93" height="28" alt="Follow @bokiko on X" /></a>
</p>

<p align="center">
  <a href="#what-you-need"><img src="https://github.com/bokiko/acurast-onboarding-fixes/raw/refs/heads/main/docs/assets/android.png" width="106" height="20" alt="Android 12 or newer" /></a>
  <a href="README.md"><img src="https://github.com/bokiko/acurast-onboarding-fixes/raw/refs/heads/main/docs/assets/markdown.png" width="133" height="20" alt="Markdown guide" /></a>
  <a href="docs/ai-assisted.md"><img src="https://github.com/bokiko/acurast-onboarding-fixes/raw/refs/heads/main/docs/assets/browser.png" width="179" height="20" alt="Read in your browser" /></a>
  <a href="LICENSE"><img src="https://github.com/bokiko/acurast-onboarding-fixes/raw/refs/heads/main/docs/assets/license.png" width="106" height="20" alt="MIT license" /></a>
</p>

# Acurast setup stopped. What now?

“Something went wrong. Contact your IT team.” An installation Android refuses.
Or Core opens, but says **Manager: not set**.

This guide is for phones that got stuck during Acurast Core onboarding.
The community USB method below got our blocked phones online, including a
Pixel running Android 17.

**[Start USB setup with an AI assistant →](docs/ai-assisted.md)**

You connect the phone to a computer. The assistant checks the phone, prepares
the tools, and works through the setup with you.

**Read this guide in your browser. You do not need to download or clone the
repository. Reading it installs nothing.** USB setup is a separate action:
it uses computer tools and installs Acurast Core on your phone.

## Start with the error you see

- **QR setup ends with only a Reset button.** We observed this failure on
  Android 16 and 17. Repeating the same factory reset did not resolve it.
  The USB route uses a different way to set up Core’s device management.
- **Android blocks installation or USB commands.** The assistant checks the
  exact restriction. Samsung and Xiaomi may need different steps.
- **Core says `Manager: not set`.** Pairing has not completed. Check the Core
  version first: our Android 17 phone silently discarded USB pairing on
  1.26.0 and accepted it on 1.27.1.
- **Core says it cannot pay fees during setup.** Check pairing. Do not send
  tokens to the processor address to fix this error.

[Find your exact error](docs/troubleshooting.md)

## What you need

- A phone you own and can dedicate to Core, running Android 12 or newer.
  Back up anything you want to keep. The phone must not be rooted, and its
  bootloader must be locked.
- A computer, a USB data cable, and an AI assistant that can run commands on
  that computer. A browser-only chat can explain the steps but cannot operate
  your USB phone.
- Wi-Fi, power, and access to your own [Acurast Hub](https://hub.acurast.com/)
  wallet session.
- Time to stay with the phone and finish its confirmation screens.

**Core takes over the phone for dedicated use.** Once Core is registered as
device owner, returning the phone to normal use may require a factory reset.
The assistant must check everything it can before that step.

USB setup does not bypass Android requirements, root checks, or attestation.

## How the AI-assisted setup works

Open [AI-assisted setup](docs/ai-assisted.md) and copy the short message into
an assistant you use on your computer. Read the message before pasting it.

The assistant follows the guide and handles the computer work. You handle
passwords, wallet approvals, and the phone’s physical confirmations.

1. **Check the phone.** It identifies the intended device, reads its current
   state, and explains any blocker before changing anything.
2. **Prepare the tools.** It explains any needed downloads, obtains them from
   the documented sources, and builds the small pairing helper. It verifies
   the official Core app before installing it.
3. **Prepare pairing privately.** In your own Hub session, you use
   **Copy QR Data** and save it to a private local file. The helper reads
   that file directly. The assistant must not print its contents or load
   them into the chat.
4. **Check before committing.** It checks the pairing format and Android
   transport before registering Core as device owner. A failed check means
   stop.
5. **Finish and verify.** You read and accept Core’s disclaimer if you agree.
   Setup is complete only when the intended processor is confirmed online
   in your Hub.

The USB method uses **Core 1.27.1 or newer**. Our recorded working version is
**1.27.1 (136)**; later releases need checking. The version named in the Hub
QR may be older.

[USB procedure](docs/usb-onboarding.md) ·
[Checks and stop conditions](docs/checklist.md)

## Keep control of the setup

This guide does not grant an assistant access to your computer or phone.
That access comes from the assistant you use and the permissions you give it.

An assistant with command access can read files and change devices. These
instructions set boundaries; they are not a technical barrier against mistakes.
Review the proposed setup before authorizing it. A reset, firmware change,
or replacement of an existing paired processor needs a separate explanation
and your specific approval.

**An assistant following this guide will never ask you to:**

- Paste wallet recovery words, private keys, or passwords into chat.
- Upload your onboarding QR, signed QR data, or private setup file.
- Send tokens to a stranger—or to the processor address as a pairing fix.
- Install an APK or “fix tool” from an unsolicited message.

Keep the pairing file outside the repository and shared or cloud-synced
folders. It authorizes pairing and should stay private. Temporary files should
be removed after use where possible; Core may disconnect USB before the
phone’s copy can be deleted.

The helper’s [source and build instructions](tools/README.md) are public.
Its checks preserve the pairing data’s format; they do not authenticate your
wallet signature or guarantee onboarding. Read the
[technical review](docs/helper-review.md) for the limits.

## Phones we tested

These are results from our September 9 and 12, 2026 sessions using Core
1.27.1 and the community USB method. “Online” means the owner confirmed the
processor reporting. Results apply to these phones and versions.

| Phone | Android | Result |
| --- | --- | --- |
| Pixel 9 Pro Fold | 17 | Online after 1.26.0 silently discarded pairing |
| Pixel 6 Pro | 14 | Online; phone had undergone a separate OS downgrade |
| Samsung SM-A055F | 14 | Online |
| Samsung SM-A045F | 14 | Online after separate stock restoration and relock; Knox remained tripped |
| Samsung S23 Ultra | 15 | Device owner and pairing launch confirmed; online confirmation not preserved |
| Xiaomi Redmi Note 13 | 13 | Online after extra USB permission and setup-account removal |
| Huawei Mate 20 Pro | 10 | Could not install the tested APK: Android version too old |

The guarded helper published here has a recorded complete onboarding on the
Pixel 9 Pro Fold. Earlier sessions used the original helper. These results
do not guarantee compatibility with every phone or future Core release.

Stock restoration and Android downgrades are separate, model-specific work.
They are not routine steps in this USB guide.

[Samsung notes](docs/samsung.md) ·
[Xiaomi notes](docs/xiaomi.md) ·
[Pixel notes](docs/pixel.md) ·
[App verification](docs/downloads.md)

## If you are still blocked

Stop at the failed step. An installed app, a successful launch command, or a
disconnected USB cable does not prove pairing.

Use [troubleshooting](docs/troubleshooting.md), or
[report the problem](https://github.com/bokiko/acurast-onboarding-fixes/issues/new/choose)
with your phone model, Android and Core versions, the last successful step,
and the error. Remove accounts, serial numbers, QR codes, and other private
details from screenshots and logs.

For the standard welcome-screen QR method, use
[Acurast’s official onboarding instructions](https://docs.acurast.com/processors/become-compute-provider/).

---

Community guide by [@bokiko](https://bokiko.io), not an official Acurast product.

[Recovery boundaries](docs/recovery.md) ·
[Sources](docs/sources.md) ·
[Contribute](CONTRIBUTING.md) ·
[MIT license](LICENSE)

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;height=100&amp;section=footer" alt="Decorative wave footer" width="100%" />
