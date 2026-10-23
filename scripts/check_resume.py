#!/usr/bin/env python3
"""Validate resume/resume.json before it is published.

Fails on broken JSON, missing required fields or malformed dates.
Warns (without failing) about [placeholders] that are still unfilled.
"""
import json
import re
import sys
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "resume" / "resume.json"
DATE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
DATE_FIELDS = {"startDate", "endDate", "date", "lastModified"}

errors, placeholders = [], []


def walk(node, path):
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}"
            if key in DATE_FIELDS and isinstance(value, str) and value and not DATE.match(value):
                # Free text like "[Expected graduation]" is allowed while it is a placeholder.
                if not value.startswith("["):
                    errors.append(f"{child}: '{value}' is not YYYY, YYYY-MM or YYYY-MM-DD")
            walk(value, child)
    elif isinstance(node, list):
        for i, value in enumerate(node):
            walk(value, f"{path}[{i}]")
    elif isinstance(node, str) and re.search(r"\[[^\]]+\]", node):
        placeholders.append(path)


try:
    data = json.loads(PATH.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    sys.exit(f"ERROR: cannot read {PATH.name}: {exc}")

basics = data.get("basics")
if not isinstance(basics, dict) or not basics.get("name"):
    errors.append("basics.name is required")
for key in ("work", "education", "projects", "skills", "certificates", "languages"):
    if key in data and not isinstance(data[key], list):
        errors.append(f"{key} must be a list")

walk(data, "$")

for p in placeholders:
    print(f"warning: placeholder still to fill at {p}")
for e in errors:
    print(f"ERROR: {e}")
if errors:
    sys.exit(1)
print(f"OK: {PATH.name} is valid ({len(placeholders)} placeholders left)")
