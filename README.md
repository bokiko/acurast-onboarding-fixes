# Acurast Core onboarding guide

Practical setup notes for turning a dedicated Android phone into an **Acurast Processor Core**. Built from real Samsung, Xiaomi, and Pixel onboarding sessions, including the errors that took the longest to resolve.

**Community documentation, not an official Acurast product or compatibility certification.** The USB pairing helper is unofficial and version-sensitive. This guide is for phones you own and intend to dedicate to Core; Core lockdown can disable normal phone access and USB debugging.

## Choose your next step

| What you see | Start here |
| --- | --- |
| New to Core or phone at the welcome screen | [Official onboarding route](docs/official-route.md) |
| APK or USB commands blocked on Samsung | [Samsung notes](docs/samsung.md) |
| Xiaomi asks for a SIM/account or rejects USB commands | [Xiaomi notes](docs/xiaomi.md) |
| Using a Pixel | [Pixel notes](docs/pixel.md) |
| Official onboarding failed and you have working ADB | [Community USB procedure](docs/usb-onboarding.md) |
| An exact error or no online status | [Troubleshooting](docs/troubleshooting.md) |
| Rooted, modified, or stuck after provisioning | [Recovery boundaries](docs/recovery.md) |

**Installing an APK, becoming device owner, and pairing to the Hub are separate steps.** A successful install or a disappearing USB connection does not prove the processor is online.

## Before you start

Acurast currently lists Android 12+, a non-rooted device, and a locked bootloader. Its official Core route starts with a factory reset. See the [upstream requirements](https://docs.acurast.com/processors/become-compute-provider/). Back up anything needed before dedicating the phone. Have reliable power, internet, a data-capable USB cable for the fallback, and access to your own [Acurast Hub](https://hub.acurast.com/).

For a first diagnosis, install Google's [Platform Tools](https://developer.android.com/tools/releases/platform-tools), connect and authorize the phone, then run:

```sh
adb devices -l
python3 tools/diagnose.py --serial YOUR_DEVICE_SERIAL
```

The diagnostic reads selected state only. It does not install, remove accounts, change settings, pair, or reset. Unknown readings are shown as unknown, not as a pass.

## Field results

Recorded 2026-09-09 using Core **1.27.1 (136)** and the community USB method. These are single-session observations, not promises for other firmware or future versions.

| Device | Android | Preserved result | Notes |
| --- | --- | --- | --- |
| Samsung SM-A055F | 14 | User confirmed online | Core USB setup |
| Google Pixel 6 Pro | 14 | User confirmed online | Core USB setup |
| Samsung SM-A045F | 14 | User confirmed online | Separate stock restoration and relock first; Knox bit remained tripped |
| Samsung SM-S918B | 15 | Device owner and pairing launch confirmed | Independent online confirmation not preserved |
| Xiaomi 23124RA7EO | 13 / MIUI 14 | User confirmed online | SIM/account enabled extra USB permission; accounts removed before owner setup |

The hardened public helper is build-tested, but has **not yet been rerun end to end on a spare phone**. The original helper's mechanism worked in these sessions. See [review and limits](docs/helper-review.md) and [verified downloads](docs/downloads.md).

## What is included

Manual instructions, error-specific remedies, a redacted read-only diagnostic, and source/build instructions for the community pairing helper. No APKs, real QR codes, pairing payloads, private account data, firmware, or device backups are distributed.

[Contribute a result](CONTRIBUTING.md) · [Sources and verification](docs/sources.md) · [Helper build](tools/README.md)
