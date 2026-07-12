# Changelog

## v0.1.0 — First audited release

Codex Skills Pack now has a versioned, cross-platform release process and a fully reviewed provenance inventory.

### Included

- 120 catalogued Codex skills.
- Interactive and unattended installers for Python and Windows PowerShell.
- Safe defaults that do not overwrite existing local skills without `--force`.
- Dry-run and custom destination support.
- Machine-readable provenance in `manifest.json` and a readable catalogue in `SKILLS.md`.
- Embedded licence evidence for every redistributed skill.
- Pinned upstream revisions for the 38 entries that previously relied on metadata-only evidence.

### Verification

- Repository structure and licence validation.
- Strict provenance validation with zero unresolved entries.
- Unit tests for installers, repository validation, and provenance generation.
- CI on Ubuntu, macOS, and Windows with Python 3.10 and 3.12.

### Release assets

The release includes the Python installer, PowerShell installer, machine-readable manifest, and a SHA-256 checksum file.
