import base64
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "check-payload.py"
spec = importlib.util.spec_from_file_location("payload_check", SOURCE)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
CERT = "ab" * 32
NOW = 1800000000000


def payload(now=NOW):
    return {
        checker.PREFIX + "DEVICE_ADMIN_COMPONENT_NAME": checker.ADMIN,
        checker.PREFIX + "DEVICE_ADMIN_SIGNATURE_CHECKSUM": base64.urlsafe_b64encode(bytes.fromhex(CERT)).decode().rstrip("="),
        checker.PREFIX + "ADMIN_EXTRAS_BUNDLE": {
            "account": "SYNTHETIC-PRIVATE-MARKER", "accountType": "sr25519",
            "signature": "SYNTHETIC-SIGNATURE", "timestamp": str(now), "type": "single"}}


class PayloadTests(unittest.TestCase):
    def check(self, root):
        return checker.validate(json.dumps(root).encode(), CERT, NOW)

    def test_valid_unchanged(self):
        root = payload()
        before = json.dumps(root)
        self.assertEqual(len(self.check(root)), 64)
        self.assertEqual(json.dumps(root), before)

    def test_schema(self):
        for key, value in [("signature", 42), ("signature", " "), ("type", "batch"),
                           ("accountType", "other"), ("extra", "value"), ("timestamp", "-1")]:
            with self.subTest(key=key, value=value):
                root = payload()
                root[checker.PREFIX + "ADMIN_EXTRAS_BUNDLE"][key] = value
                with self.assertRaises(ValueError): self.check(root)
        root = payload()
        del root[checker.PREFIX + "ADMIN_EXTRAS_BUNDLE"]["signature"]
        with self.assertRaises(ValueError): self.check(root)

    def test_json_rejections(self):
        valid = json.dumps(payload())
        for raw in [b"{", b"[]", b"\xff", b" " * 65537,
                    (valid + " trailing").encode(),
                    valid.replace('"type": "single"', '"type": "single", "type": "single"').encode(),
                    valid.replace('"type": "single"', '"type": NaN').encode()]:
            with self.subTest(size=len(raw)):
                with self.assertRaises(ValueError): checker.validate(raw, CERT, NOW)

    def test_time_boundaries(self):
        for offset in [-14400000, 300000]: self.check(payload(NOW + offset))
        for offset in [-14400001, 300001]:
            with self.assertRaises(ValueError): self.check(payload(NOW + offset))

    def test_identity(self):
        root = payload()
        root[checker.PREFIX + "DEVICE_ADMIN_COMPONENT_NAME"] = "wrong"
        with self.assertRaises(ValueError): self.check(root)
        for cert in ["cd" * 32, "ab", "x" * 64]:
            with self.assertRaises(ValueError): checker.validate(json.dumps(payload()).encode(), cert, NOW)

    def test_cli_permissions_and_redaction(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            folder.chmod(0o700)
            target = folder / "payload.json"
            target.write_text(json.dumps(payload(int(time.time() * 1000))))
            target.chmod(0o600)
            def run(path=target, certificate=CERT):
                result = subprocess.run([sys.executable, str(SOURCE), str(path), certificate], capture_output=True, text=True)
                self.assertNotIn("SYNTHETIC-PRIVATE-MARKER", result.stdout + result.stderr)
                self.assertNotIn("SYNTHETIC-SIGNATURE", result.stdout + result.stderr)
                self.assertNotIn("Traceback", result.stdout + result.stderr)
                return result.returncode
            self.assertEqual(run(), 0)
            self.assertEqual(run(certificate="cd" * 32), 1)
            target.chmod(0o644)
            self.assertEqual(run(), 1)
            target.chmod(0o600)
            link = folder / "link.json"
            link.symlink_to(target)
            self.assertEqual(run(link), 1)
            folder.chmod(0o755)
            self.assertEqual(run(), 1)
            folder.chmod(0o700)
            target.write_text("SYNTHETIC-PRIVATE-MARKER")
            self.assertEqual(run(), 1)


if __name__ == "__main__":
    unittest.main()
