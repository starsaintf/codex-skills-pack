# Skill Inventory

This repository contains 120 non-system Codex skills. Codex system skills are not included.

1. `actionable-pushback`
   - Source: local-codex-user-skill
   - License: MIT
   - Description: Use when the user may be mistaken, the requested action is risky, evidence is weak or contradictory, requirements conflict, assumptions may be wrong, constraints are hidden, or Codex should respectfully disagree before acting.

2. `agent-browser`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Browser automation CLI for AI agents. Use when the user needs to interact with websites, verify dev server output, test web apps, navigate pages, fill forms, click buttons, take screenshots, extract data, or automate any browser task. Also triggers when a dev server starts so you can verify it visually.

3. `agent-browser-verify`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Automated browser verification for dev servers. Triggers when a dev server starts to run a visual gut-check with agent-browser — verifies the page loads, checks for console errors, validates key UI elements, and reports pass/fail before continuing.

4. `agent-memory-context-efficiency`
   - Source: local-codex-user-skill
   - License: MIT
   - Description: Use when improving Luna memory, context retrieval, token usage, command-output handling, shell summaries, long-running agent traces, or comparing Hermes-style memory and ztk-style token compression patterns.

5. `ai-elements`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: AI Elements component library guidance — pre-built React components for AI interfaces built on shadcn/ui. Use when building chat UIs, message displays, tool call rendering, streaming responses, reasoning panels, or any AI-native interface with the AI SDK.

6. `ai-gateway`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel AI Gateway expert guidance. Use when configuring model routing, provider failover, cost tracking, or managing multiple AI providers through a unified API.

7. `ai-generation-persistence`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: AI generation persistence patterns — unique IDs, addressable URLs, database storage, and cost tracking for every LLM generation

8. `ai-sdk`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel AI SDK expert guidance. Use when building AI-powered features — chat interfaces, text generation, structured output, tool calling, agents, MCP integration, streaming, embeddings, reranking, image generation, or working with any LLM provider.

9. `algorithmic-art`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/algorithmic-art/LICENSE.txt
   - Description: Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.

10. `android-emulator-qa`
   - Source: test-android-apps plugin backup promoted from temp
   - License: MIT, from test-android-apps plugin metadata
   - Description: Use when validating Android feature flows in an emulator with adb-driven launch, input, UI-tree inspection, screenshots, and logcat capture.

11. `android-performance`
   - Source: test-android-apps plugin backup promoted from temp
   - License: MIT, from test-android-apps plugin metadata
   - Description: Gather and interpret Android performance evidence on an adb target using Simpleperf CPU profiles, Perfetto or Compose traces, gfxinfo frame data, dumpsys meminfo snapshots, Java heap dumps, and native allocation traces. Use when asked to profile an Android app flow, find CPU-heavy functions, diagnose jank, capture startup or frame timing evidence, compare before/after performance, explain what code is taking time, or gather memory/leak profiling artifacts.

12. `auth`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Authentication integration guidance — Clerk (native Vercel Marketplace), Descope, and Auth0 setup for Next.js applications. Covers middleware auth patterns, sign-in/sign-up flows, and Marketplace provisioning. Use when implementing user authentication.

13. `bootstrap`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Project bootstrapping orchestrator for repos that depend on Vercel-linked resources (databases, auth, and managed integrations). Use when setting up or repairing a repository so linking, environment provisioning, env pulls, and first-run db/dev commands happen in the correct safe order.

14. `brainstorming`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation.

15. `brand-guidelines`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/brand-guidelines/LICENSE.txt
   - Description: Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.

16. `building-native-ui`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: Complete guide for building beautiful apps with Expo Router. Covers fundamentals, styling, components, navigation, animations, patterns, and native tabs.

17. `canvas-design`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/canvas-design/LICENSE.txt
   - Description: Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

18. `chat-sdk`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Chat SDK expert guidance. Use when building multi-platform chat bots — Slack, Telegram, Microsoft Teams, Discord, Google Chat, GitHub, Linear — with a single codebase. Covers the Chat class, adapters, threads, messages, cards, modals, streaming, state management, and webhook setup.

19. `claude-api`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/claude-api/LICENSE.txt
   - Description: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

20. `cms`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Headless CMS integration guidance — Sanity (native Vercel Marketplace), Contentful, DatoCMS, Storyblok, and Builder.io. Covers studio setup, content modeling, preview mode, revalidation webhooks, and Visual Editing. Use when building content-driven sites with a headless CMS on Vercel.

