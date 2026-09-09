#!/usr/bin/env python3
"""Read selected Android state. No raw account, owner, or device-ID output."""
import argparse
import re
import subprocess

PKG = 'com.acurast.attested.executor.canary'

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--serial', required=True, help='Explicit ADB target; not printed')
    a = p.parse_args()
    def read(*args):
        try:
            r = subprocess.run(['adb', '-s', a.serial, 'shell', *args], capture_output=True, text=True, timeout=15)
            return r.stdout if r.returncode == 0 else ''
        except (OSError, subprocess.TimeoutExpired):
            return ''
    for label, prop in [('Manufacturer', 'ro.product.manufacturer'), ('Model', 'ro.product.model'),
                        ('Android', 'ro.build.version.release'), ('Boot flash locked', 'ro.boot.flash.locked'),
                        ('Verified boot', 'ro.boot.verifiedbootstate')]:
        value = read('getprop', prop).strip()
        print(f'{label}: {value if value and len(value) < 100 else "unknown"}')
    counts = re.findall(r'^\s*Accounts:\s*(\d+)\s*$', read('dumpsys', 'account'), re.M)
    print('Accounts across reported users: ' + (str(sum(map(int, counts))) if counts else 'unknown'))
    owners = read('dpm', 'list-owners')
    if 'no owners' in owners.lower():
        status = 'none reported'
    elif 'DeviceOwner' in owners and PKG in owners:
        status = 'Core owner reported; inspect locally if other profiles exist'
    elif 'owner' in owners.lower() and 'Exception' not in owners:
        status = 'management present; inspect locally'
    else:
        status = 'unknown / permission denied'
    print('Management: ' + status)
    version = re.search(r'versionName=([^\s]+)', read('dumpsys', 'package', PKG))
    print('Core version: ' + (version[1] if version else 'not found / unknown'))
    alarm = read('appops', 'get', PKG, 'SCHEDULE_EXACT_ALARM')
    match = re.search(r'SCHEDULE_EXACT_ALARM:\s*(\w+)', alarm)
    print('Exact alarm appop: ' + (match[1] if match else 'unknown / default'))
    print('Play Protect and vendor blockers: inspect both switches and vendor UI manually')
    print('This is not an eligibility, root-status, attestation, or online check. Review before sharing.')

if __name__ == '__main__':
    main()
