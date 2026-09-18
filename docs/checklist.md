# Preflight, gates and stop conditions

Read this page alongside the [USB procedure](usb-onboarding.md). Reading installs nothing. An authorized setup may obtain the [pinned toolchain and helper](../tools/README.md); missing tools are a prerequisite to resolve, not permission to improvise.

The [test record](helper-review.md#release-validation) distinguishes earlier phone results from the revised helper's computer tests. Explain that difference before the owner authorizes setup.

## Rule 1 — install 1.27.1 or newer

Core 1.27.1 (136) is the recorded working baseline. Stop below that version. Newer releases need provenance and compatibility review; do not assume future releases work or downgrade an existing processor.

The Hub QR may name 1.26.0. On our Pixel 9 Pro Fold running Android 17 it accepted delivery but silently discarded pairing. Upgrading that phone in place to 1.27.1 applied the same pairing without changing ownership. [Version evidence](downloads.md).

## Rule 2 — device owner is a one-way door

There is no verified ordinary undo procedure for Core ownership. On our Android 17 test force-stop had no effect, data clearing was refused, and admin removal was refused. Returning the phone to normal use may require a factory reset.

That does not mean every pairing failure requires a reset: the recorded upgrade above recovered pairing while ownership remained. Stop and diagnose; do not blindly retry or attempt to remove the administrator. [Recovery boundaries](recovery.md).

## Preflight — still reversible

| Check | Required evidence | If not |
| --- | --- | --- |
| Owner's scope | Dedicated, backed-up phone; concrete setup authorized | Stop |
| Correct target | One intended phone, explicit serial on each command | Resolve ambiguity privately |
| Android/user state | Android 12+; foreground user 0, no secondary users/work profiles | Stop; this procedure does not cover other configurations |
| Firmware | No root; locked stock firmware indicators | Resolve eligibility separately; indicators do not certify attestation |
| Existing management/pairing | No unrelated owner/profile or existing paired processor | Stop; do not overwrite |
| Tools/source | Pinned downloads verified; reviewed source matches checksums; clean build succeeds | Stop |
| App | Official APK digest, signature, package and version verified; installed identity matches | Stop |
| Accounts and vendor permission | Zero accounts; required management permission retained | Owner resolves through Settings, then re-check |
| Private file | Fresh export from intended Hub; strict local validator passes | Re-export; never edit signed fields |
| Time and expiry | Phone time sensible; actual Hub validity leaves time for acceptance | Refresh data |
| Helper | On-phone check passes with all five fields and launch interface verified | Stop; no weakened checks |

## Gate A — the last reversible point

Immediately before ownership, re-check the target, foreground user, account/profile/owner state, installed Core version, that Core is not running, and payload validity. The staged bytes must still match the checked local file. Re-run the on-phone check. Confirm the owner is present for the disclaimer and understands potential reset recovery.

Confirm the owner understands the current test coverage and authorizes this phone's setup. A successful computer build does not replace the checks on the connected phone.

## Gate B — did the pairing actually apply?

First verify explicit device-owner registration success and the expected owner component. Then deliver pairing once. If ownership or launch fails, stop.

Inspect the phone promptly. A disclaimer is an intermediate sign that Core advanced; let the owner read and accept it if they agree. An overview showing **Manager: not set** means pairing is incomplete. A generated Processor address does not prove pairing.

The helper accepts only launch result 0; other results stop for inspection. Even result 0 only means Android accepted an activity start.

## Gate C — is it online?

The owner must accept within the actual Hub validity window. Then verify the intended processor online in the intended Hub wallet, either directly in an authorized session or through explicit owner confirmation.

ADB disconnection during lockdown does not prove success or failure. Report the evidence obtained. Remove temporary pairing files where accessible, verify removal, and identify any copy whose deletion could not be confirmed.

## Stop conditions

Stop at any failed check, unsupported schema/interface, unexpected existing management, unknown firmware eligibility, or failed ownership/launch. Stop if Manager is not set, or the same action has already failed; do not repeat mutations blindly.

A fee error during incomplete pairing calls for pairing diagnosis, not a transfer to the processor. If pairing is already established, investigate the actual error separately.