21. `codex-expo-run-actions`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: Wire Expo projects into the Codex app with project-local run scripts and .codex/environments/environment.toml actions. Use when the user wants the Codex app Run button, build/run actions, action buttons, or a stable Expo start/run workflow from Codex.

22. `cron-jobs`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Cron Jobs configuration and best practices. Use when adding, editing, or debugging scheduled tasks in vercel.json.

23. `deployments-cicd`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel deployment and CI/CD expert guidance. Use when deploying, promoting, rolling back, inspecting deployments, building with --prebuilt, or configuring CI workflow files for Vercel.

24. `dispatching-parallel-agents`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies

25. `email`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Email sending integration guidance — Resend (native Vercel Marketplace) with React Email templates. Covers API setup, transactional emails, domain verification, and template patterns. Use when sending emails from a Vercel-deployed application.

26. `env-vars`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel environment variable expert guidance. Use when working with .env files, vercel env commands, OIDC tokens, or managing environment-specific configuration.

27. `executing-plans`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when you have a written implementation plan to execute in a separate session with review checkpoints

28. `expo-api-routes`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: Guidelines for creating API routes in Expo Router with EAS Hosting

29. `expo-cicd-workflows`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: Helps understand and write EAS workflow YAML files for Expo projects. Use this skill when the user asks about CI/CD or workflows in an Expo or EAS context, mentions .eas/workflows/, or wants help with EAS build pipelines or deployment automation.

30. `expo-deployment`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: Deploying Expo apps to iOS App Store, Android Play Store, web hosting, and API routes

31. `expo-dev-client`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: Build and distribute Expo development clients locally or via TestFlight

32. `expo-module`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: Guide for writing Expo native modules and views using the Expo Modules API (Swift, Kotlin, TypeScript). Covers module definition DSL, native views, shared objects, config plugins, lifecycle hooks, autolinking, and type system. Use when building or modifying native modules for Expo.

33. `expo-tailwind-setup`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: Set up Tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for universal styling

34. `expo-ui-jetpack-compose`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: `@expo/ui/jetpack-compose` package lets you use Jetpack Compose Views and modifiers in your app.

35. `expo-ui-swift-ui`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: `@expo/ui/swift-ui` package lets you use SwiftUI Views and modifiers in your app.

36. `external-design-skill-router`
   - Source: local-codex-user-skill
   - License: MIT
   - Description: Use when working on Luna UI, dashboards, chat interfaces, component quality, visual consistency, style extraction, or frontend polish and you need patterns from Refero, UI Skills, or Impeccable without loading the full catalog into context.

37. `finishing-a-development-branch`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup

38. `frontend-design`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/frontend-design/LICENSE.txt
   - Description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

39. `geist`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Expert guidance for Geist, Vercel's default typography system and font family for precise Next.js interfaces. Use when configuring Geist Sans, Geist Mono, or Geist Pixel, setting up font imports, or applying Vercel typography and aesthetic guidance.

40. `geistdocs`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Expert guidance for Geistdocs, Vercel's documentation template built with Next.js and Fumadocs — MDX authoring, configuration, AI chat, i18n, feedback, deployment. Use when creating documentation sites, configuring geistdocs, writing MDX content, or setting up docs infrastructure.

41. `gh-address-comments`
   - Source: github plugin backup promoted from temp
   - License: MIT, from github plugin metadata
   - Description: Address actionable GitHub pull request review feedback. Use when the user wants to inspect unresolved review threads, requested changes, or inline review comments on a PR, then implement selected fixes. Use the GitHub app for PR metadata and flat comment reads, and use the bundled GraphQL script via `gh` whenever thread-level state, resolution status, or inline review context matters.

42. `gh-fix-ci`
   - Source: github plugin backup promoted from temp
   - License: MIT, from github plugin metadata
   - Description: Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions. Use the GitHub app from this plugin for PR metadata and patch context, and use `gh` for Actions check and log inspection before implementing any approved fix.

43. `github`
   - Source: github plugin backup promoted from temp
   - License: MIT, from github plugin metadata
   - Description: Triage and orient GitHub repository, pull request, and issue work through the connected GitHub app. Use when the user asks for general GitHub help, wants PR or issue summaries, or needs repository context before choosing a more specific GitHub workflow.

44. `internal-comms`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/internal-comms/LICENSE.txt
   - Description: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

