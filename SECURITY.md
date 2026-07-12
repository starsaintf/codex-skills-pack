# Security policy

## Supported version

Security fixes are applied to the latest state of the `main` branch. Users should update before reporting a problem that may already be fixed.

## Reporting a vulnerability

Do not open a public issue for vulnerabilities involving the installer, archive extraction, path handling, skill replacement, supply-chain integrity or malicious skill contents.

Use GitHub's private vulnerability reporting feature for this repository. Include:

- the affected file and version or commit;
- reproduction steps;
- expected and observed behaviour;
- impact;
- a suggested fix when available.

Please do not include real credentials, personal data or destructive proof-of-concept payloads.

## Scope

Relevant reports include:

- writing outside the intended skills directory;
- unsafe archive extraction or path traversal;
- silent overwrite or deletion of unrelated files;
- execution of downloaded content beyond the documented installer;
- tampered provenance or licence evidence;
- secrets committed inside a distributed skill.

A skill merely producing a poor answer is not normally a security vulnerability unless it creates an exploitable or materially unsafe behaviour.
