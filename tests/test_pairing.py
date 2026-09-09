import importlib.util
import json
import unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('pairing',Path(__file__).resolve().parents[1]/'tools/validate_pairing.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)

class PairingTests(unittest.TestCase):
    def payload(self):
        return {'android.app.extra.PROVISIONING_DEVICE_ADMIN_COMPONENT_NAME':v.ADMIN,v.KEY:{'account':'SYNTHETIC-NOT-A-REAL-ACCOUNT','accountType':'sr25519','timestamp':'2000000000000','signature':'SYNTHETIC-NOT-A-VALID-SIGNATURE','type':'single'}}
    def test_transport_does_not_authenticate_signature(self):
        self.assertEqual(v.validate(json.dumps(self.payload()).encode(),now=2000000000),0)
    def test_expired(self):
        with self.assertRaises(ValueError):v.validate(json.dumps(self.payload()).encode(),now=2000015000)
    def test_future(self):
        with self.assertRaises(ValueError):v.validate(json.dumps(self.payload()).encode(),now=1999999000)
    def test_wrong_admin(self):
        p=self.payload();p['android.app.extra.PROVISIONING_DEVICE_ADMIN_COMPONENT_NAME']='other/app'
        with self.assertRaises(ValueError):v.validate(json.dumps(p).encode(),now=2000000000)
    def test_schema(self):
        for value in [0,'',None]:
            p=self.payload();p[v.KEY]['signature']=value
            with self.assertRaises(ValueError):v.validate(json.dumps(p).encode(),now=2000000000)
    def test_duplicate(self):
        with self.assertRaises(ValueError):v.validate(b'{"x":1,"x":2}')
    def test_oversize(self):
        with self.assertRaises(ValueError):v.validate(b' '*65537)
    def test_extra_field(self):
        p=self.payload();p[v.KEY]['extra']='unexpected'
        with self.assertRaises(ValueError):v.validate(json.dumps(p).encode(),now=2000000000)

if __name__=='__main__':unittest.main()
