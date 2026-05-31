#!/usr/bin/env python3
"""Install this repository's Codex skills into CODEX_HOME."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
import textwrap
import urllib.request
import zipfile
from pathlib import Path


REPO_ZIP_URL = "https://github.com/starsaintf/codex-skills-pack/archive/refs/heads/main.zip"


def codex_home() -> Path:
    configured = os.environ.get("CODEX_HOME")
    if configured:
        return Path(configured).expanduser()
    return Path.home() / ".codex"


def read_manifest(repo_root: Path) -> dict:
    manifest_path = repo_root / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest.json not found in {repo_root}")
    return json.loads(manifest_path.read_text(encoding="utf-8-sig"))


def download_repo() -> tempfile.TemporaryDirectory[str]:
    tmp = tempfile.TemporaryDirectory(prefix="codex-skills-pack-")
    archive_path = Path(tmp.name) / "repo.zip"

    print(f"Downloading {REPO_ZIP_URL}")
    urllib.request.urlretrieve(REPO_ZIP_URL, archive_path)

    with zipfile.ZipFile(archive_path) as archive:
        archive.extractall(tmp.name)

    roots = [path for path in Path(tmp.name).iterdir() if path.is_dir()]
    if not roots:
        tmp.cleanup()
        raise RuntimeError("Downloaded archive did not contain a repository folder")

    tmp.repo_root = roots[0]  # type: ignore[attr-defined]
    return tmp


def resolve_repo_root(source: str | None) -> tuple[Path, tempfile.TemporaryDirectory[str] | None]:
    if source:
        return Path(source).expanduser().resolve(), None
    tmp = download_repo()
    return tmp.repo_root, tmp  # type: ignore[attr-defined]


def summarize(text: str, width: int = 92) -> str:
    compact = " ".join(text.split())
    return textwrap.shorten(compact, width=width, placeholder="...")


def print_skill_list(skills: list[dict], selected: set[int] | None = None) -> None:
    print()
    print("Codex Skills Pack")
    print("=" * 17)
    print(f"{len(skills)} non-system skills available")
    print()
    for index, skill in enumerate(skills, start=1):
        marker = ""
        if selected is not None:
            marker = "[x]" if index in selected else "[ ]"
            marker += " "
        description = summarize(skill.get("description", ""))
        print(f"{marker}{index:2}. {skill['name']}")
        if description:
            print(f"      {description}")
    print()


def parse_selection(text: str, max_index: int) -> set[int]:
    selected: set[int] = set()
    for chunk in text.replace(",", " ").split():
        if "-" in chunk:
            start_text, end_text = chunk.split("-", 1)
            start = int(start_text)
            end = int(end_text)
            if start > end:
                start, end = end, start
            values = range(start, end + 1)
        else:
            values = [int(chunk)]
        for value in values:
            if value < 1 or value > max_index:
                raise ValueError(f"{value} is outside 1-{max_index}")
            selected.add(value)
    return selected


def choose_skills(skills: list[dict]) -> list[dict]:
    selected = set(range(1, len(skills) + 1))
    visible = list(range(1, len(skills) + 1))

    while True:
        visible_skills = [skills[index - 1] for index in visible]
        visible_selected = {offset for offset, actual in enumerate(visible, start=1) if actual in selected}
        print_skill_list(visible_skills, visible_selected)
        print("Commands: install | all | none | filter <text> | clear | q")
        print("Toggle skills with numbers or ranges, for example: 1 4 8-12")
        choice = input("Select> ").strip()

        if not choice or choice.lower() in {"install", "i"}:
            return [skills[index - 1] for index in sorted(selected)]
        if choice.lower() in {"q", "quit", "cancel"}:
            raise SystemExit("Cancelled.")
        if choice.lower() in {"all", "a", "*"}:
            selected = set(range(1, len(skills) + 1))
            continue
        if choice.lower() in {"none", "n"}:
            selected.clear()
            continue
        if choice.lower() in {"clear", "reset"}:
            visible = list(range(1, len(skills) + 1))
            continue
        if choice.lower().startswith("filter "):
            query = choice[7:].strip().lower()
            visible = [
                index
                for index, skill in enumerate(skills, start=1)
                if query in skill["name"].lower()
                or query in skill.get("description", "").lower()
                or query in skill.get("source", "").lower()
            ]
            if not visible:
                print(f"No skills matched {query!r}.")
                visible = list(range(1, len(skills) + 1))
            continue

        try:
            toggles = parse_selection(choice, len(visible))
        except ValueError as exc:
            print(f"Invalid selection: {exc}")
            continue

        for visible_index in toggles:
            actual_index = visible[visible_index - 1]
            if actual_index in selected:
                selected.remove(actual_index)
            else:
                selected.add(actual_index)


def install_skill(source_dir: Path, dest_dir: Path, force: bool, dry_run: bool) -> str:
    if not (source_dir / "SKILL.md").exists():
        raise FileNotFoundError(f"{source_dir} does not contain SKILL.md")

    if dest_dir.exists():
        if not force:
            return "skipped"
        if dry_run:
            return "would replace"
        shutil.rmtree(dest_dir)

    if dry_run:
        return "would install"

    dest_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_dir, dest_dir)
    return "installed"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Install the Codex Skills Pack.")
    parser.add_argument("--source", help="Install from a local repository checkout instead of GitHub.")
    parser.add_argument("--dest", help="Install into this skills directory instead of CODEX_HOME/skills.")
    parser.add_argument("--force", action="store_true", help="Replace skills that are already installed.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without writing files.")
    parser.add_argument("--all", action="store_true", help="Install every skill without opening the selector.")
    parser.add_argument("--yes", "-y", action="store_true", help="Alias for --all for unattended installs.")
    parser.add_argument("--list", action="store_true", help="List all available skills and exit.")
    args = parser.parse_args(argv)

    tmp: tempfile.TemporaryDirectory[str] | None = None
    try:
        repo_root, tmp = resolve_repo_root(args.source)
        manifest = read_manifest(repo_root)
        all_skills = sorted(manifest["skills"], key=lambda skill: skill["name"])
        skills_dir = Path(args.dest).expanduser() if args.dest else codex_home() / "skills"

        print(f"Source: {repo_root}")
        print(f"Destination: {skills_dir}")
        print_skill_list(all_skills)

        if args.list:
            return 0

        if args.all or args.yes or not sys.stdin.isatty():
            selected_skills = all_skills
        else:
            selected_skills = choose_skills(all_skills)

        if not selected_skills:
            print("No skills selected. Nothing to install.")
            return 0

        print(f"Installing {len(selected_skills)} selected skill(s).")
        counts: dict[str, int] = {}
        for skill in selected_skills:
            name = skill["name"]
            source_dir = repo_root / skill["path"]
            dest_dir = skills_dir / name
            status = install_skill(source_dir, dest_dir, args.force, args.dry_run)
            counts[status] = counts.get(status, 0) + 1
            print(f"{status:13} {name}")

        summary = ", ".join(f"{count} {status}" for status, count in sorted(counts.items()))
        print(f"Done: {summary}")
        if not args.dry_run:
            print("Restart Codex to pick up newly installed skills.")
        return 0
    finally:
        if tmp:
            tmp.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
