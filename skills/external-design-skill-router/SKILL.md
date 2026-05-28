---
name: external-design-skill-router
description: Use when working on Luna UI, dashboards, chat interfaces, component quality, visual consistency, style extraction, or frontend polish and you need patterns from Refero, UI Skills, or Impeccable without loading the full catalog into context.
---

# External Design Skill Router

## Workflow

1. Identify the UI surface and user workflow being changed.
2. Pick only the relevant source pattern:
   - Refero: style reference mining, visual-language extraction, DESIGN.md translation, consistency audits.
   - UI Skills: concrete component/page patterns such as chat, dashboard, pricing, settings, forms, tables, upload, command palette, and checkout.
   - Impeccable: frontend quality passes, design critique, accessibility, copy, layout, styling, and visual polish workflows.
3. Preserve Luna-specific controls and operational features; compact or relocate controls instead of deleting them.
4. Produce implementation changes with responsive constraints, accessible labels, stable layout dimensions, and no decorative clutter.
5. Verify with code checks and, when a browser is available, visual checks across desktop and mobile.

## Luna Sources

- Source manifest: skills/external_sources/agent_design_memory_sources.json
- Router skill: skills/official/external_design_skill_router/documentation.md
- Catalog domain: external_ui_skills_directory

## Guardrails

- Do not paste entire external catalogs into context.
- Do not copy a reference style blindly; translate it into Luna's product context.
- Do not remove existing Luna dashboard functionality to achieve a cleaner look.
