# Skill Inventory

This repository contains 60 non-system Codex skills. Codex system skills are not included.

1. `agent-browser`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Browser automation CLI for AI agents. Use when the user needs to interact with websites, verify dev server output, test web apps, navigate pages, fill forms, click buttons, take screenshots, extract data, or automate any browser task. Also triggers when a dev server starts so you can verify it visually.

2. `agent-browser-verify`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Automated browser verification for dev servers. Triggers when a dev server starts to run a visual gut-check with agent-browser — verifies the page loads, checks for console errors, validates key UI elements, and reports pass/fail before continuing.

3. `agent-memory-context-efficiency`
   - Source: local-codex-user-skill
   - License: MIT
   - Description: Use when improving Luna memory, context retrieval, token usage, command-output handling, shell summaries, long-running agent traces, or comparing Hermes-style memory and ztk-style token compression patterns.

4. `ai-elements`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: AI Elements component library guidance — pre-built React components for AI interfaces built on shadcn/ui. Use when building chat UIs, message displays, tool call rendering, streaming responses, reasoning panels, or any AI-native interface with the AI SDK.

5. `ai-gateway`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel AI Gateway expert guidance. Use when configuring model routing, provider failover, cost tracking, or managing multiple AI providers through a unified API.

6. `ai-generation-persistence`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: AI generation persistence patterns — unique IDs, addressable URLs, database storage, and cost tracking for every LLM generation

7. `ai-sdk`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel AI SDK expert guidance. Use when building AI-powered features — chat interfaces, text generation, structured output, tool calling, agents, MCP integration, streaming, embeddings, reranking, image generation, or working with any LLM provider.

8. `algorithmic-art`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/algorithmic-art/LICENSE.txt
   - Description: Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.

9. `auth`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Authentication integration guidance — Clerk (native Vercel Marketplace), Descope, and Auth0 setup for Next.js applications. Covers middleware auth patterns, sign-in/sign-up flows, and Marketplace provisioning. Use when implementing user authentication.

10. `bootstrap`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Project bootstrapping orchestrator for repos that depend on Vercel-linked resources (databases, auth, and managed integrations). Use when setting up or repairing a repository so linking, environment provisioning, env pulls, and first-run db/dev commands happen in the correct safe order.

11. `brand-guidelines`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/brand-guidelines/LICENSE.txt
   - Description: Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.

12. `canvas-design`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/canvas-design/LICENSE.txt
   - Description: Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

13. `chat-sdk`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Chat SDK expert guidance. Use when building multi-platform chat bots — Slack, Telegram, Microsoft Teams, Discord, Google Chat, GitHub, Linear — with a single codebase. Covers the Chat class, adapters, threads, messages, cards, modals, streaming, state management, and webhook setup.

14. `claude-api`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/claude-api/LICENSE.txt
   - Description: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

15. `cms`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Headless CMS integration guidance — Sanity (native Vercel Marketplace), Contentful, DatoCMS, Storyblok, and Builder.io. Covers studio setup, content modeling, preview mode, revalidation webhooks, and Visual Editing. Use when building content-driven sites with a headless CMS on Vercel.

16. `cron-jobs`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Cron Jobs configuration and best practices. Use when adding, editing, or debugging scheduled tasks in vercel.json.

17. `deployments-cicd`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel deployment and CI/CD expert guidance. Use when deploying, promoting, rolling back, inspecting deployments, building with --prebuilt, or configuring CI workflow files for Vercel.

18. `email`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Email sending integration guidance — Resend (native Vercel Marketplace) with React Email templates. Covers API setup, transactional emails, domain verification, and template patterns. Use when sending emails from a Vercel-deployed application.

19. `env-vars`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel environment variable expert guidance. Use when working with .env files, vercel env commands, OIDC tokens, or managing environment-specific configuration.

20. `external-design-skill-router`
   - Source: local-codex-user-skill
   - License: MIT
   - Description: Use when working on Luna UI, dashboards, chat interfaces, component quality, visual consistency, style extraction, or frontend polish and you need patterns from Refero, UI Skills, or Impeccable without loading the full catalog into context.

