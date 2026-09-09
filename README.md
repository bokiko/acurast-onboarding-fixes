<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;height=200&amp;section=header&amp;text=Acurast%20Onboarding%20Fixes&amp;fontSize=42&amp;fontColor=ffffff&amp;animation=fadeIn&amp;fontAlignY=38&amp;desc=QR%20setup%20errors.%20Blocked%20installs.%20Clear%20fixes.&amp;descAlignY=58&amp;descAlign=50" alt="Acurast Onboarding Fixes — QR setup errors. Blocked installs. Clear fixes." width="100%" />
</p>

<!-- Static for-the-badge / flat-square equivalents keep RepoFix badge styling available without third-party badge service uptime. -->
<p align="center">
  <a href="https://github.com/bokiko/acurast-onboarding-fixes/blob/main/docs/start-here.md"><img src="https://github.com/bokiko/acurast-onboarding-fixes/raw/refs/heads/main/docs/assets/guide.png" width="158" height="28" alt="Read the live guide" /></a>
  <a href="https://x.com/bokiko"><img src="https://github.com/bokiko/acurast-onboarding-fixes/raw/refs/heads/main/docs/assets/x.png" width="93" height="28" alt="Follow @bokiko on X" /></a>
</p>

<p align="center">
  <a href="docs/start-here.md"><img src="https://github.com/bokiko/acurast-onboarding-fixes/raw/refs/heads/main/docs/assets/android.png" width="106" height="20" alt="Android 12 or newer" /></a>
  <a href="https://github.com/bokiko/acurast-onboarding-fixes/blob/main/README.md"><img src="https://github.com/bokiko/acurast-onboarding-fixes/raw/refs/heads/main/docs/assets/markdown.png" width="133" height="20" alt="Markdown guide" /></a>
  <a href="docs/start-here.md"><img src="https://github.com/bokiko/acurast-onboarding-fixes/raw/refs/heads/main/docs/assets/browser.png" width="179" height="20" alt="Read in your browser" /></a>
  <a href="LICENSE"><img src="https://github.com/bokiko/acurast-onboarding-fixes/raw/refs/heads/main/docs/assets/license.png" width="106" height="20" alt="MIT license" /></a>
</p>

<p align="center">
  <a href="docs/start-here.md"><strong>Start here</strong></a> ·
  <a href="docs/ai-assisted.md"><strong>Use an AI assistant</strong></a> ·
  <a href="docs/troubleshooting.md"><strong>Find your error</strong></a>
</p>

---

A practical guide to fixing Acurast QR onboarding errors and blocked installations on Samsung, Xiaomi, and Pixel phones—with the steps we learned while onboarding real devices.

**Read everything here on GitHub. You do not need to download, clone, or install this repository. Opening these pages does not install software, run commands, or access your phone.**

This is a community guide, not an Acurast app or an automatic installer. Installing Acurast itself is a separate action on your phone, through the official onboarding flow. An AI assistant also needs your permission and suitable local tools before it can change anything.

## Choose how you want help

| Your preference | Open this page |
| --- | --- |
| Let Claude, Kimi, or Codex help with the technical work | **[AI-assisted setup](docs/ai-assisted.md)** — copy a prompt with the repo URL |
| Follow the phone steps yourself | **[Start here](docs/start-here.md)** — a complete browser-readable walkthrough |
| Samsung is blocking setup | [Samsung steps](docs/samsung.md) |
| Xiaomi asks for a SIM/account or blocks USB | [Xiaomi steps](docs/xiaomi.md) |
| You have a Pixel | [Pixel steps](docs/pixel.md) |
| Something failed | [Find your error](docs/troubleshooting.md) |

## Give this link to your AI assistant

```text
Read https://github.com/bokiko/acurast-onboarding-fixes/blob/main/AI-ONBOARDING.md
and the guide pages it references directly from GitHub. Help me onboard my dedicated
phone to Acurast Core. Do not download or clone this repository, install computer tools,
or run installer scripts. Start by checking what access and tools you already have.
Explain each step simply and tell me exactly what I need to tap on the phone.
Ask before changing the phone, and never reset, flash, or unlock it without my explicit approval.
```

A local assistant can make the computer work much easier. An ordinary browser chat can explain steps, but cannot automatically control your USB phone. [How to use the prompt](docs/ai-assisted.md).

## What success means

**App installed → Core registered as device owner → paired to your Hub → confirmed online.** These are different stages. A successful installation or a lost USB connection alone does not prove online status.

Core is for a phone you intend to dedicate to Acurast. Its official route starts with a factory reset and later locks down normal phone access. Back up needed data first. Current published requirements include Android 12+, no root, and a locked bootloader. [Official reference](https://docs.acurast.com/processors/become-compute-provider/).

## Our field results

Recorded 2026-09-09, using Core **1.27.1 (136)** and a community USB method. These are individual observations, not a compatibility guarantee.

| Device | Android | Recorded result |
| --- | --- | --- |
| Samsung SM-A055F | 14 | Owner confirmed online |
| Google Pixel 6 Pro | 14 | Owner confirmed online |
| Samsung SM-A045F | 14 | Owner confirmed online after separate stock restoration/relock; Knox bit stayed tripped |
| Samsung SM-S918B | 15 | Device owner and pairing launch confirmed; online confirmation not preserved |
| Xiaomi 23124RA7EO | 13 / MIUI 14 | Owner confirmed online after extra USB permissions and setup-account removal |

The normal self-service walkthrough uses the phone's setup QR scanner. Our [USB technical notes](docs/usb-onboarding.md) describe an unofficial alternative that needs existing local tools and a reviewed pairing implementation; this guide does not silently fetch or run one.

[Version/provenance notes](docs/downloads.md) · [Technical helper review](docs/helper-review.md) · [Recovery boundaries](docs/recovery.md) · [Sources](docs/sources.md) · [Contribute](CONTRIBUTING.md)

---

## License

MIT — see [LICENSE](LICENSE).

---

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;height=100&amp;section=footer" alt="Decorative wave footer" width="100%" />

<p align="center">
  Made by <a href="https://bokiko.io">@bokiko</a>
</p>
