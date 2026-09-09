# Xiaomi: the extra USB permission

Observed on **23124RA7EO, Android 13 / MIUI 14**. Read here in GitHub; no repo download is needed. The ordinary self-service path is [welcome-screen QR onboarding](start-here.md). The following findings concern the community USB alternative with existing local tools.

## Exact phone steps that resolved our USB restriction

1. Settings → About phone → Detailed info and specs / All specs → tap **OS/MIUI version seven times**.
2. Settings → Additional settings → Developer options → enable **USB debugging**.
3. Also enable **Install via USB** and **USB debugging (Security settings)**.
4. Xiaomi required account sign-in and a SIM on our phone. The owner handled those physically; the extra permission then worked. Do not use Mi Unlock or OEM unlocking.
5. Android subsequently rejected device-owner setup because setup accounts remained. Remove Google through Settings → Accounts & sync → Google → account → More → Remove account, and Xiaomi through Settings → Xiaomi Account → Sign out.
6. Verify zero accounts and retained USB access before continuing an authorized owner/pairing operation.

Account removal affects locally synced data, not the cloud account. Preserve unsynced data first, and enter any sign-out password on the phone. Ordinary USB debugging alone allowed reads but blocked input and owner commands in our case.

## What we can honestly promise

The owner confirmed this phone online after extra permissions, account removal, ownership and pairing. We did not verify a SIM-free alternative, a MIUI-optimization-based alternative, or SIM removal afterward.

A manual APK installation solved installation only; it did not fix management permission. If your assistant lacks existing suitable computer tools or a reviewed pairing implementation, it should explain that limitation rather than download files silently. [AI instructions](ai-assisted.md).

For Google's scanning settings, open Play Store → profile → Play Protect → gear. Our preparation turned off Improve harmful app detection, then Scan apps with Play Protect, choosing Turn off rather than Pause when offered. Do not remove the Play Store itself.

This describes the preparation used, not a setting change proven necessary on Xiaomi. It reduces scanning; behavior after re-enabling it was not tested.

Optional reference: [Xiaomi USB security setup described by AirDroid](https://help.airdroid.com/hc/en-us/articles/360045329413-How-to-Enable-USB-debugging-on-Xiaomi).
