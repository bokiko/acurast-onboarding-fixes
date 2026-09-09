#!/usr/bin/env python3
"""Build the helper on macOS, Windows, or Linux; never contacts a phone."""
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
ITEMS = [
 ('android.jar','https://repo.maven.apache.org/maven2/com/google/android/android/4.1.1.4/android-4.1.1.4.jar','84072541cbb711eff89f7277100ff854929a446dba7ceb1b195c340e0b4fd3cb'),
 ('json.jar','https://repo.maven.apache.org/maven2/org/json/json/20240303/json-20240303.jar','3cf6cd6892e32e2b4c1c39e0f52f5248a2f5b37646fdfbb79a66b46b618414ed'),
 ('r8.jar','https://dl.google.com/dl/android/maven2/com/android/tools/r8/8.9.35/r8-8.9.35.jar','204b2fc2b0f4e888dc0ef748b58090def1bf4185068d36abbb94841dbc7107a8')]

def main():
    java, javac = shutil.which('java'), shutil.which('javac')
    if not java or not javac:
        raise RuntimeError('Java compiler missing. Install JDK 17, reopen your terminal, and follow Start here step 3.')
    deps=ROOT/'build/deps'; classes=ROOT/'build/classes'
    deps.mkdir(parents=True,exist_ok=True); classes.mkdir(parents=True,exist_ok=True)
    for name,url,expected in ITEMS:
        path=deps/name
        if not path.exists():
            print('Downloading '+name,flush=True)
            with urllib.request.urlopen(url,timeout=90) as response: content=response.read()
            if hashlib.sha256(content).hexdigest()!=expected: raise RuntimeError('Downloaded dependency hash mismatch: '+name)
            path.write_bytes(content)
        if hashlib.sha256(path.read_bytes()).hexdigest()!=expected: raise RuntimeError('Cached dependency hash mismatch: '+name)
    print('All build dependency hashes verified',flush=True)
    subprocess.run([javac,'-source','8','-target','8','-cp',os.pathsep.join(str(deps/n) for n in ['android.jar','json.jar']),'-d',str(classes),str(ROOT/'tools/CoreProvision.java')],check=True)
    subprocess.run([java,'-cp',str(deps/'r8.jar'),'com.android.tools.r8.D8','--min-api','30','--lib',str(deps/'android.jar'),'--output',str(ROOT/'build/helper.zip'),str(classes/'CoreProvision.class')],check=True)
    print('BUILD OK: build/helper.zip is ready. No phone settings were changed.')

if __name__=='__main__':
    try:main()
    except (OSError,RuntimeError,subprocess.CalledProcessError) as e:
        print('BUILD FAILED: '+str(e),file=sys.stderr);sys.exit(1)
