from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "resolve_provenance.py"
SPEC = importlib.util.spec_from_file_location("resolve_provenance", MODULE_PATH)
assert SPEC and SPEC.loader
resolver = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(resolver)


class ResolveProvenanceTests(unittest.TestCase):
    def make_repo(self) -> Path:
        root = Path(tempfile.mkdtemp())
        skill_dir = root / "skills" / "example"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text("# Example\n", encoding="utf-8")
        (root / "provenance").mkdir()
        manifest = {
            "skills": [
                {
                    "name": "example",
                    "path": "skills/example",
                    "description": "Example skill",
                    "license": "MIT from metadata",
                    "source": "example plugin",
                    "license_evidence": "metadata only",
                    "origin_url": "",
                    "origin_ref": "not captured",
                    "audit_status": resolver.UNRESOLVED_STATUS,
                }
            ]
        }
        sources = {
            "example plugin": {
                "skills": ["example"],
                "repository": "https://github.com/example/project",
                "revision": "abc123",
                "skill_base": "skills",
                "license_evidence_url": "https://github.com/example/project/blob/abc123/LICENSE",
                "license_name": "MIT",
                "copyright": "Copyright (c) Example",
            }
        }
        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        (root / "provenance" / "upstream_sources.json").write_text(
            json.dumps(sources), encoding="utf-8"
        )
        return root

    def test_resolve_then_check(self) -> None:
        root = self.make_repo()
        changed, errors = resolver.resolve(root)
        self.assertEqual(changed, 1)
        self.assertEqual(errors, [])
        resolved = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(resolved["skills"][0]["audit_status"], resolver.RESOLVED_STATUS)
        self.assertTrue((root / "skills" / "example" / "LICENSE.txt").is_file())

        changed, errors = resolver.resolve(root, check=True)
        self.assertEqual(changed, 0)
        self.assertEqual(errors, [])

    def test_unknown_unresolved_source_fails(self) -> None:
        root = self.make_repo()
        (root / "provenance" / "upstream_sources.json").write_text("{}", encoding="utf-8")
        _, errors = resolver.resolve(root)
        self.assertTrue(errors)

    def test_mapping_cannot_touch_another_skill_from_same_source(self) -> None:
        root = self.make_repo()
        manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        protected = dict(manifest["skills"][0])
        protected.update(
            {
                "name": "protected",
                "path": "skills/protected",
                "license": "Apache-2.0",
                "license_evidence": "Embedded license file: skills/protected/LICENSE.txt",
                "audit_status": "license-file-present",
            }
        )
        protected_dir = root / "skills" / "protected"
        protected_dir.mkdir()
        (protected_dir / "SKILL.md").write_text("# Protected\n", encoding="utf-8")
        (protected_dir / "LICENSE.txt").write_text("Apache-2.0\n", encoding="utf-8")
        manifest["skills"].append(protected)
        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

        _, errors = resolver.resolve(root)
        self.assertEqual(errors, [])
        after = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        protected_after = next(skill for skill in after["skills"] if skill["name"] == "protected")
        self.assertEqual(protected_after["license"], "Apache-2.0")
        self.assertEqual((protected_dir / "LICENSE.txt").read_text(encoding="utf-8"), "Apache-2.0\n")


if __name__ == "__main__":
    unittest.main()
