#!/usr/bin/env python3
"""Resolve metadata-only skill provenance from pinned upstream sources.

This script is intentionally network-free. The upstream repositories, revisions,
skill paths, licence declarations, and copyright notices are recorded in
provenance/upstream_sources.json after manual verification.
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


def license_text(source: dict[str, str], skill_name: str) -> str:
    upstream_skill = (
        f"{source['repository']}/tree/{source['revision']}/"
        f"{source['skill_base'].strip('/')}/{skill_name}"
    )
    return (
        "MIT License\n\n"
        f"{source['copyright']}\n\n"
        f"{MIT_TERMS}\n"
        "Upstream provenance\n"
        "-------------------\n"
        f"Skill source: {upstream_skill}\n"
        f"Pinned revision: {source['revision']}\n"
        f"Licence evidence: {source['license_evidence_url']}\n"
    )


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


def resolve(repo_root: Path, check: bool = False) -> tuple[int, list[str]]:
    manifest_path = repo_root / "manifest.json"
    sources_path = repo_root / "provenance" / "upstream_sources.json"
    manifest = load_json(manifest_path)
    sources: dict[str, dict[str, str]] = load_json(sources_path)

    changed = 0
    unresolved_sources: list[str] = []
    skills: list[dict[str, Any]] = manifest["skills"]

    for skill in skills:
        if skill.get("audit_status") != UNRESOLVED_STATUS:
            continue

        source_key = skill.get("source", "")
        source = sources.get(source_key)
        if source is None:
            unresolved_sources.append(f"{skill['name']}: {source_key}")
            continue

        skill_name = skill["name"]
        relative_license = Path(skill["path"]) / "LICENSE.txt"
        license_path = repo_root / relative_license
        expected_license = license_text(source, skill_name)

        origin_url = (
            f"{source['repository']}/tree/{source['revision']}/"
            f"{source['skill_base'].strip('/')}/{skill_name}"
        )
        updated = {
            "license": f"{source['license_name']}, see {relative_license.as_posix()}",
            "license_evidence": f"Embedded license file: {relative_license.as_posix()}",
            "origin_url": origin_url,
            "origin_ref": (
                f"Pinned to {source['repository']}@{source['revision']}; "
                f"licence evidence: {source['license_evidence_url']}"
            ),
            "audit_status": RESOLVED_STATUS,
        }

        if any(skill.get(key) != value for key, value in updated.items()):
            changed += 1
        skill.update(updated)

        if check:
            if not license_path.is_file() or license_path.read_text(encoding="utf-8") != expected_license:
                unresolved_sources.append(f"{skill_name}: generated LICENSE.txt is missing or stale")
        else:
            license_path.write_text(expected_license, encoding="utf-8")

    if unresolved_sources:
        return changed, unresolved_sources

    expected_manifest = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    expected_inventory = render_skills_md(skills)

    if check:
        if manifest_path.read_text(encoding="utf-8-sig") != expected_manifest:
            unresolved_sources.append("manifest.json has unresolved or non-canonical provenance data")
        inventory_path = repo_root / "SKILLS.md"
        if not inventory_path.is_file() or inventory_path.read_text(encoding="utf-8") != expected_inventory:
            unresolved_sources.append("SKILLS.md is stale")
    else:
        manifest_path.write_text(expected_manifest, encoding="utf-8")
        (repo_root / "SKILLS.md").write_text(expected_inventory, encoding="utf-8")

    return changed, unresolved_sources


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
