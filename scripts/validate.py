#!/usr/bin/env python3
"""Validate the skill pack manifest and skill folders."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9-]+$")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---"):
        raise ValueError(f"{path} is missing YAML frontmatter")

    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"{path} has unterminated YAML frontmatter")

    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^(name|description):\s*(.+)$", line)
        if match:
            data[match.group(1)] = match.group(2).strip().strip('"')
    return data


def main() -> int:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    names = set()

    for skill in manifest.get("skills", []):
        name = skill.get("name")
        rel_path = skill.get("path")
        if not name or not NAME_RE.match(name):
            raise ValueError(f"Invalid skill name in manifest: {name!r}")
        if name in names:
            raise ValueError(f"Duplicate skill in manifest: {name}")
        names.add(name)

        skill_dir = ROOT / rel_path
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            raise FileNotFoundError(f"{skill_md} does not exist")

        frontmatter = parse_frontmatter(skill_md)
        if frontmatter.get("name") != name:
            raise ValueError(f"{skill_md} name does not match manifest name {name}")
        if not frontmatter.get("description"):
            raise ValueError(f"{skill_md} is missing description")

    print(f"Validated {len(names)} skills.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
