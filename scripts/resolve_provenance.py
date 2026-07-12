#!/usr/bin/env python3
"""Resolve and verify skill provenance from pinned upstream sources.

This script is intentionally network-free. The exact affected skills, upstream
repositories, revisions, paths, licence declarations, and copyright notices are
recorded in provenance/upstream_sources.json after manual verification.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

UNRESOLVED_STATUS = "metadata-only-needs-upstream-license-file"
RESOLVED_STATUS = "license-file-present"

MIT_TERMS = """Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the \"Software\"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def upstream_skill_url(source: dict[str, Any], skill_name: str) -> str:
    return (
        f"{source['repository']}/tree/{source['revision']}/"
        f"{source['skill_base'].strip('/')}/{skill_name}"
    )


def license_text(source: dict[str, Any], skill_name: str) -> str:
    return (
        "MIT License\n\n"
        f"{source['copyright']}\n\n"
        f"{MIT_TERMS}\n"
        "Upstream provenance\n"
        "-------------------\n"
        f"Skill source: {upstream_skill_url(source, skill_name)}\n"
        f"Pinned revision: {source['revision']}\n"
        f"Licence evidence: {source['license_evidence_url']}\n"
    )


def expected_fields(skill: dict[str, Any], source: dict[str, Any]) -> dict[str, str]:
    relative_license = (Path(skill["path"]) / "LICENSE.txt").as_posix()
    return {
        "license": f"{source['license_name']}, see {relative_license}",
        "license_evidence": f"Embedded license file: {relative_license}",
        "origin_url": upstream_skill_url(source, skill["name"]),
        "origin_ref": (
            f"Pinned to {source['repository']}@{source['revision']}; "
            f"licence evidence: {source['license_evidence_url']}"
        ),
        "audit_status": RESOLVED_STATUS,
    }


def render_skills_md(skills: list[dict[str, Any]]) -> str:
    lines = [
        "# Skills",
        "",
        "This inventory is generated from `manifest.json`. Each redistributed skill records a pinned upstream source and licence evidence.",
        "",
    ]
    for index, skill in enumerate(skills, start=1):
        lines.extend(
            [
                f"{index}. `{skill['name']}`",
                f"   - Source: {skill['source']}",
                f"   - License: {skill['license']}",
                f"   - Evidence: {skill['license_evidence']}",
                f"   - Audit status: {skill['audit_status']}",
                f"   - Origin: {skill['origin_url'] or skill['origin_ref']}",
                f"   - Description: {skill['description']}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def build_targets(sources: dict[str, dict[str, Any]]) -> tuple[dict[str, tuple[str, dict[str, Any]]], list[str]]:
    targets: dict[str, tuple[str, dict[str, Any]]] = {}
    errors: list[str] = []
    for source_key, source in sources.items():
        names = source.get("skills")
        if not isinstance(names, list) or not names:
            errors.append(f"{source_key}: skills must be a non-empty list")
            continue
        for name in names:
            if not isinstance(name, str) or not name:
                errors.append(f"{source_key}: contains an invalid skill name")
            elif name in targets:
                errors.append(f"{name}: appears in more than one provenance source")
            else:
                targets[name] = (source_key, source)
    return targets, errors


def resolve(repo_root: Path, check: bool = False) -> tuple[int, list[str]]:
    manifest_path = repo_root / "manifest.json"
    sources_path = repo_root / "provenance" / "upstream_sources.json"
    manifest = load_json(manifest_path)
    sources: dict[str, dict[str, Any]] = load_json(sources_path)
    targets, errors = build_targets(sources)

    changed = 0
    skills: list[dict[str, Any]] = manifest["skills"]
    manifest_names = {skill.get("name") for skill in skills}
    for missing in sorted(set(targets) - manifest_names):
        errors.append(f"{missing}: mapped skill is missing from manifest.json")

    for skill in skills:
        name = str(skill.get("name", ""))
        target = targets.get(name)

        if skill.get("audit_status") == UNRESOLVED_STATUS and target is None:
            errors.append(f"{name}: unresolved skill has no exact pinned source mapping")
            continue
        if target is None:
            continue

        expected_source_key, source = target
        if skill.get("source") != expected_source_key:
            errors.append(
                f"{name}: source {skill.get('source')!r} does not match mapped source {expected_source_key!r}"
            )
            continue

        expected = expected_fields(skill, source)
        expected_license = license_text(source, name)
        license_path = repo_root / skill["path"] / "LICENSE.txt"
        fields_match = all(skill.get(key) == value for key, value in expected.items())
        license_matches = (
            license_path.is_file()
            and license_path.read_text(encoding="utf-8") == expected_license
        )

        if check:
            if not fields_match:
                errors.append(f"{name}: provenance fields are unresolved or stale")
            if not license_matches:
                errors.append(f"{name}: generated LICENSE.txt is missing or stale")
            continue

        if not fields_match or not license_matches:
            changed += 1
        skill.update(expected)
        license_path.write_text(expected_license, encoding="utf-8")

    if errors:
        return changed, errors

    expected_manifest = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    expected_inventory = render_skills_md(skills)

    if check:
        if manifest_path.read_text(encoding="utf-8-sig") != expected_manifest:
            errors.append("manifest.json is not in canonical generated form")
        inventory_path = repo_root / "SKILLS.md"
        if not inventory_path.is_file() or inventory_path.read_text(encoding="utf-8") != expected_inventory:
            errors.append("SKILLS.md is stale")
    else:
        manifest_path.write_text(expected_manifest, encoding="utf-8")
        (repo_root / "SKILLS.md").write_text(expected_inventory, encoding="utf-8")

    return changed, errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="Verify resolved files without changing them.")
    args = parser.parse_args(argv)

    changed, errors = resolve(args.repo_root.resolve(), args.check)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    action = "Verified" if args.check else "Resolved"
    print(f"{action} provenance for {changed} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
