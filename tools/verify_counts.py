#!/usr/bin/env python3
from pathlib import Path
import json
import sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
errors = []
for relative, expected in manifest["files"].items():
    path = root / relative
    actual = path.read_text(encoding="utf-8").count(manifest["marker"]) if path.exists() else -1
    if actual != expected:
        errors.append(f"{relative}: expected {expected}, got {actual}")
actual_total = sum((root / p).read_text(encoding="utf-8").count(manifest["marker"]) for p in manifest["files"])
if actual_total != manifest["total_items"]:
    errors.append(f"total: expected {manifest['total_items']}, got {actual_total}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {len(manifest['files'])} files, {actual_total} count-verified items")