45. `investigation-mode`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Orchestrated debugging coordinator. Triggers on frustration signals (stuck, hung, broken, waiting) and systematically triages: runtime logs → workflow status → browser verify → deploy/env. Reports findings at every step.

46. `json-render`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: AI chat response rendering guidance — handling UIMessage parts, tool call displays, streaming states, and structured data presentation. Use when building custom chat UIs, rendering tool results, or troubleshooting AI response display issues.

47. `marketplace`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Marketplace expert guidance — discovering, installing, and building integrations, auto-provisioned environment variables, unified billing, and the vercel integration CLI. Use when consuming third-party services, building custom integrations, or managing marketplace resources on Vercel.

48. `mcp-builder`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/mcp-builder/LICENSE.txt
   - Description: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

49. `micro`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Expert guidance for micro — asynchronous HTTP microservices framework by Vercel. Use when building lightweight HTTP servers, API endpoints, or microservices using the micro library.

50. `native-data-fetching`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: Use when implementing or debugging ANY network request, API call, or data fetching. Covers fetch API, React Query, SWR, error handling, caching, offline support, and Expo Router data loaders (`useLoaderData`).

51. `ncc`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Expert guidance for @vercel/ncc — a simple CLI for compiling Node.js modules into a single file with all dependencies included. Use when bundling serverless functions, CLI tools, or any Node.js project into a self-contained file.

52. `netlify-ai-gateway`
   - Source: netlify plugin backup promoted from temp
   - License: MIT, from netlify plugin metadata
   - Description: Guide for using Netlify AI Gateway to access AI models. Use when adding AI capabilities or selecting/changing AI models. Must be read before choosing a model. Covers supported providers (OpenAI, Anthropic, Google), SDK setup, environment variables, and the list of available models.

53. `netlify-blobs`
   - Source: netlify plugin backup promoted from temp
   - License: MIT, from netlify plugin metadata
   - Description: Guide for using Netlify Blobs object storage. Use when storing files, images, documents, or simple key-value data without a full database. Covers getStore(), CRUD operations, metadata, listing, deploy-scoped vs site-scoped stores, and local development.

54. `netlify-caching`
   - Source: netlify plugin backup promoted from temp
   - License: MIT, from netlify plugin metadata
   - Description: Guide for controlling caching on Netlify's CDN. Use when configuring cache headers, setting up stale-while-revalidate, implementing on-demand cache purge, or understanding Netlify's CDN caching behavior. Covers Cache-Control, Netlify-CDN-Cache-Control, cache tags, durable cache, and framework-specific caching patterns.

55. `netlify-cli-and-deploy`
   - Source: netlify plugin backup promoted from temp
   - License: MIT, from netlify plugin metadata
   - Description: Guide for using the Netlify CLI and deploying sites. Use when installing the CLI, linking sites, deploying (Git-based or manual), managing environment variables, or running local development. Covers netlify dev, netlify deploy, Git vs non-Git workflows, and environment variable management.

56. `netlify-config`
   - Source: netlify plugin backup promoted from temp
   - License: MIT, from netlify plugin metadata
   - Description: Reference for netlify.toml configuration. Use when configuring build settings, redirects, rewrites, headers, deploy contexts, environment variables, or any site-level configuration. Covers the complete netlify.toml syntax including redirects with splats/conditions, headers, deploy contexts, functions config, and edge functions config.

57. `netlify-deploy`
   - Source: netlify plugin backup promoted from temp
   - License: MIT, from netlify plugin metadata
   - Description: Deploy projects to Netlify with the Netlify CLI. Use when the user wants to link a repo, validate deploy settings, run a deploy, or choose between preview and production flows.

58. `netlify-edge-functions`
   - Source: netlify plugin backup promoted from temp
   - License: MIT, from netlify plugin metadata
   - Description: Guide for writing Netlify Edge Functions. Use when building middleware, geolocation-based logic, request/response manipulation, authentication checks, A/B testing, or any low-latency edge compute. Covers Deno runtime, context.next() middleware pattern, geolocation, and when to choose edge vs serverless.

59. `netlify-forms`
   - Source: netlify plugin backup promoted from temp
   - License: MIT, from netlify plugin metadata
   - Description: Guide for using Netlify Forms for HTML form handling. Use when adding contact forms, feedback forms, file upload forms, or any form that should be collected by Netlify. Covers the data-netlify attribute, spam filtering, AJAX submissions, file uploads, notifications, and the submissions API.

