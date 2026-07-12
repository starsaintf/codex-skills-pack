#!/usr/bin/env python3
"""Validate the skill manifest, paths, provenance metadata, and licence evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath

ALLOWED_AUDIT_STATUSES = {
    "license-file-present",
    "root-mit-local",
    "metadata-only-needs-upstream-license-file",
}
VERIFIED_AUDIT_STATUSES = {"license-file-present", "root-mit-local"}
REQUIRED_FIELDS = {
    "name",
    "path",
    "description",
    "license",
    "source",
    "license_evidence",
    "origin_url",
    "origin_ref",
    "audit_status",
}


def safe_repo_path(value: str) -> bool:
    path = PurePosixPath(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts


def validate(repo_root: Path, strict_provenance: bool = False) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    manifest_path = repo_root / "manifest.json"

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError:
        return ["manifest.json is missing"], warnings
    except json.JSONDecodeError as exc:
        return [f"manifest.json is invalid JSON: {exc}"], warnings

    skills = manifest.get("skills")
    if not isinstance(skills, list) or not skills:
        return ["manifest.json must contain a non-empty skills array"], warnings

    names: set[str] = set()
    paths: set[str] = set()
    unresolved: list[str] = []

    for index, skill in enumerate(skills, start=1):
        label = skill.get("name") or f"entry #{index}"
        missing = sorted(REQUIRED_FIELDS - set(skill))
        if missing:
            errors.append(f"{label}: missing fields: {', '.join(missing)}")
            continue

        name = skill["name"]
        path_value = skill["path"]
        status = skill["audit_status"]

        if not isinstance(name, str) or not name.strip():
            errors.append(f"entry #{index}: name must be a non-empty string")
        elif name in names:
            errors.append(f"{name}: duplicate skill name")
        else:
            names.add(name)

        if not isinstance(path_value, str) or not safe_repo_path(path_value):
            errors.append(f"{label}: path must be a safe relative path")
            continue
        if path_value in paths:
            errors.append(f"{label}: duplicate skill path {path_value}")
        paths.add(path_value)

        skill_dir = repo_root / path_value
        if not skill_dir.is_dir():
            errors.append(f"{label}: directory does not exist: {path_value}")
        elif not (skill_dir / "SKILL.md").is_file():
            errors.append(f"{label}: missing {path_value}/SKILL.md")

        if status not in ALLOWED_AUDIT_STATUSES:
            errors.append(f"{label}: unsupported audit_status {status!r}")
        elif status not in VERIFIED_AUDIT_STATUSES:
            unresolved.append(name)

        if status == "license-file-present":
            evidence = str(skill.get("license_evidence", ""))
            marker = "Embedded license file: "
            if not evidence.startswith(marker):
                errors.append(f"{label}: licence evidence must name the embedded file")
            else:
                license_path = evidence[len(marker):].strip()
                if not safe_repo_path(license_path) or not (repo_root / license_path).is_file():
                    errors.append(f"{label}: licence evidence file is missing: {license_path}")

        if status == "root-mit-local" and not (repo_root / "LICENSE").is_file():
            errors.append(f"{label}: root MIT licence is missing")

    if unresolved:
        message = (
            f"{len(unresolved)} skill(s) still need stronger upstream licence evidence: "
            + ", ".join(sorted(unresolved))
        )
        if strict_provenance:
            errors.append(message)
        else:
            warnings.append(message)

    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--strict-provenance",
        action="store_true",
        help="Fail when any skill still relies on metadata-only licence evidence.",
    )
    args = parser.parse_args(argv)

    errors, warnings = validate(args.repo_root.resolve(), args.strict_provenance)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"Validation failed with {len(errors)} error(s).")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
