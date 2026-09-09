# Start here: set up your phone without coding experience

This page walks you from an unprepared phone to checking it online in Acurast Hub. Keep it open on your **computer** while you work on the **phone**. You do not need to understand programming or install Android Studio.

There are two routes: **QR setup at the phone's welcome screen**, and **USB setup if QR setup is blocked**. Try the first route when possible. USB setup uses this project's unofficial helper. The original method worked in our field sessions; the published helper's added checks have not yet been retested through a full phone onboarding. A successful computer check is not a guarantee of online registration.

**Want less terminal work? [Use a local AI assistant](ai-assisted.md).** Claude, Kimi, or Codex can follow our [instruction file](../AI-ONBOARDING.md) and run computer steps when local access is available. You still handle private sign-in, physical prompts, and final confirmation.

## Find your place

1. [What you need](#1-what-you-need)
2. [Try the welcome-screen QR route](#2-try-the-welcome-screen-qr-route)
3. [Prepare your computer for USB setup](#3-prepare-your-computer-for-usb-setup)
4. [Prepare your phone](#4-prepare-your-phone)
5. [Connect and check the phone](#5-connect-and-check-the-phone)
6. [Download and install the verified Acurast app](#6-download-and-install-the-verified-acurast-app)
7. [Build the small pairing helper](#7-build-the-small-pairing-helper)
8. [Get and save your QR data](#8-get-and-save-your-qr-data)
9. [Check pairing before changing ownership](#9-check-pairing-before-changing-ownership)
10. [Give Core control of the dedicated phone](#10-give-core-control-of-the-dedicated-phone)
11. [Finish pairing and check online](#11-finish-pairing-and-check-online)
12. [Clean up private setup files](#12-clean-up-private-setup-files)
13. [Something went wrong: find your message](#13-something-went-wrong-find-your-message)

## 1. What you need

- A phone you own, dedicated to Acurast. Core takes over the phone; getting back to normal use may require erasing it.
- Android 12 or newer, not rooted, with its bootloader locked. If you bought it used and it shows an unlocked-bootloader warning at startup, stop before USB setup. This guide does not repair modified firmware.
- Wi-Fi, a charger, and for USB setup a cable that transfers data. Some cables charge only.
- A Mac, Windows 10/11 **Intel/AMD 64-bit** PC, or Ubuntu **Intel/AMD 64-bit** computer for the USB instructions below. Windows ARM, other Linux distributions, and Chromebooks do not have a complete computer-setup walkthrough here.
- Access to your wallet in [Acurast Hub](https://hub.acurast.com/). Open that link in your normal computer browser, click the wallet connection control, choose the wallet you already use, and approve the connection in its wallet window. Confirm the selected account is the one you intend to use. Keep recovery words and passwords private.

**No wallet yet?** You will need to create one before pairing. On the Hub's wallet connection screen, choose a supported wallet and use its official installation link. In the wallet's own setup choose **Create a new wallet**, follow its backup and recovery-word confirmation screens, and store the recovery words offline. Return to Hub and connect that wallet. Wallet interfaces vary; do not enter recovery words into this repository or a terminal. Wallet creation/signing stays inside the wallet app, not a guide command.

Back up any personal files before dedicating the phone. Do not factory-reset a phone if you do not know the credentials needed to reactivate it. If your phone already works as an Acurast processor, stop: these steps are for onboarding, not repairing or replacing an existing processor identity.

**Four words used below:** an **APK** is an Android app installation file; **ADB** is Google's USB communication tool; a **terminal** is a computer window where you paste commands; **device owner** means the app that manages this dedicated phone.

## 2. Try the welcome-screen QR route

**On the computer:** open [Acurast Hub](https://hub.acurast.com/), connect your wallet, and choose **Add New Device** (wording may be “add device” or “onboard”). Keep the QR visible. It has an expiry time.

**On the phone:** it needs to be at the first welcome/language screen after a factory reset for this route. If it is already there, do not reset again. If a reset is needed, back up first, then use:

| Phone | Settings path to reset |
| --- | --- |
| Samsung | Settings → General management → Reset → Factory data reset |
| Pixel | Settings → System → Reset options → Erase all data (factory reset) |
| Xiaomi / Redmi / POCO | Settings → About phone → Factory reset → Erase all data; some versions place this under Additional settings → Backup & reset |

Read the phone's confirmation before erasing. Account verification may still be required afterward.

1. At the initial welcome screen, tap the **same blank spot six times** to open Android's setup QR scanner. Do this before completing normal phone setup; do not use the ordinary Camera app.
2. If asked, connect to Wi-Fi and allow the setup scanner to prepare. Prompt order varies.
3. Scan the QR shown on the computer and follow the download/setup screens.
4. Read the Acurast disclaimer and accept it if you agree.
5. Look in the Hub for the new processor and its online status. If it is online, you are finished; skip the USB route.

If six taps do nothing, confirm you are on the initial welcome screen. If the phone is already at its home screen, the normal Camera scanner will not turn it into a managed Core device. Use the USB route below if it is suitable, rather than repeatedly resetting.

**If installation is blocked:** write down the exact message. For the USB route, finish the phone's normal setup to reach its home screen, connect Wi-Fi, and skip optional Google/vendor account sign-in where possible. Xiaomi may need an account later to enable its extra USB permission. If the phone is stuck in organization-managed setup and cannot reach normal Settings, do not try to remove that management with this guide.

The six-tap gesture comes from Android's [documented QR setup method](https://support.google.com/work/android/answer/9566881?hl=en); the Core factory-reset/Hub route comes from [Acurast](https://docs.acurast.com/processors/become-compute-provider/). You do not need to read those references to follow the steps above.

## 3. Prepare your computer for USB setup

Expand **only your computer's box**. The tools download onto your computer, not the phone. Downloads may take several minutes.

### How to paste commands

Use the code box's copy button, paste into the command window named below, then press **Enter**. Copy commands, not example output. Run one box at a time. Wait until the cursor returns to a new prompt before the next box. A box may print nothing and still succeed; we say when that is expected. If a command reports an error, use section 13 before continuing.

Keep the **same command window open** for the entire setup. Its temporary settings disappear when you close it. Do not use a Python window showing `>>>`; type `exit()` there and open the terminal described below.

<details>
<summary><strong>I use a Mac — click to expand</strong></summary>

**A. Install Python.** Click [Python 3.14.7 for Mac (.pkg)](https://www.python.org/ftp/python/3.14.7/python-3.14.7-macos11.pkg). Open the downloaded file and follow Continue → Install. After installation, open Finder → Applications → Python 3.14 and double-click **Install Certificates.command** if present. This prepares secure downloads used later.

**B. Install Java 17.** Open Apple menu → About This Mac. If it says **Chip: Apple M…**, use [Java 17 for Apple silicon](https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.20.1%2B1/OpenJDK17U-jdk_aarch64_mac_hotspot_17.0.20.1_1.pkg). If it says **Processor: Intel**, use [Java 17 for Intel Mac](https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.20.1%2B1/OpenJDK17U-jdk_x64_mac_hotspot_17.0.20.1_1.pkg). Open the `.pkg` and follow the installer. Java prepares our small helper; you will not write Java code.

**C. Download two ZIP files.** Click [Google USB tools for Mac](https://dl.google.com/android/repository/platform-tools-latest-darwin.zip) and [this guide's files](https://github.com/bokiko/acurast-core-onboarding-guide/archive/refs/heads/main.zip). Open Finder → Downloads. Double-click each ZIP if your browser has not already extracted it. You need two actual folders named `platform-tools` and `acurast-core-onboarding-guide-main` directly in Downloads. If a second download adds `-2`, rename the newly extracted folder to the exact name used here; do not overwrite an older folder containing private files.

**D. Open Terminal.** Press **Command + Space**, type **Terminal**, then press Enter. Paste:

```sh
cd "$HOME/Downloads/acurast-core-onboarding-guide-main"
export PATH="$HOME/Downloads/platform-tools:$PATH"
export JAVA_HOME="$(/usr/libexec/java_home -v 17)"
export PATH="$JAVA_HOME/bin:$PATH"
python3 --version
javac -version
adb version
```

You should see Python 3, `javac 17...`, and `Android Debug Bridge version...`. These commands set up only this Terminal window. If macOS asks to install Command Line Tools instead of showing Python, finish the Python installer and reopen Terminal first.

</details>

<details>
<summary><strong>I use Windows 10/11 (Intel/AMD 64-bit) — click to expand</strong></summary>

**A. Install Python.** Click [Python 3.14.7 for Windows (.exe)](https://www.python.org/ftp/python/3.14.7/python-3.14.7-amd64.exe). Open it. Tick **Add python.exe to PATH** and leave the Python launcher enabled, then choose Install Now. If the installer offers Modify instead, Python may already be installed; the version check below will tell you.

**B. Install Java 17.** Click [Java 17 for Windows (.msi)](https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.20.1%2B1/OpenJDK17U-jdk_x64_windows_hotspot_17.0.20.1_1.msi). Open it and follow Next. In Custom Setup, keep **Add to PATH** enabled and enable **Set JAVA_HOME variable** if available. Install, then close any old command windows.

**C. Download and extract.** Click [Google USB tools for Windows](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) and [this guide's files](https://github.com/bokiko/acurast-core-onboarding-guide/archive/refs/heads/main.zip). In File Explorer → Downloads, right-click each ZIP → Extract All. Choose Downloads as the destination so the actual folders are:

- `Downloads\platform-tools` (contains `adb.exe`)
- `Downloads\acurast-core-onboarding-guide-main` (contains `README.md` and `tools`)

Windows sometimes adds an extra outer folder named after the ZIP. If so, move the inner folder directly into Downloads. Do not run files from inside the ZIP preview.

**D. Open PowerShell.** Press Start, type **PowerShell**, and open **Windows PowerShell**. Do not open Command Prompt, Python, or “Run as administrator.” Paste:

```powershell
Set-Location "$HOME\Downloads\acurast-core-onboarding-guide-main"
$env:Path = "$HOME\Downloads\platform-tools;" + $env:Path
function python3 { py -3 @args }
python3 --version
javac -version
adb version
```

You should see Python 3, `javac 17...`, and `Android Debug Bridge version...`. The small `python3` function makes later commands work in this PowerShell window. It runs the installed Python launcher; it does not install another Python. If `py` is missing but `python --version` works, use `function python3 { python @args }` instead.

If Java is missing, reopen PowerShell after installation and repeat this box. If it remains missing, open the Java installer → Change/Modify and enable its PATH feature.

**USB driver only if the phone is not detected later:** Samsung users can download the [official Samsung Windows driver](https://developer.samsung.com/android-usb-driver). Open that page, click the driver download button, open the installer and finish it, then reconnect. For other phones, try Settings → Windows Update → Advanced options → Optional updates → Driver updates. Avoid random driver download sites. More detection steps are in section 13.

</details>

<details>
<summary><strong>I use Ubuntu (Intel/AMD 64-bit) — click to expand</strong></summary>

Open Terminal with **Ctrl + Alt + T**. Install the tools from Ubuntu's repositories:

```sh
sudo apt update
sudo apt install python3 openjdk-17-jdk adb android-sdk-platform-tools-common unzip
```

`sudo` may ask for your computer password. Nothing appears while you type it; press Enter afterward. This installs computer tools, not phone apps. The `android-sdk-platform-tools-common` package provides USB permission rules on Ubuntu.

Download [this guide's ZIP](https://github.com/bokiko/acurast-core-onboarding-guide/archive/refs/heads/main.zip) in your browser. Open Files → Downloads, right-click the ZIP and extract it. Ensure `acurast-core-onboarding-guide-main` is directly in Downloads. Then paste in Terminal:

```sh
cd "$HOME/Downloads/acurast-core-onboarding-guide-main"
export JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
export PATH="$JAVA_HOME/bin:$PATH"
python3 --version
javac -version
adb version
```

Expect Python 3, `javac 17...`, and an Android Debug Bridge version. This path is for Ubuntu Intel/AMD 64-bit only. If installation says a package is unavailable, stop and report your Ubuntu version rather than substituting untrusted packages.

</details>

**All three version checks passed?** Continue below. You do not need Git, Homebrew, Android Studio, or a code editor. Mac was used for the recorded phone sessions; Windows and Ubuntu instructions and the build are provided, but their full phone-onboarding paths have not been physically reproduced by this project.

## 4. Prepare your phone

**On the phone**, get to its home screen and connect to Wi-Fi. Open Settings → About phone and check Android version (Samsung may put it under Software information). Use only a dedicated phone meeting section 1.

### Enable USB debugging

| Phone | What to tap |
| --- | --- |
| Samsung | Settings → About phone → Software information → tap **Build number seven times** → enter phone PIN if asked → back to main Settings → Developer options → **USB debugging on** |
| Pixel | Settings → About phone → tap **Build number seven times** → enter PIN if asked → Settings → System → Developer options → **USB debugging on** |
| Xiaomi / Redmi / POCO | Settings → About phone → Detailed info and specs / All specs → tap **OS version or MIUI version seven times** → Settings → Additional settings → Developer options → **USB debugging on** |

If the menu says developer mode is already enabled, stop tapping and open Developer options. “Debugging” here means allowing this computer to communicate with the phone. Do **not** enable OEM unlocking or Mi Unlock.

### Samsung: check Auto Blocker

Settings → Security and privacy → Auto Blocker. If present and it blocks outside-store installation or USB commands, switch the master control **off** and confirm. Its restrictions include USB commands and app installs. If Maximum restrictions is present, inspect it too. Older phones may not have this feature; do not search for an app to add it.

### Xiaomi: enable the second USB switch

In Developer options also enable **Install via USB** and **USB debugging (Security settings)**. Ordinary USB debugging alone was not enough on our MIUI 14 phone.

If asked, sign into your Xiaomi account on the phone and insert a SIM to satisfy its prompt. In our session those extra requirements were real; we have no verified SIM-free workaround for that phone. A SIM temporarily moved from your other phone may be an option. We did not test removing it after onboarding. Do not sign into Mi Unlock or unlock the bootloader.

If a SIM/account cannot be supplied and the extra switch remains blocked, stop the USB method here. Manually installing the APK will not fix the missing device-owner permission.

### All phones: inspect Play Protect

Our recorded setup had these two Google switches off. This reduces app scanning; we did not prove both are required on every phone or test turning them back on after Core lockdown.

1. Open **Play Store** on the phone.
2. Tap the profile circle at top right → **Play Protect** → settings gear.
3. Turn **Improve harmful app detection** off first.
4. Turn **Scan apps with Play Protect** off.
5. If asked “Pause app scanning instead?”, choose **Turn off**, not Pause.
6. Verify both switches are off. Do not uninstall or disable the entire Play Store.

If Play Store only asks you to sign in, do not add a Google account just for this screen. After section 5 connects ADB, use this command in your computer's terminal to open Play Protect directly:

```sh
adb -s $ACURAST_SERIAL shell am start -a com.google.android.gms.settings.VERIFY_APPS_SETTINGS
```

If that Android action is unavailable on your version, use the Play Store menu. Return to section 6 once preparation is complete.

### Remove setup accounts before device-owner setup

Do this **after** Xiaomi's permission setup. Removing an account from the phone removes its locally synced data; it does not delete the cloud account. Preserve unsynced files first.

| Phone | What to tap |
| --- | --- |
| Samsung | Settings → Accounts and backup → Manage accounts → choose each setup account → Remove account |
| Pixel | Settings → Passwords & accounts (or Passwords, passkeys & accounts) → account → Remove account |
| Xiaomi Google account | Settings → Accounts & sync → Google → select account if listed → More → Remove account → confirm |
| Xiaomi account | Settings → Xiaomi Account → scroll to **Sign out** → finish any password or local-data confirmation on the phone |

Do not publish your account screen. Section 5's diagnostic checks the count without printing the addresses. If these are accounts you need on your daily phone, stop and use another dedicated device.

## 5. Connect and check the phone

Connect **only the phone you are setting up** to the computer. Unlock its screen. If Android asks **Allow USB debugging?**, check “Always allow from this computer” only if this is your trusted computer, then tap **Allow**. Choosing File transfer from the USB notification may help establish the data connection; it does not replace the debugging authorization.

**In the same computer terminal**, paste:

```sh
adb devices -l
```

A made-up example of good output is:

```text
List of devices attached
EXAMPLE123    device product:example model:ExamplePhone
```

Your first value will be different. It is the phone's **serial**. The word after it must be `device`. If it says `unauthorized`, unlock the phone and accept the prompt. If there is no row, use section 13.

Tell this terminal which phone to use. **Replace `YOUR_SERIAL_HERE` with your actual first value**, keeping the quotes:

**Mac / Ubuntu:**

```sh
ACURAST_SERIAL='YOUR_SERIAL_HERE'
```

**Windows PowerShell:**

```powershell
$ACURAST_SERIAL='YOUR_SERIAL_HERE'
```

Both commands normally print nothing. Now all computer types run the same diagnostic:

```sh
python3 tools/diagnose.py --serial $ACURAST_SERIAL
```

What to check:

| Output line | What you want / what to do |
| --- | --- |
| Model | Must be the phone in your hand |
| Android | 12 or newer |
| Boot flash locked | `1` is a useful indicator; unknown is not a pass |
| Verified boot | `green` was observed on our stock devices; a property alone does not prove eligibility |
| Accounts across reported users | `0`; otherwise return to account removal in section 4 |
| Management | `none reported`; existing management needs investigation before proceeding |
| Core version | “not found / unknown” is normal before installation |
| Exact alarm appop | Unknown/default is normal at this point |

If Xiaomi prints `Calling identity is not authorized`, return to its **USB debugging (Security settings)** switch. Do not treat permission-denied account/owner readings as zero. The diagnostic never changes the phone.

## 6. Download and install the verified Acurast app

**In the computer terminal**, run this box. It downloads from Acurast's official GitHub release into the guide's local `build` folder and verifies the exact file hash. It can take several minutes; wait for the success line.

```sh
python3 -c "import pathlib,urllib.request,hashlib; p=pathlib.Path('build/processor-1.27.1.apk'); p.parent.mkdir(exist_ok=True); print('Downloading official Core APK, please wait...',flush=True); urllib.request.urlretrieve('https://github.com/Acurast/acurast-processor-update/releases/download/processor-1.27.1/processor-1.27.1.apk',p); actual=hashlib.sha256(p.read_bytes()).hexdigest(); expected='7bb39cf9f6922c4c67f1b9b5a38303ba8a93b0ce195586613da7707b69a6744c'; print('APK VERIFIED' if actual==expected else 'STOP: APK HASH MISMATCH'); raise SystemExit(0 if actual==expected else 1)"
```

**Continue only if it says `APK VERIFIED`.** The exact asset is `processor-1.27.1.apk`, not Lite or the separate `-canary.apk`. The installed package happens to end in `.canary`; do not guess the download from that suffix. Version 1.27.1 is the version we verified and used, not a claim that it is the latest. Do not downgrade an existing installation.

Now install it:

```sh
adb -s $ACURAST_SERIAL install build/processor-1.27.1.apk
```

**Success looks like:** `Performing Streamed Install`, then `Success`. Watch the phone for an installation prompt. Do not open Core yet.

**If Xiaomi blocks USB installation**, copy the already-verified file to the phone:

```sh
adb -s $ACURAST_SERIAL push build/processor-1.27.1.apk /sdcard/Download/Acurast-Core-1.27.1.apk
```

On the phone open **File Manager → Downloads → Acurast-Core-1.27.1.apk**. If asked, allow File Manager to install unknown apps, return to the file, and tap Install. Choose Done rather than Open. This only solves the installation step; the extra USB security permission is still required later.

Verify the installed version with:

```sh
python3 tools/diagnose.py --serial $ACURAST_SERIAL
```

**Continue when `Core version: 1.27.1` appears** and the account and management checks are still ready. For hash/download errors, use section 13; do not ignore the mismatch.

## 7. Build the small pairing helper

“Build” just means the computer prepares a small file the phone can run. You do not edit code. In the terminal:

```sh
python3 tools/build.py
```

It downloads three verified build dependencies and creates `build/helper.zip`. Expect:

```text
All build dependency hashes verified
BUILD OK: build/helper.zip is ready. No phone settings were changed.
```

A Java warning mentioning “bootstrap class path” may appear; the final `BUILD OK` is what matters. If it says `BUILD FAILED`, stop and use section 13. This helper delivers your pairing data; it does not download Core, remove accounts, or connect Wi-Fi for you.

## 8. Get and save your QR data

Wait until this step to create fresh pairing data so you do not use up its expiry time while installing computer tools.

**In the computer browser:**

1. Open [Acurast Hub](https://hub.acurast.com/) and connect your intended wallet.
2. Select **Add New Device** and show the new QR.
3. If **Advanced** is collapsed, open it. For this USB route the custom APK URL is not used; Core is already installed. Do not change Wi-Fi fields as a substitute for connecting the phone to Wi-Fi yourself.
4. Note the displayed **Expires at** time. The helper accepts the recorded single-device format; do not choose a different batch format.
5. Click **Copy QR Data**. Keep this data private. It should be JSON text, not a screenshot or just an APK link.

**Back in the terminal**, create a private folder outside the guide:

```sh
python3 -c "from pathlib import Path; p=Path.home()/'AcurastPrivate'; p.mkdir(exist_ok=True); print('Private folder ready')"
```

Now save the copied data using **only your computer's box**. These commands copy the clipboard to a file without pasting its contents into shell history.

**Mac:**

```sh
pbpaste > "$HOME/AcurastPrivate/provisioning.json"
chmod 600 "$HOME/AcurastPrivate/provisioning.json"
ACURAST_PAIRING="$HOME/AcurastPrivate/provisioning.json"
```

**Windows PowerShell:**

```powershell
$ACURAST_PAIRING = "$HOME\AcurastPrivate\provisioning.json"
[System.IO.File]::WriteAllText($ACURAST_PAIRING, (Get-Clipboard -Raw), (New-Object System.Text.UTF8Encoding($false)))
```

**Ubuntu:** Open the Text Editor app from Activities. Create a new document, paste with Ctrl+V, choose Save As, open your Home folder → AcurastPrivate, and name the file **provisioning.json** (not `.txt`). Return to Terminal:

```sh
chmod 600 "$HOME/AcurastPrivate/provisioning.json"
ACURAST_PAIRING="$HOME/AcurastPrivate/provisioning.json"
```

**All computer types:** check the file without printing its secret values:

```sh
python3 tools/validate_pairing.py "$ACURAST_PAIRING"
```

Success says `Structure checked; age ... minutes`. It also says the signature is **NOT verified**. This check only catches formatting/time problems; obtain data from your own Hub and confirm its account and displayed expiry yourself. If it fails, copy fresh QR data and repeat this step. Do not edit timestamps, signatures, or field names to force a pass.

## 9. Check pairing before changing ownership

In the terminal, run each line and wait for it to finish:

```sh
adb -s $ACURAST_SERIAL push build/helper.zip /data/local/tmp/acurast-core-helper.zip
adb -s $ACURAST_SERIAL push "$ACURAST_PAIRING" /data/local/tmp/acurast-pairing.json
adb -s $ACURAST_SERIAL shell chmod 600 /data/local/tmp/acurast-pairing.json
```

The first two lines should say a file was pushed. The third normally prints nothing. Now check the helper on the phone:

```sh
adb -s $ACURAST_SERIAL shell 'CLASSPATH=/data/local/tmp/acurast-core-helper.zip app_process /system/bin CoreProvision /data/local/tmp/acurast-pairing.json check'
```

The important final line is:

```text
Check only: app not launched, settings unchanged.
```

If it fails, do not continue to ownership. Repeat section 8 if the data is old or incorrectly saved, confirm the phone's date/time, and see section 13. This check does not prove that the Hub will accept pairing.

## 10. Give Core control of the dedicated phone

This is the point where Core becomes the phone's manager. Use a backed-up, dedicated phone. Once lockdown happens, ordinary Settings and USB access may disappear; returning it to normal use may require a reset.

In the terminal, run:

```sh
adb -s $ACURAST_SERIAL shell am force-stop com.acurast.attested.executor.canary
adb -s $ACURAST_SERIAL shell appops set com.acurast.attested.executor.canary SCHEDULE_EXACT_ALARM allow
```

Normally these print nothing. If either reports an error, stop. Now run:

```sh
adb -s $ACURAST_SERIAL shell dpm set-device-owner com.acurast.attested.executor.canary/com.acurast.attested.executor.lockdown.LockdownDeviceAdminReceiver
```

**You must see `Success: Device owner set to package ...`.** If you see an accounts error, remove the accounts as described in section 4. If you see `Calling identity is not authorized`, check Xiaomi's extra security switch. Do not run pairing until owner registration succeeds.

Check ownership:

```sh
adb -s $ACURAST_SERIAL shell dpm list-owners
```

Expect one owner mentioning `com.acurast.attested.executor.canary` and `DeviceOwner`. If this read is denied even though registration explicitly succeeded, keep the exact messages for a help report; do not guess that no owner exists.

## 11. Finish pairing and check online

Check the Hub QR has not expired, then run:

```sh
adb -s $ACURAST_SERIAL shell 'CLASSPATH=/data/local/tmp/acurast-core-helper.zip app_process /system/bin CoreProvision /data/local/tmp/acurast-pairing.json launch'
```

`Activity launch result: 0` means Android opened the requested app. It does **not** yet mean online.

**Look at the phone.** Read and accept the disclaimer if shown and you agree. Core may turn off USB debugging; the computer losing the connection at this moment happened in our successful sessions. Keep power and Wi-Fi connected.

**Look at the browser's Hub.** Close the QR panel with its X if it remains open and inspect your processor list. Confirm the new processor belongs to the wallet you intended and shows online. Allow the display to update; refresh if needed. If it remains offline, check the actual phone message and section 13. Do not reset or repeatedly pair merely because USB disappeared.

**Finished means the intended processor is online in your Hub.** Installed app, owner success, and USB disconnection are intermediate observations.

## 12. Clean up private setup files

After confirmed online—or after an aborted attempt when you no longer need the files—remove the private QR data from your computer. In the terminal:

```sh
python3 -c "from pathlib import Path; p=Path.home()/'AcurastPrivate'/'provisioning.json'; p.unlink(missing_ok=True); print('Private pairing file removed from this computer')"
```

Clear the clipboard by copying an ordinary word. Delete any QR screenshots you saved; if your clipboard manager keeps history, delete that entry there too. These steps are normal deletion, not a promise of secure erasure from backups or clipboard history.

If the phone still allows ADB, remove its staged files:

```sh
adb -s $ACURAST_SERIAL shell rm -f /data/local/tmp/acurast-pairing.json /data/local/tmp/acurast-core-helper.zip
```

If it says device not found after Core lockdown, cleanup on the phone may no longer be possible. The helper does not automatically erase those staged files. Do not claim they were removed just because the phone is online.

## 13. Something went wrong: find your message

Stop at the failing step. You do not need to understand the whole error; use its matching row.

| What you see | What to do |
| --- | --- |
| `cd` / `Set-Location`: folder not found | Open Downloads and check the guide folder is extracted, not still a ZIP, and named exactly `acurast-core-onboarding-guide-main`. Repeat section 3's terminal box. |
| Python window shows `>>>` | Type `exit()`; open Terminal on Mac/Ubuntu or PowerShell on Windows. Commands go there. |
| `python3` / `py` not found | Finish the Python installer. Reopen the command window. On Windows repeat the `function python3` line in section 3. |
| `javac` missing / `BUILD FAILED` | Install **JDK 17**, not only a Java runtime. Reopen the command window and repeat section 3's environment commands. Check `javac -version` shows 17. |
| `adb` not found / not recognized | Check the extracted `platform-tools` folder contains `adb` or `adb.exe`; repeat section 3's PATH line. On Ubuntu finish the package installation. |
| Empty device list | Unlock phone, enable USB debugging, reconnect, try a different data cable and port, then `adb devices -l` again. On Windows check the driver instructions in section 3. |
| `unauthorized` | Watch the unlocked phone for “Allow USB debugging?” and accept. If absent, disconnect/reconnect; in Developer options revoke USB debugging authorizations and reconnect to get a fresh prompt. |
| `offline` | Reconnect the cable and rerun `adb devices -l`. If still offline, run `adb kill-server`, then `adb start-server`, and authorize again. This restarts the computer's ADB service, affecting other ADB sessions too. |
| Ubuntu `no permissions` | Confirm `android-sdk-platform-tools-common` installed, unplug/replug, and log out/in if needed. Do not run the whole guide as root. |
| More than one device / wrong phone | Unplug the others, read `adb devices -l`, and set the serial again in section 5. |
| Variable missing / device not found after opening new terminal | The terminal forgot its temporary settings. Repeat section 3's command box, section 5's serial assignment, and section 8's file-path assignment. Do not re-register ownership if it already succeeded. |
| `INSTALL_FAILED_USER_RESTRICTED` | Look at the phone for a blocked install/prompt. Follow Samsung Auto Blocker or Xiaomi extra USB permission instructions; the manual APK route is in section 6. |
| `INSTALL_FAILED_VERSION_DOWNGRADE` | A newer app is already installed. Stop; do not force downgrade or erase an existing processor. Report its version. |
| `Calling identity is not authorized` / `INJECT_EVENTS` | On our Xiaomi this required **USB debugging (Security settings)**, including its account/SIM prompt. Ordinary USB debugging was insufficient. |
| `already some accounts on the device` | Remove Google/vendor setup accounts through the phone's Settings using section 4; rerun the diagnostic until zero is reported, then retry the failed owner command. |
| Existing owner / already managed | Stop. Do not delete another administrator or reset blindly. If Core is already owner from this attempt, establish its pairing state before retrying. |
| `APK HASH MISMATCH` | Do not install that file. Retry the official download once. If it still differs, report the message; do not replace the expected hash. |
| Download fails / certificate error | Check computer internet/date/time. On Mac run Applications → Python 3.14 → Install Certificates.command. Retry; do not disable certificate verification. |
| Payload check failed | Click Copy QR Data again, repeat section 8's save step, and check file is `provisioning.json`, not `.txt`. Use fresh data; never paste a QR image into the text file. |
| `Provisioning failed (...)` during check | Confirm fresh payload and correct date/time, repeat host validation, verify Core 1.27.1. If still failing, stop and report the exception class and device versions, without the JSON. |
| USB vanished after launch | Inspect phone and Hub. This can be expected lockdown; it is not by itself proof of success or failure. |
| Hub remains offline | Verify intended wallet, phone Wi-Fi, any disclaimer/error, and QR expiry. Record the last successful step. Avoid repeated owner/pair/reset commands without understanding the state. |

### How to ask for help without exposing your account

Run `python3 tools/diagnose.py --serial $ACURAST_SERIAL` if ADB still works. Its account/owner summary avoids printing identifiers. Review the output yourself before sharing. Record: phone model, Android/vendor OS version, Core version, step number, exact error, and whether the Hub ever showed online.

Open this repository's **Issues → New issue → Onboarding result or problem** (or [open the issue form](https://github.com/bokiko/acurast-core-onboarding-guide/issues/new?template=onboarding.md)). Paste only those details. Do **not** attach your QR, JSON file, wallet recovery words, account screen, serial, or unreviewed logs. If asked to inspect `dumpsys` or logcat later, treat their full output as private.

### What is and is not verified

Mac was the computer used for the recorded phone sessions. Core 1.27.1 was confirmed online by the owner on SM-A055F, Pixel 6 Pro, restored SM-A045F, and Xiaomi 23124RA7EO. On SM-S918B, owner registration and pairing launch were recorded but its online confirmation was not preserved. Firmware recovery and bootloader relocking are outside this beginner walkthrough. The public helper's original transport mechanism worked; its added validation still needs a fresh end-to-end phone test.

Optional background, not required reading to follow this page: [field results](../README.md#field-results), [helper limitations](helper-review.md), [recovery boundaries](recovery.md), [sources](sources.md).
