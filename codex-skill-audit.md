# Codex Skill Audit

Codex home: `C:\Users\Lambert\.codex`
System skills included: `False`

## Summary

- Total `SKILL.md` files audited: 902
- Unique named skills: 402
- Likely concrete installable skills: 171
- Non-installable/cache/vendor/session artifacts: 731
- Duplicate skill names: 327
- Missing frontmatter: 0
- Missing `name`: 0
- Missing `description`: 0

## Counts By Kind

- `plugin-skill`: 51
- `temp`: 696
- `user-installed-skill`: 120
- `vendor-import`: 35

## Likely Concrete Installable Skills

1. `actionable-pushback`
   - Kind: `user-installed-skill`
   - Path: `skills/actionable-pushback`
   - License file: `False`
   - Description: Use when the user may be mistaken, the requested action is risky, evidence is weak or contradictory, requirements conflict, ass...

2. `agent-browser`
   - Kind: `user-installed-skill`
   - Path: `skills/agent-browser`
   - License file: `False`
   - Description: Use when the user needs to interact with websites, verify dev server output, test web apps, navigate pages, fill forms, click b...

3. `agent-browser-verify`
   - Kind: `user-installed-skill`
   - Path: `skills/agent-browser-verify`
   - License file: `False`
   - Description: Use when a dev server needs browser verification, screenshots, console checks, or visual regression checks after frontend changes.

4. `agent-memory-context-efficiency`
   - Kind: `user-installed-skill`
   - Path: `skills/agent-memory-context-efficiency`
   - License file: `False`
   - Description: Use when improving Luna memory, context retrieval, token usage, command-output handling, shell summaries, long-running agent tr...

5. `ai-elements`
   - Kind: `user-installed-skill`
   - Path: `skills/ai-elements`
   - License file: `False`
   - Description: Use when building chat UIs, message displays, tool call rendering, streaming responses, reasoning panels, or any AI-native inte...

6. `ai-gateway`
   - Kind: `user-installed-skill`
   - Path: `skills/ai-gateway`
   - License file: `False`
   - Description: Use when configuring model routing, provider failover, cost tracking, or managing multiple AI providers through a unified API.

7. `ai-generation-persistence`
   - Kind: `user-installed-skill`
   - Path: `skills/ai-generation-persistence`
   - License file: `False`
   - Description: Use when AI generations need stable IDs, addressable URLs, database persistence, resumability, or cost tracking.

8. `ai-sdk`
   - Kind: `user-installed-skill`
   - Path: `skills/ai-sdk`
   - License file: `False`
   - Description: Use when building AI-powered features — chat interfaces, text generation, structured output, tool calling, agents, MCP integrat...

9. `algorithmic-art`
   - Kind: `user-installed-skill`
   - Path: `skills/algorithmic-art`
   - License file: `True`
   - Description: Use when creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users...

10. `android-emulator-qa`
   - Kind: `user-installed-skill`
   - Path: `skills/android-emulator-qa`
   - License file: `True`
   - Description: Use when validating Android feature flows in an emulator with adb-driven launch, input, UI-tree inspection, screenshots, and lo...

11. `android-performance`
   - Kind: `user-installed-skill`
   - Path: `skills/android-performance`
   - License file: `False`
   - Description: Use when asked to profile an Android app flow, find CPU-heavy functions, diagnose jank, capture startup or frame timing evidenc...

12. `auth`
   - Kind: `user-installed-skill`
   - Path: `skills/auth`
   - License file: `False`
   - Description: Use when implementing user authentication.

13. `bootstrap`
   - Kind: `user-installed-skill`
   - Path: `skills/bootstrap`
   - License file: `False`
   - Description: Use when setting up or repairing a repository so linking, environment provisioning, env pulls, and first-run db/dev commands ha...

14. `brainstorming`
   - Kind: `user-installed-skill`
   - Path: `skills/brainstorming`
   - License file: `False`
   - Description: Use when starting creative or product work such as new features, components, functionality, designs, or behavior changes.

15. `brand-guidelines`
   - Kind: `user-installed-skill`
   - Path: `skills/brand-guidelines`
   - License file: `True`
   - Description: Use when applying anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthrop...

16. `building-native-ui`
   - Kind: `user-installed-skill`
   - Path: `skills/building-native-ui`
   - License file: `False`
   - Description: Use when building polished native app interfaces with Expo Router, React Native styling, navigation, animations, or platform UI...

17. `canvas-design`
   - Kind: `user-installed-skill`
   - Path: `skills/canvas-design`
   - License file: `True`
   - Description: Use when creating beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the u...

18. `chat-sdk`
   - Kind: `user-installed-skill`
   - Path: `skills/chat-sdk`
   - License file: `False`
   - Description: Use when building multi-platform chat bots — Slack, Telegram, Microsoft Teams, Discord, Google Chat, GitHub, Linear — with a si...

19. `claude-api`
   - Kind: `user-installed-skill`
   - Path: `skills/claude-api`
   - License file: `True`
   - Description: Use when building, debugging, or optimizing Claude API and Anthropic SDK applications.

20. `cms`
   - Kind: `user-installed-skill`
   - Path: `skills/cms`
   - License file: `False`
   - Description: Use when building content-driven sites with a headless CMS on Vercel.

21. `codex-expo-run-actions`
   - Kind: `user-installed-skill`
   - Path: `skills/codex-expo-run-actions`
   - License file: `False`
   - Description: Use when the user wants the Codex app Run button, build/run actions, action buttons, or a stable Expo start/run workflow from C...

22. `cron-jobs`
   - Kind: `user-installed-skill`
   - Path: `skills/cron-jobs`
   - License file: `False`
   - Description: Use when adding, editing, or debugging scheduled tasks in vercel.json.

23. `deployments-cicd`
   - Kind: `user-installed-skill`
   - Path: `skills/deployments-cicd`
   - License file: `False`
   - Description: Use when deploying, promoting, rolling back, inspecting deployments, building with --prebuilt, or configuring CI workflow files...

24. `dispatching-parallel-agents`
   - Kind: `user-installed-skill`
   - Path: `skills/dispatching-parallel-agents`
   - License file: `False`
   - Description: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies

25. `email`
   - Kind: `user-installed-skill`
   - Path: `skills/email`
   - License file: `False`
   - Description: Use when sending emails from a Vercel-deployed application.

26. `env-vars`
   - Kind: `user-installed-skill`
   - Path: `skills/env-vars`
   - License file: `False`
   - Description: Use when working with .env files, vercel env commands, OIDC tokens, or managing environment-specific configuration.

27. `executing-plans`
   - Kind: `user-installed-skill`
   - Path: `skills/executing-plans`
   - License file: `False`
   - Description: Use when you have a written implementation plan to execute in a separate session with review checkpoints

28. `expo-api-routes`
   - Kind: `user-installed-skill`
   - Path: `skills/expo-api-routes`
   - License file: `False`
   - Description: Use when working on creating API routes in Expo Router with EAS Hosting

29. `expo-cicd-workflows`
   - Kind: `user-installed-skill`
   - Path: `skills/expo-cicd-workflows`
   - License file: `False`
   - Description: Use when working with expo cicd workflows: Helps understand and write EAS workflow YAML files for Expo projects. Use this skill...

30. `expo-deployment`
   - Kind: `user-installed-skill`
   - Path: `skills/expo-deployment`
   - License file: `False`
   - Description: Use when deploying Expo apps to the iOS App Store, Android Play Store, web hosting, or EAS API routes.

31. `expo-dev-client`
   - Kind: `user-installed-skill`
   - Path: `skills/expo-dev-client`
   - License file: `False`
   - Description: Use when building or distributing Expo development clients locally, with EAS, or through TestFlight.

32. `expo-module`
   - Kind: `user-installed-skill`
   - Path: `skills/expo-module`
   - License file: `False`
   - Description: Use when building or modifying native modules for Expo.

33. `expo-tailwind-setup`
   - Kind: `user-installed-skill`
   - Path: `skills/expo-tailwind-setup`
   - License file: `False`
   - Description: Use when setting up tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for universal styling

34. `expo-ui-jetpack-compose`
   - Kind: `user-installed-skill`
   - Path: `skills/expo-ui-jetpack-compose`
   - License file: `False`
   - Description: Use when adding Jetpack Compose views or modifiers to Expo apps with @expo/ui/jetpack-compose.

35. `expo-ui-swift-ui`
   - Kind: `user-installed-skill`
   - Path: `skills/expo-ui-swift-ui`
   - License file: `False`
   - Description: Use when adding SwiftUI views or modifiers to Expo apps with @expo/ui/swift-ui.

36. `external-design-skill-router`
   - Kind: `user-installed-skill`
   - Path: `skills/external-design-skill-router`
   - License file: `False`
   - Description: Use when working on Luna UI, dashboards, chat interfaces, component quality, visual consistency, style extraction, or frontend ...

37. `finishing-a-development-branch`
   - Kind: `user-installed-skill`
   - Path: `skills/finishing-a-development-branch`
   - License file: `False`
   - Description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of de...

38. `frontend-design`
   - Kind: `user-installed-skill`
   - Path: `skills/frontend-design`
   - License file: `True`
   - Description: Use when creating distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks...

39. `geist`
   - Kind: `user-installed-skill`
   - Path: `skills/geist`
   - License file: `False`
   - Description: Use when configuring Geist Sans, Geist Mono, or Geist Pixel, setting up font imports, or applying Vercel typography and aesthet...

40. `geistdocs`
   - Kind: `user-installed-skill`
   - Path: `skills/geistdocs`
   - License file: `False`
   - Description: Use when creating documentation sites, configuring geistdocs, writing MDX content, or setting up docs infrastructure.

41. `gh-address-comments`
   - Kind: `user-installed-skill`
   - Path: `skills/gh-address-comments`
   - License file: `True`
   - Description: Use when the user wants to inspect unresolved review threads, requested changes, or inline review comments on a PR, then implem...

42. `gh-fix-ci`
   - Kind: `user-installed-skill`
   - Path: `skills/gh-fix-ci`
   - License file: `True`
   - Description: Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions. Use the GitHub app from this plugin f...

43. `github`
   - Kind: `user-installed-skill`
   - Path: `skills/github`
   - License file: `False`
   - Description: Use when the user asks for general GitHub help, wants PR or issue summaries, or needs repository context before choosing a more...

44. `internal-comms`
   - Kind: `user-installed-skill`
   - Path: `skills/internal-comms`
   - License file: `True`
   - Description: Use when writing all kinds of internal communications, using the formats that my company likes to use. Claude should use this s...

45. `investigation-mode`
   - Kind: `user-installed-skill`
   - Path: `skills/investigation-mode`
   - License file: `False`
   - Description: Use when debugging stuck, hung, broken, flaky, or confusing behavior that needs systematic investigation.

46. `json-render`
   - Kind: `user-installed-skill`
   - Path: `skills/json-render`
   - License file: `False`
   - Description: Use when building custom chat UIs, rendering tool results, or troubleshooting AI response display issues.

47. `marketplace`
   - Kind: `user-installed-skill`
   - Path: `skills/marketplace`
   - License file: `False`
   - Description: Use when consuming third-party services, building custom integrations, or managing marketplace resources on Vercel.

48. `mcp-builder`
   - Kind: `user-installed-skill`
   - Path: `skills/mcp-builder`
   - License file: `True`
   - Description: Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