21. `frontend-design`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/frontend-design/LICENSE.txt
   - Description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

22. `geist`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Expert guidance for Geist, Vercel's default typography system and font family for precise Next.js interfaces. Use when configuring Geist Sans, Geist Mono, or Geist Pixel, setting up font imports, or applying Vercel typography and aesthetic guidance.

23. `geistdocs`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Expert guidance for Geistdocs, Vercel's documentation template built with Next.js and Fumadocs — MDX authoring, configuration, AI chat, i18n, feedback, deployment. Use when creating documentation sites, configuring geistdocs, writing MDX content, or setting up docs infrastructure.

24. `internal-comms`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/internal-comms/LICENSE.txt
   - Description: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

25. `investigation-mode`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Orchestrated debugging coordinator. Triggers on frustration signals (stuck, hung, broken, waiting) and systematically triages: runtime logs → workflow status → browser verify → deploy/env. Reports findings at every step.

26. `json-render`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: AI chat response rendering guidance — handling UIMessage parts, tool call displays, streaming states, and structured data presentation. Use when building custom chat UIs, rendering tool results, or troubleshooting AI response display issues.

27. `marketplace`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Marketplace expert guidance — discovering, installing, and building integrations, auto-provisioned environment variables, unified billing, and the vercel integration CLI. Use when consuming third-party services, building custom integrations, or managing marketplace resources on Vercel.

28. `mcp-builder`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/mcp-builder/LICENSE.txt
   - Description: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

29. `micro`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Expert guidance for micro — asynchronous HTTP microservices framework by Vercel. Use when building lightweight HTTP servers, API endpoints, or microservices using the micro library.

30. `ncc`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Expert guidance for @vercel/ncc — a simple CLI for compiling Node.js modules into a single file with all dependencies included. Use when bundling serverless functions, CLI tools, or any Node.js project into a self-contained file.

