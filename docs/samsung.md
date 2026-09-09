# Samsung installation blockers

Use the [shared USB procedure](usb-onboarding.md) for commands. Models and results are in the [field table](../README.md#field-results).

## Auto Blocker

In **Settings → Security and privacy → Auto Blocker**, check the master switch. If it is blocking the verified APK or USB management, turn it off for this dedicated-device setup. Inspect any Maximum restrictions setting; do not assume toggling an unrelated security setting is sufficient.

Samsung documents that Auto Blocker can reject outside-store apps and USB commands. Menu availability varies by software. See [Samsung's explanation](https://www.samsung.com/us/support/answer/ANS10003636/). On our S23 Ultra the master page explicitly showed Off. Some older tested phones did not have the same feature.

## Play Protect

Our completed preparation used both switches off:

1. Open Play Store → profile → Play Protect → settings gear.
2. Turn off **Improve harmful app detection**.
3. Turn off **Scan apps with Play Protect**.
4. If offered Pause or Turn off, choose **Turn off** for the recorded setup, then verify both switches are off.

These changes reduce app scanning. This is a report of the dedicated-phone configuration used; we did not isolate whether every toggle was necessary or test re-enabling them after Core lockdown. Do not disable the entire Play Store package.

If ADB already works, this opened Play Protect in our sessions:

```sh
adb -s "$ACURAST_SERIAL" shell am start -a com.google.android.gms.settings.VERIFY_APPS_SETTINGS
```

The action is version-dependent; use the normal Play Store menu if unavailable. Tap controls on the phone if remote input is blocked.

## Modified firmware

Our A04 case required separate stock restoration and bootloader relock before onboarding. The Knox warranty bit stayed tripped. This is not a required step for normal stock phones and does not establish that any modified Samsung can be restored successfully. Read [recovery boundaries](recovery.md).
