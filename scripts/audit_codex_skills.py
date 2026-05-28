#!/usr/bin/env python3
"""Audit SKILL.md files under a Codex home directory."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "cp1252"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def parse_frontmatter(path: Path) -> dict[str, object]:
    text = read_text(path)
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}

    data: dict[str, object] = {}
    current_key: str | None = None
    current_list: list[str] | None = None
    for raw_line in match.group(1).splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        key_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if key_match:
            key, value = key_match.groups()
            key = key.strip()
            value = value.strip()
            current_key = key
            current_list = None
            if value:
                data[key] = value.strip("\"'")
            else:
                data[key] = {}
            continue
        list_match = re.match(r"^\s*-\s*(.+)$", line)
        if list_match and current_key:
            if current_list is None:
                current_list = []
                data[current_key] = current_list
            current_list.append(list_match.group(1).strip().strip("\"'"))
    return data


def has_license(skill_dir: Path) -> bool:
    return any((skill_dir / name).exists() for name in ("LICENSE", "LICENSE.md", "LICENSE.txt"))


def source_kind(path: Path, codex_home: Path) -> str:
    relative = path.relative_to(codex_home)
    parts = relative.parts
    text = str(relative).replace("\\", "/")

    if len(parts) >= 2 and parts[0] == "skills" and parts[1] == ".system":
        return "system-skill"
    if len(parts) >= 2 and parts[0] == "skills":
        return "user-installed-skill"
    if text.startswith("plugins/cache/") and "/skills/" in text:
        return "plugin-skill"
    if text.startswith("plugins/cache/"):
        return "plugin-cache-other"
    if text.startswith("cache/"):
        return "codex-cache"
    if text.startswith("vendor_imports/"):
        return "vendor-import"
    if text.startswith(".tmp/") or text.startswith("tmp/"):
        return "temp"
    if text.startswith("sessions/"):
        return "session-artifact"
    return "other"


def likely_installable(kind: str, path: Path) -> bool:
    if kind in {"user-installed-skill", "plugin-skill"}:
        return True
    return False


def audit(codex_home: Path, include_system: bool) -> dict[str, object]:
    records = []
    for skill_md in codex_home.rglob("SKILL.md"):
        kind = source_kind(skill_md, codex_home)
        if not include_system and kind == "system-skill":
            continue
        frontmatter = parse_frontmatter(skill_md)
        name = str(frontmatter.get("name", "")).strip()
        description = str(frontmatter.get("description", "")).strip()
        skill_dir = skill_md.parent
        relative = skill_md.relative_to(codex_home)
        records.append(
            {
                "path": str(relative).replace("\\", "/"),
                "dir": str(skill_dir.relative_to(codex_home)).replace("\\", "/"),
                "kind": kind,
                "name": name,
                "description": description,
                "has_frontmatter": bool(frontmatter),
                "has_name": bool(name),
                "has_description": bool(description),
                "has_license_file": has_license(skill_dir),
                "likely_installable": likely_installable(kind, skill_md),
            }
        )

    by_kind = Counter(record["kind"] for record in records)
    by_name = defaultdict(list)
    for record in records:
        if record["name"]:
            by_name[record["name"]].append(record)

    duplicate_names = {
        name: [
            {
                "kind": item["kind"],
                "dir": item["dir"],
                "has_license_file": item["has_license_file"],
                "likely_installable": item["likely_installable"],
            }
            for item in items
        ]
        for name, items in sorted(by_name.items())
        if len(items) > 1
    }

    installable = [record for record in records if record["likely_installable"]]
    non_installable = [record for record in records if not record["likely_installable"]]
    missing_frontmatter = [record for record in records if not record["has_frontmatter"]]
    missing_name = [record for record in records if not record["has_name"]]
    missing_description = [record for record in records if not record["has_description"]]

    return {
        "codex_home": str(codex_home),
        "include_system": include_system,
        "total_skill_md": len(records),
        "counts_by_kind": dict(sorted(by_kind.items())),
        "unique_named_skills": len(by_name),
        "duplicate_name_count": len(duplicate_names),
        "installable_count": len(installable),
        "non_installable_count": len(non_installable),
        "missing_frontmatter_count": len(missing_frontmatter),
        "missing_name_count": len(missing_name),
        "missing_description_count": len(missing_description),
        "installable": installable,
        "non_installable_samples": non_installable[:200],
        "duplicate_names": duplicate_names,
        "records": records,
    }


def write_markdown(report: dict[str, object], path: Path) -> None:
    counts = report["counts_by_kind"]
    installable = report["installable"]
    duplicate_names = report["duplicate_names"]

    lines = [
        "# Codex Skill Audit",
        "",
        f"Codex home: `{report['codex_home']}`",
        f"System skills included: `{report['include_system']}`",
        "",
        "## Summary",
        "",
        f"- Total `SKILL.md` files audited: {report['total_skill_md']}",
        f"- Unique named skills: {report['unique_named_skills']}",
        f"- Likely concrete installable skills: {report['installable_count']}",
        f"- Non-installable/cache/vendor/session artifacts: {report['non_installable_count']}",
        f"- Duplicate skill names: {report['duplicate_name_count']}",
        f"- Missing frontmatter: {report['missing_frontmatter_count']}",
        f"- Missing `name`: {report['missing_name_count']}",
        f"- Missing `description`: {report['missing_description_count']}",
        "",
        "## Counts By Kind",
        "",
    ]
    for kind, count in counts.items():
        lines.append(f"- `{kind}`: {count}")

    lines.extend(["", "## Likely Concrete Installable Skills", ""])
    for index, record in enumerate(installable, start=1):
        description = " ".join(str(record["description"]).split())
        if len(description) > 130:
            description = description[:127] + "..."
        lines.append(f"{index}. `{record['name']}`")
        lines.append(f"   - Kind: `{record['kind']}`")
        lines.append(f"   - Path: `{record['dir']}`")
        lines.append(f"   - License file: `{record['has_license_file']}`")
        lines.append(f"   - Description: {description}")
        lines.append("")

    lines.extend(["", "## Duplicate Names", ""])
    if duplicate_names:
        for name, items in duplicate_names.items():
            lines.append(f"- `{name}`: {len(items)} copies")
            for item in items[:8]:
                lines.append(f"  - `{item['kind']}` `{item['dir']}`")
            if len(items) > 8:
                lines.append(f"  - ... {len(items) - 8} more")
    else:
        lines.append("No duplicate names found.")

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- `user-installed-skill` and `plugin-skill` are treated as concrete installable skills.",
            "- `plugin-cache-other`, `codex-cache`, `vendor-import`, `temp`, `session-artifact`, and `other` are not treated as installable without manual review.",
            "- Codex system skills are excluded by default.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--codex-home", default=str(Path.home() / ".codex"))
    parser.add_argument("--include-system", action="store_true")
    parser.add_argument("--json-out", default="codex-skill-audit.json")
    parser.add_argument("--md-out", default="codex-skill-audit.md")
    args = parser.parse_args()

    codex_home = Path(args.codex_home).expanduser().resolve()
    report = audit(codex_home, args.include_system)
    Path(args.json_out).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    write_markdown(report, Path(args.md_out))
    print(f"Audited {report['total_skill_md']} SKILL.md files")
    print(f"Likely installable: {report['installable_count']}")
    print(f"Wrote {args.json_out}")
    print(f"Wrote {args.md_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