60. `netlify-frameworks`
   - Source: netlify plugin backup promoted from temp
   - License: MIT, from netlify plugin metadata
   - Description: Guide for deploying web frameworks on Netlify. Use when setting up a framework project (Vite/React, Astro, TanStack Start, Next.js, Nuxt, SvelteKit, Remix) for Netlify deployment, configuring adapters or plugins, or troubleshooting framework-specific Netlify integration. Covers what Netlify needs from each framework and how adapters handle server-side rendering.

61. `netlify-functions`
   - Source: netlify plugin backup promoted from temp
   - License: MIT, from netlify plugin metadata
   - Description: Guide for writing Netlify serverless functions. Use when creating API endpoints, background processing, scheduled tasks, or any server-side logic using Netlify Functions. Covers modern syntax (default export + Config), TypeScript, path routing, background functions, scheduled functions, streaming, and method routing.

62. `netlify-identity`
   - Source: netlify plugin backup promoted from temp
   - License: MIT, from netlify plugin metadata
   - Description: Use when the task involves authentication, user signups, logins, password recovery, OAuth providers, role-based access control, or protecting routes and functions. Always use `@netlify/identity`. Never use `netlify-identity-widget` or `gotrue-js` — they are deprecated.

63. `netlify-image-cdn`
   - Source: netlify plugin backup promoted from temp
   - License: MIT, from netlify plugin metadata
   - Description: Guide for using Netlify Image CDN for image optimization and transformation. Use when serving optimized images, creating responsive image markup, setting up user-uploaded image pipelines, or configuring image transformations. Covers the /.netlify/images endpoint, query parameters, remote image allowlisting, clean URL rewrites, and composing uploads with Functions + Blobs.

