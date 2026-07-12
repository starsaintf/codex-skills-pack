from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("installer", ROOT / "install.py")
assert SPEC and SPEC.loader
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def test_parse_selection_supports_ranges_and_commas(self) -> None:
        self.assertEqual(installer.parse_selection("1, 3-5", 6), {1, 3, 4, 5})

    def test_parse_selection_rejects_out_of_range_values(self) -> None:
        with self.assertRaises(ValueError):
            installer.parse_selection("0", 3)

    def test_split_by_provenance(self) -> None:
        skills = [
            {"name": "verified", "audit_status": "license-file-present"},
            {"name": "local", "audit_status": "root-mit-local"},
            {"name": "pending", "audit_status": "metadata-only-needs-upstream-license-file"},
        ]
        verified, unresolved = installer.split_by_provenance(skills)
        self.assertEqual([item["name"] for item in verified], ["verified", "local"])
        self.assertEqual([item["name"] for item in unresolved], ["pending"])

    def test_install_skill_copies_a_valid_skill(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source"
            destination = root / "destination"
            source.mkdir()
            (source / "SKILL.md").write_text("# Example\n", encoding="utf-8")
            self.assertEqual(installer.install_skill(source, destination, False, False), "installed")
            self.assertTrue((destination / "SKILL.md").is_file())

    def test_read_manifest_requires_skills_array(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "manifest.json").write_text(json.dumps({"name": "bad"}), encoding="utf-8")
            with self.assertRaises(ValueError):
                installer.read_manifest(root)


if __name__ == "__main__":
    unittest.main()
