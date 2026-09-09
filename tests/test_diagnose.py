import contextlib
import importlib.util
import io
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch

spec=importlib.util.spec_from_file_location('diagnose',Path(__file__).resolve().parents[1]/'tools/diagnose.py')
d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)

class DiagnosticTests(unittest.TestCase):
    def test_private_fields_not_printed_and_no_mutations(self):
        calls=[]
        def run(cmd,**kwargs):
            calls.append(cmd)
            tail=cmd[4:]
            data=''
            if tail==['dumpsys','account']:
                data='Accounts: 1\nAccount {name=SYNTHETIC-PRIVATE-ACCOUNT,type=example}\n'
            elif tail==['dpm','list-owners']:
                data='1 owner: User 0: admin=private.other/admin,DeviceOwner\n'
            return SimpleNamespace(returncode=0,stdout=data)
        out=io.StringIO()
        with patch('sys.argv',['diagnose','--serial','SYNTHETIC-SERIAL']),patch.object(d.subprocess,'run',side_effect=run),contextlib.redirect_stdout(out):d.main()
        self.assertNotIn('SYNTHETIC-',out.getvalue())
        self.assertNotIn('private.other',out.getvalue())
        self.assertIn('Accounts across reported users: 1',out.getvalue())
        for c in calls:
            self.assertEqual(c[:4],['adb','-s','SYNTHETIC-SERIAL','shell'])
            self.assertIn(c[4],['getprop','dumpsys','dpm','appops'])
            if c[4]=='dpm':self.assertEqual(c[5: ],['list-owners'])
            if c[4]=='appops':self.assertEqual(c[5],'get')
    def test_unavailable_is_unknown(self):
        out=io.StringIO()
        with patch('sys.argv',['diagnose','--serial','SYNTHETIC-SERIAL']),patch.object(d.subprocess,'run',side_effect=FileNotFoundError),contextlib.redirect_stdout(out):d.main()
        self.assertIn('Accounts across reported users: unknown',out.getvalue())
        self.assertIn('Management: unknown',out.getvalue())

if __name__=='__main__':unittest.main()