49. `micro`
   - Kind: `user-installed-skill`
   - Path: `skills/micro`
   - License file: `False`
   - Description: Use when building lightweight HTTP servers, API endpoints, or microservices using the micro library.

50. `native-data-fetching`
   - Kind: `user-installed-skill`
   - Path: `skills/native-data-fetching`
   - License file: `False`
   - Description: Use when implementing or debugging ANY network request, API call, or data fetching. Covers fetch API, React Query, SWR, error h...

51. `ncc`
   - Kind: `user-installed-skill`
   - Path: `skills/ncc`
   - License file: `False`
   - Description: Use when bundling serverless functions, CLI tools, or any Node.js project into a self-contained file.

52. `netlify-ai-gateway`
   - Kind: `user-installed-skill`
   - Path: `skills/netlify-ai-gateway`
   - License file: `True`
   - Description: Use when adding AI capabilities or selecting/changing AI models. Must be read before choosing a model. Covers supported provide...

53. `netlify-blobs`
   - Kind: `user-installed-skill`
   - Path: `skills/netlify-blobs`
   - License file: `True`
   - Description: Use when storing files, images, documents, or simple key-value data without a full database. Covers getStore(), CRUD operations...

54. `netlify-caching`
   - Kind: `user-installed-skill`
   - Path: `skills/netlify-caching`
   - License file: `True`
   - Description: Use when configuring cache headers, setting up stale-while-revalidate, implementing on-demand cache purge, or understanding Net...

55. `netlify-cli-and-deploy`
   - Kind: `user-installed-skill`
   - Path: `skills/netlify-cli-and-deploy`
   - License file: `True`
   - Description: Use when installing the CLI, linking sites, deploying (Git-based or manual), managing environment variables, or running local d...

56. `netlify-config`
   - Kind: `user-installed-skill`
   - Path: `skills/netlify-config`
   - License file: `True`
   - Description: Use when configuring build settings, redirects, rewrites, headers, deploy contexts, environment variables, or any site-level co...

57. `netlify-deploy`
   - Kind: `user-installed-skill`
   - Path: `skills/netlify-deploy`
   - License file: `True`
   - Description: Use when the user wants to link a repo, validate deploy settings, run a deploy, or choose between preview and production flows.

58. `netlify-edge-functions`
   - Kind: `user-installed-skill`
   - Path: `skills/netlify-edge-functions`
   - License file: `True`
   - Description: Use when building middleware, geolocation-based logic, request/response manipulation, authentication checks, A/B testing, or an...

59. `netlify-forms`
   - Kind: `user-installed-skill`
   - Path: `skills/netlify-forms`
   - License file: `True`
   - Description: Use when adding contact forms, feedback forms, file upload forms, or any form that should be collected by Netlify. Covers the d...

60. `netlify-frameworks`
   - Kind: `user-installed-skill`
   - Path: `skills/netlify-frameworks`
   - License file: `True`
   - Description: Use when setting up a framework project (Vite/React, Astro, TanStack Start, Next.js, Nuxt, SvelteKit, Remix) for Netlify deploy...

61. `netlify-functions`
   - Kind: `user-installed-skill`
   - Path: `skills/netlify-functions`
   - License file: `True`
   - Description: Use when creating API endpoints, background processing, scheduled tasks, or any server-side logic using Netlify Functions. Cove...

62. `netlify-identity`
   - Kind: `user-installed-skill`
   - Path: `skills/netlify-identity`
   - License file: `True`
   - Description: Use when the task involves authentication, user signups, logins, password recovery, OAuth providers, role-based access control,...

63. `netlify-image-cdn`
   - Kind: `user-installed-skill`
   - Path: `skills/netlify-image-cdn`
   - License file: `True`
   - Description: Use when serving optimized images, creating responsive image markup, setting up user-uploaded image pipelines, or configuring i...

