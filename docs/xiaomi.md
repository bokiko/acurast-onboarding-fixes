# Xiaomi: the extra USB permission matters

Observed on **23124RA7EO, Android 13, MIUI 14**, on 2026-09-09. Other Xiaomi/Redmi/POCO versions may behave differently.

## The sequence that worked

1. Ordinary USB debugging let us read device state, but remote taps and device-owner registration were rejected.
2. **Install via USB** and **USB debugging (Security settings)** required Xiaomi sign-in and a SIM on this phone.
3. The owner inserted a SIM and enabled the extra switches through Developer options. The previously denied device-owner command then reached Android's account checks.
4. Google and Xiaomi accounts were present. We removed Google from the phone and signed out of Xiaomi using Settings; Android then reported zero accounts.
5. Device-owner registration succeeded. The helper delivered the Hub pairing extras, Core disconnected ADB, and the owner confirmed it online.

Do not confuse ordinary **USB debugging** with **USB debugging (Security settings)**. Do not enable OEM unlocking or Mi Unlock for this procedure.

If sign-in is needed, enter credentials on the phone, not in a terminal or issue report. Before owner registration, remove setup accounts from this device through the normal Settings UI. This removes locally synchronized account data, not the cloud account itself. Back up unsynced data first. Xiaomi may ask for a password to sign out. Check that the extra USB permission still works afterward.

The SIM was inserted for setup; we did **not** record removing it afterward. We have no verified SIM-free workaround for this specific restriction. A borrowed or temporarily moved SIM may be practical, but do not assume a particular inactive SIM will satisfy the prompt.

## Manual APK install only solves installation

When `adb install` returned `INSTALL_FAILED_USER_RESTRICTED`, copying the verified APK to Downloads and installing through File Manager succeeded:

```sh
adb -s "$ACURAST_SERIAL" push processor-1.27.1.apk /sdcard/Download/Acurast-Core-1.27.1.apk
```

On the phone open that file, allow installation from File Manager if requested, and install. This did **not** resolve the separate device-owner restriction. Do not stop at “app installed.”

## What did not work in our session

Suggesting MIUI optimization changes did not produce a successful alternative. Remote property modification was denied. We do not publish this as a tested bypass. More generally, [AirDroid's Xiaomi instructions](https://help.airdroid.com/hc/en-us/articles/360045329413-How-to-Enable-USB-debugging-on-Xiaomi) also distinguish the additional USB security switch.

Check [Play Protect](samsung.md#play-protect) too; those are Google controls, not Samsung-only controls. Continue with the [shared USB procedure](usb-onboarding.md) once accounts and permissions are ready.
