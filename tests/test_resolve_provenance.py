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


if __name__ == "__main__":
    unittest.main()
