# Contributing

Thank you for helping make Codex skills easier to install and safer to redistribute.

## Before opening a pull request

1. Open an issue for large changes or new distribution behaviour.
2. Keep each pull request focused on one change.
3. Run the validator and test suite locally.
4. Never add credentials, private prompts, proprietary temporary files or Codex system skills.

```sh
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
python3 install.py --source . --all --dry-run
```

## Adding a skill

Every skill must have:

- a unique lowercase directory under `skills/`;
- a `SKILL.md` file;
- one matching entry in `manifest.json`;
- a matching generated/readable entry in `SKILLS.md`;
- a clear source and upstream origin;
- licence evidence that can be reviewed independently.

Use `audit_status: license-file-present` only when the referenced licence file is actually included in the repository. Use `root-mit-local` only for work authored for this repository and covered by the root MIT licence.

Do not present metadata-only licence claims as verified. New skills without reviewable licence evidence should not be added to normal releases.

## Pull request description

Explain:

- what changed;
- why it belongs in this distribution;
- where the code or skill came from;
- what licence applies;
- how you tested installation;
- any compatibility or security risk.

## Review standard

A change may be declined even when it works technically if its provenance is unclear, it weakens installer safety, or it creates maintenance work without enough ecosystem value.