31. `next-forge`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: next-forge expert guidance — production-grade Turborepo monorepo SaaS starter by Vercel. Use when working in a next-forge project, scaffolding with `npx next-forge init`, or editing @repo/* workspace packages.

32. `nextjs`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Next.js App Router expert guidance. Use when building, debugging, or architecting Next.js applications — routing, Server Components, Server Actions, Cache Components, layouts, middleware/proxy, data fetching, rendering strategies, and deployment on Vercel.

33. `observability`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Observability expert guidance — Drains (logs, traces, speed insights, web analytics), Web Analytics, Speed Insights, runtime logs, custom events, OpenTelemetry integration, and monitoring dashboards. Use when instrumenting, debugging, or optimizing application performance and user experience on Vercel.

34. `payments`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Stripe payments integration guidance — native Vercel Marketplace setup, checkout sessions, webhook handling, subscription billing, and the Stripe SDK. Use when implementing payments, subscriptions, or processing transactions.

35. `react-best-practices`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: React best-practices reviewer for TSX files. Triggers after editing multiple TSX components to run a condensed quality checklist covering component structure, hooks usage, accessibility, performance, and TypeScript patterns.

36. `routing-middleware`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Routing Middleware guidance — request interception before cache, rewrites, redirects, personalization. Works with any framework. Supports Edge, Node.js, and Bun runtimes. Use when intercepting requests at the platform level.

37. `runtime-cache`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Runtime Cache API guidance — ephemeral per-region key-value cache with tag-based invalidation. Shared across Functions, Routing Middleware, and Builds. Use when implementing caching strategies beyond framework-level caching.

38. `satori`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Expert guidance for Satori — Vercel's library that converts HTML and CSS to SVG, commonly used to generate dynamic OG images for Next.js and other frameworks.

39. `shadcn`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: shadcn/ui expert guidance — CLI, component installation, composition patterns, custom registries, theming, Tailwind CSS integration, and high-quality interface design. Use when initializing shadcn, adding components, composing product UI, building custom registries, configuring themes, or troubleshooting component issues.

40. `sign-in-with-vercel`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Sign in with Vercel guidance — OAuth 2.0/OIDC identity provider for user authentication via Vercel accounts. Use when implementing user login with Vercel as the identity provider.

41. `slack-gif-creator`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/slack-gif-creator/LICENSE.txt
   - Description: Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack.

42. `swr`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: SWR data-fetching expert guidance. Use when building React apps with client-side data fetching, caching, revalidation, mutations, optimistic UI, pagination, or infinite loading using the SWR library.

43. `theme-factory`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/theme-factory/LICENSE.txt
   - Description: Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.

44. `turbopack`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Turbopack expert guidance. Use when configuring the Next.js bundler, optimizing HMR, debugging build issues, or understanding the Turbopack vs Webpack differences.

45. `turborepo`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Turborepo expert guidance. Use when setting up or optimizing monorepo builds, configuring task caching, remote caching, parallel execution, or the --affected flag for incremental CI.

46. `v0-dev`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: v0 by Vercel expert guidance. Use when discussing AI code generation, generating UI components from prompts, v0 CLI usage, v0 SDK/API integration, or integrating v0 into development workflows with GitHub and Vercel deployment.

47. `vercel-agent`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Agent guidance — AI-powered code review, incident investigation, and SDK installation. Automates PR analysis and anomaly debugging. Use when configuring or understanding Vercel's AI development tools.

48. `vercel-api`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel app and REST API expert guidance. Use when the agent needs live access to Vercel projects, deployments, environment variables, domains, logs, or documentation through the connected Vercel app or REST API.

49. `vercel-cli`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel CLI expert guidance. Use when deploying, managing environment variables, linking projects, viewing logs, managing domains, or interacting with the Vercel platform from the command line.

50. `vercel-firewall`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Firewall and security expert guidance. Use when configuring DDoS protection, WAF rules, rate limiting, bot filtering, IP allow/block lists, OWASP rulesets, Attack Challenge Mode, or any security configuration on the Vercel platform.

51. `vercel-flags`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Flags guidance — feature flags platform with unified dashboard, Flags Explorer, gradual rollouts, A/B testing, and provider adapters. Use when implementing feature flags, experimentation, or staged rollouts.

52. `vercel-functions`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Functions expert guidance — Serverless Functions, Edge Functions, Fluid Compute, streaming, Cron Jobs, and runtime configuration. Use when configuring, debugging, or optimizing server-side code running on Vercel.

53. `vercel-queues`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Queues guidance (public beta) — durable event streaming with topics, consumer groups, retries, and delayed delivery. $0.60/1M ops. Powers Workflow DevKit. Use when building async processing, fan-out patterns, or event-driven architectures.

54. `vercel-sandbox`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Sandbox guidance — ephemeral Firecracker microVMs for running untrusted code safely. Supports AI agents, code generation, and experimentation. Use when executing user-generated or AI-generated code in isolation.

55. `vercel-services`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Services — deploy multiple services within a single Vercel project. Use for monorepo layouts or when combining a backend (Python, Go) with a frontend (Next.js, Vite) in one deployment.

56. `vercel-storage`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel storage expert guidance — Blob, Edge Config, and Marketplace storage (Neon Postgres, Upstash Redis). Use when choosing, configuring, or using data storage with Vercel applications.

57. `verification`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Full-story verification — infers what the user is building, then verifies the complete flow end-to-end: browser → API → data → response. Triggers on dev server start and 'why isn't this working' signals.

58. `web-artifacts-builder`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/web-artifacts-builder/LICENSE.txt
   - Description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

59. `webapp-testing`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/webapp-testing/LICENSE.txt
   - Description: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

60. `workflow`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Workflow DevKit (WDK) expert guidance. Use when building durable workflows, long-running tasks, API routes or agents that need pause/resume, retries, step-based execution, or crash-safe orchestration with Vercel Workflow.