64. `next-forge`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: next-forge expert guidance — production-grade Turborepo monorepo SaaS starter by Vercel. Use when working in a next-forge project, scaffolding with `npx next-forge init`, or editing @repo/* workspace packages.

65. `nextjs`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Next.js App Router expert guidance. Use when building, debugging, or architecting Next.js applications — routing, Server Components, Server Actions, Cache Components, layouts, middleware/proxy, data fetching, rendering strategies, and deployment on Vercel.

66. `notion-knowledge-capture`
   - Source: notion plugin backup promoted from temp
   - License: MIT, from notion plugin metadata
   - Description: Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking.

67. `notion-meeting-intelligence`
   - Source: notion plugin backup promoted from temp
   - License: MIT, from notion plugin metadata
   - Description: Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.

68. `notion-research-documentation`
   - Source: notion plugin backup promoted from temp
   - License: MIT, from notion plugin metadata
   - Description: Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.

69. `notion-spec-to-implementation`
   - Source: notion plugin backup promoted from temp
   - License: MIT, from notion plugin metadata
   - Description: Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them.

70. `observability`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Observability expert guidance — Drains (logs, traces, speed insights, web analytics), Web Analytics, Speed Insights, runtime logs, custom events, OpenTelemetry integration, and monitoring dashboards. Use when instrumenting, debugging, or optimizing application performance and user experience on Vercel.

71. `payments`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Stripe payments integration guidance — native Vercel Marketplace setup, checkout sessions, webhook handling, subscription billing, and the Stripe SDK. Use when implementing payments, subscriptions, or processing transactions.

72. `react-best-practices`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: React best-practices reviewer for TSX files. Triggers after editing multiple TSX components to run a condensed quality checklist covering component structure, hooks usage, accessibility, performance, and TypeScript patterns.

73. `receiving-code-review`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation

74. `render-debug`
   - Source: render plugin backup promoted from temp
   - License: MIT, from render plugin metadata
   - Description: Debug failed Render deployments by analyzing logs, metrics, and database state. Identifies errors (missing env vars, port binding, OOM, etc.) and suggests fixes. Use when deployments fail, services won't start, or users mention errors, logs, or debugging.

75. `render-deploy`
   - Source: render plugin backup promoted from temp
   - License: MIT, from render plugin metadata
   - Description: Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. Use when the user wants to deploy, host, publish, or set up their application on Render's cloud platform.

76. `render-migrate-from-heroku`
   - Source: render plugin backup promoted from temp
   - License: MIT, from render plugin metadata
   - Description: Migrate from Heroku to Render by reading local project files and generating equivalent Render services. Triggers: any mention of migrating from Heroku, moving off Heroku, Heroku to Render migration, or switching from Heroku. Reads Procfile, dependency files, and app config from the local repo. Optionally uses Heroku MCP to enrich with live config vars, add-on details, and dyno sizes. Uses Render MCP or Blueprint YAML to create services.

77. `render-monitor`
   - Source: render plugin backup promoted from temp
   - License: MIT, from render plugin metadata
   - Description: Monitor Render services in real-time. Check health, performance metrics, logs, and resource usage. Use when users want to check service status, view metrics, monitor performance, or verify deployments are healthy.

78. `render-workflows`
   - Source: render plugin backup promoted from temp
   - License: MIT, from render plugin metadata
   - Description: Sets up, develops, tests, and deploys Render Workflows. Covers first-time scaffolding (via CLI or manual), SDK installation (Python or TypeScript), task patterns (retries, subtasks, fan-out), local development, Dashboard deployment, and troubleshooting. Use when a user wants to set up Render Workflows for the first time, scaffold a workflow service, add or modify workflow tasks, test workflows locally, or deploy workflows to Render.

79. `requesting-code-review`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when completing tasks, implementing major features, or before merging to verify work meets requirements

80. `routing-middleware`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Routing Middleware guidance — request interception before cache, rewrites, redirects, personalization. Works with any framework. Supports Edge, Node.js, and Bun runtimes. Use when intercepting requests at the platform level.

81. `runtime-cache`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Runtime Cache API guidance — ephemeral per-region key-value cache with tag-based invalidation. Shared across Functions, Routing Middleware, and Builds. Use when implementing caching strategies beyond framework-level caching.

82. `satori`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Expert guidance for Satori — Vercel's library that converts HTML and CSS to SVG, commonly used to generate dynamic OG images for Next.js and other frameworks.

83. `sentry`
   - Source: sentry plugin backup promoted from temp
   - License: MIT, from sentry plugin metadata
   - Description: Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry API; perform read-only queries with the bundled script and require `SENTRY_AUTH_TOKEN`.

84. `shadcn`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: shadcn/ui expert guidance — CLI, component installation, composition patterns, custom registries, theming, Tailwind CSS integration, and high-quality interface design. Use when initializing shadcn, adding components, composing product UI, building custom registries, configuring themes, or troubleshooting component issues.

85. `sign-in-with-vercel`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Sign in with Vercel guidance — OAuth 2.0/OIDC identity provider for user authentication via Vercel accounts. Use when implementing user login with Vercel as the identity provider.

86. `slack-gif-creator`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/slack-gif-creator/LICENSE.txt
   - Description: Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack.

87. `stripe-best-practices`
   - Source: stripe plugin backup promoted from temp
   - License: MIT, from stripe plugin metadata
   - Description: Guides Stripe integration decisions — API selection (Checkout Sessions vs PaymentIntents), Connect platform setup (Accounts v2, controller properties), billing/subscriptions, Treasury financial accounts, integration surfaces (Checkout, Payment Element), and migrating from deprecated Stripe APIs. Use when building, modifying, or reviewing any Stripe integration — including accepting payments, building marketplaces, integrating Stripe, processing payments, setting up subscriptions, or creating connected accounts.

88. `subagent-driven-development`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when executing implementation plans with independent tasks in the current session

89. `supabase`
   - Source: supabase plugin backup promoted from temp
   - License: MIT, from supabase plugin metadata
   - Description: Use when doing ANY task involving Supabase. Triggers: Supabase products (Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues); client libraries and SSR integrations (supabase-js, @supabase/ssr) in Next.js, React, SvelteKit, Astro, Remix; auth issues (login, logout, sessions, JWT, cookies, getSession, getUser, getClaims, RLS); Supabase CLI or MCP server; schema changes, migrations, security audits, Postgres extensions (pg_graphql, pg_cron, pg_vector).

90. `supabase-postgres-best-practices`
   - Source: supabase plugin backup promoted from temp
   - License: MIT, from supabase plugin metadata
   - Description: Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, or database configurations.

91. `swr`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: SWR data-fetching expert guidance. Use when building React apps with client-side data fetching, caching, revalidation, mutations, optimistic UI, pagination, or infinite loading using the SWR library.

92. `systematic-debugging`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes

93. `test-driven-development`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when implementing any feature or bugfix, before writing implementation code

94. `theme-factory`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/theme-factory/LICENSE.txt
   - Description: Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.

95. `turbopack`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Turbopack expert guidance. Use when configuring the Next.js bundler, optimizing HMR, debugging build issues, or understanding the Turbopack vs Webpack differences.

96. `turborepo`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Turborepo expert guidance. Use when setting up or optimizing monorepo builds, configuring task caching, remote caching, parallel execution, or the --affected flag for incremental CI.

97. `upgrade-stripe`
   - Source: stripe plugin backup promoted from temp
   - License: MIT, from stripe plugin metadata
   - Description: Guide for upgrading Stripe API versions and SDKs

98. `upgrading-expo`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: Guidelines for upgrading Expo SDK versions and fixing dependency issues

99. `use-dom`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Description: Use Expo DOM components to run web code in a webview on native and as-is on web. Migrate web code to native incrementally.

100. `using-git-worktrees`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback

101. `using-superpowers`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions

102. `v0-dev`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: v0 by Vercel expert guidance. Use when discussing AI code generation, generating UI components from prompts, v0 CLI usage, v0 SDK/API integration, or integrating v0 into development workflows with GitHub and Vercel deployment.

103. `vercel-agent`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Agent guidance — AI-powered code review, incident investigation, and SDK installation. Automates PR analysis and anomaly debugging. Use when configuring or understanding Vercel's AI development tools.

104. `vercel-api`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel app and REST API expert guidance. Use when the agent needs live access to Vercel projects, deployments, environment variables, domains, logs, or documentation through the connected Vercel app or REST API.

105. `vercel-cli`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel CLI expert guidance. Use when deploying, managing environment variables, linking projects, viewing logs, managing domains, or interacting with the Vercel platform from the command line.

106. `vercel-firewall`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Firewall and security expert guidance. Use when configuring DDoS protection, WAF rules, rate limiting, bot filtering, IP allow/block lists, OWASP rulesets, Attack Challenge Mode, or any security configuration on the Vercel platform.

107. `vercel-flags`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Flags guidance — feature flags platform with unified dashboard, Flags Explorer, gradual rollouts, A/B testing, and provider adapters. Use when implementing feature flags, experimentation, or staged rollouts.

108. `vercel-functions`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Functions expert guidance — Serverless Functions, Edge Functions, Fluid Compute, streaming, Cron Jobs, and runtime configuration. Use when configuring, debugging, or optimizing server-side code running on Vercel.

109. `vercel-queues`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Queues guidance (public beta) — durable event streaming with topics, consumer groups, retries, and delayed delivery. $0.60/1M ops. Powers Workflow DevKit. Use when building async processing, fan-out patterns, or event-driven architectures.

110. `vercel-sandbox`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Sandbox guidance — ephemeral Firecracker microVMs for running untrusted code safely. Supports AI agents, code generation, and experimentation. Use when executing user-generated or AI-generated code in isolation.

111. `vercel-services`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Services — deploy multiple services within a single Vercel project. Use for monorepo layouts or when combining a backend (Python, Go) with a frontend (Next.js, Vite) in one deployment.

112. `vercel-storage`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel storage expert guidance — Blob, Edge Config, and Marketplace storage (Neon Postgres, Upstash Redis). Use when choosing, configuring, or using data storage with Vercel applications.

113. `verification`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Full-story verification — infers what the user is building, then verifies the complete flow end-to-end: browser → API → data → response. Triggers on dev server start and 'why isn't this working' signals.

114. `verification-before-completion`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always

115. `web-artifacts-builder`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/web-artifacts-builder/LICENSE.txt
   - Description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

116. `webapp-testing`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/webapp-testing/LICENSE.txt
   - Description: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

117. `workflow`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, from vercel/vercel-plugin metadata
   - Description: Vercel Workflow DevKit (WDK) expert guidance. Use when building durable workflows, long-running tasks, API routes or agents that need pause/resume, retries, step-based execution, or crash-safe orchestration with Vercel Workflow.

118. `writing-plans`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when you have a spec or requirements for a multi-step task, before touching code

119. `writing-skills`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Description: Use when creating new skills, editing existing skills, or verifying skills work before deployment

120. `yeet`
   - Source: github plugin backup promoted from temp
   - License: MIT, from github plugin metadata
   - Description: Publish local changes to GitHub by confirming scope, committing intentionally, pushing the branch, and opening a draft PR through the GitHub app from this plugin, with `gh` used only as a fallback where connector coverage is insufficient.
