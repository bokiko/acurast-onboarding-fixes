# Samsung steps

Read this page in GitHub; no guide files or computer software need to be downloaded. Start with the [full phone QR walkthrough](start-here.md).

## If setup is blocked at the welcome screen

If QR setup stops before you can reach ordinary Settings, write down the exact warning and the last step that worked. Open [AI-assisted help](ai-assisted.md) and include your phone model, Android version if known, and that Settings is unavailable. Keep the QR and account details private.

The switches below require access to Settings; they are not steps you can follow from the welcome screen. Your assistant should identify the blocker and check whether a supported next step is available with existing tools. If it cannot establish one, stop there rather than reset repeatedly or try an unexplained command.

## If Settings is accessible and Samsung blocks the app or USB

If ordinary Settings is accessible, open **Settings → Security and privacy → Auto Blocker**. Inspect the master switch and any Maximum restrictions. If it blocks the intended verified Acurast setup, turn the master control off after reading its confirmation. Some older models lack this feature.

Open **Play Store → profile → Play Protect → gear**. Our preparation used **Improve harmful app detection off**, then **Scan apps with Play Protect off**. If asked Pause or Turn off, our choice was **Turn off**. Verify both switches; do not disable the whole Play Store app. These changes reduce protection and were not individually proven necessary on every firmware.

Resetting may restore defaults. A blocker disabled at the home screen is not a guarantee it will remain disabled after another reset. If QR setup still fails, give your [local AI assistant](ai-assisted.md) the exact error; it must check existing tools before offering a USB alternative.

## If an existing local USB setup is being used

Confirm the installed Core version is **1.27.1 or newer** before registering the device owner. The version named in the Hub QR's advanced field may be older. On our Android 17 test an older build accepted the provisioning intent and discarded the pairing with no error shown anywhere, which is not a Pixel-specific behaviour as far as we can tell. See [version notes](downloads.md) and work through the [preflight, gates and stop conditions](checklist.md).

Settings → About phone → Software information → tap **Build number seven times** → enter PIN if asked → return to Settings → Developer options → **USB debugging on**. Accept the trusted computer's authorization prompt on the unlocked phone.

Before device-owner registration, remove setup accounts normally: Settings → Accounts and backup → Manage accounts → account → Remove account. Preserve unsynced data first; this removes the account from the phone, not the cloud account itself.

## Stock firmware

Our SM-A045F needed separate stock restoration/relock first, and its Knox bit stayed tripped. That is not a standard onboarding step. No generic flash or relock recipe is provided. [Recovery boundaries](recovery.md).

Optional reference: [Samsung Auto Blocker documentation](https://www.samsung.com/us/support/answer/ANS10003636/).
