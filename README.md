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

“Something went wrong. Contact your IT team.”
An app that won’t install. Or **Manager: not set** after setup.

This guide helps you work through those problems using a USB cable and an
AI assistant on your computer. We used this method to get blocked phones
online, including a Pixel running Android 17.

**[Set up your phone with AI help →](docs/ai-assisted.md)**

Connect your phone, copy the message, and let the assistant guide you.
Prefer to do it yourself? Follow the [USB steps](docs/usb-onboarding.md).

Read everything here in your browser. There’s no need to download or clone
this guide, and reading it installs nothing. During setup, the assistant
helps install the tools you need and Core on your phone.

## What you need

- **A spare Android phone:** Android 12 or newer, not rooted, with a locked
  bootloader. Back up anything you want to keep.
- **A computer and a USB data cable:** the published build steps currently
  cover Apple Silicon Macs.
- **An AI assistant that can run commands on that computer.** A browser-only
  chat can explain the steps, but you’ll need to run the commands yourself.
- **Wi-Fi, power, and your own [Acurast Hub](https://hub.acurast.com/) wallet.**

Core dedicates the phone to Acurast. To use it as a normal phone again, you
may need a factory reset.

## You connect the phone. The assistant handles the computer work.

1. **Connect your phone.** The assistant checks its Android version, setup
   state, and any Samsung or Xiaomi restrictions.
2. **Prepare Core.** It gets the tools from the documented sources, checks
   the official app, and explains what it will change.
3. **Pair with your Hub.** You save **Copy QR Data** to a private local file.
   The setup tool reads it directly; you never paste it into AI chat.
4. **Finish on the phone.** Read and accept Core’s disclaimer if you agree.
   Then check that your phone is online in your Hub.

You handle passwords, wallet approvals, and phone confirmations.
The assistant explains the next step and checks the result before continuing.

**[Open the setup message →](docs/ai-assisted.md#2-paste-this-into-its-chat-box)**

## Keep your wallet and QR private

- Never share recovery words, private keys, or passwords with an assistant.
- Keep the onboarding QR and its data out of chats and public posts.
- Don’t send tokens to the processor address to fix a pairing error.

[How your pairing data is handled](docs/ai-assisted.md#3-keep-control-of-the-setup)

## Recognise one of these errors?

| What you see | What to do next |
| --- | --- |
| QR setup ends with only a Reset button | We saw this on Android 16 and 17. Try the USB steps instead of repeating the same reset. |
| Android blocks installation or USB commands | Check the [Samsung](docs/samsung.md) or [Xiaomi](docs/xiaomi.md) steps. |
| Core says **Manager: not set** | Pairing is incomplete. Check the Core version first; 1.27.1 worked where 1.26.0 silently failed in our test. |
| Core says it cannot pay fees during setup | Check pairing first. Don’t fund the processor address as a fix. |

[More errors and fixes](docs/troubleshooting.md)

## Phones we got online

Recorded in September 2026 using Core 1.27.1 and the community USB method.

| Phone | Android | Result |
| --- | --- | --- |
| Pixel 9 Pro Fold | 17 | Online after updating Core from 1.26.0 to 1.27.1 |
| Pixel 6 Pro | 14 | Online after a separate OS downgrade |
| Samsung Galaxy A05 | 14 | Online |
| Samsung Galaxy A04 | 14 | Online after separate stock restoration; Knox remained tripped |
| Xiaomi Redmi Note 13 | 13 | Online after extra USB permission and account removal |

On the S23 Ultra running Android 15, we recorded device ownership and the
pairing launch, but did not preserve online confirmation.

These are individual phone results. The latest helper changes have passed
computer tests and still need a full phone test.
[What was tested](docs/helper-review.md) · [Field notes](docs/sources.md)

For the standard welcome-screen QR method, use
[Acurast’s official instructions](https://docs.acurast.com/processors/become-compute-provider/).

---

Community guide by [@bokiko](https://bokiko.io).

[Troubleshooting](docs/troubleshooting.md) ·
[Technical USB steps](docs/usb-onboarding.md) ·
[Source and build](tools/README.md) ·
[Recovery notes](docs/recovery.md) ·
[Contribute](CONTRIBUTING.md) ·
[MIT license](LICENSE)

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;height=100&amp;section=footer" alt="Decorative wave footer" width="100%" />
