# Technical helper review

Community maintainer review, not an independent security audit or official Acurast API.

## Historical phone evidence

The original helper preserved five Hub strings in a typed PersistableBundle and launched Core's MainActivity through Android shell. Inspection of Core 1.27.1's parser informed that transport.

On September 12, 2026, the previous guarded source completed a check and launch on a Pixel 9 Pro Fold running Android 17. Core 1.27.1 advanced to the disclaimer and the owner confirmed the processor online. Core 1.26.0 silently discarded the same pairing on that phone. Earlier fleet sessions used the original helper.

**That phone result does not validate the revised source in this PR.** It also does not prove eligibility, rewards, or compatibility with other Android/Core versions.

## Revised implementation

The [helper](../tools/CoreProvision.java) retains the typed transport and adds fixed redacted error codes, bounded reads, an explicit shell-UID/foreground-user gate, deterministic exact-signature selection, and failure status for every launch result except the observed result 0. Result 0 still proves only activity-start acceptance.

The separate [local validator](../tools/check-payload.py) requires a private regular file and directory, strict JSON without duplicate keys, the supported five-string schema, local time bounds, and a matching APK signer-certificate checksum. It never outputs payload values and makes no network requests. Android's own JSON parser differs from the desktop test library; the strict host check and unchanged staged-byte comparison are mandatory.

Neither program verifies the Hub's cryptographic pairing signature. Certificate identity, signed pairing validity, and transport compatibility are separate checks.

## Release validation

Status on **2026-09-18**: **host checks passed; phone validation pending. Keep PR #7 in draft.**

| Check | Evidence |
| --- | --- |
| Pinned inputs | Official tool archives downloaded and SHA-256 pinned; JDK digest checked against Adoptium metadata; SDK platform/build-tools additionally compared with Google's repository metadata |
| Clean recipe | Documented extraction/compile/DEX commands executed from a new folder on macOS Apple Silicon, Temurin 17.0.18+8; result contains only classes.dex |
| Repeat build | Independent output folders produced the same helper ZIP digest |
| Java host checks | 31 assertions, including subprocess exit-status/output-redaction checks: unchanged fields, rejected schema/time/type cases, exact overload selection, shell/user restrictions, and nonzero launch rejection |
| Private validator | Six Python unittest groups using synthetic values: schema, strict JSON/duplicate keys, expiry boundaries, certificate mismatch, file/directory modes, symlink rejection, and CLI output redaction |
| Official APK | 1.27.1 asset digest reconfirmed against GitHub release metadata and downloaded file; apksigner verification passed; aapt2 confirmed package, 136 / 1.27.1, minSdk 30 and targetSdk 36 |
| Android runtime | **Not run for this revision** |
| Full Hub onboarding | **Not run for this revision** |
| Windows/Linux/Intel Mac recipe | **Not validated** |

Host Python version: 3.14.3. Desktop org.json 20240303 is used only in Java unit tests, never bundled into the phone helper.

Reproduced helper.zip SHA-256 for this source and pinned toolchain:

```text
6232dea240bd90ce147b7686c79afc78b60fd2a8adf4f33c47c9ae119e95798c
```

The [source checksum file](../tools/source.sha256) binds the helper and validator bytes at pinned source revision aba76f02ef40d929abfe4053a8b59c5d6d8542e3. Rebuild and update this record whenever they change.

### Remaining spare-phone test

Use an identified, backed-up spare phone with explicit authorization for the specific test. Start from the pasted prompt for this PR's exact revision, without relying on a pre-existing helper. Do not treat work on this repository as phone permission.

1. Establish eligibility, vendor permissions, user/account/profile/owner state, and the exact installed APK identity.
2. Confirm invalid synthetic fixtures fail on Android without leaking values or changing ownership. Check size, malformed input, timestamps, supported schema, runtime errors, and hidden-interface compatibility. Do not launch fabricated pairing data.
3. Create the real Hub file privately; verify strict host validation, byte identity after transfer, permissions, and on-phone check mode. Confirm check mode does not launch Core or change management.
4. Record all Gate A evidence before specifically authorized ownership. Verify owner registration, accepted launch, phone-side pairing state, owner acceptance within the validity window, and intended Hub online status.
5. Record ADB lockdown timing and exactly which private files could be removed. Do not deliberately strand an enrolled phone to test launch failures.
6. Review redacted evidence and confirm the guide's supported scope. Remove the release hold only after the exact source/recipe has completed this test. A result on one device does not justify claiming all Android/OEM combinations.

Android 12 and 16 runtime coverage remains unverified unless tested separately. Tests requiring a reset, firmware changes, or replacing a paired processor need their own plan and approval.

## Limits

- Written privacy rules do not sandbox an assistant with file access.
- The four-hour age/five-minute future bound is a local sanity check; actual Hub expiry and correct phone time control.
- Hidden APIs, Android permissions, and Core's parser can change. Stop instead of weakening checks.
- Owner registration and pairing are separate; failure does not automatically undo ownership.
- Some nonzero Android activity results may be benign in other contexts. This helper deliberately accepts only the observed result 0 and stops for inspection otherwise.
- Foreground user 0 and shell UID checks do not enumerate profiles, establish firmware integrity, or verify device eligibility. The checklist remains mandatory.
- Staged files may remain after ADB lockdown. Deletion is not guaranteed secure erasure.
- Host tests cannot exercise Android parceling, Binder permissions, device policy, or on-chain status.
