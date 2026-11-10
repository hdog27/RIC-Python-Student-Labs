"""A temporary JSON round-trip, without changing any real save file."""
import json
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as folder:
    path = Path(folder) / "books.json"
    original = [{"title": "Example", "read": False}]
    path.write_text(json.dumps(original, indent=2), encoding="utf-8")
    print(path.read_text(encoding="utf-8"))
    restored = json.loads(path.read_text(encoding="utf-8"))
    print("Same data:", restored == original)
