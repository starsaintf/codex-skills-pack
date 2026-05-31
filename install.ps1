param(
    [string]$Source = "",
    [string]$Dest = "",
    [switch]$Force,
    [switch]$All,
    [switch]$Yes,
    [switch]$List
)

$ErrorActionPreference = "Stop"
$RepoZipUrl = "https://github.com/starsaintf/codex-skills-pack/archive/refs/heads/main.zip"

function Get-CodexSkillsDirectory {
    if ($env:CODEX_HOME) {
        return (Join-Path $env:CODEX_HOME "skills")
    }
    return (Join-Path $HOME ".codex\skills")
}

function Get-PythonCommand {
    foreach ($candidate in @("python", "py", "python3")) {
        $command = Get-Command $candidate -ErrorAction SilentlyContinue
        if ($command) {
            return $candidate
        }
    }
    return ""
}

function Show-SkillNames {
    param([array]$Skills)

    Write-Host ""
    Write-Host "Codex Skills Pack"
    Write-Host "================="
    Write-Host "$($Skills.Count) non-system skills available"
    Write-Host ""

    for ($i = 0; $i -lt $Skills.Count; $i++) {
        $number = ($i + 1).ToString().PadLeft(2)
        Write-Host "$number. $($Skills[$i].name)"
    }

    Write-Host ""
}

function Convert-Selection {
    param([string]$Selection, [int]$Max)

    $indexes = New-Object System.Collections.Generic.List[int]
    foreach ($part in ($Selection -replace ",", " ").Split(" ", [System.StringSplitOptions]::RemoveEmptyEntries)) {
        if ($part -match "^(\d+)-(\d+)$") {
            $start = [int]$Matches[1]
            $end = [int]$Matches[2]
            if ($start -gt $end) {
                $tmp = $start
                $start = $end
                $end = $tmp
            }
            for ($value = $start; $value -le $end; $value++) {
                if ($value -lt 1 -or $value -gt $Max) { throw "$value is outside 1-$Max" }
                $indexes.Add($value - 1)
            }
        }
        elseif ($part -match "^\d+$") {
            $value = [int]$part
            if ($value -lt 1 -or $value -gt $Max) { throw "$value is outside 1-$Max" }
            $indexes.Add($value - 1)
        }
        else {
            throw "Unrecognized selection '$part'"
        }
    }

    return $indexes | Sort-Object -Unique
}

function Install-WithPowerShellFallback {
    param([string]$RepoRoot)

    $manifest = Get-Content -LiteralPath (Join-Path $RepoRoot "manifest.json") -Raw | ConvertFrom-Json
    $skillsDir = if ($Dest) { $Dest } else { Get-CodexSkillsDirectory }

    Write-Host "Source: $RepoRoot"
    Write-Host "Destination: $skillsDir"
    Show-SkillNames -Skills $manifest.skills

    if ($List) { return }

    if ($All -or $Yes -or -not [Environment]::UserInteractive) {
        $selectedSkills = $manifest.skills
    }
    else {
        Write-Host "Enter numbers or ranges to install, for example: 1 4 8-12"
        Write-Host "Enter A for all, or Q to cancel."
        $selection = Read-Host "Select"
        if ([string]::IsNullOrWhiteSpace($selection) -or $selection -match "^(a|all|\*)$") {
            $selectedSkills = $manifest.skills
        }
        elseif ($selection -match "^(q|quit|cancel)$") {
            Write-Host "Cancelled."
            return
        }
        else {
            $indexes = Convert-Selection -Selection $selection -Max $manifest.skills.Count
            $selectedSkills = @()
            foreach ($index in $indexes) {
                $selectedSkills += $manifest.skills[$index]
            }
        }
    }

    New-Item -ItemType Directory -Path $skillsDir -Force | Out-Null
    Write-Host "Installing $($selectedSkills.Count) selected skill(s)."

    foreach ($skill in $selectedSkills) {
        $sourcePath = Join-Path $RepoRoot $skill.path
        $destPath = Join-Path $skillsDir $skill.name

        if (Test-Path -LiteralPath $destPath) {
            if (-not $Force) {
                Write-Host ("skipped       " + $skill.name)
                continue
            }
            Remove-Item -LiteralPath $destPath -Recurse -Force
        }

        Copy-Item -LiteralPath $sourcePath -Destination $destPath -Recurse
        Write-Host ("installed     " + $skill.name)
    }

    Write-Host "Done. Restart Codex to pick up newly installed skills."
}

$tempRoot = ""

try {
    if ($Source) {
        $repoRoot = (Get-Item -LiteralPath $Source).FullName
    }
    else {
        $tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("codex-skills-pack-" + [System.Guid]::NewGuid().ToString("N"))
        $zipPath = Join-Path $tempRoot "repo.zip"
        New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null

        Write-Host "Downloading $RepoZipUrl"
        Invoke-WebRequest -Uri $RepoZipUrl -OutFile $zipPath
        Expand-Archive -LiteralPath $zipPath -DestinationPath $tempRoot -Force

        $repoDir = Get-ChildItem -LiteralPath $tempRoot -Directory | Where-Object { $_.Name -ne "__MACOSX" } | Select-Object -First 1
        if (-not $repoDir) { throw "Downloaded archive did not contain a repository folder." }
        $repoRoot = $repoDir.FullName
    }

    $python = Get-PythonCommand
    if ($python) {
        $arguments = @((Join-Path $repoRoot "install.py"), "--source", $repoRoot)
        if ($Dest) { $arguments += @("--dest", $Dest) }
        if ($Force) { $arguments += "--force" }
        if ($All) { $arguments += "--all" }
        if ($Yes) { $arguments += "--yes" }
        if ($List) { $arguments += "--list" }
        & $python @arguments
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    }
    else {
        Install-WithPowerShellFallback -RepoRoot $repoRoot
    }
}
finally {
    if ($tempRoot -and (Test-Path -LiteralPath $tempRoot)) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force
    }
}
