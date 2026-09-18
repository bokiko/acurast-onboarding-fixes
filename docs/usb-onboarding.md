# Community USB method

This route uses a computer and USB cable to install the official Core app, register device ownership, and deliver the Hub's signed pairing data. You can use [AI-assisted help](ai-assisted.md) or follow the commands below manually.

The build steps cover macOS Apple Silicon. See [what has been tested](helper-review.md#release-validation) for the difference between earlier phone results and the latest helper changes.

Reading requires no download or clone. Actual setup requires the [pinned tools and source](../tools/README.md). Work through the [checklist](checklist.md) at every stage. Commands are separate stages, not a script to paste and run end to end. Stop whenever a command fails.

## Prepare the computer and phone

Build the helper and verify the official APK using [tools/README.md](../tools/README.md) and [app verification](downloads.md). Keep the build folder separate from private pairing data. Do not use an APK from a QR download URL without checking official provenance.

Use a dedicated, backed-up Android 12+ phone with eligible stock firmware, a locked bootloader, and no root. Resolve existing accounts and vendor USB restrictions using the applicable [Samsung](samsung.md), [Xiaomi](xiaomi.md), or [Pixel](pixel.md) notes. Do not remove unrelated management or overwrite an existing processor.

Select the target privately with ADB's device list, then set `CORE_SERIAL` locally to its exact serial. Never paste serials into public logs. Set `CORE_ADB` to the absolute path of the verified platform-tools/adb binary and `CORE_WORK` to the absolute build folder. No example value is a real device identifier.

For an authorized phone inspection:

```sh
"$CORE_ADB" -s "$CORE_SERIAL" shell getprop ro.build.version.sdk
"$CORE_ADB" -s "$CORE_SERIAL" shell am get-current-user
"$CORE_ADB" -s "$CORE_SERIAL" shell getprop ro.boot.verifiedbootstate
"$CORE_ADB" -s "$CORE_SERIAL" shell getprop ro.boot.flash.locked
```

Require API 31+, foreground user 0, and expected locked/verified stock indicators. Missing or conflicting indicators need investigation; they do not by themselves prove eligibility. Inspect Android Settings for zero accounts, no work profile/secondary users, and no existing device management. Reconcile with locally inspected system state; do not print raw account or policy dumps into chat.

Only after the app checks and an authorized installation plan:

```sh
"$CORE_ADB" -s "$CORE_SERIAL" install "$CORE_WORK/processor-1.27.1.apk"
```

If an app is already installed, stop to identify its version, signer, and pairing state. Do not add replacement, downgrade, or clear-data flags automatically. Confirm the installed package and version, not just the downloaded filename. Package is `com.acurast.attested.executor.canary`; the tested version is 1.27.1 / 136.

## Private pairing file

Create a new private directory outside the repository and cloud sync, with mode 700. In a trusted local editor without AI/cloud features, the owner saves Hub **Copy QR Data** as plain UTF-8 `payload.json` there. Set the file mode to 600. Set `CORE_PAYLOAD` to its absolute path. Do not put the payload in a command, clipboard-reading tool, chat, screenshot, or public QR decoder.

Using the public signer-certificate SHA-256 hex digest from verified apksigner output, set `CORE_CERT_SHA256` to those 64 hex digits. This is an APK certificate digest, not the APK file digest.

```sh
chmod 700 "$(dirname "$CORE_PAYLOAD")"
chmod 600 "$CORE_PAYLOAD"
python3 "$CORE_WORK/check-payload.py" "$CORE_PAYLOAD" "$CORE_CERT_SHA256"
```

The validator rejects duplicate keys, nonstandard JSON, wrong field types, and certificate mismatches without printing values. Its time check is only a local four-hour age/five-minute future bound. Confirm actual Hub expiry and phone time separately. It does not authenticate the Hub signature.

## Stage and check before ownership

Use a new private staging directory. If it already exists, stop and inspect; do not silently reuse or delete it.

```sh
"$CORE_ADB" -s "$CORE_SERIAL" shell 'umask 077; mkdir /data/local/tmp/acurast-provision'
"$CORE_ADB" -s "$CORE_SERIAL" push "$CORE_WORK/helper.zip" /data/local/tmp/acurast-provision/helper.zip
"$CORE_ADB" -s "$CORE_SERIAL" shell chmod 444 /data/local/tmp/acurast-provision/helper.zip
"$CORE_ADB" -s "$CORE_SERIAL" push "$CORE_PAYLOAD" /data/local/tmp/acurast-provision/payload.json
"$CORE_ADB" -s "$CORE_SERIAL" shell chmod 600 /data/local/tmp/acurast-provision/payload.json
```

Verify directory mode 700, helper mode 444, payload mode 600, and shell ownership. Compare SHA-256 of the local and staged helper and payload privately; do not return payload hashes or file contents to chat. Stop on any mismatch. The folder must not be accessible to other users. Make the DEX archive read-only before loading it.

```sh
"$CORE_ADB" -s "$CORE_SERIAL" shell 'CLASSPATH=/data/local/tmp/acurast-provision/helper.zip app_process /system/bin CoreProvision /data/local/tmp/acurast-provision/payload.json check'
```

Expected: typed bundle and all five fields verified, launch interface matched, and check-only completion. The helper requires shell UID 2000 and foreground Android user 0. It does not launch Core in check mode. A host build cannot prove this step works on a given phone.

## Ownership — stop at Gate A

Complete [Gate A](checklist.md#gate-a--the-last-reversible-point). Explain that this helper revision has passed computer tests but has not yet completed a full phone test, and confirm the owner's setup authorization. Core must not be running; re-check accounts, profiles, owner state, version, file identity, and expiry. The owner must understand that recovery may require a reset.

Only then, in an authorized session:

```sh
"$CORE_ADB" -s "$CORE_SERIAL" shell dpm set-device-owner --user 0 com.acurast.attested.executor.canary/com.acurast.attested.executor.lockdown.LockdownDeviceAdminReceiver
```

Require explicit success and verify that exact component is the device owner for user 0. If access disappears or the result is unclear, inspect the phone and stop rather than executing the next command.

## Deliver pairing and verify

Only after ownership is confirmed:

```sh
"$CORE_ADB" -s "$CORE_SERIAL" shell 'CLASSPATH=/data/local/tmp/acurast-provision/helper.zip app_process /system/bin CoreProvision /data/local/tmp/acurast-provision/payload.json launch'
```

The helper only accepts result 0; a nonzero result or exception stops the procedure. Result 0 is not pairing success. Inspect the phone promptly: Manager: not set means pairing is incomplete. A disclaimer requires the owner to read and accept within the actual validity window. Verify the intended processor online in the intended Hub wallet.

Core may disconnect ADB. That is not evidence of online status. Follow [Gate B and Gate C](checklist.md#gate-b--did-the-pairing-actually-apply).

## Cleanup

If ADB remains accessible, remove only the two files created in the dedicated staging directory, then remove the empty directory. Verify they are gone. Remove the private local payload through the owner's file manager, and handle editor/clipboard copies too. Do not promise secure erasure, and disclose phone copies that could not be removed because ADB disappeared.

## Why ordinary string extras are not enough

The helper puts the five unchanged Hub strings inside an Android PersistableBundle under android.app.extra.PROVISIONING_ADMIN_EXTRAS_BUNDLE. It parcel-roundtrips the intent and uses the recorded hidden launch interface for Core's provisioning activity.

Ordinary am start string extras do not create that typed bundle. App installation and device ownership alone do not pair a processor. See [source and build](../tools/README.md), [review limits](helper-review.md), and [recovery boundaries](recovery.md).
