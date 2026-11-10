"""Offline setup check. Does not touch student work or require packages."""
import json
import sys
import tempfile
from pathlib import Path

if sys.version_info < (3, 11):
    raise SystemExit("Python 3.11 or later is required.")
print("Python", sys.version.split()[0])
with tempfile.TemporaryDirectory() as folder:
    path = Path(folder) / "check.json"
    sample = [{"name": "Notebook", "count": 2}]
    path.write_text(json.dumps(sample), encoding="utf-8")
    assert json.loads(path.read_text(encoding="utf-8")) == sample
print("Writable temporary folder: OK")
print("JSON round-trip: OK")
print("Setup OK")
