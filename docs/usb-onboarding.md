# Community USB onboarding

This is the fallback used in our field sessions, **not an Acurast-supported provisioning API**. The public helper adds validation to the original working mechanism and is not yet independently reproduced end to end. Use a dedicated phone; read [helper limits](helper-review.md) before setting device owner. The [official route](official-route.md) remains the starting recommendation.

Commands below use Bash/zsh on macOS or Linux, Python 3, and Google ADB. Run from this repository unless a path says otherwise. Windows-native shell instructions are not tested. Execute one stage at a time and inspect the result; do not paste the entire page as a script.

## 1. Identify and prepare one phone

Enable Developer options and USB debugging in the phone's Settings, connect a data cable, and accept the authorization prompt. Model-specific extra steps: [Samsung](samsung.md), [Xiaomi](xiaomi.md), [Pixel](pixel.md).

```sh
adb devices -l
ACURAST_SERIAL='YOUR_DEVICE_SERIAL'
python3 tools/diagnose.py --serial "$ACURAST_SERIAL"
```

Replace the placeholder with the intended phone's serial. Every device command below uses it explicitly. A device must show `device`, not `unauthorized` or `offline`.

Check Android version, stock/non-rooted firmware and locked bootloader. A reported property is a clue, not proof of attestation eligibility. Do not unlock a bootloader to make ADB work.

Resolve an existing device owner through its legitimate management process. Remove any setup accounts from this phone through Settings before the owner stage; preserve unsynced data first. On Xiaomi, first use any required account/SIM to enable the extra USB permissions, then sign out and verify those permissions still work. Do not clear account-provider app data as a shortcut.

Inspect Play Protect and manufacturer blockers on the phone. We used the configuration documented on the vendor pages; it has not been proven necessary on every firmware.

## 2. Obtain, verify, and install Core

Follow [verified downloads](downloads.md). Set the actual local file path:

```sh
ACURAST_APK='/absolute/path/to/processor-1.27.1.apk'
adb -s "$ACURAST_SERIAL" install "$ACURAST_APK"
```

Expect `Success`. Do not automatically downgrade, uninstall an existing paired processor, or use `-d` to force an older version. If installation is rejected, inspect the on-phone prompt and [troubleshooting](troubleshooting.md). Xiaomi's manual File Manager route is documented separately.

```sh
adb -s "$ACURAST_SERIAL" shell dumpsys package com.acurast.attested.executor.canary
```

Inspect locally for `versionName=1.27.1` and `versionCode=136`; do not publish the whole dump. Other releases are outside the recorded validation. Leave the newly installed app closed until pairing preparation is ready.

## 3. Save your own fresh Hub QR data privately

In your own Hub session create a new single-device QR, then use **Copy QR Data**. Save the complete JSON unchanged as `provisioning.json` in a private directory **outside the repository**. Do not paste signed data into a shell command, issue, chat, or Git file. The clipboard and the file contain pairing data even though they are not a wallet seed.

```sh
ACURAST_PAIRING='/absolute/private/path/to/provisioning.json'
chmod 600 "$ACURAST_PAIRING"
python3 tools/validate_pairing.py "$ACURAST_PAIRING"
```

Check that the Hub wallet is yours and its displayed expiry has not passed. The local validator checks structure and a conservative recorded four-hour timestamp window, **not the signature or intended account**. A different Hub expiry wins; do not edit signed values to make the check pass. Generate another QR if needed. This tool accepts only the recorded `sr25519` / `single` schema.

The helper uses the admin extras only. It does not configure Wi-Fi or download/install the URL embedded in the QR. Connect the phone to the intended network before continuing.

## 4. Build and check the transport

Follow [tools/build instructions](../tools/README.md), then:

```sh
adb -s "$ACURAST_SERIAL" push build/helper.zip /data/local/tmp/acurast-core-helper.zip
adb -s "$ACURAST_SERIAL" push "$ACURAST_PAIRING" /data/local/tmp/acurast-pairing.json
adb -s "$ACURAST_SERIAL" shell chmod 600 /data/local/tmp/acurast-pairing.json
adb -s "$ACURAST_SERIAL" shell 'CLASSPATH=/data/local/tmp/acurast-core-helper.zip app_process /system/bin CoreProvision /data/local/tmp/acurast-pairing.json check'
```

The check constructs and parcel-roundtrips a typed `PersistableBundle`, then validates the hidden launch interface. It does not launch Core or change ownership. Stop on any failure. Successful transport is not signature verification or proof that Core will accept pairing.

## 5. Make Core the device owner

This changes management of the phone. Recovery after lockdown can require wiping it; it is not an ordinary app permission.

```sh
adb -s "$ACURAST_SERIAL" shell am force-stop com.acurast.attested.executor.canary
adb -s "$ACURAST_SERIAL" shell appops set com.acurast.attested.executor.canary SCHEDULE_EXACT_ALARM allow
adb -s "$ACURAST_SERIAL" shell dpm set-device-owner com.acurast.attested.executor.canary/com.acurast.attested.executor.lockdown.LockdownDeviceAdminReceiver
```

Expect an explicit successful owner registration. The exact-alarm appop was part of the field configuration; its necessity was not isolated. If any command fails, stop and use the exact error in [troubleshooting](troubleshooting.md).

```sh
adb -s "$ACURAST_SERIAL" shell dpm list-owners
```

Confirm Core is the owner. Some Android versions restrict this read command; locally inspect `adb -s "$ACURAST_SERIAL" shell dumpsys device_policy` if needed. Do not assume permission denial means “no owners.”

Android documents ADB owner setup for eligible development devices; our account-free phones accepted it without a further reset at this stage. This is not a general promise to bypass setup eligibility or the official Core reset flow. [Android reference](https://developer.android.com/work/dpc/dedicated-devices/cookbook#development-setup).

## 6. Deliver pairing and verify online

```sh
adb -s "$ACURAST_SERIAL" shell 'CLASSPATH=/data/local/tmp/acurast-core-helper.zip app_process /system/bin CoreProvision /data/local/tmp/acurast-pairing.json launch'
```

A result of `0` means Android accepted the activity start. In our sessions Core disabled USB debugging during lockdown; sometimes a disclaimer appeared first. Read and accept it yourself if you agree.

Check the phone and your Hub until the intended processor is shown online. If it stays offline, inspect the actual error and connectivity rather than treating USB disconnection as success. The helper neither verifies nor reports network registration.

## 7. Private-file cleanup

If ADB is still available after a check, aborted attempt, or completed launch, remove staged private data when no longer needed:

```sh
adb -s "$ACURAST_SERIAL" shell rm -f /data/local/tmp/acurast-pairing.json /data/local/tmp/acurast-core-helper.zip
```

If Core has already disabled ADB, this cleanup may not be possible; do not promise automatic deletion. The public helper retains the staged file just as the original did. Keep that limitation in mind before using the method. Delete the private host JSON, any QR screenshot, and clipboard contents when finished using your normal file/clipboard controls. Never publish them.
