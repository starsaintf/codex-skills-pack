from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts" / "validate_repository.py")
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class RepositoryValidatorTests(unittest.TestCase):
    def make_repo(self, audit_status: str = "root-mit-local") -> Path:
        self.tempdir = tempfile.TemporaryDirectory()
        root = Path(self.tempdir.name)
        (root / "LICENSE").write_text("MIT", encoding="utf-8")
        skill_dir = root / "skills" / "example"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text("# Example", encoding="utf-8")
        manifest = {
            "skills": [
                {
                    "name": "example",
                    "path": "skills/example",
                    "description": "Example skill",
                    "license": "MIT",
                    "source": "local-codex-user-skill",
                    "license_evidence": "Root LICENSE applies to local-authored skill",
                    "origin_url": "",
                    "origin_ref": "local repository/root MIT license",
                    "audit_status": audit_status,
                }
            ]
        }
        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return root

    def tearDown(self) -> None:
        if hasattr(self, "tempdir"):
            self.tempdir.cleanup()

    def test_valid_local_skill_passes(self) -> None:
        errors, warnings = validator.validate(self.make_repo())
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_unresolved_provenance_warns_by_default(self) -> None:
        root = self.make_repo("metadata-only-needs-upstream-license-file")
        errors, warnings = validator.validate(root)
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)

    def test_unresolved_provenance_fails_in_strict_mode(self) -> None:
        root = self.make_repo("metadata-only-needs-upstream-license-file")
        errors, _ = validator.validate(root, strict_provenance=True)
        self.assertEqual(len(errors), 1)


if __name__ == "__main__":
    unittest.main()
