#!/usr/bin/env python3
"""Validate the skill pack manifest and skill folders."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9-]+$")
REQUIRED_METADATA = (
    "license",
    "source",
    "license_evidence",
    "audit_status",
)
VALID_AUDIT_STATUSES = {
    "license-file-present",
    "metadata-only-needs-upstream-license-file",
    "root-mit-local",
}


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


def classify_license_file(skill_dir: Path) -> tuple[str | None, Path | None]:
    license_files = sorted(skill_dir.glob("LICENSE*"))
    if not license_files:
        return None, None

    license_path = license_files[0]
    text = license_path.read_text(encoding="utf-8-sig", errors="replace").lower()
    if "apache license" in text and "version 2.0" in text:
        return "Apache-2.0", license_path
    if "permission is hereby granted" in text:
        return "MIT", license_path
    return "UNKNOWN", license_path


def main() -> int:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    names = set()
    sources = set()
    exact_licenses = set()

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

        for key in REQUIRED_METADATA:
            if not skill.get(key):
                raise ValueError(f"{name} is missing manifest metadata field {key!r}")

        audit_status = skill["audit_status"]
        if audit_status not in VALID_AUDIT_STATUSES:
            raise ValueError(f"{name} has invalid audit_status {audit_status!r}")

        sources.add(skill["source"])
        exact_licenses.add(skill["license"])

        detected_license, license_path = classify_license_file(skill_dir)
        if license_path:
            rel_license = license_path.relative_to(ROOT).as_posix()
            if detected_license == "UNKNOWN":
                raise ValueError(f"{rel_license} has an unknown license text")
            if detected_license not in skill["license"]:
                raise ValueError(
                    f"{name} manifest license {skill['license']!r} does not match {rel_license}"
                )
            if rel_license not in skill["license_evidence"]:
                raise ValueError(f"{name} license_evidence must reference {rel_license}")

        if skill["source"] == "vercel/vercel-plugin skill":
            if "Apache-2.0" not in skill["license"]:
                raise ValueError(f"{name} is Vercel-derived but not marked Apache-2.0")
            if not license_path:
                raise ValueError(f"{name} is Vercel-derived but lacks LICENSE.txt")
            if skill.get("origin_url") != "https://github.com/vercel/vercel-plugin":
                raise ValueError(f"{name} Vercel-derived origin_url is incorrect")

    if len(sources) <= 1:
        raise ValueError("manifest source metadata is flattened; expected multiple provenance sources")
    if exact_licenses == {"MIT"}:
        raise ValueError("manifest license metadata is flattened to MIT")

    skills_md = ROOT / "SKILLS.md"
    if skills_md.exists():
        skills_text = skills_md.read_text(encoding="utf-8-sig")
        for skill in manifest.get("skills", []):
            expected = f"`{skill['name']}`"
            if expected not in skills_text:
                raise ValueError(f"SKILLS.md does not list {skill['name']}")
            if skill["license"] not in skills_text:
                raise ValueError(f"SKILLS.md does not include license for {skill['name']}")

    print(f"Validated {len(names)} skills.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
