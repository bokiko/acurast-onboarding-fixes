# Set up your phone with AI help

Connect your spare phone to your computer with a USB data cable.
Your assistant handles the computer steps; you handle taps, passwords,
and wallet approvals.

Core will dedicate this phone to Acurast. Back up anything you want to keep.
Returning it to normal use may require a factory reset.

## 1. Open the assistant you use

Use an assistant that can run commands on the computer connected to your
phone. The published build steps currently cover Apple Silicon Macs.

If your assistant only works in a browser, it can explain the
[manual USB steps](usb-onboarding.md) while you run them yourself.

## 2. Paste this into its chat box

Copy this message into your assistant:

```text
Read this guide and the setup pages it links to:
https://github.com/bokiko/acurast-onboarding-fixes/blob/main/AI-ONBOARDING.md

Help me set up my spare Android phone for Acurast Core using USB.
Check my computer tools and the intended phone first. Explain the setup
and what has been tested, then help me through it one step at a time.
Use the documented downloads and follow the phone checklist.

Keep my Hub QR data in a private local file that the setup tool reads
directly. Never print it or put it in chat. I will handle passwords,
wallet approvals, and phone confirmations.

Ask separately before resetting the phone, changing its firmware or
bootloader, or replacing an existing paired processor.
Finish by checking that the intended phone is online in my Acurast Hub.
```

The assistant should explain any tools it needs before downloading them.
You do not need to clone this guide or understand the build commands.

## 3. Keep control of the setup

Your assistant’s permissions determine what it can access. Review its
setup plan before letting it change the phone.

When it’s time to pair:

1. Open your own [Acurast Hub](https://hub.acurast.com/) and select your wallet.
2. Use **Copy QR Data** and save it as a private local file when instructed.
3. Give the assistant the file’s location, not its contents.

Use a local editor without cloud sync or AI features. Keep the file outside
shared folders and the repository. The [technical steps](usb-onboarding.md#private-pairing-file)
explain how to protect it.

Never paste your QR data, recovery words, private keys, or passwords into
chat. Enter credentials only on the phone or in your wallet.

After setup, remove temporary pairing files and clear the clipboard.
The assistant should tell you if it could not remove a phone copy because
Core disconnected USB. [Privacy and test details](helper-review.md)

## 4. Finish on the phone

Keep the phone powered and on Wi-Fi. Follow the assistant’s instructions
for the USB prompt and any account or permission settings.

Read Core’s disclaimer and accept it if you agree. Do this while the Hub
pairing data is still valid. Then confirm the intended phone is online in
your Hub.

## 5. If it gets stuck

Tell the assistant:

> Stop repeating that step. Check the troubleshooting page and tell me
> what went wrong and what to do next.

An installed app or a lost USB connection does not mean setup is complete.
[Find your error](troubleshooting.md) · [What has been tested](helper-review.md)
