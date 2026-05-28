---
name: agent-memory-context-efficiency
description: Use when improving Luna memory, context retrieval, token usage, command-output handling, shell summaries, long-running agent traces, or comparing Hermes-style memory and ztk-style token compression patterns.
---

# Agent Memory Context Efficiency

## Workflow

1. Separate memory into hot context, searchable session recall, durable facts, and skillized workflows.
2. Keep hot memory bounded; retrieve cold memories only when they score relevant to the current task.
3. Prefer deterministic compression for command output:
   - Preserve exit code, failing lines, stack traces, changed files, and next actions.
   - Summarize repeated success logs and unchanged sections.
   - Keep raw output addressable through evidence records when possible.
4. Promote repeated successful workflows into Luna or Codex skills only after validation.
5. Record evidence, score the change, and preserve rollback snapshots for memory, prompt, tool, or skill changes.

## Luna Sources

- Source manifest: skills/external_sources/agent_design_memory_sources.json
- Router skill: skills/official/agent_memory_context_efficiency_router/documentation.md
- Runtime engines: src/luna/hermes_memory.py and src/luna/ztk_context.py

## Decision Rule

Use Hermes-like bounded and searchable memory for recall policy. Use ztk-like output compression for shell/tool transcript control. Keep Luna's Evidence Vault and versioned self-evolution layer as the promotion and audit authority.