64. `next-forge`
   - Kind: `user-installed-skill`
   - Path: `skills/next-forge`
   - License file: `False`
   - Description: Use when working in a next-forge project, scaffolding with `npx next-forge init`, or editing @repo/* workspace packages.

65. `nextjs`
   - Kind: `user-installed-skill`
   - Path: `skills/nextjs`
   - License file: `False`
   - Description: Use when building, debugging, or architecting Next.js applications — routing, Server Components, Server Actions, Cache Componen...

66. `notion-knowledge-capture`
   - Kind: `user-installed-skill`
   - Path: `skills/notion-knowledge-capture`
   - License file: `True`
   - Description: Use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking.

67. `notion-meeting-intelligence`
   - Kind: `user-installed-skill`
   - Path: `skills/notion-meeting-intelligence`
   - License file: `True`
   - Description: Use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.

68. `notion-research-documentation`
   - Kind: `user-installed-skill`
   - Path: `skills/notion-research-documentation`
   - License file: `True`
   - Description: Use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.

69. `notion-spec-to-implementation`
   - Kind: `user-installed-skill`
   - Path: `skills/notion-spec-to-implementation`
   - License file: `True`
   - Description: Use when implementing PRDs/feature specs and creating Notion plans + tasks from them.

70. `observability`
   - Kind: `user-installed-skill`
   - Path: `skills/observability`
   - License file: `False`
   - Description: Use when instrumenting, debugging, or optimizing application performance and user experience on Vercel.

71. `payments`
   - Kind: `user-installed-skill`
   - Path: `skills/payments`
   - License file: `False`
   - Description: Use when implementing payments, subscriptions, or processing transactions.

72. `react-best-practices`
   - Kind: `user-installed-skill`
   - Path: `skills/react-best-practices`
   - License file: `False`
   - Description: Use when reviewing or editing multiple React TSX components for correctness, hooks usage, composition, rendering, or maintainab...

73. `receiving-code-review`
   - Kind: `user-installed-skill`
   - Path: `skills/receiving-code-review`
   - License file: `False`
   - Description: Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically q...

74. `render-debug`
   - Kind: `user-installed-skill`
   - Path: `skills/render-debug`
   - License file: `False`
   - Description: Use when deployments fail, services won't start, or users mention errors, logs, or debugging.

75. `render-deploy`
   - Kind: `user-installed-skill`
   - Path: `skills/render-deploy`
   - License file: `False`
   - Description: Use when the user wants to deploy, host, publish, or set up their application on Render's cloud platform.

76. `render-migrate-from-heroku`
   - Kind: `user-installed-skill`
   - Path: `skills/render-migrate-from-heroku`
   - License file: `False`
   - Description: Use when migrating from Heroku to Render by reading local project files and generating equivalent Render services. Triggers: an...

77. `render-monitor`
   - Kind: `user-installed-skill`
   - Path: `skills/render-monitor`
   - License file: `False`
   - Description: Use when users want to check service status, view metrics, monitor performance, or verify deployments are healthy.

78. `render-workflows`
   - Kind: `user-installed-skill`
   - Path: `skills/render-workflows`
   - License file: `False`
   - Description: Use when a user wants to set up Render Workflows for the first time, scaffold a workflow service, add or modify workflow tasks,...

79. `requesting-code-review`
   - Kind: `user-installed-skill`
   - Path: `skills/requesting-code-review`
   - License file: `False`
   - Description: Use when completing tasks, implementing major features, or before merging to verify work meets requirements

80. `routing-middleware`
   - Kind: `user-installed-skill`
   - Path: `skills/routing-middleware`
   - License file: `False`
   - Description: Use when intercepting requests at the platform level.

81. `runtime-cache`
   - Kind: `user-installed-skill`
   - Path: `skills/runtime-cache`
   - License file: `False`
   - Description: Use when implementing caching strategies beyond framework-level caching.

82. `satori`
   - Kind: `user-installed-skill`
   - Path: `skills/satori`
   - License file: `False`
   - Description: Use when working with Satori — Vercel's library that converts HTML and CSS to SVG, commonly used to generate dynamic OG images ...

83. `sentry`
   - Kind: `user-installed-skill`
   - Path: `skills/sentry`
   - License file: `True`
   - Description: Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data...

84. `shadcn`
   - Kind: `user-installed-skill`
   - Path: `skills/shadcn`
   - License file: `False`
   - Description: Use when initializing shadcn, adding components, composing product UI, building custom registries, configuring themes, or troub...

85. `sign-in-with-vercel`
   - Kind: `user-installed-skill`
   - Path: `skills/sign-in-with-vercel`
   - License file: `False`
   - Description: Use when implementing user login with Vercel as the identity provider.

86. `slack-gif-creator`
   - Kind: `user-installed-skill`
   - Path: `skills/slack-gif-creator`
   - License file: `True`
   - Description: Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack.

87. `stripe-best-practices`
   - Kind: `user-installed-skill`
   - Path: `skills/stripe-best-practices`
   - License file: `False`
   - Description: Use when building, modifying, or reviewing any Stripe integration — including accepting payments, building marketplaces, integr...

88. `subagent-driven-development`
   - Kind: `user-installed-skill`
   - Path: `skills/subagent-driven-development`
   - License file: `False`
   - Description: Use when executing implementation plans with independent tasks in the current session

89. `supabase`
   - Kind: `user-installed-skill`
   - Path: `skills/supabase`
   - License file: `False`
   - Description: Use when doing ANY task involving Supabase. Triggers: Supabase products (Database, Auth, Edge Functions, Realtime, Storage, Vec...

90. `supabase-postgres-best-practices`
   - Kind: `user-installed-skill`
   - Path: `skills/supabase-postgres-best-practices`
   - License file: `False`
   - Description: Use when writing, reviewing, or optimizing Supabase Postgres queries, schemas, indexes, RLS policies, or database performance.

91. `swr`
   - Kind: `user-installed-skill`
   - Path: `skills/swr`
   - License file: `False`
   - Description: Use when building React apps with client-side data fetching, caching, revalidation, mutations, optimistic UI, pagination, or in...

92. `systematic-debugging`
   - Kind: `user-installed-skill`
   - Path: `skills/systematic-debugging`
   - License file: `False`
   - Description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes

93. `test-driven-development`
   - Kind: `user-installed-skill`
   - Path: `skills/test-driven-development`
   - License file: `False`
   - Description: Use when implementing any feature or bugfix, before writing implementation code

94. `theme-factory`
   - Kind: `user-installed-skill`
   - Path: `skills/theme-factory`
   - License file: `True`
   - Description: Use when working on styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. T...

95. `turbopack`
   - Kind: `user-installed-skill`
   - Path: `skills/turbopack`
   - License file: `False`
   - Description: Use when configuring the Next.js bundler, optimizing HMR, debugging build issues, or understanding the Turbopack vs Webpack dif...

96. `turborepo`
   - Kind: `user-installed-skill`
   - Path: `skills/turborepo`
   - License file: `False`
   - Description: Use when setting up or optimizing monorepo builds, configuring task caching, remote caching, parallel execution, or the --affec...

97. `upgrade-stripe`
   - Kind: `user-installed-skill`
   - Path: `skills/upgrade-stripe`
   - License file: `False`
   - Description: Use when upgrading Stripe API versions, SDK versions, webhook versions, or integration patterns.

98. `upgrading-expo`
   - Kind: `user-installed-skill`
   - Path: `skills/upgrading-expo`
   - License file: `False`
   - Description: Use when working on upgrading Expo SDK versions and fixing dependency issues

99. `use-dom`
   - Kind: `user-installed-skill`
   - Path: `skills/use-dom`
   - License file: `False`
   - Description: Use when migrating web code into Expo DOM components, embedding web experiences in native apps, or sharing web UI across native...

100. `using-git-worktrees`
   - Kind: `user-installed-skill`
   - Path: `skills/using-git-worktrees`
   - License file: `False`
   - Description: Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures a...

101. `using-superpowers`
   - Kind: `user-installed-skill`
   - Path: `skills/using-superpowers`
   - License file: `False`
   - Description: Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY respons...

102. `v0-dev`
   - Kind: `user-installed-skill`
   - Path: `skills/v0-dev`
   - License file: `False`
   - Description: Use when discussing AI code generation, generating UI components from prompts, v0 CLI usage, v0 SDK/API integration, or integra...

103. `vercel-agent`
   - Kind: `user-installed-skill`
   - Path: `skills/vercel-agent`
   - License file: `False`
   - Description: Use when configuring or understanding Vercel's AI development tools.

104. `vercel-api`
   - Kind: `user-installed-skill`
   - Path: `skills/vercel-api`
   - License file: `False`
   - Description: Use when the agent needs live access to Vercel projects, deployments, environment variables, domains, logs, or documentation th...

105. `vercel-cli`
   - Kind: `user-installed-skill`
   - Path: `skills/vercel-cli`
   - License file: `False`
   - Description: Use when deploying, managing environment variables, linking projects, viewing logs, managing domains, or interacting with the V...

106. `vercel-firewall`
   - Kind: `user-installed-skill`
   - Path: `skills/vercel-firewall`
   - License file: `False`
   - Description: Use when configuring DDoS protection, WAF rules, rate limiting, bot filtering, IP allow/block lists, OWASP rulesets, Attack Cha...

107. `vercel-flags`
   - Kind: `user-installed-skill`
   - Path: `skills/vercel-flags`
   - License file: `False`
   - Description: Use when implementing feature flags, experimentation, or staged rollouts.

108. `vercel-functions`
   - Kind: `user-installed-skill`
   - Path: `skills/vercel-functions`
   - License file: `False`
   - Description: Use when configuring, debugging, or optimizing server-side code running on Vercel.

109. `vercel-queues`
   - Kind: `user-installed-skill`
   - Path: `skills/vercel-queues`
   - License file: `False`
   - Description: Use when building async processing, fan-out patterns, or event-driven architectures.

110. `vercel-sandbox`
   - Kind: `user-installed-skill`
   - Path: `skills/vercel-sandbox`
   - License file: `False`
   - Description: Use when executing user-generated or AI-generated code in isolation.

111. `vercel-services`
   - Kind: `user-installed-skill`
   - Path: `skills/vercel-services`
   - License file: `False`
   - Description: Use when working with Vercel Services — deploy multiple services within a single Vercel project. Use for monorepo layouts or wh...

112. `vercel-storage`
   - Kind: `user-installed-skill`
   - Path: `skills/vercel-storage`
   - License file: `False`
   - Description: Use when choosing, configuring, or using data storage with Vercel applications.

113. `verification`
   - Kind: `user-installed-skill`
   - Path: `skills/verification`
   - License file: `False`
   - Description: Use when verifying the full user-facing flow end-to-end across browser, API, database, deployment, or telemetry layers.

114. `verification-before-completion`
   - Kind: `user-installed-skill`
   - Path: `skills/verification-before-completion`
   - License file: `False`
   - Description: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification ...

115. `web-artifacts-builder`
   - Kind: `user-installed-skill`
   - Path: `skills/web-artifacts-builder`
   - License file: `True`
   - Description: Use when creating elaborate multi-component HTML artifacts with modern frontend tooling, rich interactions, or generated visual...

116. `webapp-testing`
   - Kind: `user-installed-skill`
   - Path: `skills/webapp-testing`
   - License file: `True`
   - Description: Use when testing local web applications with Playwright, browser automation, screenshots, console logs, or interaction checks.

117. `workflow`
   - Kind: `user-installed-skill`
   - Path: `skills/workflow`
   - License file: `False`
   - Description: Use when building durable workflows, long-running tasks, API routes or agents that need pause/resume, retries, step-based execu...

118. `writing-plans`
   - Kind: `user-installed-skill`
   - Path: `skills/writing-plans`
   - License file: `False`
   - Description: Use when you have a spec or requirements for a multi-step task, before touching code

119. `writing-skills`
   - Kind: `user-installed-skill`
   - Path: `skills/writing-skills`
   - License file: `False`
   - Description: Use when creating new skills, editing existing skills, or verifying skills work before deployment

120. `yeet`
   - Kind: `user-installed-skill`
   - Path: `skills/yeet`
   - License file: `True`
   - Description: Use when publishing local changes to GitHub by checking scope, committing intentionally, pushing a branch, or opening a draft PR.

121. `agent-browser`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/agent-browser`
   - License file: `False`
   - Description: Browser automation CLI for AI agents. Use when the user needs to interact with websites, verify dev server output, test web app...

122. `agent-browser-verify`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/agent-browser-verify`
   - License file: `False`
   - Description: Automated browser verification for dev servers. Triggers when a dev server starts to run a visual gut-check with agent-browser ...

123. `ai-elements`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/ai-elements`
   - License file: `False`
   - Description: AI Elements component library guidance — pre-built React components for AI interfaces built on shadcn/ui. Use when building cha...

124. `ai-gateway`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/ai-gateway`
   - License file: `False`
   - Description: Vercel AI Gateway expert guidance. Use when configuring model routing, provider failover, cost tracking, or managing multiple A...

125. `ai-generation-persistence`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/ai-generation-persistence`
   - License file: `False`
   - Description: AI generation persistence patterns — unique IDs, addressable URLs, database storage, and cost tracking for every LLM generation

126. `ai-sdk`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/ai-sdk`
   - License file: `False`
   - Description: Vercel AI SDK expert guidance. Use when building AI-powered features — chat interfaces, text generation, structured output, too...

127. `auth`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/auth`
   - License file: `False`
   - Description: Authentication integration guidance — Clerk (native Vercel Marketplace), Descope, and Auth0 setup for Next.js applications. Cov...

128. `bootstrap`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/bootstrap`
   - License file: `False`
   - Description: Project bootstrapping orchestrator for repos that depend on Vercel-linked resources (databases, auth, and managed integrations)...

129. `chat-sdk`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/chat-sdk`
   - License file: `False`
   - Description: Vercel Chat SDK expert guidance. Use when building multi-platform chat bots — Slack, Telegram, Microsoft Teams, Discord, Google...

130. `cms`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/cms`
   - License file: `False`
   - Description: Headless CMS integration guidance — Sanity (native Vercel Marketplace), Contentful, DatoCMS, Storyblok, and Builder.io. Covers ...

131. `cron-jobs`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/cron-jobs`
   - License file: `False`
   - Description: Vercel Cron Jobs configuration and best practices. Use when adding, editing, or debugging scheduled tasks in vercel.json.

132. `deployments-cicd`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/deployments-cicd`
   - License file: `False`
   - Description: Vercel deployment and CI/CD expert guidance. Use when deploying, promoting, rolling back, inspecting deployments, building with...

133. `email`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/email`
   - License file: `False`
   - Description: Email sending integration guidance — Resend (native Vercel Marketplace) with React Email templates. Covers API setup, transacti...

134. `env-vars`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/env-vars`
   - License file: `False`
   - Description: Vercel environment variable expert guidance. Use when working with .env files, vercel env commands, OIDC tokens, or managing en...

135. `geist`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/geist`
   - License file: `False`
   - Description: Expert guidance for Geist, Vercel's default typography system and font family for precise Next.js interfaces. Use when configur...

136. `geistdocs`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/geistdocs`
   - License file: `False`
   - Description: Expert guidance for Geistdocs, Vercel's documentation template built with Next.js and Fumadocs — MDX authoring, configuration, ...

137. `investigation-mode`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/investigation-mode`
   - License file: `False`
   - Description: Orchestrated debugging coordinator. Triggers on frustration signals (stuck, hung, broken, waiting) and systematically triages: ...

138. `json-render`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/json-render`
   - License file: `False`
   - Description: AI chat response rendering guidance — handling UIMessage parts, tool call displays, streaming states, and structured data prese...

139. `marketplace`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/marketplace`
   - License file: `False`
   - Description: Vercel Marketplace expert guidance — discovering, installing, and building integrations, auto-provisioned environment variables...

140. `micro`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/micro`
   - License file: `False`
   - Description: Expert guidance for micro — asynchronous HTTP microservices framework by Vercel. Use when building lightweight HTTP servers, AP...

141. `ncc`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/ncc`
   - License file: `False`
   - Description: Expert guidance for @vercel/ncc — a simple CLI for compiling Node.js modules into a single file with all dependencies included....

142. `next-forge`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/next-forge`
   - License file: `False`
   - Description: next-forge expert guidance — production-grade Turborepo monorepo SaaS starter by Vercel. Use when working in a next-forge proje...

143. `nextjs`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/nextjs`
   - License file: `False`
   - Description: Next.js App Router expert guidance. Use when building, debugging, or architecting Next.js applications — routing, Server Compon...

144. `observability`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/observability`
   - License file: `False`
   - Description: Vercel Observability expert guidance — Drains (logs, traces, speed insights, web analytics), Web Analytics, Speed Insights, run...

145. `payments`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/payments`
   - License file: `False`
   - Description: Stripe payments integration guidance — native Vercel Marketplace setup, checkout sessions, webhook handling, subscription billi...

146. `react-best-practices`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/react-best-practices`
   - License file: `False`
   - Description: React best-practices reviewer for TSX files. Triggers after editing multiple TSX components to run a condensed quality checklis...

147. `routing-middleware`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/routing-middleware`
   - License file: `False`
   - Description: Vercel Routing Middleware guidance — request interception before cache, rewrites, redirects, personalization. Works with any fr...

148. `runtime-cache`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/runtime-cache`
   - License file: `False`
   - Description: Vercel Runtime Cache API guidance — ephemeral per-region key-value cache with tag-based invalidation. Shared across Functions, ...

149. `satori`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/satori`
   - License file: `False`
   - Description: Expert guidance for Satori — Vercel's library that converts HTML and CSS to SVG, commonly used to generate dynamic OG images fo...

150. `shadcn`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/shadcn`
   - License file: `False`
   - Description: shadcn/ui expert guidance — CLI, component installation, composition patterns, custom registries, theming, Tailwind CSS integra...

151. `sign-in-with-vercel`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/sign-in-with-vercel`
   - License file: `False`
   - Description: Sign in with Vercel guidance — OAuth 2.0/OIDC identity provider for user authentication via Vercel accounts. Use when implement...

152. `swr`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/swr`
   - License file: `False`
   - Description: SWR data-fetching expert guidance. Use when building React apps with client-side data fetching, caching, revalidation, mutation...

153. `turbopack`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/turbopack`
   - License file: `False`
   - Description: Turbopack expert guidance. Use when configuring the Next.js bundler, optimizing HMR, debugging build issues, or understanding t...

154. `turborepo`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/turborepo`
   - License file: `False`
   - Description: Turborepo expert guidance. Use when setting up or optimizing monorepo builds, configuring task caching, remote caching, paralle...

155. `v0-dev`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/v0-dev`
   - License file: `False`
   - Description: v0 by Vercel expert guidance. Use when discussing AI code generation, generating UI components from prompts, v0 CLI usage, v0 S...

156. `vercel-agent`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-agent`
   - License file: `False`
   - Description: Vercel Agent guidance — AI-powered code review, incident investigation, and SDK installation. Automates PR analysis and anomaly...

157. `vercel-api`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-api`
   - License file: `False`
   - Description: Vercel app and REST API expert guidance. Use when the agent needs live access to Vercel projects, deployments, environment vari...

158. `vercel-cli`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-cli`
   - License file: `False`
   - Description: Vercel CLI expert guidance. Use when deploying, managing environment variables, linking projects, viewing logs, managing domain...

159. `vercel-firewall`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-firewall`
   - License file: `False`
   - Description: Vercel Firewall and security expert guidance. Use when configuring DDoS protection, WAF rules, rate limiting, bot filtering, IP...

160. `vercel-flags`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-flags`
   - License file: `False`
   - Description: Vercel Flags guidance — feature flags platform with unified dashboard, Flags Explorer, gradual rollouts, A/B testing, and provi...

161. `vercel-functions`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-functions`
   - License file: `False`
   - Description: Vercel Functions expert guidance — Serverless Functions, Edge Functions, Fluid Compute, streaming, Cron Jobs, and runtime confi...

162. `vercel-queues`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-queues`
   - License file: `False`
   - Description: Vercel Queues guidance (public beta) — durable event streaming with topics, consumer groups, retries, and delayed delivery. $0....

163. `vercel-sandbox`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-sandbox`
   - License file: `False`
   - Description: Vercel Sandbox guidance — ephemeral Firecracker microVMs for running untrusted code safely. Supports AI agents, code generation...

164. `vercel-services`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-services`
   - License file: `False`
   - Description: Vercel Services — deploy multiple services within a single Vercel project. Use for monorepo layouts or when combining a backend...

165. `vercel-storage`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-storage`
   - License file: `False`
   - Description: Vercel storage expert guidance — Blob, Edge Config, and Marketplace storage (Neon Postgres, Upstash Redis). Use when choosing, ...

166. `verification`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/verification`
   - License file: `False`
   - Description: Full-story verification — infers what the user is building, then verifies the complete flow end-to-end: browser → API → data → ...

167. `workflow`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/vercel/d947469e/skills/workflow`
   - License file: `False`
   - Description: Vercel Workflow DevKit (WDK) expert guidance. Use when building durable workflows, long-running tasks, API routes or agents tha...

168. `gh-address-comments`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/github/d947469e/skills/gh-address-comments`
   - License file: `True`
   - Description: Address actionable GitHub pull request review feedback. Use when the user wants to inspect unresolved review threads, requested...

169. `gh-fix-ci`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/github/d947469e/skills/gh-fix-ci`
   - License file: `True`
   - Description: Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions. Use the GitHub app from this plugin f...

170. `github`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/github/d947469e/skills/github`
   - License file: `False`
   - Description: Triage and orient GitHub repository, pull request, and issue work through the connected GitHub app. Use when the user asks for ...

171. `yeet`
   - Kind: `plugin-skill`
   - Path: `plugins/cache/openai-curated/github/d947469e/skills/yeet`
   - License file: `True`
   - Description: Publish local changes to GitHub by confirming scope, committing intentionally, pushing the branch, and opening a draft PR throu...


## Duplicate Names

- `Zotero`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/zotero/skills/zotero`
  - `temp` `.tmp/plugins/plugins/zotero/skills/zotero`
- `agent-browser`: 4 copies
  - `user-installed-skill` `skills/agent-browser`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/agent-browser`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/agent-browser`
  - `temp` `.tmp/plugins/plugins/vercel/skills/agent-browser`
- `agent-browser-verify`: 4 copies
  - `user-installed-skill` `skills/agent-browser-verify`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/agent-browser-verify`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/agent-browser-verify`
  - `temp` `.tmp/plugins/plugins/vercel/skills/agent-browser-verify`
- `agents-sdk`: 3 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/openai-developers/skills/agents-sdk`
  - `temp` `.tmp/plugins/plugins/openai-developers/skills/agents-sdk`
  - `temp` `.tmp/plugins/plugins/cloudflare/skills/agents-sdk`
- `ai-elements`: 4 copies
  - `user-installed-skill` `skills/ai-elements`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/ai-elements`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/ai-elements`
  - `temp` `.tmp/plugins/plugins/vercel/skills/ai-elements`
- `ai-gateway`: 4 copies
  - `user-installed-skill` `skills/ai-gateway`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/ai-gateway`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/ai-gateway`
  - `temp` `.tmp/plugins/plugins/vercel/skills/ai-gateway`
- `ai-generation-persistence`: 4 copies
  - `user-installed-skill` `skills/ai-generation-persistence`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/ai-generation-persistence`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/ai-generation-persistence`
  - `temp` `.tmp/plugins/plugins/vercel/skills/ai-generation-persistence`
- `ai-sdk`: 4 copies
  - `user-installed-skill` `skills/ai-sdk`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/ai-sdk`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/ai-sdk`
  - `temp` `.tmp/plugins/plugins/vercel/skills/ai-sdk`
- `alpha`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/plugin-eval/fixtures/multi-skill-plugin/skills/alpha`
  - `temp` `.tmp/plugins/plugins/plugin-eval/fixtures/multi-skill-plugin/skills/alpha`
- `alphafold-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/alphafold-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/alphafold-skill`
- `android-emulator-qa`: 3 copies
  - `user-installed-skill` `skills/android-emulator-qa`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/test-android-apps/skills/android-emulator-qa`
  - `temp` `.tmp/plugins/plugins/test-android-apps/skills/android-emulator-qa`
- `android-performance`: 3 copies
  - `user-installed-skill` `skills/android-performance`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/test-android-apps/skills/android-performance`
  - `temp` `.tmp/plugins/plugins/test-android-apps/skills/android-performance`
- `attack-path-analysis`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/codex-security/skills/attack-path-analysis`
  - `temp` `.tmp/plugins/plugins/codex-security/skills/attack-path-analysis`
- `auth`: 4 copies
  - `user-installed-skill` `skills/auth`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/auth`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/auth`
  - `temp` `.tmp/plugins/plugins/vercel/skills/auth`
- `beta`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/plugin-eval/fixtures/multi-skill-plugin/skills/beta`
  - `temp` `.tmp/plugins/plugins/plugin-eval/fixtures/multi-skill-plugin/skills/beta`
- `bgee-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/bgee-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/bgee-skill`
- `bindingdb-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/bindingdb-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/bindingdb-skill`
- `biobankjapan-phewas-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/biobankjapan-phewas-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/biobankjapan-phewas-skill`
- `biorxiv-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/biorxiv-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/biorxiv-skill`
- `biostudies-arrayexpress-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/biostudies-arrayexpress-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/biostudies-arrayexpress-skill`
- `bootstrap`: 4 copies
  - `user-installed-skill` `skills/bootstrap`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/bootstrap`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/bootstrap`
  - `temp` `.tmp/plugins/plugins/vercel/skills/bootstrap`
- `brainstorming`: 3 copies
  - `user-installed-skill` `skills/brainstorming`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/brainstorming`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/brainstorming`
- `build-chatgpt-app`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/openai-developers/skills/build-chatgpt-app`
  - `temp` `.tmp/plugins/plugins/openai-developers/skills/build-chatgpt-app`
- `building-native-ui`: 3 copies
  - `user-installed-skill` `skills/building-native-ui`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/building-native-ui`
  - `temp` `.tmp/plugins/plugins/expo/skills/building-native-ui`
- `cbioportal-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/cbioportal-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/cbioportal-skill`
- `cellxgene-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/cellxgene-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/cellxgene-skill`
- `chat-sdk`: 4 copies
  - `user-installed-skill` `skills/chat-sdk`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/chat-sdk`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/chat-sdk`
  - `temp` `.tmp/plugins/plugins/vercel/skills/chat-sdk`
- `chatgpt-app-submission`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/openai-developers/skills/chatgpt-app-submission`
  - `temp` `.tmp/plugins/plugins/openai-developers/skills/chatgpt-app-submission`
- `chebi-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/chebi-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/chebi-skill`
- `chembl-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/chembl-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/chembl-skill`
- `civic-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/civic-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/civic-skill`
- `clinicaltrials-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/clinicaltrials-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/clinicaltrials-skill`
- `clinvar-variation-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/clinvar-variation-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/clinvar-variation-skill`
- `cloudflare`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/cloudflare/skills/cloudflare`
  - `temp` `.tmp/plugins/plugins/cloudflare/skills/cloudflare`
- `cms`: 4 copies
  - `user-installed-skill` `skills/cms`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/cms`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/cms`
  - `temp` `.tmp/plugins/plugins/vercel/skills/cms`
- `code-review`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/coderabbit/skills/coderabbit-review`
  - `temp` `.tmp/plugins/plugins/coderabbit/skills/coderabbit-review`
- `codex-expo-run-actions`: 3 copies
  - `user-installed-skill` `skills/codex-expo-run-actions`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/codex-expo-run-actions`
  - `temp` `.tmp/plugins/plugins/expo/skills/codex-expo-run-actions`
- `conversation-intelligence`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-conversation-intelligence`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-conversation-intelligence`
- `cron-jobs`: 4 copies
  - `user-installed-skill` `skills/cron-jobs`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/cron-jobs`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/cron-jobs`
  - `temp` `.tmp/plugins/plugins/vercel/skills/cron-jobs`
- `deployments-cicd`: 4 copies
  - `user-installed-skill` `skills/deployments-cicd`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/deployments-cicd`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/deployments-cicd`
  - `temp` `.tmp/plugins/plugins/vercel/skills/deployments-cicd`
- `dispatching-parallel-agents`: 3 copies
  - `user-installed-skill` `skills/dispatching-parallel-agents`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/dispatching-parallel-agents`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/dispatching-parallel-agents`
- `durable-objects`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/cloudflare/skills/durable-objects`
  - `temp` `.tmp/plugins/plugins/cloudflare/skills/durable-objects`
- `efo-ontology-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/efo-ontology-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/efo-ontology-skill`
- `email`: 4 copies
  - `user-installed-skill` `skills/email`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/email`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/email`
  - `temp` `.tmp/plugins/plugins/vercel/skills/email`
- `encode-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/encode-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/encode-skill`
- `ensembl-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/ensembl-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/ensembl-skill`
- `env-vars`: 4 copies
  - `user-installed-skill` `skills/env-vars`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/env-vars`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/env-vars`
  - `temp` `.tmp/plugins/plugins/vercel/skills/env-vars`
- `epigraphdb-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/epigraphdb-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/epigraphdb-skill`
- `eqtl-catalogue-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/eqtl-catalogue-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/eqtl-catalogue-skill`
- `eva-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/eva-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/eva-skill`
- `evaluate-plugin`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/plugin-eval/skills/evaluate-plugin`
  - `temp` `.tmp/plugins/plugins/plugin-eval/skills/evaluate-plugin`
- `evaluate-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/plugin-eval/skills/evaluate-skill`
  - `temp` `.tmp/plugins/plugins/plugin-eval/skills/evaluate-skill`
- `executing-plans`: 3 copies
  - `user-installed-skill` `skills/executing-plans`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/executing-plans`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/executing-plans`
- `expo-api-routes`: 3 copies
  - `user-installed-skill` `skills/expo-api-routes`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/expo-api-routes`
  - `temp` `.tmp/plugins/plugins/expo/skills/expo-api-routes`
- `expo-cicd-workflows`: 3 copies
  - `user-installed-skill` `skills/expo-cicd-workflows`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/expo-cicd-workflows`
  - `temp` `.tmp/plugins/plugins/expo/skills/expo-cicd-workflows`
- `expo-deployment`: 3 copies
  - `user-installed-skill` `skills/expo-deployment`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/expo-deployment`
  - `temp` `.tmp/plugins/plugins/expo/skills/expo-deployment`
- `expo-dev-client`: 3 copies
  - `user-installed-skill` `skills/expo-dev-client`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/expo-dev-client`
  - `temp` `.tmp/plugins/plugins/expo/skills/expo-dev-client`
- `expo-module`: 3 copies
  - `user-installed-skill` `skills/expo-module`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/expo-module`
  - `temp` `.tmp/plugins/plugins/expo/skills/expo-module`
- `expo-tailwind-setup`: 3 copies
  - `user-installed-skill` `skills/expo-tailwind-setup`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/expo-tailwind-setup`
  - `temp` `.tmp/plugins/plugins/expo/skills/expo-tailwind-setup`
- `expo-ui-jetpack-compose`: 3 copies
  - `user-installed-skill` `skills/expo-ui-jetpack-compose`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/expo-ui-jetpack-compose`
  - `temp` `.tmp/plugins/plugins/expo/skills/expo-ui-jetpack-compose`
- `expo-ui-swift-ui`: 3 copies
  - `user-installed-skill` `skills/expo-ui-swift-ui`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/expo-ui-swift-ui`
  - `temp` `.tmp/plugins/plugins/expo/skills/expo-ui-swift-ui`
- `figma-code-connect`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/figma/skills/figma-code-connect`
  - `temp` `.tmp/plugins/plugins/figma/skills/figma-code-connect`
- `figma-create-new-file`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/figma/skills/figma-create-new-file`
  - `temp` `.tmp/plugins/plugins/figma/skills/figma-create-new-file`
- `figma-generate-design`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/figma/skills/figma-generate-design`
  - `temp` `.tmp/plugins/plugins/figma/skills/figma-generate-design`
- `figma-generate-diagram`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/figma/skills/figma-generate-diagram`
  - `temp` `.tmp/plugins/plugins/figma/skills/figma-generate-diagram`
- `figma-generate-library`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/figma/skills/figma-generate-library`
  - `temp` `.tmp/plugins/plugins/figma/skills/figma-generate-library`
- `figma-use`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/figma/skills/figma-use`
  - `temp` `.tmp/plugins/plugins/figma/skills/figma-use`
- `figma-use-figjam`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/figma/skills/figma-use-figjam`
  - `temp` `.tmp/plugins/plugins/figma/skills/figma-use-figjam`
- `figma-use-slides`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/figma/skills/figma-use-slides`
  - `temp` `.tmp/plugins/plugins/figma/skills/figma-use-slides`
- `finding-discovery`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/codex-security/skills/finding-discovery`
  - `temp` `.tmp/plugins/plugins/codex-security/skills/finding-discovery`
- `finishing-a-development-branch`: 3 copies
  - `user-installed-skill` `skills/finishing-a-development-branch`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/finishing-a-development-branch`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/finishing-a-development-branch`
- `finngen-phewas-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/finngen-phewas-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/finngen-phewas-skill`
- `fix-finding`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/codex-security/skills/fix-finding`
  - `temp` `.tmp/plugins/plugins/codex-security/skills/fix-finding`
- `game-playtest`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/game-studio/skills/game-playtest`
  - `temp` `.tmp/plugins/plugins/game-studio/skills/game-playtest`
- `game-studio`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/game-studio/skills/game-studio`
  - `temp` `.tmp/plugins/plugins/game-studio/skills/game-studio`
- `game-ui-frontend`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/game-studio/skills/game-ui-frontend`
  - `temp` `.tmp/plugins/plugins/game-studio/skills/game-ui-frontend`
- `geist`: 4 copies
  - `user-installed-skill` `skills/geist`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/geist`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/geist`
  - `temp` `.tmp/plugins/plugins/vercel/skills/geist`
- `geistdocs`: 4 copies
  - `user-installed-skill` `skills/geistdocs`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/geistdocs`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/geistdocs`
  - `temp` `.tmp/plugins/plugins/vercel/skills/geistdocs`
- `genebass-gene-burden-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/genebass-gene-burden-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/genebass-gene-burden-skill`
- `gh-address-comments`: 5 copies
  - `vendor-import` `vendor_imports/skills/skills/.curated/gh-address-comments`
  - `user-installed-skill` `skills/gh-address-comments`
  - `plugin-skill` `plugins/cache/openai-curated/github/d947469e/skills/gh-address-comments`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/github/skills/gh-address-comments`
  - `temp` `.tmp/plugins/plugins/github/skills/gh-address-comments`
- `gh-fix-ci`: 5 copies
  - `vendor-import` `vendor_imports/skills/skills/.curated/gh-fix-ci`
  - `user-installed-skill` `skills/gh-fix-ci`
  - `plugin-skill` `plugins/cache/openai-curated/github/d947469e/skills/gh-fix-ci`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/github/skills/gh-fix-ci`
  - `temp` `.tmp/plugins/plugins/github/skills/gh-fix-ci`
- `github`: 4 copies
  - `user-installed-skill` `skills/github`
  - `plugin-skill` `plugins/cache/openai-curated/github/d947469e/skills/github`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/github/skills/github`
  - `temp` `.tmp/plugins/plugins/github/skills/github`
- `gmail`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/gmail/skills/gmail`
  - `temp` `.tmp/plugins/plugins/gmail/skills/gmail`
- `gmail-inbox-triage`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/gmail/skills/gmail-inbox-triage`
  - `temp` `.tmp/plugins/plugins/gmail/skills/gmail-inbox-triage`
- `gnomad-graphql-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/gnomad-graphql-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/gnomad-graphql-skill`
- `google-calendar`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/google-calendar/skills/google-calendar`
  - `temp` `.tmp/plugins/plugins/google-calendar/skills/google-calendar`
- `google-calendar-daily-brief`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/google-calendar/skills/google-calendar-daily-brief`
  - `temp` `.tmp/plugins/plugins/google-calendar/skills/google-calendar-daily-brief`
- `google-calendar-free-up-time`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/google-calendar/skills/google-calendar-free-up-time`
  - `temp` `.tmp/plugins/plugins/google-calendar/skills/google-calendar-free-up-time`
- `google-calendar-group-scheduler`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/google-calendar/skills/google-calendar-group-scheduler`
  - `temp` `.tmp/plugins/plugins/google-calendar/skills/google-calendar-group-scheduler`
- `google-calendar-meeting-prep`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/google-calendar/skills/google-calendar-meeting-prep`
  - `temp` `.tmp/plugins/plugins/google-calendar/skills/google-calendar-meeting-prep`
- `google-docs`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/google-drive/skills/google-docs`
  - `temp` `.tmp/plugins/plugins/google-drive/skills/google-docs`
- `google-drive`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/google-drive/skills/google-drive`
  - `temp` `.tmp/plugins/plugins/google-drive/skills/google-drive`
- `google-drive-comments`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/google-drive/skills/google-drive-comments`
  - `temp` `.tmp/plugins/plugins/google-drive/skills/google-drive-comments`
- `google-sheets`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/google-drive/skills/google-sheets`
  - `temp` `.tmp/plugins/plugins/google-drive/skills/google-sheets`
- `google-slides`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/google-drive/skills/google-slides`
  - `temp` `.tmp/plugins/plugins/google-drive/skills/google-slides`
- `gsap`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hyperframes/skills/gsap`
  - `temp` `.tmp/plugins/plugins/hyperframes/skills/gsap`
- `gtex-eqtl-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/gtex-eqtl-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/gtex-eqtl-skill`
- `gwas-catalog-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/gwas-catalog-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/gwas-catalog-skill`
- `heygen-avatar`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/heygen/skills/heygen-avatar`
  - `temp` `.tmp/plugins/plugins/heygen/skills/heygen-avatar`
- `heygen-video`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/heygen/skills/heygen-video`
  - `temp` `.tmp/plugins/plugins/heygen/skills/heygen-video`
- `hf-cli`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hugging-face/skills/cli`
  - `temp` `.tmp/plugins/plugins/hugging-face/skills/cli`
- `hmdb-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/hmdb-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/hmdb-skill`
- `hubspot`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hubspot/skills/hubspot`
  - `temp` `.tmp/plugins/plugins/hubspot/skills/hubspot`
- `hubspot-crm-data-hygiene`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hubspot/skills/hubspot-crm-data-hygiene`
  - `temp` `.tmp/plugins/plugins/hubspot/skills/hubspot-crm-data-hygiene`
- `hubspot-customer-prep`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hubspot/skills/hubspot-customer-prep`
  - `temp` `.tmp/plugins/plugins/hubspot/skills/hubspot-customer-prep`
- `hubspot-pipeline-health`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hubspot/skills/hubspot-pipeline-health`
  - `temp` `.tmp/plugins/plugins/hubspot/skills/hubspot-pipeline-health`
- `huggingface-community-evals`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hugging-face/skills/community-evals`
  - `temp` `.tmp/plugins/plugins/hugging-face/skills/community-evals`
- `huggingface-datasets`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hugging-face/skills/datasets`
  - `temp` `.tmp/plugins/plugins/hugging-face/skills/datasets`
- `huggingface-gradio`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hugging-face/skills/gradio`
  - `temp` `.tmp/plugins/plugins/hugging-face/skills/gradio`
- `huggingface-jobs`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hugging-face/skills/jobs`
  - `temp` `.tmp/plugins/plugins/hugging-face/skills/jobs`
- `huggingface-llm-trainer`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hugging-face/skills/llm-trainer`
  - `temp` `.tmp/plugins/plugins/hugging-face/skills/llm-trainer`
- `huggingface-paper-publisher`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hugging-face/skills/paper-publisher`
  - `temp` `.tmp/plugins/plugins/hugging-face/skills/paper-publisher`
- `huggingface-papers`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hugging-face/skills/papers`
  - `temp` `.tmp/plugins/plugins/hugging-face/skills/papers`
- `huggingface-trackio`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hugging-face/skills/trackio`
  - `temp` `.tmp/plugins/plugins/hugging-face/skills/trackio`
- `huggingface-vision-trainer`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hugging-face/skills/vision-trainer`
  - `temp` `.tmp/plugins/plugins/hugging-face/skills/vision-trainer`
- `human-protein-atlas-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/human-protein-atlas-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/human-protein-atlas-skill`
- `hyperframes`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hyperframes/skills/hyperframes`
  - `temp` `.tmp/plugins/plugins/hyperframes/skills/hyperframes`
- `hyperframes-cli`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hyperframes/skills/hyperframes-cli`
  - `temp` `.tmp/plugins/plugins/hyperframes/skills/hyperframes-cli`
- `hyperframes-registry`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hyperframes/skills/hyperframes-registry`
  - `temp` `.tmp/plugins/plugins/hyperframes/skills/hyperframes-registry`
- `improve-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/plugin-eval/skills/improve-skill`
  - `temp` `.tmp/plugins/plugins/plugin-eval/skills/improve-skill`
- `investigation-mode`: 4 copies
  - `user-installed-skill` `skills/investigation-mode`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/investigation-mode`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/investigation-mode`
  - `temp` `.tmp/plugins/plugins/vercel/skills/investigation-mode`
- `ipd-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/ipd-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/ipd-skill`
- `json-render`: 4 copies
  - `user-installed-skill` `skills/json-render`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/json-render`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/json-render`
  - `temp` `.tmp/plugins/plugins/vercel/skills/json-render`
- `linear`: 3 copies
  - `vendor-import` `vendor_imports/skills/skills/.curated/linear`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/linear/skills/linear`
  - `temp` `.tmp/plugins/plugins/linear/skills/linear`
- `locus-to-gene-mapper-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/locus-to-gene-mapper-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/locus-to-gene-mapper-skill`
- `marketplace`: 4 copies
  - `user-installed-skill` `skills/marketplace`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/marketplace`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/marketplace`
  - `temp` `.tmp/plugins/plugins/vercel/skills/marketplace`
- `metabolights-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/metabolights-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/metabolights-skill`
- `metric-pack-designer`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/plugin-eval/skills/metric-pack-designer`
  - `temp` `.tmp/plugins/plugins/plugin-eval/skills/metric-pack-designer`
- `mgnify-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/mgnify-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/mgnify-skill`
- `micro`: 4 copies
  - `user-installed-skill` `skills/micro`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/micro`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/micro`
  - `temp` `.tmp/plugins/plugins/vercel/skills/micro`
- `minimal-plugin-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/plugin-eval/fixtures/minimal-plugin/skills/minimal-plugin-skill`
  - `temp` `.tmp/plugins/plugins/plugin-eval/fixtures/minimal-plugin/skills/minimal-plugin-skill`
- `minimal-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/plugin-eval/fixtures/minimal-skill`
  - `temp` `.tmp/plugins/plugins/plugin-eval/fixtures/minimal-skill`
- `native-data-fetching`: 3 copies
  - `user-installed-skill` `skills/native-data-fetching`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/native-data-fetching`
  - `temp` `.tmp/plugins/plugins/expo/skills/native-data-fetching`
- `ncbi-blast-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/ncbi-blast-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/ncbi-blast-skill`
- `ncbi-clinicaltables-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/ncbi-clinicaltables-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/ncbi-clinicaltables-skill`
- `ncbi-datasets-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/ncbi-datasets-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/ncbi-datasets-skill`
- `ncbi-entrez-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/ncbi-entrez-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/ncbi-entrez-skill`
- `ncbi-pmc-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/ncbi-pmc-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/ncbi-pmc-skill`
- `ncc`: 4 copies
  - `user-installed-skill` `skills/ncc`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/ncc`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/ncc`
  - `temp` `.tmp/plugins/plugins/vercel/skills/ncc`
- `neon-postgres`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/neon-postgres/skills/neon-postgres`
  - `temp` `.tmp/plugins/plugins/neon-postgres/skills/neon-postgres`
- `neon-postgres-egress-optimizer`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/neon-postgres/skills/neon-postgres-egress-optimizer`
  - `temp` `.tmp/plugins/plugins/neon-postgres/skills/neon-postgres-egress-optimizer`
- `netlify-ai-gateway`: 3 copies
  - `user-installed-skill` `skills/netlify-ai-gateway`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/netlify/skills/netlify-ai-gateway`
  - `temp` `.tmp/plugins/plugins/netlify/skills/netlify-ai-gateway`
- `netlify-blobs`: 3 copies
  - `user-installed-skill` `skills/netlify-blobs`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/netlify/skills/netlify-blobs`
  - `temp` `.tmp/plugins/plugins/netlify/skills/netlify-blobs`
- `netlify-caching`: 3 copies
  - `user-installed-skill` `skills/netlify-caching`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/netlify/skills/netlify-caching`
  - `temp` `.tmp/plugins/plugins/netlify/skills/netlify-caching`
- `netlify-cli-and-deploy`: 3 copies
  - `user-installed-skill` `skills/netlify-cli-and-deploy`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/netlify/skills/netlify-cli-and-deploy`
  - `temp` `.tmp/plugins/plugins/netlify/skills/netlify-cli-and-deploy`
- `netlify-config`: 3 copies
  - `user-installed-skill` `skills/netlify-config`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/netlify/skills/netlify-config`
  - `temp` `.tmp/plugins/plugins/netlify/skills/netlify-config`
- `netlify-deploy`: 4 copies
  - `vendor-import` `vendor_imports/skills/skills/.curated/netlify-deploy`
  - `user-installed-skill` `skills/netlify-deploy`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/netlify/skills/netlify-deploy`
  - `temp` `.tmp/plugins/plugins/netlify/skills/netlify-deploy`
- `netlify-edge-functions`: 3 copies
  - `user-installed-skill` `skills/netlify-edge-functions`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/netlify/skills/netlify-edge-functions`
  - `temp` `.tmp/plugins/plugins/netlify/skills/netlify-edge-functions`
- `netlify-forms`: 3 copies
  - `user-installed-skill` `skills/netlify-forms`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/netlify/skills/netlify-forms`
  - `temp` `.tmp/plugins/plugins/netlify/skills/netlify-forms`
- `netlify-frameworks`: 3 copies
  - `user-installed-skill` `skills/netlify-frameworks`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/netlify/skills/netlify-frameworks`
  - `temp` `.tmp/plugins/plugins/netlify/skills/netlify-frameworks`
- `netlify-functions`: 3 copies
  - `user-installed-skill` `skills/netlify-functions`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/netlify/skills/netlify-functions`
  - `temp` `.tmp/plugins/plugins/netlify/skills/netlify-functions`
- `netlify-identity`: 3 copies
  - `user-installed-skill` `skills/netlify-identity`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/netlify/skills/netlify-identity`
  - `temp` `.tmp/plugins/plugins/netlify/skills/netlify-identity`
- `netlify-image-cdn`: 3 copies
  - `user-installed-skill` `skills/netlify-image-cdn`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/netlify/skills/netlify-image-cdn`
  - `temp` `.tmp/plugins/plugins/netlify/skills/netlify-image-cdn`
- `next-forge`: 4 copies
  - `user-installed-skill` `skills/next-forge`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/next-forge`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/next-forge`
  - `temp` `.tmp/plugins/plugins/vercel/skills/next-forge`
- `nextjs`: 4 copies
  - `user-installed-skill` `skills/nextjs`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/nextjs`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/nextjs`
  - `temp` `.tmp/plugins/plugins/vercel/skills/nextjs`
- `notion-knowledge-capture`: 4 copies
  - `vendor-import` `vendor_imports/skills/skills/.curated/notion-knowledge-capture`
  - `user-installed-skill` `skills/notion-knowledge-capture`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/notion/skills/notion-knowledge-capture`
  - `temp` `.tmp/plugins/plugins/notion/skills/notion-knowledge-capture`
- `notion-meeting-intelligence`: 4 copies
  - `vendor-import` `vendor_imports/skills/skills/.curated/notion-meeting-intelligence`
  - `user-installed-skill` `skills/notion-meeting-intelligence`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/notion/skills/notion-meeting-intelligence`
  - `temp` `.tmp/plugins/plugins/notion/skills/notion-meeting-intelligence`
- `notion-research-documentation`: 4 copies
  - `vendor-import` `vendor_imports/skills/skills/.curated/notion-research-documentation`
  - `user-installed-skill` `skills/notion-research-documentation`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/notion/skills/notion-research-documentation`
  - `temp` `.tmp/plugins/plugins/notion/skills/notion-research-documentation`
- `notion-spec-to-implementation`: 4 copies
  - `vendor-import` `vendor_imports/skills/skills/.curated/notion-spec-to-implementation`
  - `user-installed-skill` `skills/notion-spec-to-implementation`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/notion/skills/notion-spec-to-implementation`
  - `temp` `.tmp/plugins/plugins/notion/skills/notion-spec-to-implementation`
- `observability`: 4 copies
  - `user-installed-skill` `skills/observability`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/observability`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/observability`
  - `temp` `.tmp/plugins/plugins/vercel/skills/observability`
- `openai-api-troubleshooting`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/openai-developers/skills/openai-api-troubleshooting`
  - `temp` `.tmp/plugins/plugins/openai-developers/skills/openai-api-troubleshooting`
- `openai-platform-api-key`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/openai-developers/skills/openai-platform-api-key`
  - `temp` `.tmp/plugins/plugins/openai-developers/skills/openai-platform-api-key`
- `opentargets-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/opentargets-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/opentargets-skill`
- `outlook-calendar`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/outlook-calendar/skills/outlook-calendar`
  - `temp` `.tmp/plugins/plugins/outlook-calendar/skills/outlook-calendar`
- `outlook-calendar-daily-brief`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/outlook-calendar/skills/outlook-calendar-daily-brief`
  - `temp` `.tmp/plugins/plugins/outlook-calendar/skills/outlook-calendar-daily-brief`
- `outlook-calendar-free-up-time`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/outlook-calendar/skills/outlook-calendar-free-up-time`
  - `temp` `.tmp/plugins/plugins/outlook-calendar/skills/outlook-calendar-free-up-time`
- `outlook-calendar-group-scheduler`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/outlook-calendar/skills/outlook-calendar-group-scheduler`
  - `temp` `.tmp/plugins/plugins/outlook-calendar/skills/outlook-calendar-group-scheduler`
- `outlook-calendar-meeting-prep`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/outlook-calendar/skills/outlook-calendar-meeting-prep`
  - `temp` `.tmp/plugins/plugins/outlook-calendar/skills/outlook-calendar-meeting-prep`
- `outlook-calendar-shared-calendars`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/outlook-calendar/skills/outlook-calendar-shared-calendars`
  - `temp` `.tmp/plugins/plugins/outlook-calendar/skills/outlook-calendar-shared-calendars`
- `outlook-email`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/outlook-email/skills/outlook-email`
  - `temp` `.tmp/plugins/plugins/outlook-email/skills/outlook-email`
- `outlook-email-inbox-triage`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/outlook-email/skills/outlook-email-inbox-triage`
  - `temp` `.tmp/plugins/plugins/outlook-email/skills/outlook-email-inbox-triage`
- `outlook-email-reply-drafting`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/outlook-email/skills/outlook-email-reply-drafting`
  - `temp` `.tmp/plugins/plugins/outlook-email/skills/outlook-email-reply-drafting`
- `outlook-email-shared-mailboxes`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/outlook-email/skills/outlook-email-shared-mailboxes`
  - `temp` `.tmp/plugins/plugins/outlook-email/skills/outlook-email-shared-mailboxes`
- `outlook-email-subscription-cleanup`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/outlook-email/skills/outlook-email-subscription-cleanup`
  - `temp` `.tmp/plugins/plugins/outlook-email/skills/outlook-email-subscription-cleanup`
- `outlook-email-task-extraction`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/outlook-email/skills/outlook-email-task-extraction`
  - `temp` `.tmp/plugins/plugins/outlook-email/skills/outlook-email-task-extraction`
- `payments`: 4 copies
  - `user-installed-skill` `skills/payments`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/payments`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/payments`
  - `temp` `.tmp/plugins/plugins/vercel/skills/payments`
- `pharmgkb-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/pharmgkb-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/pharmgkb-skill`
- `phaser-2d-game`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/game-studio/skills/phaser-2d-game`
  - `temp` `.tmp/plugins/plugins/game-studio/skills/phaser-2d-game`
- `plugin-eval`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/plugin-eval/skills/plugin-eval`
  - `temp` `.tmp/plugins/plugins/plugin-eval/skills/plugin-eval`
- `pride-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/pride-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/pride-skill`
- `proteomexchange-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/proteomexchange-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/proteomexchange-skill`
- `pubchem-pug-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/pubchem-pug-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/pubchem-pug-skill`
- `quickgo-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/quickgo-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/quickgo-skill`
- `rcsb-pdb-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/rcsb-pdb-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/rcsb-pdb-skill`
- `react-best-practices`: 5 copies
  - `user-installed-skill` `skills/react-best-practices`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/react-best-practices`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/react-best-practices`
  - `temp` `.tmp/plugins/plugins/vercel/skills/react-best-practices`
  - `temp` `.tmp/plugins/plugins/build-web-apps/skills/react-best-practices`
- `react-three-fiber-game`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/game-studio/skills/react-three-fiber-game`
  - `temp` `.tmp/plugins/plugins/game-studio/skills/react-three-fiber-game`
- `reactome-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/reactome-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/reactome-skill`
- `receiving-code-review`: 3 copies
  - `user-installed-skill` `skills/receiving-code-review`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/receiving-code-review`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/receiving-code-review`
- `remotion-best-practices`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/remotion/skills/remotion`
  - `temp` `.tmp/plugins/plugins/remotion/skills/remotion`
- `render-debug`: 3 copies
  - `user-installed-skill` `skills/render-debug`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/render/skills/render-debug`
  - `temp` `.tmp/plugins/plugins/render/skills/render-debug`
- `render-deploy`: 4 copies
  - `vendor-import` `vendor_imports/skills/skills/.curated/render-deploy`
  - `user-installed-skill` `skills/render-deploy`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/render/skills/render-deploy`
  - `temp` `.tmp/plugins/plugins/render/skills/render-deploy`
- `render-migrate-from-heroku`: 3 copies
  - `user-installed-skill` `skills/render-migrate-from-heroku`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/render/skills/render-migrate-from-heroku`
  - `temp` `.tmp/plugins/plugins/render/skills/render-migrate-from-heroku`
- `render-monitor`: 3 copies
  - `user-installed-skill` `skills/render-monitor`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/render/skills/render-monitor`
  - `temp` `.tmp/plugins/plugins/render/skills/render-monitor`
- `render-workflows`: 3 copies
  - `user-installed-skill` `skills/render-workflows`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/render/skills/render-workflows`
  - `temp` `.tmp/plugins/plugins/render/skills/render-workflows`
- `requesting-code-review`: 3 copies
  - `user-installed-skill` `skills/requesting-code-review`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/requesting-code-review`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/requesting-code-review`
- `research-router-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/research-router-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/research-router-skill`
- `rhea-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/rhea-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/rhea-skill`
- `rnacentral-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/rnacentral-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/rnacentral-skill`
- `routing-middleware`: 4 copies
  - `user-installed-skill` `skills/routing-middleware`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/routing-middleware`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/routing-middleware`
  - `temp` `.tmp/plugins/plugins/vercel/skills/routing-middleware`
- `runtime-cache`: 4 copies
  - `user-installed-skill` `skills/runtime-cache`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/runtime-cache`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/runtime-cache`
  - `temp` `.tmp/plugins/plugins/vercel/skills/runtime-cache`
- `sandbox-sdk`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/cloudflare/skills/sandbox-sdk`
  - `temp` `.tmp/plugins/plugins/cloudflare/skills/sandbox-sdk`
- `satori`: 4 copies
  - `user-installed-skill` `skills/satori`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/satori`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/satori`
  - `temp` `.tmp/plugins/plugins/vercel/skills/satori`
- `security-scan`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/codex-security/skills/security-scan`
  - `temp` `.tmp/plugins/plugins/codex-security/skills/security-scan`
- `sentry`: 4 copies
  - `vendor-import` `vendor_imports/skills/skills/.curated/sentry`
  - `user-installed-skill` `skills/sentry`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/sentry/skills/sentry`
  - `temp` `.tmp/plugins/plugins/sentry/skills/sentry`
- `shadcn`: 5 copies
  - `user-installed-skill` `skills/shadcn`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/shadcn`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/shadcn`
  - `temp` `.tmp/plugins/plugins/vercel/skills/shadcn`
  - `temp` `.tmp/plugins/plugins/build-web-apps/skills/shadcn-best-practices`
- `sharepoint`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/sharepoint/skills/sharepoint`
  - `temp` `.tmp/plugins/plugins/sharepoint/skills/sharepoint`
- `sharepoint-powerpoint`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/sharepoint/skills/sharepoint-powerpoint`
  - `temp` `.tmp/plugins/plugins/sharepoint/skills/sharepoint-powerpoint`
- `sharepoint-shared-doc-maintenance`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/sharepoint/skills/sharepoint-shared-doc-maintenance`
  - `temp` `.tmp/plugins/plugins/sharepoint/skills/sharepoint-shared-doc-maintenance`
- `sharepoint-site-discovery`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/sharepoint/skills/sharepoint-site-discovery`
  - `temp` `.tmp/plugins/plugins/sharepoint/skills/sharepoint-site-discovery`
- `sharepoint-spreadsheet-formula-builder`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/sharepoint/skills/sharepoint-spreadsheet-formula-builder`
  - `temp` `.tmp/plugins/plugins/sharepoint/skills/sharepoint-spreadsheet-formula-builder`
- `sharepoint-spreadsheets`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/sharepoint/skills/sharepoint-spreadsheets`
  - `temp` `.tmp/plugins/plugins/sharepoint/skills/sharepoint-spreadsheets`
- `sharepoint-word-docs`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/sharepoint/skills/sharepoint-word-docs`
  - `temp` `.tmp/plugins/plugins/sharepoint/skills/sharepoint-word-docs`
- `sign-in-with-vercel`: 4 copies
  - `user-installed-skill` `skills/sign-in-with-vercel`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/sign-in-with-vercel`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/sign-in-with-vercel`
  - `temp` `.tmp/plugins/plugins/vercel/skills/sign-in-with-vercel`
- `slack`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/slack/skills/slack`
  - `temp` `.tmp/plugins/plugins/slack/skills/slack`
- `slack-channel-summarization`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/slack/skills/slack-channel-summarization`
  - `temp` `.tmp/plugins/plugins/slack/skills/slack-channel-summarization`
- `slack-daily-digest`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/slack/skills/slack-daily-digest`
  - `temp` `.tmp/plugins/plugins/slack/skills/slack-daily-digest`
- `slack-notification-triage`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/slack/skills/slack-notification-triage`
  - `temp` `.tmp/plugins/plugins/slack/skills/slack-notification-triage`
- `slack-outgoing-message`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/slack/skills/slack-outgoing-message`
  - `temp` `.tmp/plugins/plugins/slack/skills/slack-outgoing-message`
- `slack-reply-drafting`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/slack/skills/slack-reply-drafting`
  - `temp` `.tmp/plugins/plugins/slack/skills/slack-reply-drafting`
- `sprite-pipeline`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/game-studio/skills/sprite-pipeline`
  - `temp` `.tmp/plugins/plugins/game-studio/skills/sprite-pipeline`
- `string-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/string-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/string-skill`
- `stripe-best-practices`: 4 copies
  - `user-installed-skill` `skills/stripe-best-practices`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/stripe/skills/stripe-best-practices`
  - `temp` `.tmp/plugins/plugins/stripe/skills/stripe-best-practices`
  - `temp` `.tmp/plugins/plugins/build-web-apps/skills/stripe-best-practices`
- `subagent-driven-development`: 3 copies
  - `user-installed-skill` `skills/subagent-driven-development`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/subagent-driven-development`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/subagent-driven-development`
- `supabase`: 3 copies
  - `user-installed-skill` `skills/supabase`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/supabase/skills/supabase`
  - `temp` `.tmp/plugins/plugins/supabase/skills/supabase`
- `supabase-postgres-best-practices`: 4 copies
  - `user-installed-skill` `skills/supabase-postgres-best-practices`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/supabase/skills/supabase-postgres-best-practices`
  - `temp` `.tmp/plugins/plugins/supabase/skills/supabase-postgres-best-practices`
  - `temp` `.tmp/plugins/plugins/build-web-apps/skills/supabase-best-practices`
- `swr`: 4 copies
  - `user-installed-skill` `skills/swr`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/swr`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/swr`
  - `temp` `.tmp/plugins/plugins/vercel/skills/swr`
- `systematic-debugging`: 3 copies
  - `user-installed-skill` `skills/systematic-debugging`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/systematic-debugging`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/systematic-debugging`
- `teams`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/teams/skills/teams`
  - `temp` `.tmp/plugins/plugins/teams/skills/teams`
- `teams-channel-summarization`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/teams/skills/teams-channel-summarization`
  - `temp` `.tmp/plugins/plugins/teams/skills/teams-channel-summarization`
- `teams-daily-digest`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/teams/skills/teams-daily-digest`
  - `temp` `.tmp/plugins/plugins/teams/skills/teams-daily-digest`
- `teams-messages`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/teams/skills/teams-messages`
  - `temp` `.tmp/plugins/plugins/teams/skills/teams-messages`
- `teams-notification-triage`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/teams/skills/teams-notification-triage`
  - `temp` `.tmp/plugins/plugins/teams/skills/teams-notification-triage`
- `teams-planner-task-management`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/teams/skills/teams-planner-task-management`
  - `temp` `.tmp/plugins/plugins/teams/skills/teams-planner-task-management`
- `teams-reply-drafting`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/teams/skills/teams-reply-drafting`
  - `temp` `.tmp/plugins/plugins/teams/skills/teams-reply-drafting`
- `temporal-developer`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/temporal/skills/temporal-developer`
  - `temp` `.tmp/plugins/plugins/temporal/skills/temporal-developer`
- `test-driven-development`: 3 copies
  - `user-installed-skill` `skills/test-driven-development`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/test-driven-development`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/test-driven-development`
- `threat-model`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/codex-security/skills/threat-model`
  - `temp` `.tmp/plugins/plugins/codex-security/skills/threat-model`
- `three-webgl-game`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/game-studio/skills/three-webgl-game`
  - `temp` `.tmp/plugins/plugins/game-studio/skills/three-webgl-game`
- `tpmi-phewas-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/tpmi-phewas-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/tpmi-phewas-skill`
- `transformers-js`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hugging-face/skills/transformers.js`
  - `temp` `.tmp/plugins/plugins/hugging-face/skills/transformers.js`
- `turbopack`: 4 copies
  - `user-installed-skill` `skills/turbopack`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/turbopack`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/turbopack`
  - `temp` `.tmp/plugins/plugins/vercel/skills/turbopack`
- `turborepo`: 4 copies
  - `user-installed-skill` `skills/turborepo`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/turborepo`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/turborepo`
  - `temp` `.tmp/plugins/plugins/vercel/skills/turborepo`
- `twilio-account-setup`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-account-setup`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-account-setup`
- `twilio-agent-augmentation-architect`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-agent-augmentation-architect`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-agent-augmentation-architect`
- `twilio-agent-connect`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-agent-connect`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-agent-connect`
- `twilio-ai-agent-architect`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-ai-agent-architect`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-ai-agent-architect`
- `twilio-call-recordings`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-call-recordings`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-call-recordings`
- `twilio-cli-reference`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-cli-reference`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-cli-reference`
- `twilio-compliance-onboarding`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-compliance-onboarding`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-compliance-onboarding`
- `twilio-compliance-traffic`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-compliance-traffic`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-compliance-traffic`
- `twilio-conference-calls`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-conference-calls`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-conference-calls`
- `twilio-content-template-builder`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-content-template-builder`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-content-template-builder`
- `twilio-conversation-orchestrator`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-conversation-orchestrator`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-conversation-orchestrator`
- `twilio-conversations-classic-api`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-conversations-classic-api`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-conversations-classic-api`
- `twilio-customer-memory`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-customer-memory`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-customer-memory`
- `twilio-customer-support-architect`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-customer-support-architect`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-customer-support-architect`
- `twilio-debugging-observability`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-debugging-observability`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-debugging-observability`
- `twilio-email-deliverability-advisor`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-email-deliverability-advisor`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-email-deliverability-advisor`
- `twilio-email-send`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-email-send`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-email-send`
- `twilio-enterprise-knowledge`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-enterprise-knowledge`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-enterprise-knowledge`
- `twilio-iam-auth-setup`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-iam-auth-setup`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-iam-auth-setup`
- `twilio-identity-verification-advisor`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-identity-verification-advisor`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-identity-verification-advisor`
- `twilio-isv-sms-best-practices`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-sms-isv-setup`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-sms-isv-setup`
- `twilio-lookup-phone-intelligence`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-lookup-phone-intelligence`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-lookup-phone-intelligence`
- `twilio-marketing-promotions-advisor`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-marketing-promotions-advisor`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-marketing-promotions-advisor`
- `twilio-messaging-channel-advisor`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-messaging-channel-advisor`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-messaging-channel-advisor`
- `twilio-messaging-overview`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-messaging-overview`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-messaging-overview`
- `twilio-messaging-services`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-messaging-services`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-messaging-services`
- `twilio-messaging-webhooks`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-messaging-webhooks`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-messaging-webhooks`
- `twilio-notifications-alerts-advisor`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-notifications-alerts-advisor`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-notifications-alerts-advisor`
- `twilio-numbers-senders`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-numbers-senders`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-numbers-senders`
- `twilio-organizations-setup`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-organizations-setup`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-organizations-setup`
- `twilio-rcs-messaging`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-rcs-messaging`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-rcs-messaging`
- `twilio-regulatory-compliance-bundles`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-regulatory-compliance-bundles`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-regulatory-compliance-bundles`
- `twilio-reliability-patterns`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-reliability-patterns`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-reliability-patterns`
- `twilio-security-api-auth`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-security-api-auth`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-security-api-auth`
- `twilio-security-compliance-hipaa`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-security-compliance-hipaa`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-security-compliance-hipaa`
- `twilio-security-hardening`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-security-hardening`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-security-hardening`
- `twilio-send-message`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-send-message`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-send-message`
- `twilio-sendgrid-account-setup`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-sendgrid-account-setup`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-sendgrid-account-setup`
- `twilio-sendgrid-deliverability-advisor`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-sendgrid-deliverability-advisor`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-sendgrid-deliverability-advisor`
- `twilio-sendgrid-email-send`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-sendgrid-email-send`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-sendgrid-email-send`
- `twilio-sendgrid-email-settings`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-sendgrid-email-settings`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-sendgrid-email-settings`
- `twilio-sendgrid-engagement-quality`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-sendgrid-engagement-quality`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-sendgrid-engagement-quality`
- `twilio-sendgrid-inbound-parse`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-sendgrid-inbound-parse`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-sendgrid-inbound-parse`
- `twilio-sendgrid-suppressions`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-sendgrid-suppressions`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-sendgrid-suppressions`
- `twilio-sendgrid-webhooks`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-sendgrid-webhooks`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-sendgrid-webhooks`
- `twilio-sms-send-message`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-sms-send-message`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-sms-send-message`
- `twilio-taskrouter-routing`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-taskrouter-routing`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-taskrouter-routing`
- `twilio-verify-send-otp`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-verify-send-otp`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-verify-send-otp`
- `twilio-voice-conversation-relay`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-voice-conversation-relay`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-voice-conversation-relay`
- `twilio-voice-outbound-calls`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-voice-outbound-calls`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-voice-outbound-calls`
- `twilio-voice-twiml`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-voice-twiml`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-voice-twiml`
- `twilio-webhook-architecture`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-webhook-architecture`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-webhook-architecture`
- `twilio-whatsapp-manage-senders`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-whatsapp-manage-senders`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-whatsapp-manage-senders`
- `twilio-whatsapp-send-message`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/twilio-developer-kit/skills/twilio-whatsapp-send-message`
  - `temp` `.tmp/plugins/plugins/twilio-developer-kit/skills/twilio-whatsapp-send-message`
- `ukb-topmed-phewas-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/ukb-topmed-phewas-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/ukb-topmed-phewas-skill`
- `uniprot-skill`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/life-science-research/skills/uniprot-skill`
  - `temp` `.tmp/plugins/plugins/life-science-research/skills/uniprot-skill`
- `upgrade-stripe`: 3 copies
  - `user-installed-skill` `skills/upgrade-stripe`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/stripe/skills/upgrade-stripe`
  - `temp` `.tmp/plugins/plugins/stripe/skills/upgrade-stripe`
- `upgrading-expo`: 3 copies
  - `user-installed-skill` `skills/upgrading-expo`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/upgrading-expo`
  - `temp` `.tmp/plugins/plugins/expo/skills/upgrading-expo`
- `use-dom`: 3 copies
  - `user-installed-skill` `skills/use-dom`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/expo/skills/use-dom`
  - `temp` `.tmp/plugins/plugins/expo/skills/use-dom`
- `using-git-worktrees`: 3 copies
  - `user-installed-skill` `skills/using-git-worktrees`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/using-git-worktrees`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/using-git-worktrees`
- `using-superpowers`: 3 copies
  - `user-installed-skill` `skills/using-superpowers`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/using-superpowers`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/using-superpowers`
- `v0-dev`: 4 copies
  - `user-installed-skill` `skills/v0-dev`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/v0-dev`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/v0-dev`
  - `temp` `.tmp/plugins/plugins/vercel/skills/v0-dev`
- `validation`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/codex-security/skills/validation`
  - `temp` `.tmp/plugins/plugins/codex-security/skills/validation`
- `vercel-agent`: 4 copies
  - `user-installed-skill` `skills/vercel-agent`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-agent`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/vercel-agent`
  - `temp` `.tmp/plugins/plugins/vercel/skills/vercel-agent`
- `vercel-api`: 4 copies
  - `user-installed-skill` `skills/vercel-api`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-api`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/vercel-api`
  - `temp` `.tmp/plugins/plugins/vercel/skills/vercel-api`
- `vercel-cli`: 4 copies
  - `user-installed-skill` `skills/vercel-cli`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-cli`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/vercel-cli`
  - `temp` `.tmp/plugins/plugins/vercel/skills/vercel-cli`
- `vercel-firewall`: 4 copies
  - `user-installed-skill` `skills/vercel-firewall`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-firewall`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/vercel-firewall`
  - `temp` `.tmp/plugins/plugins/vercel/skills/vercel-firewall`
- `vercel-flags`: 4 copies
  - `user-installed-skill` `skills/vercel-flags`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-flags`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/vercel-flags`
  - `temp` `.tmp/plugins/plugins/vercel/skills/vercel-flags`
- `vercel-functions`: 4 copies
  - `user-installed-skill` `skills/vercel-functions`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-functions`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/vercel-functions`
  - `temp` `.tmp/plugins/plugins/vercel/skills/vercel-functions`
- `vercel-queues`: 4 copies
  - `user-installed-skill` `skills/vercel-queues`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-queues`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/vercel-queues`
  - `temp` `.tmp/plugins/plugins/vercel/skills/vercel-queues`
- `vercel-sandbox`: 4 copies
  - `user-installed-skill` `skills/vercel-sandbox`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-sandbox`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/vercel-sandbox`
  - `temp` `.tmp/plugins/plugins/vercel/skills/vercel-sandbox`
- `vercel-services`: 4 copies
  - `user-installed-skill` `skills/vercel-services`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-services`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/vercel-services`
  - `temp` `.tmp/plugins/plugins/vercel/skills/vercel-services`
- `vercel-storage`: 4 copies
  - `user-installed-skill` `skills/vercel-storage`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/vercel-storage`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/vercel-storage`
  - `temp` `.tmp/plugins/plugins/vercel/skills/vercel-storage`
- `verification`: 4 copies
  - `user-installed-skill` `skills/verification`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/verification`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/verification`
  - `temp` `.tmp/plugins/plugins/vercel/skills/verification`
- `verification-before-completion`: 3 copies
  - `user-installed-skill` `skills/verification-before-completion`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/verification-before-completion`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/verification-before-completion`
- `web-3d-asset-pipeline`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/game-studio/skills/web-3d-asset-pipeline`
  - `temp` `.tmp/plugins/plugins/game-studio/skills/web-3d-asset-pipeline`
- `web-game-foundations`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/game-studio/skills/web-game-foundations`
  - `temp` `.tmp/plugins/plugins/game-studio/skills/web-game-foundations`
- `web-perf`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/cloudflare/skills/web-perf`
  - `temp` `.tmp/plugins/plugins/cloudflare/skills/web-perf`
- `website-to-hyperframes`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/hyperframes/skills/website-to-hyperframes`
  - `temp` `.tmp/plugins/plugins/hyperframes/skills/website-to-hyperframes`
- `workers-best-practices`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/cloudflare/skills/workers-best-practices`
  - `temp` `.tmp/plugins/plugins/cloudflare/skills/workers-best-practices`
- `workflow`: 4 copies
  - `user-installed-skill` `skills/workflow`
  - `plugin-skill` `plugins/cache/openai-curated/vercel/d947469e/skills/workflow`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/vercel/skills/workflow`
  - `temp` `.tmp/plugins/plugins/vercel/skills/workflow`
- `wrangler`: 2 copies
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/cloudflare/skills/wrangler`
  - `temp` `.tmp/plugins/plugins/cloudflare/skills/wrangler`
- `writing-plans`: 3 copies
  - `user-installed-skill` `skills/writing-plans`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/writing-plans`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/writing-plans`
- `writing-skills`: 3 copies
  - `user-installed-skill` `skills/writing-skills`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/superpowers/skills/writing-skills`
  - `temp` `.tmp/plugins/plugins/superpowers/skills/writing-skills`
- `yeet`: 5 copies
  - `vendor-import` `vendor_imports/skills/skills/.curated/yeet`
  - `user-installed-skill` `skills/yeet`
  - `plugin-skill` `plugins/cache/openai-curated/github/d947469e/skills/yeet`
  - `temp` `.tmp/plugins-backup-A3dKVF/repo/plugins/github/skills/yeet`
  - `temp` `.tmp/plugins/plugins/github/skills/yeet`

## Notes

- `user-installed-skill` and `plugin-skill` are treated as concrete installable skills.
- `plugin-cache-other`, `codex-cache`, `vendor-import`, `temp`, `session-artifact`, and `other` are not treated as installable without manual review.
- Codex system skills are excluded by default.
