# Codex Skills Pack

An open-source pack of Codex skills collected from this machine and packaged so other Codex users can install them with one command.

## What This Installs

This repository installs ready-to-use Codex skills into your Codex skills directory.

- Skills are copied into `$CODEX_HOME/skills` when `CODEX_HOME` is set.
- Otherwise, skills are copied into `~/.codex/skills`.
- Existing skills are skipped by default so local customizations are not overwritten.
- Restart Codex after installation so new skills are discovered.

Codex system skills are intentionally excluded.

## Quick Install

Users run the installer file for their platform; they do not run individual skill files directly.

- macOS, Linux, or any OS with Python: run `install.py`
- Windows PowerShell: run `install.ps1`

One-line install for macOS, Linux, or any OS with Python:

```sh
python3 -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/starsaintf/codex-skills-pack/main/install.py').read().decode())"
```

One-line install for Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/starsaintf/codex-skills-pack/main/install.ps1 | iex
```

The installer opens an interactive terminal selector. Users can review the full skill list, choose specific skills, enter ranges like `1 4 8-12`, or select all.

## Requirements

- Codex with local skill support.
- Python 3 for `install.py`.
- PowerShell for `install.ps1` on Windows.
- Network access when installing directly from GitHub.

No package manager or Python dependency install is required.

## Included Skills

This pack includes 120 non-system skills:

- `actionable-pushback`
- `agent-browser`
- `agent-browser-verify`
- `agent-memory-context-efficiency`
- `ai-elements`
- `ai-gateway`
- `ai-generation-persistence`
- `ai-sdk`
- `algorithmic-art`
- `android-emulator-qa`
- `android-performance`
- `auth`
- `bootstrap`
- `brainstorming`
- `brand-guidelines`
- `building-native-ui`
- `canvas-design`
- `chat-sdk`
- `claude-api`
- `cms`
- `codex-expo-run-actions`
- `cron-jobs`
- `deployments-cicd`
- `dispatching-parallel-agents`
- `email`
- `env-vars`
- `executing-plans`
- `expo-api-routes`
- `expo-cicd-workflows`
- `expo-deployment`
- `expo-dev-client`
- `expo-module`
- `expo-tailwind-setup`
- `expo-ui-jetpack-compose`
- `expo-ui-swift-ui`
- `external-design-skill-router`
- `finishing-a-development-branch`
- `frontend-design`
- `geist`
- `geistdocs`
- `gh-address-comments`
- `gh-fix-ci`
- `github`
- `internal-comms`
- `investigation-mode`
- `json-render`
- `marketplace`
- `mcp-builder`
- `micro`
- `native-data-fetching`
- `ncc`
- `netlify-ai-gateway`
- `netlify-blobs`
- `netlify-caching`
- `netlify-cli-and-deploy`
- `netlify-config`
- `netlify-deploy`
- `netlify-edge-functions`
- `netlify-forms`
- `netlify-frameworks`
- `netlify-functions`
- `netlify-identity`
- `netlify-image-cdn`
- `next-forge`
- `nextjs`
- `notion-knowledge-capture`
- `notion-meeting-intelligence`
- `notion-research-documentation`
- `notion-spec-to-implementation`
- `observability`
- `payments`
- `react-best-practices`
- `receiving-code-review`
- `render-debug`
- `render-deploy`
- `render-migrate-from-heroku`
- `render-monitor`
- `render-workflows`
- `requesting-code-review`
- `routing-middleware`
- `runtime-cache`
- `satori`
- `sentry`
- `shadcn`
- `sign-in-with-vercel`
- `slack-gif-creator`
- `stripe-best-practices`
- `subagent-driven-development`
- `supabase`
- `supabase-postgres-best-practices`
- `swr`
- `systematic-debugging`
- `test-driven-development`
- `theme-factory`
- `turbopack`
- `turborepo`
- `upgrade-stripe`
- `upgrading-expo`
- `use-dom`
- `using-git-worktrees`
- `using-superpowers`
- `v0-dev`
- `vercel-agent`
- `vercel-api`
- `vercel-cli`
- `vercel-firewall`
- `vercel-flags`
- `vercel-functions`
- `vercel-queues`
- `vercel-sandbox`
- `vercel-services`
- `vercel-storage`
- `verification`
- `verification-before-completion`
- `web-artifacts-builder`
- `webapp-testing`
- `workflow`
- `writing-plans`
- `writing-skills`
- `yeet`

Codex system skills are intentionally excluded.

See [SKILLS.md](SKILLS.md) for the full source, license, and description inventory.

## Local Install And Options

After cloning this repository, run the installer from the repository root.

Interactive install from a local checkout:

```sh
python3 install.py
```

Install every skill without opening the selector:

```sh
python3 install.py --all
```

List all skills without installing:

```sh
python3 install.py --list
```

Preview without writing files:

```sh
python3 install.py --dry-run
```

Update existing installed skills by replacing matching directories:

```sh
python3 install.py --force
```

Install from a local checkout:

```sh
python3 install.py --source .
```

Install to a custom Codex home:

```sh
CODEX_HOME=/path/to/.codex python3 install.py
```

On Windows PowerShell:

```powershell
$env:CODEX_HOME = "C:\path\to\.codex"; python .\install.py --source .
```

## Safe Update Workflow

Preview first:

```sh
python3 install.py --dry-run --all
```

Then install or update:

```sh
python3 install.py --all --force
```

Use `--force` only when you want installed skills with the same names to be replaced.

## Maintainer Publishing

Create a public GitHub repository named `codex-skills-pack` under the `starsaintf` account, then push this folder:

```sh
git init
git add .
git commit -m "Publish Codex skills pack"
git branch -M main
git remote add origin git@github.com:starsaintf/codex-skills-pack.git
git push -u origin main
```

If you publish under a different account or repository name, update `REPO_ZIP_URL` in `install.py`, `$RepoZipUrl` in `install.ps1`, and the install commands above.

## Licensing

This repository's packaging, installers, generated inventories, and local-only skills are MIT licensed under the root `LICENSE`.

Individual skills may carry their own license. When a skill directory contains `LICENSE.txt`, that file travels with the skill and controls that skill's redistribution terms.

Several included skills were imported from Anthropic's public `anthropics/skills` repository and retain Apache-2.0 license files. The restricted/source-available Anthropic document skills (`docx`, `pdf`, `pptx`, and `xlsx`) are intentionally excluded.

Vercel plugin skills were imported from the Apache-2.0 `vercel/vercel-plugin` package metadata and now include per-skill Apache-2.0 `LICENSE.txt` files so selected installs preserve the license.

`manifest.json` and `SKILLS.md` include per-skill `source`, `license`, `license_evidence`, `origin_url`, `origin_ref`, and `audit_status` fields. Treat entries marked `metadata-only-needs-upstream-license-file` as provenance-tracked but still needing stronger upstream license-file evidence before broad redistribution.

Codex system skills from `~/.codex/skills/.system` are not included.
