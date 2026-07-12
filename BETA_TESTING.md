# Beta testing

Help verify that Codex Skills Pack works outside the maintainer's environment.

## What to test

Use a temporary destination so the test cannot overwrite your existing Codex setup.

### macOS or Linux

```sh
repo_dir="$(pwd)"
test_dir="$(mktemp -d)"
python3 install.py --source "$repo_dir" --dest "$test_dir" --all --dry-run
python3 install.py --source "$repo_dir" --dest "$test_dir" --all
```

### Windows PowerShell

```powershell
$TestDir = Join-Path $env:TEMP ("codex-skills-pack-" + [guid]::NewGuid())
.\install.ps1 -Source . -Dest $TestDir -All -DryRun
.\install.ps1 -Source . -Dest $TestDir -All
```

## Report the result

Open an installation report and include:

- operating system and version;
- Python or PowerShell version;
- Codex version, when known;
- command used;
- number of skills installed;
- whether an existing destination was preserved correctly;
- any error output with credentials and private paths removed.

A successful report is useful. Failure reports are equally useful when they are reproducible.

## Verified adopters

After testing, you may also add yourself or your project to [`ADOPTERS.md`](ADOPTERS.md) through a pull request. Entries require public evidence and must reflect real use.
