# Codex Skills Pack

A cross-platform distribution and maintenance layer for reusable Codex skills.

The repository packages 120 catalogued skills behind one installer, records where every skill came from, and keeps licence evidence beside the code. It is designed for people who want to install a useful set of Codex skills without manually copying directories or silently overwriting local customisations.

## Current release

The first audited release is [`v0.1.0`](https://github.com/starsaintf/codex-skills-pack/releases/tag/v0.1.0).

Release assets include the Python installer, PowerShell installer, machine-readable manifest, and SHA-256 checksums.

## Trust model

Every redistributed skill currently has recorded licence evidence. The catalogue also pins upstream revisions for entries that were recovered from plugin backups.

- Codex system skills are excluded.
- Restricted or proprietary temporary skills are excluded.
- Existing local skills are never overwritten unless `--force` is supplied.
- `--dry-run` previews changes without writing files.
- `manifest.json` and `SKILLS.md` record source, licence, evidence, origin and audit status.
- Strict provenance validation must pass before a release can be published.

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

# List available skills
python3 install.py --source . --list

# Preview installation
python3 install.py --source . --all --dry-run

# Install every skill
python3 install.py --source . --all

# Replace matching installed skills
python3 install.py --source . --all --force
```

Restart Codex after installation so newly installed skills are discovered.

## Help verify the installers

Independent installation reports are the most useful contribution right now.

Follow [`BETA_TESTING.md`](BETA_TESTING.md) to test in a temporary directory, then open an [installation report](https://github.com/starsaintf/codex-skills-pack/issues/new?template=installation-report.yml). The public beta is tracked in [issue #7](https://github.com/starsaintf/codex-skills-pack/issues/7).

After real use, people and projects can add a reviewable entry to [`ADOPTERS.md`](ADOPTERS.md). Supportive or unverified entries are not accepted.

## Repository validation

The repository ships a validator and tests used by CI on Windows, macOS and Linux.

```sh
python3 scripts/validate_repository.py --strict-provenance
python3 scripts/resolve_provenance.py --check
python3 -m unittest discover -s tests -v
```

The release workflow also compiles the Python files, performs an installer dry-run, generates checksums, and refuses to publish when any verification step fails.

## Catalogue

See [`SKILLS.md`](SKILLS.md) for the readable catalogue and [`manifest.json`](manifest.json) for the machine-readable inventory.

## Contributing and security

Contributions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before adding or updating a skill. Report security problems through the private process in [`SECURITY.md`](SECURITY.md), not a public issue.

The current maintenance priorities are documented in [`ROADMAP.md`](ROADMAP.md).

## Licence

The repository packaging, installers, tests, generated inventories and locally authored skills are MIT licensed under the root [`LICENSE`](LICENSE).

Individual skills may use a different licence. A skill-level `LICENSE.txt` controls that skill where present. Do not treat the root MIT licence as overriding an embedded upstream licence.
