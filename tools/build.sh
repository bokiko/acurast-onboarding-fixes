#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
# JDK 17 must provide javac/java on PATH. No phone is contacted.
mkdir -p build/deps build/classes
python3 - <<'PY'
import hashlib, pathlib, urllib.request
items = [
 ('android.jar','https://repo.maven.apache.org/maven2/com/google/android/android/4.1.1.4/android-4.1.1.4.jar','84072541cbb711eff89f7277100ff854929a446dba7ceb1b195c340e0b4fd3cb'),
 ('json.jar','https://repo.maven.apache.org/maven2/org/json/json/20240303/json-20240303.jar','3cf6cd6892e32e2b4c1c39e0f52f5248a2f5b37646fdfbb79a66b46b618414ed'),
 ('r8.jar','https://dl.google.com/dl/android/maven2/com/android/tools/r8/8.9.35/r8-8.9.35.jar','204b2fc2b0f4e888dc0ef748b58090def1bf4185068d36abbb94841dbc7107a8')]
for name,url,expected in items:
 p=pathlib.Path('build/deps')/name
 if not p.exists():
  with urllib.request.urlopen(url, timeout=90) as r: content=r.read()
  if hashlib.sha256(content).hexdigest()!=expected: raise SystemExit('Downloaded dependency hash mismatch: '+name)
  p.write_bytes(content)
 if hashlib.sha256(p.read_bytes()).hexdigest()!=expected: raise SystemExit('Cached dependency hash mismatch: '+name)
print('All build dependency hashes verified')
PY
javac -source 8 -target 8 -cp build/deps/android.jar:build/deps/json.jar -d build/classes tools/CoreProvision.java
java -cp build/deps/r8.jar com.android.tools.r8.D8 --min-api 30 --lib build/deps/android.jar --output build/helper.zip build/classes/CoreProvision.class
