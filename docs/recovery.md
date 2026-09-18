# Recovery boundaries and incomplete setup

## Owner set, pairing not complete

If ADB remains available, inspect the owner and the exact on-device error. A fresh valid Hub payload may be needed, but first establish whether Core is already paired. Do not replace an existing processor identity or repeatedly launch pairing without understanding the state.

Core ownership has no verified ordinary undo procedure. On our Android 17 test force-stop had no effect, data clearing was refused, and admin removal was refused. Returning the phone to normal use may require a factory reset. A recorded in-place upgrade from Core 1.26.0 to 1.27.1 recovered pairing while ownership remained; that is not an ownership undo or a general retry promise. Diagnose the exact state before proposing a recovery. The [checklist](checklist.md) puts all available checks before ownership.

Do not assume fastboot or Settings can reset a locked-down phone. Use manufacturer-specific recovery guidance; this guide supplies no generic reset or flashing command.

If ADB disappeared, inspect the phone and Hub. This happened during normal Core lockdown in our sessions. A disclaimer may need acceptance. If the phone is locked down but never pairs, use current Acurast support instructions. A factory reset may be required to return it to general use and will erase local state; ordinary APK uninstall is not a guaranteed device-owner removal mechanism.

## Stock restoration is separate work

One Samsung SM-A045F was restored with exact compatible stock firmware, then physically relocked and wiped. It subsequently onboarded, but its Knox warranty bit remained tripped. We do not infer that other tripped devices will pass every future check.

No firmware images, partition backups, flashing scripts, or generic relock command are provided here. Model, region, bootloader revision, and partition layout matter. Relocking with incompatible or modified firmware can leave a phone unusable. If restoration is needed, obtain model-specific manufacturer/service guidance and make a separate recovery plan before any write or wipe.

This guide does not cover FRP/account-lock bypass, bootloader exploits, or removal of another organization's management. For an account-locked device, use its legitimate account recovery process.
