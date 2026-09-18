# Sources and verification record

Checked 2026-09-09. Upstream documents may change; field observations apply to the versions recorded in the README.

| Source | Used for |
| --- | --- |
| [Acurast provider onboarding](https://docs.acurast.com/processors/become-compute-provider/) | Official prerequisites and Core factory-reset/Hub route |
| [Acurast processors](https://docs.acurast.com/processors/) | Dedicated Core purpose and official onboarding links |
| [Acurast 1.27.1 release](https://github.com/Acurast/acurast-processor-update/releases/tag/processor-1.27.1) | Exact official download and asset SHA-256 |
| [Android dedicated-device development setup](https://developer.android.com/work/dpc/dedicated-devices/cookbook#development-setup) | ADB device-owner setup for eligible development devices; not endorsement of our Core helper |
| [Samsung Auto Blocker](https://www.samsung.com/us/support/answer/ANS10003636/) | Outside-store installation and USB command restrictions |
| [AirDroid Xiaomi USB setup](https://help.airdroid.com/hc/en-us/articles/360045329413-How-to-Enable-USB-debugging-on-Xiaomi) | Third-party description of the extra Xiaomi USB security setting and sign-in |

Field evidence: private setup records and explicit user confirmations, summarized without identifiers. The original 1.27.1 APK was inspected locally: its pairing parser expects a PersistableBundle, which informed the helper. That inspection was of 1.27.1 specifically, and a later session found 1.26.0 discarding the same USB-delivered bundle, so the parser finding should not be read as applying to earlier builds. Full APK decompilation and private logs are not published.

Planning received Claude and Kimi critiques. Those were reviews of supplied observations, not device tests or independent verification. The repository maintainer is responsible for the published claims.

Browser walkthrough references: [Android QR setup](https://support.google.com/work/android/answer/9566881?hl=en), [developer options](https://developer.android.com/studio/debug/dev-options), and [Xiaomi developer settings](https://www.mi.com/global/support/faq/details/KA-168765/). These references support the steps explained in this guide; reading external tutorials is not required.

The guide now documents a pinned local build and explicit USB procedure. The revised helper has host validation only so far; historical phone sessions do not validate the new code. See [release validation](helper-review.md#release-validation).

## Field observations

The September 9 and 12, 2026 records and the maintainer's review briefing support these observations. They are historical reports, not new device tests performed for this PR. No private logs or identifiers are published.

| Device | Observation | Evidence limit |
| --- | --- | --- |
| Galaxy A05 (SM-A055F), Android 14 | Owner confirmed online via USB | Earlier helper |
| Galaxy A04 (SM-A045F), Android 14 | Owner confirmed online after separate stock restore/relock; Knox remained tripped | Not a guarantee for other modified devices |
| Pixel 6 Pro, Android 14 | Owner confirmed online after a separate downgrade from Android 17 | No safe downgrade recipe inferred |
| Pixel 9 Pro Fold, Android 17 | Previous guarded helper completed pairing on 1.27.1 after 1.26.0 discarded it | Single guarded-helper device result |
| S23 Ultra (SM-S918B), Android 15 | Ownership and pairing launch recorded | Online confirmation not preserved |
| Redmi Note 13 (23124RA7EO), Android 13 / MIUI 14 | Owner confirmed online after extra USB permission and account removal | SIM-free path and permission behavior after SIM removal untested |
| Huawei Mate 20 Pro, Android 10 | APK installation failed with INSTALL_FAILED_OLDER_SDK | Result for that OS/app combination, not every possible firmware |

Samsung identifies [SM-A055F as Galaxy A05](https://www.samsung.com/in/support/model/SM-A055FLGHINS/) and [SM-A045F as Galaxy A04](https://www.samsung.com/ae/support/model/SM-A045FZKGMEA/). Earlier review shorthand calling these A05s/A04s was incorrect.

Build references: [D8](https://developer.android.com/tools/d8), [SDK packages](https://developer.android.com/tools/sdkmanager), [APK signatures](https://developer.android.com/tools/apksigner), and [Google package metadata](https://dl.google.com/android/repository/repository2-3.xml). The Core 1.27.1 asset digest was reconfirmed through the official GitHub release API on 2026-09-18.
