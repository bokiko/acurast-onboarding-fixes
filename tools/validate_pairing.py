#!/usr/bin/env python3
"""Local structural check; never authenticates a Hub signature."""
import argparse
import json
import time
from pathlib import Path

KEY = 'android.app.extra.PROVISIONING_ADMIN_EXTRAS_BUNDLE'
ADMIN = 'com.acurast.attested.executor.canary/com.acurast.attested.executor.lockdown.LockdownDeviceAdminReceiver'
FIELDS = {'account', 'accountType', 'timestamp', 'signature', 'type'}

def validate(raw, now=None):
    if len(raw) > 65536:
        raise ValueError('Payload exceeds 64 KiB')
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError('Duplicate JSON key')
            out[key] = value
        return out
    try:
        root = json.loads(raw, object_pairs_hook=unique)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise ValueError('Invalid JSON') from None
    if not isinstance(root, dict) or root.get('android.app.extra.PROVISIONING_DEVICE_ADMIN_COMPONENT_NAME') != ADMIN:
        raise ValueError('Unexpected admin component')
    data = root.get(KEY)
    if not isinstance(data, dict) or set(data) != FIELDS:
        raise ValueError('Unexpected pairing fields; expected recorded single-device schema')
    if any(not isinstance(v, str) or not v.strip() for v in data.values()):
        raise ValueError('Pairing fields must be nonempty strings')
    if data['accountType'] != 'sr25519' or data['type'] != 'single':
        raise ValueError('Unsupported account or pairing type')
    if not data['timestamp'].isascii() or not data['timestamp'].isdigit():
        raise ValueError('Timestamp must be milliseconds as a decimal string')
    age = (time.time() if now is None else now) - int(data['timestamp']) / 1000
    if age < -300 or age > 4 * 3600:
        raise ValueError('Timestamp outside recorded 4-hour window; check clock and generate fresh QR')
    return age

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('payload', type=Path)
    args = parser.parse_args()
    try:
        with args.payload.open('rb') as f:
            age = validate(f.read(65537))
    except (OSError, ValueError):
        parser.exit(1, 'Payload check failed. Check file, schema, and expiry; no payload values logged.\n')
    print(f'Structure checked; age {age / 60:.1f} minutes. Signature NOT verified. Confirm Hub expiry and intended account yourself.')

if __name__ == '__main__':
    main()
