# Codex Skills Pack

An open-source pack of Codex skills collected from this machine and packaged so other Codex users can install them with one command.

## Install

macOS, Linux, or any OS with Python:

```sh
python3 -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/starsaintf/codex-skills-pack/main/install.py').read().decode())"
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/starsaintf/codex-skills-pack/main/install.ps1 | iex
```

The installer opens an interactive terminal selector. Users can review the full skill list, choose specific skills, enter ranges like `1 4 8-12`, or select all.

The installer copies skills into `$CODEX_HOME/skills` when `CODEX_HOME` is set, otherwise into `~/.codex/skills`.

Restart Codex after installation so the new skills are discovered.

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

See [SKILLS.md](SKILLS.md) for the full source, license, and description inventory that should be reviewed before pushing or publishing.

## Installer Options

Download and install from GitHub:

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

Overwrite existing installed skills:

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

## Publishing

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

This repository is MIT licensed except where an individual skill contains its own `LICENSE.txt`.

Several included skills were imported from Anthropic's public `anthropics/skills` repository and retain their Apache-2.0 license files. The root license covers the packaging, installer, manifest, and local skills without their own embedded license.

Vercel plugin skills were imported from the Apache-2.0 `vercel/vercel-plugin` package metadata and are identified in `manifest.json`.

Codex system skills from `~/.codex/skills/.system` are not included.
