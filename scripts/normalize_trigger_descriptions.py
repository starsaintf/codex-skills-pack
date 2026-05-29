#!/usr/bin/env python3
"""Normalize skill descriptions into active task-trigger wording."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

CURATED_TRIGGERS = {
    "agent-browser-verify": "Use when a dev server needs browser verification, screenshots, console checks, or visual regression checks after frontend changes.",
    "ai-generation-persistence": "Use when AI generations need stable IDs, addressable URLs, database persistence, resumability, or cost tracking.",
    "brainstorming": "Use when starting creative or product work such as new features, components, functionality, designs, or behavior changes.",
    "building-native-ui": "Use when building polished native app interfaces with Expo Router, React Native styling, navigation, animations, or platform UI patterns.",
    "claude-api": "Use when building, debugging, or optimizing Claude API and Anthropic SDK applications.",
    "expo-deployment": "Use when deploying Expo apps to the iOS App Store, Android Play Store, web hosting, or EAS API routes.",
    "expo-dev-client": "Use when building or distributing Expo development clients locally, with EAS, or through TestFlight.",
    "expo-ui-jetpack-compose": "Use when adding Jetpack Compose views or modifiers to Expo apps with @expo/ui/jetpack-compose.",
    "expo-ui-swift-ui": "Use when adding SwiftUI views or modifiers to Expo apps with @expo/ui/swift-ui.",
    "investigation-mode": "Use when debugging stuck, hung, broken, flaky, or confusing behavior that needs systematic investigation.",
    "react-best-practices": "Use when reviewing or editing multiple React TSX components for correctness, hooks usage, composition, rendering, or maintainability.",
    "supabase-postgres-best-practices": "Use when writing, reviewing, or optimizing Supabase Postgres queries, schemas, indexes, RLS policies, or database performance.",
    "upgrade-stripe": "Use when upgrading Stripe API versions, SDK versions, webhook versions, or integration patterns.",
    "use-dom": "Use when migrating web code into Expo DOM components, embedding web experiences in native apps, or sharing web UI across native and web.",
    "verification": "Use when verifying the full user-facing flow end-to-end across browser, API, database, deployment, or telemetry layers.",
    "web-artifacts-builder": "Use when creating elaborate multi-component HTML artifacts with modern frontend tooling, rich interactions, or generated visual experiences.",
    "webapp-testing": "Use when testing local web applications with Playwright, browser automation, screenshots, console logs, or interaction checks.",
    "yeet": "Use when publishing local changes to GitHub by checking scope, committing intentionally, pushing a branch, or opening a draft PR.",
}


def frontmatter_block(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("unterminated frontmatter")
    return text[: end + 4], text[end + 4 :]


def field_value(frontmatter: str, field: str) -> str:
    match = re.search(rf"^{field}:\s*(.+)$", frontmatter, re.MULTILINE)
    if not match:
        raise ValueError(f"missing {field}")
    return match.group(1).strip().strip('"')


def sentence_from_use_when(description: str) -> str | None:
    match = re.search(r"\bUse when\b.+", description, re.IGNORECASE)
    if not match:
        return None
    value = match.group(0).strip()
    value = re.sub(r"\s+", " ", value)
    return "Use when" + value[len("Use when") :]


def lower_first(value: str) -> str:
    return value[:1].lower() + value[1:] if value else value


def normalize_description(name: str, description: str) -> str:
    if name in CURATED_TRIGGERS:
        return CURATED_TRIGGERS[name]

    description = re.sub(r"\s+", " ", description.strip().strip('"'))
    existing = sentence_from_use_when(description)
    if existing:
        return existing

    replacements = [
        (r"^Guide for (.+)$", r"using \1"),
        (r"^Guidelines for (.+)$", r"working on \1"),
        (r"^Expert guidance for (.+)$", r"working with \1"),
        (r"^Reference for (.+)$", r"needing reference for \1"),
        (r"^Toolkit for (.+)$", r"working on \1"),
        (r"^Suite of tools for (.+)$", r"building \1"),
    ]
    for pattern, replacement in replacements:
        match = re.match(pattern, description)
        if match:
            trigger = re.sub(pattern, replacement, description)
            return f"Use when {lower_first(trigger)}"

    gerund_map = {
        "Build": "building",
        "Creating": "creating",
        "Create": "creating",
        "Deploy": "deploying",
        "Deploying": "deploying",
        "Debug": "debugging",
        "Debugging": "debugging",
        "Gather": "gathering",
        "Monitor": "monitoring",
        "Migrate": "migrating",
        "Prepare": "preparing",
        "Research": "researching",
        "Capture": "capturing",
        "Turn": "turning",
        "Set up": "setting up",
        "Sets up": "setting up",
        "Applies": "applying",
        "A set of resources to help me write": "writing",
        "Knowledge and utilities for creating": "creating",
        "Postgres performance optimization and best practices from": "optimizing",
        "Vercel Services": "working with Vercel Services",
    }
    for prefix, gerund in gerund_map.items():
        if description.startswith(prefix):
            rest = description[len(prefix) :].strip(" .-")
            return f"Use when {gerund} {lower_first(rest)}".strip()

    return f"Use when working with {name.replace('-', ' ')}: {description}"


def replace_description(frontmatter: str, description: str) -> str:
    return re.sub(
        r"^description:\s*.+$",
        f"description: {description}",
        frontmatter,
        count=1,
        flags=re.MULTILINE,
    )


def load_existing_manifest_metadata() -> dict[str, dict[str, str]]:
    manifest_path = ROOT / "manifest.json"
    if not manifest_path.exists():
        return {}
    manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    return {skill["name"]: skill for skill in manifest.get("skills", [])}


def load_skills() -> list[dict[str, str]]:
    existing_metadata = load_existing_manifest_metadata()
    skills: list[dict[str, str]] = []
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8-sig")
        frontmatter, body = frontmatter_block(text)
        name = field_value(frontmatter, "name")
        old_description = field_value(frontmatter, "description")
        new_description = normalize_description(name, old_description)
        if new_description != old_description:
            skill_md.write_text(
                replace_description(frontmatter, new_description) + body,
                encoding="utf-8",
            )
        skill = dict(existing_metadata.get(name, {}))
        skill.update(
            {
                "name": name,
                "path": f"skills/{skill_md.parent.name}",
                "description": new_description,
            }
        )
        skill.setdefault("license", "MIT")
        skill.setdefault("source", "local-codex-user-skill")
        skill.setdefault("license_evidence", "Root LICENSE applies to local-authored skill")
        skill.setdefault("origin_url", "")
        skill.setdefault("origin_ref", "local repository/root MIT license")
        skill.setdefault("audit_status", "root-mit-local")
        skills.append(skill)
    return sorted(skills, key=lambda item: item["name"])


def write_manifest(skills: list[dict[str, str]]) -> None:
    manifest_path = ROOT / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["skills"] = skills
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def write_skills_md(skills: list[dict[str, str]]) -> None:
    lines = ["# Skills", ""]
    for index, skill in enumerate(skills, 1):
        lines.extend(
            [
                f"{index}. `{skill['name']}`",
                f"   - Source: {skill['source']}",
                f"   - License: {skill['license']}",
                f"   - Evidence: {skill.get('license_evidence', '')}",
                f"   - Audit status: {skill.get('audit_status', '')}",
                f"   - Origin: {skill.get('origin_url') or skill.get('origin_ref', '')}",
                f"   - Description: {skill['description']}",
                "",
            ]
        )
    (ROOT / "SKILLS.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    skills = load_skills()
    write_manifest(skills)
    write_skills_md(skills)
    print(f"Normalized {len(skills)} skill descriptions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
