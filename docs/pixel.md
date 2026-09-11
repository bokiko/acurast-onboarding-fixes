# Pixel steps

A Pixel 6 Pro on Android 14 completed our community USB method with Core 1.27.1 (136), and the owner confirmed it online. This is one field result, not a guarantee for every Pixel.

For self-service setup, follow [Start here](start-here.md): welcome-screen QR scanning does not require downloading this guide or installing computer tools.

A Pixel 9 Pro Fold on Android 17 later paired on Core 1.27.1 through the same method, but only after Core 1.26.0 — the version named in that account's Hub QR — accepted the provisioning intent and discarded the pairing silently. Install 1.27.1 or newer and confirm the installed version on the phone; see [version notes](downloads.md) and the [checklist](checklist.md).

If using an already-equipped local assistant for USB troubleshooting:

- Enable debugging through Settings → About phone → tap Build number seven times → System → Developer options → USB debugging.
- Accept the trusted computer prompt on the unlocked phone.
- Remove setup accounts before device-owner setup through Settings → Passwords & accounts (wording may include passkeys) → account → Remove account, preserving unsynced data first.
- Inspect Play Store → profile → Play Protect → gear. Our preparation used both scanning switches off; it did not establish that this is universally required.

No Samsung Auto Blocker or Xiaomi SIM permission workaround was involved. [AI-assisted help](ai-assisted.md) explains how to point an assistant at the repo URL.
