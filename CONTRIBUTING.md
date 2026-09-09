# Contributing

Submit a documentation correction or a field result with model identifier, Android/OS version, build (without serial), Core version, exact route, sanitized error, and observed outcome. Distinguish app installed, owner set, pairing launched, and confirmed online.

Never include real QR images/data, pairing signatures, account addresses, Wi-Fi credentials, serials, APKs, or firmware backups. Review diagnostic output before posting. Unsupported ideas belong under “not yet tested,” not in the working procedure.

For helper changes, run `python3 -m unittest discover -s tests`, build with `tools/build.sh`, and document whether a disposable device was actually used. Host tests cannot establish Android runtime or Hub success. No independent end-to-end reproduction of the public hardened helper is claimed yet.
