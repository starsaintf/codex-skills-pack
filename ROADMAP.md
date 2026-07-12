# Roadmap

## Now: distribution hardening

- Run repository validation and installer tests across Windows, macOS and Linux.
- Exclude provenance-unresolved skills from default installation.
- Add contribution and private security-reporting processes.
- Resolve or remove every metadata-only licence entry.

## Next: release discipline

- Publish versioned releases instead of relying only on the moving `main` branch.
- Attach a manifest checksum and installer checksums to each release.
- Pin every imported skill to a captured upstream commit or release.
- Generate `SKILLS.md` from `manifest.json` to prevent catalogue drift.
- Add smoke tests for the PowerShell-only fallback path.

## Later: ecosystem maintenance

- Add compatibility metadata for Codex versions and operating systems.
- Track deprecations and upstream changes.
- Support signed or attestable release artifacts.
- Add issue templates for new skills, provenance repair and installer bugs.

The immediate release blocker is provenance. The project should not claim a fully audited catalogue while any skill still relies only on uncaptured metadata.
