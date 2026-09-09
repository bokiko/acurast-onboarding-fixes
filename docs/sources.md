# Sources and verification record

Checked 2026-09-09. Upstream documents may change; field observations apply to the versions recorded in the README.

| Source | Used for |
| --- | --- |
| [Acurast provider onboarding](https://docs.acurast.com/processors/become-compute-provider/) | Official prerequisites and Core factory-reset/Hub route |
| [Acurast processors](https://docs.acurast.com/processors/) | Dedicated Core purpose and official onboarding links |
| [Acurast 1.27.1 release](https://github.com/Acurast/acurast-processor-update/releases/tag/processor-1.27.1) | Exact official download and asset SHA-256 |
| [Android dedicated-device development setup](https://developer.android.com/work/dpc/dedicated-devices/cookbook#development-setup) | ADB device-owner setup for eligible development devices; not endorsement of our Core helper |
| [Samsung Auto Blocker](https://www.samsung.com/us/support/answer/ANS10003636/) | Outside-store installation and USB command restrictions |
| [AirDroid Xiaomi USB setup](https://help.airdroid.com/hc/en-us/articles/360045329413-How-to-Enable-USB-debugging-on-Xiaomi) | Extra Xiaomi USB security setting and sign-in |

Field evidence: private setup records and explicit user confirmations, summarized without identifiers. The original 1.27.1 APK was inspected locally: its pairing parser expects a PersistableBundle, which informed the helper. Full APK decompilation and private logs are not published.

Planning received Claude and Kimi critiques. Those were reviews of supplied observations, not device tests or independent verification. The repository maintainer is responsible for the published claims.

Beginner walkthrough references checked 2026-09-09: [Google Platform Tools](https://developer.android.com/tools/releases/platform-tools), [Python Mac releases](https://www.python.org/downloads/macos/), [Temurin 17 binaries](https://github.com/adoptium/temurin17-binaries/releases), [Android QR setup](https://support.google.com/work/android/answer/9566881?hl=en), [developer options](https://developer.android.com/studio/debug/dev-options), [Xiaomi developer settings](https://www.mi.com/global/support/faq/details/KA-168765/). Direct Python and Java download links were checked against official hosts/releases.

AI instructions use official installer documentation: [Claude Code](https://code.claude.com/docs/en/overview), [Kimi Code](https://moonshotai.github.io/kimi-code/), [Codex CLI](https://developers.openai.com/codex/cli/). A normal cloud chat is not claimed to have local USB access.
