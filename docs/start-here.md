# Set up your phone while reading this page

**No guide download is needed. Keep this page open on your computer.** It does not install software or connect to your phone. The main route below uses the phone's built-in setup scanner; it needs no computer commands.

You can also [give the guide URL to Claude, Kimi, or Codex](ai-assisted.md) and ask for help. Direct AI control requires existing local tools and your permission.

## 1. Check what you have

- A phone you own and intend to dedicate to Acurast Core.
- Android 12 or newer, not rooted, with a locked bootloader.
- Wi-Fi and reliable power.
- A computer browser with access to your own [Acurast Hub](https://hub.acurast.com/) wallet session.

On the phone open **Settings → About phone** to find its model. Android version may be under **Software information** on Samsung or **Detailed info and specs** on Xiaomi. If startup warns that the bootloader is unlocked, stop and get model-specific help; do not change it with a generic command.

Core will take over the dedicated phone. Its official setup starts with erasing local data, so back up anything needed first. If it already runs a paired Acurast processor, do not start again. If it belongs to another organization's management system, resolve that with its administrator.

## 2. Open your Hub on the computer

1. Open your usual browser and go to [hub.acurast.com](https://hub.acurast.com/).
2. Use the wallet connection control, choose the wallet you already use, and approve the connection inside that wallet.
3. Confirm the selected account is the one you intend to use for this phone.
4. Choose **Add New Device**. Keep the displayed QR open on the computer.

Button wording can vary. If you do not yet have a supported wallet, that is a separate prerequisite; this guide does not install one or create accounts for you. Do not type wallet recovery words into a terminal, GitHub, or AI chat.

## 3. Get to the phone's welcome screen

If the phone is already at its initial welcome/language screen, skip the reset. Otherwise, **only after backing up and deciding to erase this dedicated phone**, open:

| Phone | Reset menu |
| --- | --- |
| Samsung | Settings → General management → Reset → Factory data reset |
| Pixel | Settings → System → Reset options → Erase all data (factory reset) |
| Xiaomi / Redmi / POCO | Settings → About phone → Factory reset → Erase all data; some versions use Additional settings → Backup & reset |

Read the final on-phone warning. You may need your PIN and previous account credentials after reset. If you do not have those credentials, stop before erasing.

## 4. Scan during setup

1. At the **initial welcome screen**, tap the **same blank spot six times**.
2. Android should open its setup QR scanner, or first ask you to connect to Wi-Fi. Follow that prompt.
3. Point the phone at the QR on the computer. Do not use the ordinary Camera app from an already-configured home screen.
4. Follow the on-phone download and management setup prompts.
5. Read the Acurast disclaimer and accept it if you agree.

**What is being installed?** The phone's setup flow obtains the Acurast app. That is necessary to run Acurast and is separate from reading this repository. The guide itself does not download or execute anything on your computer.

If the QR has expired, close it in Hub, generate a fresh device QR, and scan again. Do not edit its timestamp or signature. If six taps do nothing, confirm you are still on the first welcome screen rather than the regular home screen.

## 5. Confirm success

Keep the phone on Wi-Fi and power. In the computer browser, close the QR panel if needed and inspect your Hub's processor list. Confirm the new phone appears under the intended wallet and shows online. Allow the display to update; refresh if necessary.

An installed app is not enough. **Finished means your intended processor is online in your Hub.** If a disclaimer remains on the phone, read it and complete the relevant prompt yourself.

## 6. If Samsung blocks installation

Write down the exact warning first. If you can reach the ordinary Android home screen/Settings, inspect:

1. **Settings → Security and privacy → Auto Blocker.** If it is blocking the verified Acurast setup, you can switch it off after reading its confirmation. Older models may not have this option.
2. **Play Store → profile circle → Play Protect → settings gear.** Our setup used **Improve harmful app detection off**, followed by **Scan apps with Play Protect off**. If asked Pause or Turn off, the recorded choice was **Turn off**.
3. Verify the actual switches. Do not uninstall or disable the whole Play Store.

Those changes reduce scanning/blocking. They describe our tested preparation, not a guarantee that every phone needs them. A factory reset can restore defaults, so changing them and resetting again may not solve welcome-screen QR blocking.

If you are already at the home screen and need the community USB alternative, use [AI-assisted help](ai-assisted.md) with existing local tools. An ordinary camera scan or manual APK install does not replace Core's ownership and pairing steps. Do not repeatedly reset without identifying the blocker.

## 7. If Xiaomi blocks USB or asks for a SIM

This section applies to the **USB alternative**, not a requirement to enable debugging before normal welcome-screen QR setup.

On our Xiaomi, ordinary USB debugging permitted reading the phone but did not permit ownership changes. Here is the menu sequence:

1. Settings → About phone → Detailed info and specs / All specs → tap **OS version / MIUI version seven times**.
2. Settings → Additional settings → Developer options → turn on **USB debugging**.
3. Also enable **Install via USB** and **USB debugging (Security settings)**.
4. If Xiaomi asks for account sign-in and a SIM, handle those on the phone. In our session they were required; no SIM-free fix was verified.
5. After enabling permissions, remove setup accounts from this phone before device-owner registration: Settings → Accounts & sync → Google → account → More → Remove account; and Settings → Xiaomi Account → Sign out.

Removing an account from the phone removes locally synced data, not the cloud account. Preserve unsynced data first. Enter passwords on the phone. Verify the extra USB permission still works afterward. Do not enable OEM unlocking or Mi Unlock.

A manually installed APK solved only installation in our Xiaomi case. It did not resolve the extra USB permission or device-owner requirement. Do not call the setup finished at that point.

## 8. Optional checks with tools already on your computer

If you do not already have Google's ADB tool, skip these commands and use the normal QR route or ask your assistant to explain the limitation. **This guide does not ask you to install computer tools.**

Where commands go:

- **Mac:** Command+Space → type Terminal → Enter.
- **Windows:** Start → type PowerShell → open Windows PowerShell.
- **Ubuntu:** Ctrl+Alt+T to open Terminal.

Connect the intended phone with a data cable. For Samsung enable debugging through Settings → About phone → Software information → tap Build number seven times → Settings → Developer options → USB debugging. For Pixel use Settings → About phone → tap Build number seven times → System → Developer options → USB debugging. Xiaomi uses section 7.

Unlock the phone and accept **Allow USB debugging?** for your trusted computer. Paste this in the computer terminal and press Enter:

```sh
adb devices -l
```

A made-up success example:

```text
List of devices attached
EXAMPLE123    device product:example model:ExamplePhone
```

Your first value is the serial. Keep it private. The next word must be `device`. If it says `unauthorized`, accept the prompt on the unlocked phone. If the list is empty, try another data cable/port and verify debugging. If the computer says `adb` is not recognized, the tool is unavailable in that terminal; do not paste random installer commands.

For the next checks, replace **YOUR_SERIAL** in each line with your actual serial (do not type the made-up example):

```sh
adb -s YOUR_SERIAL shell getprop ro.product.model
adb -s YOUR_SERIAL shell getprop ro.build.version.release
adb -s YOUR_SERIAL shell getprop ro.boot.flash.locked
adb -s YOUR_SERIAL shell getprop ro.boot.verifiedbootstate
adb -s YOUR_SERIAL shell dpm list-owners
```

Run one line at a time. These read state; they do not install or manage the phone. Expect your model, Android version, and—on our stock devices—`1` and `green` for the boot indicators. Empty/unknown is not proof of eligibility. `no owners` means none reported; permission denial does not mean there is no owner. Redact identifiers before sharing output.

## 9. Find your problem

| What you see | Next action |
| --- | --- |
| Welcome screen QR scanner does not open | Confirm initial setup screen and same-spot six taps; do not use the normal Camera scanner |
| QR expired | Generate a new QR in your own Hub |
| Samsung blocked app/USB | Inspect Auto Blocker and the exact message; section 6 |
| Xiaomi requests SIM/account | Follow section 7; no verified SIM-free USB workaround is recorded |
| `unauthorized` in ADB | Unlock phone and accept USB debugging prompt |
| Empty ADB device list | Check cable supports data, USB port, debugging, and on-phone prompt |
| `adb` not found | Existing computer tools are insufficient; use QR route or ask for help, not an unapproved download |
| `Calling identity is not authorized` | Xiaomi's extra USB security permission fixed our instance; ordinary USB debugging was insufficient |
| `already some accounts on the device` | Remove setup accounts normally from the phone, preserving unsynced data |
| Already managed by another owner | Stop and resolve with the current legitimate management process |
| APK installed, Hub still empty | Installation, device owner and pairing are separate; ask for help with the exact stage |
| USB disappeared after Core launch | Inspect phone and Hub; normal lockdown can disconnect it, but that alone is not success |
| Hub stays offline | Check intended wallet, phone Wi-Fi, disclaimer and exact error; avoid repeated reset/owner/pairing attempts |

For help, tell your assistant the phone model, Android version, last successful step and exact error. Never send recovery words, passwords, a real QR, or unreviewed account/log dumps to a public issue.

You can stay in this repository: [AI help](ai-assisted.md) · [more error explanations](troubleshooting.md) · [USB method limits](usb-onboarding.md). Official references for the summarized route: [Acurast](https://docs.acurast.com/processors/become-compute-provider/) and [Android QR setup](https://support.google.com/work/android/answer/9566881?hl=en).
