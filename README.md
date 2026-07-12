# Codex Skills Pack

A cross-platform distribution and maintenance layer for reusable Codex skills.

The repository packages 120 catalogued skills behind one installer, records where every skill came from, and keeps licence evidence beside the code where possible. It is designed for people who want to install a useful set of Codex skills without manually copying directories or silently overwriting local customisations.

## Trust model

Skills with verified licence evidence are installable by default. Entries that still rely on metadata-only provenance remain visible in the catalogue but are excluded unless the user explicitly passes `--include-unverified`.

This is intentional. A large skill collection is not useful if users cannot tell what they are installing or whether it can be redistributed safely.

- Codex system skills are excluded.
- Restricted or proprietary temporary skills are excluded.
- Existing local skills are never overwritten unless `--force` is supplied.
- `--dry-run` previews changes without writing files.
- `manifest.json` and `SKILLS.md` record source, licence, evidence, origin and audit status.

## Install

### macOS, Linux or any system with Python 3

```sh
python3 -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/starsaintf/codex-skills-pack/main/install.py').read().decode())"
```

### Windows PowerShell

```powershell
irm https://raw.githubusercontent.com/starsaintf/codex-skills-pack/main/install.ps1 | iex
```

The installer writes to `$CODEX_HOME/skills` when `CODEX_HOME` is set. Otherwise it uses `~/.codex/skills`.

## Common commands

Clone the repository, then run commands from its root:

```sh
# Interactive selection
python3 install.py --source .

# List verified skills
python3 install.py --source . --list

# Preview installation
python3 install.py --source . --all --dry-run

# Install every verified skill
python3 install.py --source . --all

# Replace matching installed skills
python3 install.py --source . --all --force

# Include provenance-unresolved entries explicitly
python3 install.py --source . --list --include-unverified
```

Restart Codex after installation so newly installed skills are discovered.

## Repository validation

The repository ships a validator and tests used by CI on Windows, macOS and Linux.

```sh
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

The normal validator reports unresolved provenance as a warning. Maintainers can use strict mode before a release:

```sh
python3 scripts/validate_repository.py --strict-provenance
```

Strict mode will continue to fail until every metadata-only entry has a captured upstream source and licence file. That failure is a tracked release-quality signal, not something to hide.

## Catalogue

See [`SKILLS.md`](SKILLS.md) for the readable catalogue and [`manifest.json`](manifest.json) for the machine-readable inventory.

## Contributing and security

Contributions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before adding or updating a skill. Report security problems through the private process in [`SECURITY.md`](SECURITY.md), not a public issue.

The current maintenance priorities are documented in [`ROADMAP.md`](ROADMAP.md).

## Licence

The repository packaging, installers, tests, generated inventories and locally authored skills are MIT licensed under the root [`LICENSE`](LICENSE).

Individual skills may use a different licence. A skill-level `LICENSE.txt` controls that skill where present. Do not treat the root MIT licence as overriding an embedded upstream licence.
