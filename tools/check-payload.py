#!/usr/bin/env python3
"""Local, non-networked QR envelope check. Never print payload values."""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import time

ADMIN = "com.acurast.attested.executor.canary/com.acurast.attested.executor.lockdown.LockdownDeviceAdminReceiver"
PREFIX = "android.app.extra.PROVISIONING_"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError("constant")


def validate(raw, certificate_hex, now):
    if len(raw) > 65536:
        raise ValueError("size")
    root = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object,
                      parse_constant=reject_constant)
    if not isinstance(root, dict) or root.get(PREFIX + "DEVICE_ADMIN_COMPONENT_NAME") != ADMIN:
        raise ValueError("admin")
    data = root.get(PREFIX + "ADMIN_EXTRAS_BUNDLE")
    fields = {"account", "accountType", "timestamp", "signature", "type"}
    if not isinstance(data, dict) or set(data) != fields:
        raise ValueError("schema")
    if any(not isinstance(v, str) or not v.strip() for v in data.values()):
        raise ValueError("type")
    if data["accountType"] != "sr25519" or data["type"] != "single":
        raise ValueError("pairing type")
    if not re.fullmatch(r"[0-9]{1,16}", data["timestamp"]):
        raise ValueError("timestamp")
    if not now - 14400000 <= int(data["timestamp"]) <= now + 300000:
        raise ValueError("window")
    if not re.fullmatch(r"[0-9a-fA-F]{64}", certificate_hex):
        raise ValueError("certificate")
    expected = base64.urlsafe_b64encode(bytes.fromhex(certificate_hex)).decode().rstrip("=")
    checksum = root.get(PREFIX + "DEVICE_ADMIN_SIGNATURE_CHECKSUM")
    if not isinstance(checksum, str) or checksum not in (expected, expected + "="):
        raise ValueError("certificate mismatch")
    return hashlib.sha256(raw).hexdigest()


def main():
    try:
        if len(sys.argv) != 3:
            raise ValueError("usage")
        path = Path(sys.argv[1])
        # POSIX-only procedure: require a private regular file in a private directory.
        info = path.lstat()
        parent = path.parent.stat()
        if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid()
                or info.st_mode & 0o077 or parent.st_mode & 0o077
                or parent.st_uid != os.getuid()):
            raise ValueError("permissions")
        with path.open("rb") as stream:
            raw = stream.read(65537)
        validate(raw, sys.argv[2], int(time.time() * 1000))
        print("PASS: private file, strict JSON, pairing schema, local time bound, APK certificate match. Hub signature and actual expiry NOT verified.")
        return 0
    except Exception:
        print("STOP: private payload validation failed; check permissions, fresh Hub export, schema, and verified APK certificate locally. No values logged.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
