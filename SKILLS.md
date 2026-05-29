# Skills

1. `actionable-pushback`
   - Source: local-codex-user-skill
   - License: MIT
   - Evidence: Root LICENSE applies to local-authored skill
   - Audit status: root-mit-local
   - Origin: local repository/root MIT license
   - Description: Use when the user may be mistaken, the requested action is risky, evidence is weak or contradictory, requirements conflict, assumptions may be wrong, constraints are hidden, or Codex should respectfully disagree before acting.

2. `agent-browser`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/agent-browser/LICENSE.txt
   - Evidence: Embedded license file: skills/agent-browser/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when the user needs to interact with websites, verify dev server output, test web apps, navigate pages, fill forms, click buttons, take screenshots, extract data, or automate any browser task. Also triggers when a dev server starts so you can verify it visually.

3. `agent-browser-verify`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/agent-browser-verify/LICENSE.txt
   - Evidence: Embedded license file: skills/agent-browser-verify/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when a dev server needs browser verification, screenshots, console checks, or visual regression checks after frontend changes.

4. `agent-memory-context-efficiency`
   - Source: local-codex-user-skill
   - License: MIT
   - Evidence: Root LICENSE applies to local-authored skill
   - Audit status: root-mit-local
   - Origin: local repository/root MIT license
   - Description: Use when improving Luna memory, context retrieval, token usage, command-output handling, shell summaries, long-running agent traces, or comparing Hermes-style memory and ztk-style token compression patterns.

5. `ai-elements`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/ai-elements/LICENSE.txt
   - Evidence: Embedded license file: skills/ai-elements/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when building chat UIs, message displays, tool call rendering, streaming responses, reasoning panels, or any AI-native interface with the AI SDK.

6. `ai-gateway`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/ai-gateway/LICENSE.txt
   - Evidence: Embedded license file: skills/ai-gateway/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when configuring model routing, provider failover, cost tracking, or managing multiple AI providers through a unified API.

7. `ai-generation-persistence`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/ai-generation-persistence/LICENSE.txt
   - Evidence: Embedded license file: skills/ai-generation-persistence/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when AI generations need stable IDs, addressable URLs, database persistence, resumability, or cost tracking.

8. `ai-sdk`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/ai-sdk/LICENSE.txt
   - Evidence: Embedded license file: skills/ai-sdk/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when building AI-powered features — chat interfaces, text generation, structured output, tool calling, agents, MCP integration, streaming, embeddings, reranking, image generation, or working with any LLM provider.

9. `algorithmic-art`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/algorithmic-art/LICENSE.txt
   - Evidence: Embedded license file: skills/algorithmic-art/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/anthropics/skills
   - Description: Use when creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations

10. `android-emulator-qa`
   - Source: test-android-apps plugin backup promoted from temp
   - License: Apache-2.0, see skills/android-emulator-qa/LICENSE.txt
   - Evidence: Embedded license file: skills/android-emulator-qa/LICENSE.txt
   - Audit status: license-file-present
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when validating Android feature flows in an emulator with adb-driven launch, input, UI-tree inspection, screenshots, and logcat capture.

11. `android-performance`
   - Source: test-android-apps plugin backup promoted from temp
   - License: MIT, from test-android-apps plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from test-android-apps plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when asked to profile an Android app flow, find CPU-heavy functions, diagnose jank, capture startup or frame timing evidence, compare before/after performance, explain what code is taking time, or gather memory/leak profiling artifacts.

12. `auth`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/auth/LICENSE.txt
   - Evidence: Embedded license file: skills/auth/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when implementing user authentication.

13. `bootstrap`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/bootstrap/LICENSE.txt
   - Evidence: Embedded license file: skills/bootstrap/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when setting up or repairing a repository so linking, environment provisioning, env pulls, and first-run db/dev commands happen in the correct safe order.

14. `brainstorming`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when starting creative or product work such as new features, components, functionality, designs, or behavior changes.

15. `brand-guidelines`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/brand-guidelines/LICENSE.txt
   - Evidence: Embedded license file: skills/brand-guidelines/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/anthropics/skills
   - Description: Use when applying anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply

16. `building-native-ui`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when building polished native app interfaces with Expo Router, React Native styling, navigation, animations, or platform UI patterns.

17. `canvas-design`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/canvas-design/LICENSE.txt
   - Evidence: Embedded license file: skills/canvas-design/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/anthropics/skills
   - Description: Use when creating beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations

18. `chat-sdk`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/chat-sdk/LICENSE.txt
   - Evidence: Embedded license file: skills/chat-sdk/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when building multi-platform chat bots — Slack, Telegram, Microsoft Teams, Discord, Google Chat, GitHub, Linear — with a single codebase. Covers the Chat class, adapters, threads, messages, cards, modals, streaming, state management, and webhook setup.

19. `claude-api`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/claude-api/LICENSE.txt
   - Evidence: Embedded license file: skills/claude-api/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/anthropics/skills
   - Description: Use when building, debugging, or optimizing Claude API and Anthropic SDK applications.

20. `cms`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/cms/LICENSE.txt
   - Evidence: Embedded license file: skills/cms/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when building content-driven sites with a headless CMS on Vercel.

21. `codex-expo-run-actions`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when the user wants the Codex app Run button, build/run actions, action buttons, or a stable Expo start/run workflow from Codex.

22. `cron-jobs`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/cron-jobs/LICENSE.txt
   - Evidence: Embedded license file: skills/cron-jobs/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when adding, editing, or debugging scheduled tasks in vercel.json.

23. `deployments-cicd`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/deployments-cicd/LICENSE.txt
   - Evidence: Embedded license file: skills/deployments-cicd/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when deploying, promoting, rolling back, inspecting deployments, building with --prebuilt, or configuring CI workflow files for Vercel.

24. `dispatching-parallel-agents`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies

25. `email`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/email/LICENSE.txt
   - Evidence: Embedded license file: skills/email/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when sending emails from a Vercel-deployed application.

26. `env-vars`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/env-vars/LICENSE.txt
   - Evidence: Embedded license file: skills/env-vars/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when working with .env files, vercel env commands, OIDC tokens, or managing environment-specific configuration.

27. `executing-plans`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when you have a written implementation plan to execute in a separate session with review checkpoints

28. `expo-api-routes`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when working on creating API routes in Expo Router with EAS Hosting

29. `expo-cicd-workflows`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when working with expo cicd workflows: Helps understand and write EAS workflow YAML files for Expo projects. Use this skill when the user asks about CI/CD or workflows in an Expo or EAS context, mentions .eas/workflows/, or wants help with EAS build pipelines or deployment automation.

30. `expo-deployment`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when deploying Expo apps to the iOS App Store, Android Play Store, web hosting, or EAS API routes.

31. `expo-dev-client`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when building or distributing Expo development clients locally, with EAS, or through TestFlight.

32. `expo-module`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when building or modifying native modules for Expo.

33. `expo-tailwind-setup`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when setting up tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for universal styling

34. `expo-ui-jetpack-compose`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when adding Jetpack Compose views or modifiers to Expo apps with @expo/ui/jetpack-compose.

35. `expo-ui-swift-ui`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when adding SwiftUI views or modifiers to Expo apps with @expo/ui/swift-ui.

36. `external-design-skill-router`
   - Source: local-codex-user-skill
   - License: MIT
   - Evidence: Root LICENSE applies to local-authored skill
   - Audit status: root-mit-local
   - Origin: local repository/root MIT license
   - Description: Use when working on Luna UI, dashboards, chat interfaces, component quality, visual consistency, style extraction, or frontend polish and you need patterns from Refero, UI Skills, or Impeccable without loading the full catalog into context.

37. `finishing-a-development-branch`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup

38. `frontend-design`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/frontend-design/LICENSE.txt
   - Evidence: Embedded license file: skills/frontend-design/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/anthropics/skills
   - Description: Use when creating distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics

39. `geist`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/geist/LICENSE.txt
   - Evidence: Embedded license file: skills/geist/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when configuring Geist Sans, Geist Mono, or Geist Pixel, setting up font imports, or applying Vercel typography and aesthetic guidance.

40. `geistdocs`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/geistdocs/LICENSE.txt
   - Evidence: Embedded license file: skills/geistdocs/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when creating documentation sites, configuring geistdocs, writing MDX content, or setting up docs infrastructure.

41. `gh-address-comments`
   - Source: github plugin backup promoted from temp
   - License: Apache-2.0, see skills/gh-address-comments/LICENSE.txt
   - Evidence: Embedded license file: skills/gh-address-comments/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/openai/plugins
   - Description: Use when the user wants to inspect unresolved review threads, requested changes, or inline review comments on a PR, then implement selected fixes. Use the GitHub app for PR metadata and flat comment reads, and use the bundled GraphQL script via `gh` whenever thread-level state, resolution status, or inline review context matters.

42. `gh-fix-ci`
   - Source: github plugin backup promoted from temp
   - License: Apache-2.0, see skills/gh-fix-ci/LICENSE.txt
   - Evidence: Embedded license file: skills/gh-fix-ci/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/openai/plugins
   - Description: Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions. Use the GitHub app from this plugin for PR metadata and patch context, and use `gh` for Actions check and log inspection before implementing any approved fix.

43. `github`
   - Source: github plugin backup promoted from temp
   - License: MIT, from github plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from github plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://github.com/openai/plugins
   - Description: Use when the user asks for general GitHub help, wants PR or issue summaries, or needs repository context before choosing a more specific GitHub workflow.

44. `internal-comms`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/internal-comms/LICENSE.txt
   - Evidence: Embedded license file: skills/internal-comms/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/anthropics/skills
   - Description: Use when writing all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.)

45. `investigation-mode`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/investigation-mode/LICENSE.txt
   - Evidence: Embedded license file: skills/investigation-mode/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when debugging stuck, hung, broken, flaky, or confusing behavior that needs systematic investigation.

46. `json-render`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/json-render/LICENSE.txt
   - Evidence: Embedded license file: skills/json-render/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when building custom chat UIs, rendering tool results, or troubleshooting AI response display issues.

47. `marketplace`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/marketplace/LICENSE.txt
   - Evidence: Embedded license file: skills/marketplace/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when consuming third-party services, building custom integrations, or managing marketplace resources on Vercel.

48. `mcp-builder`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/mcp-builder/LICENSE.txt
   - Evidence: Embedded license file: skills/mcp-builder/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/anthropics/skills
   - Description: Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

49. `micro`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/micro/LICENSE.txt
   - Evidence: Embedded license file: skills/micro/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when building lightweight HTTP servers, API endpoints, or microservices using the micro library.

50. `native-data-fetching`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when implementing or debugging ANY network request, API call, or data fetching. Covers fetch API, React Query, SWR, error handling, caching, offline support, and Expo Router data loaders (`useLoaderData`).

51. `ncc`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/ncc/LICENSE.txt
   - Evidence: Embedded license file: skills/ncc/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when bundling serverless functions, CLI tools, or any Node.js project into a self-contained file.'

52. `netlify-ai-gateway`
   - Source: netlify plugin backup promoted from temp
   - License: Apache-2.0, see skills/netlify-ai-gateway/LICENSE.txt
   - Evidence: Embedded license file: skills/netlify-ai-gateway/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.netlify.com
   - Description: Use when adding AI capabilities or selecting/changing AI models. Must be read before choosing a model. Covers supported providers (OpenAI, Anthropic, Google), SDK setup, environment variables, and the list of available models.

53. `netlify-blobs`
   - Source: netlify plugin backup promoted from temp
   - License: Apache-2.0, see skills/netlify-blobs/LICENSE.txt
   - Evidence: Embedded license file: skills/netlify-blobs/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.netlify.com
   - Description: Use when storing files, images, documents, or simple key-value data without a full database. Covers getStore(), CRUD operations, metadata, listing, deploy-scoped vs site-scoped stores, and local development.

54. `netlify-caching`
   - Source: netlify plugin backup promoted from temp
   - License: Apache-2.0, see skills/netlify-caching/LICENSE.txt
   - Evidence: Embedded license file: skills/netlify-caching/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.netlify.com
   - Description: Use when configuring cache headers, setting up stale-while-revalidate, implementing on-demand cache purge, or understanding Netlify's CDN caching behavior. Covers Cache-Control, Netlify-CDN-Cache-Control, cache tags, durable cache, and framework-specific caching patterns.

55. `netlify-cli-and-deploy`
   - Source: netlify plugin backup promoted from temp
   - License: Apache-2.0, see skills/netlify-cli-and-deploy/LICENSE.txt
   - Evidence: Embedded license file: skills/netlify-cli-and-deploy/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.netlify.com
   - Description: Use when installing the CLI, linking sites, deploying (Git-based or manual), managing environment variables, or running local development. Covers netlify dev, netlify deploy, Git vs non-Git workflows, and environment variable management.

56. `netlify-config`
   - Source: netlify plugin backup promoted from temp
   - License: Apache-2.0, see skills/netlify-config/LICENSE.txt
   - Evidence: Embedded license file: skills/netlify-config/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.netlify.com
   - Description: Use when configuring build settings, redirects, rewrites, headers, deploy contexts, environment variables, or any site-level configuration. Covers the complete netlify.toml syntax including redirects with splats/conditions, headers, deploy contexts, functions config, and edge functions config.

57. `netlify-deploy`
   - Source: netlify plugin backup promoted from temp
   - License: Apache-2.0, see skills/netlify-deploy/LICENSE.txt
   - Evidence: Embedded license file: skills/netlify-deploy/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.netlify.com
   - Description: Use when the user wants to link a repo, validate deploy settings, run a deploy, or choose between preview and production flows.

58. `netlify-edge-functions`
   - Source: netlify plugin backup promoted from temp
   - License: Apache-2.0, see skills/netlify-edge-functions/LICENSE.txt
   - Evidence: Embedded license file: skills/netlify-edge-functions/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.netlify.com
   - Description: Use when building middleware, geolocation-based logic, request/response manipulation, authentication checks, A/B testing, or any low-latency edge compute. Covers Deno runtime, context.next() middleware pattern, geolocation, and when to choose edge vs serverless.

59. `netlify-forms`
   - Source: netlify plugin backup promoted from temp
   - License: Apache-2.0, see skills/netlify-forms/LICENSE.txt
   - Evidence: Embedded license file: skills/netlify-forms/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.netlify.com
   - Description: Use when adding contact forms, feedback forms, file upload forms, or any form that should be collected by Netlify. Covers the data-netlify attribute, spam filtering, AJAX submissions, file uploads, notifications, and the submissions API.

60. `netlify-frameworks`
   - Source: netlify plugin backup promoted from temp
   - License: Apache-2.0, see skills/netlify-frameworks/LICENSE.txt
   - Evidence: Embedded license file: skills/netlify-frameworks/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.netlify.com
   - Description: Use when setting up a framework project (Vite/React, Astro, TanStack Start, Next.js, Nuxt, SvelteKit, Remix) for Netlify deployment, configuring adapters or plugins, or troubleshooting framework-specific Netlify integration. Covers what Netlify needs from each framework and how adapters handle server-side rendering.

61. `netlify-functions`
   - Source: netlify plugin backup promoted from temp
   - License: Apache-2.0, see skills/netlify-functions/LICENSE.txt
   - Evidence: Embedded license file: skills/netlify-functions/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.netlify.com
   - Description: Use when creating API endpoints, background processing, scheduled tasks, or any server-side logic using Netlify Functions. Covers modern syntax (default export + Config), TypeScript, path routing, background functions, scheduled functions, streaming, and method routing.

62. `netlify-identity`
   - Source: netlify plugin backup promoted from temp
   - License: Apache-2.0, see skills/netlify-identity/LICENSE.txt
   - Evidence: Embedded license file: skills/netlify-identity/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.netlify.com
   - Description: Use when the task involves authentication, user signups, logins, password recovery, OAuth providers, role-based access control, or protecting routes and functions. Always use `@netlify/identity`. Never use `netlify-identity-widget` or `gotrue-js` — they are deprecated.

63. `netlify-image-cdn`
   - Source: netlify plugin backup promoted from temp
   - License: Apache-2.0, see skills/netlify-image-cdn/LICENSE.txt
   - Evidence: Embedded license file: skills/netlify-image-cdn/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.netlify.com
   - Description: Use when serving optimized images, creating responsive image markup, setting up user-uploaded image pipelines, or configuring image transformations. Covers the /.netlify/images endpoint, query parameters, remote image allowlisting, clean URL rewrites, and composing uploads with Functions + Blobs.

64. `next-forge`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/next-forge/LICENSE.txt
   - Evidence: Embedded license file: skills/next-forge/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when working in a next-forge project, scaffolding with `npx next-forge init`, or editing @repo/* workspace packages.'

65. `nextjs`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/nextjs/LICENSE.txt
   - Evidence: Embedded license file: skills/nextjs/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when building, debugging, or architecting Next.js applications — routing, Server Components, Server Actions, Cache Components, layouts, middleware/proxy, data fetching, rendering strategies, and deployment on Vercel.

66. `notion-knowledge-capture`
   - Source: notion plugin backup promoted from temp
   - License: MIT, see skills/notion-knowledge-capture/LICENSE.txt
   - Evidence: Embedded license file: skills/notion-knowledge-capture/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.notion.so
   - Description: Use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking.

67. `notion-meeting-intelligence`
   - Source: notion plugin backup promoted from temp
   - License: MIT, see skills/notion-meeting-intelligence/LICENSE.txt
   - Evidence: Embedded license file: skills/notion-meeting-intelligence/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.notion.so
   - Description: Use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.

68. `notion-research-documentation`
   - Source: notion plugin backup promoted from temp
   - License: MIT, see skills/notion-research-documentation/LICENSE.txt
   - Evidence: Embedded license file: skills/notion-research-documentation/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.notion.so
   - Description: Use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.

69. `notion-spec-to-implementation`
   - Source: notion plugin backup promoted from temp
   - License: MIT, see skills/notion-spec-to-implementation/LICENSE.txt
   - Evidence: Embedded license file: skills/notion-spec-to-implementation/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://www.notion.so
   - Description: Use when implementing PRDs/feature specs and creating Notion plans + tasks from them.

70. `observability`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/observability/LICENSE.txt
   - Evidence: Embedded license file: skills/observability/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when instrumenting, debugging, or optimizing application performance and user experience on Vercel.

71. `payments`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/payments/LICENSE.txt
   - Evidence: Embedded license file: skills/payments/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when implementing payments, subscriptions, or processing transactions.

72. `react-best-practices`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/react-best-practices/LICENSE.txt
   - Evidence: Embedded license file: skills/react-best-practices/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when reviewing or editing multiple React TSX components for correctness, hooks usage, composition, rendering, or maintainability.

73. `receiving-code-review`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation

74. `render-debug`
   - Source: render plugin backup promoted from temp
   - License: MIT, from render plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from render plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://render.com
   - Description: Use when deployments fail, services won't start, or users mention errors, logs, or debugging.

75. `render-deploy`
   - Source: render plugin backup promoted from temp
   - License: MIT, from render plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from render plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://render.com
   - Description: Use when the user wants to deploy, host, publish, or set up their application on Render's cloud platform.

76. `render-migrate-from-heroku`
   - Source: render plugin backup promoted from temp
   - License: MIT, from render plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from render plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://render.com
   - Description: Use when migrating from Heroku to Render by reading local project files and generating equivalent Render services. Triggers: any mention of migrating from Heroku, moving off Heroku, Heroku to Render migration, or switching from Heroku. Reads Procfile, dependency files, and app config from the local repo. Optionally uses Heroku MCP to enrich with live config vars, add-on details, and dyno sizes. Uses Render MCP or Blueprint YAML to create services

77. `render-monitor`
   - Source: render plugin backup promoted from temp
   - License: MIT, from render plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from render plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://render.com
   - Description: Use when users want to check service status, view metrics, monitor performance, or verify deployments are healthy.

78. `render-workflows`
   - Source: render plugin backup promoted from temp
   - License: MIT, from render plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from render plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://render.com
   - Description: Use when a user wants to set up Render Workflows for the first time, scaffold a workflow service, add or modify workflow tasks, test workflows locally, or deploy workflows to Render.

79. `requesting-code-review`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when completing tasks, implementing major features, or before merging to verify work meets requirements

80. `routing-middleware`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/routing-middleware/LICENSE.txt
   - Evidence: Embedded license file: skills/routing-middleware/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when intercepting requests at the platform level.

81. `runtime-cache`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/runtime-cache/LICENSE.txt
   - Evidence: Embedded license file: skills/runtime-cache/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when implementing caching strategies beyond framework-level caching.

82. `satori`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/satori/LICENSE.txt
   - Evidence: Embedded license file: skills/satori/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when working with Satori — Vercel's library that converts HTML and CSS to SVG, commonly used to generate dynamic OG images for Next.js and other frameworks.

83. `sentry`
   - Source: sentry plugin backup promoted from temp
   - License: Apache-2.0, see skills/sentry/LICENSE.txt
   - Evidence: Embedded license file: skills/sentry/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://sentry.io
   - Description: Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry API; perform read-only queries with the bundled script and require `SENTRY_AUTH_TOKEN`.

84. `shadcn`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/shadcn/LICENSE.txt
   - Evidence: Embedded license file: skills/shadcn/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when initializing shadcn, adding components, composing product UI, building custom registries, configuring themes, or troubleshooting component issues.

85. `sign-in-with-vercel`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/sign-in-with-vercel/LICENSE.txt
   - Evidence: Embedded license file: skills/sign-in-with-vercel/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when implementing user login with Vercel as the identity provider.

86. `slack-gif-creator`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/slack-gif-creator/LICENSE.txt
   - Evidence: Embedded license file: skills/slack-gif-creator/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/anthropics/skills
   - Description: Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack.

87. `stripe-best-practices`
   - Source: stripe plugin backup promoted from temp
   - License: MIT, from stripe plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from stripe plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://stripe.com
   - Description: Use when building, modifying, or reviewing any Stripe integration — including accepting payments, building marketplaces, integrating Stripe, processing payments, setting up subscriptions, or creating connected accounts.

88. `subagent-driven-development`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when executing implementation plans with independent tasks in the current session

89. `supabase`
   - Source: supabase plugin backup promoted from temp
   - License: MIT, from supabase plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from supabase plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://supabase.com
   - Description: Use when doing ANY task involving Supabase. Triggers: Supabase products (Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues); client libraries and SSR integrations (supabase-js, @supabase/ssr) in Next.js, React, SvelteKit, Astro, Remix; auth issues (login, logout, sessions, JWT, cookies, getSession, getUser, getClaims, RLS); Supabase CLI or MCP server; schema changes, migrations, security audits, Postgres extensions (pg_graphql, pg_cron, pg_vector).

90. `supabase-postgres-best-practices`
   - Source: supabase plugin backup promoted from temp
   - License: MIT, from supabase plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from supabase plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://supabase.com
   - Description: Use when writing, reviewing, or optimizing Supabase Postgres queries, schemas, indexes, RLS policies, or database performance.

91. `swr`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/swr/LICENSE.txt
   - Evidence: Embedded license file: skills/swr/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when building React apps with client-side data fetching, caching, revalidation, mutations, optimistic UI, pagination, or infinite loading using the SWR library.

92. `systematic-debugging`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes

93. `test-driven-development`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when implementing any feature or bugfix, before writing implementation code

94. `theme-factory`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/theme-factory/LICENSE.txt
   - Evidence: Embedded license file: skills/theme-factory/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/anthropics/skills
   - Description: Use when working on styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.

95. `turbopack`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/turbopack/LICENSE.txt
   - Evidence: Embedded license file: skills/turbopack/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when configuring the Next.js bundler, optimizing HMR, debugging build issues, or understanding the Turbopack vs Webpack differences.

96. `turborepo`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/turborepo/LICENSE.txt
   - Evidence: Embedded license file: skills/turborepo/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when setting up or optimizing monorepo builds, configuring task caching, remote caching, parallel execution, or the --affected flag for incremental CI.

97. `upgrade-stripe`
   - Source: stripe plugin backup promoted from temp
   - License: MIT, from stripe plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from stripe plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://stripe.com
   - Description: Use when upgrading Stripe API versions, SDK versions, webhook versions, or integration patterns.

98. `upgrading-expo`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when working on upgrading Expo SDK versions and fixing dependency issues

99. `use-dom`
   - Source: expo plugin backup promoted from temp
   - License: MIT, from expo plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from expo plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: https://expo.dev
   - Description: Use when migrating web code into Expo DOM components, embedding web experiences in native apps, or sharing web UI across native and web.

100. `using-git-worktrees`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback

101. `using-superpowers`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions

102. `v0-dev`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/v0-dev/LICENSE.txt
   - Evidence: Embedded license file: skills/v0-dev/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when discussing AI code generation, generating UI components from prompts, v0 CLI usage, v0 SDK/API integration, or integrating v0 into development workflows with GitHub and Vercel deployment.

103. `vercel-agent`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/vercel-agent/LICENSE.txt
   - Evidence: Embedded license file: skills/vercel-agent/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when configuring or understanding Vercel's AI development tools.

104. `vercel-api`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/vercel-api/LICENSE.txt
   - Evidence: Embedded license file: skills/vercel-api/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when the agent needs live access to Vercel projects, deployments, environment variables, domains, logs, or documentation through the connected Vercel app or REST API.

105. `vercel-cli`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/vercel-cli/LICENSE.txt
   - Evidence: Embedded license file: skills/vercel-cli/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when deploying, managing environment variables, linking projects, viewing logs, managing domains, or interacting with the Vercel platform from the command line.

106. `vercel-firewall`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/vercel-firewall/LICENSE.txt
   - Evidence: Embedded license file: skills/vercel-firewall/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when configuring DDoS protection, WAF rules, rate limiting, bot filtering, IP allow/block lists, OWASP rulesets, Attack Challenge Mode, or any security configuration on the Vercel platform.

107. `vercel-flags`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/vercel-flags/LICENSE.txt
   - Evidence: Embedded license file: skills/vercel-flags/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when implementing feature flags, experimentation, or staged rollouts.

108. `vercel-functions`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/vercel-functions/LICENSE.txt
   - Evidence: Embedded license file: skills/vercel-functions/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when configuring, debugging, or optimizing server-side code running on Vercel.

109. `vercel-queues`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/vercel-queues/LICENSE.txt
   - Evidence: Embedded license file: skills/vercel-queues/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when building async processing, fan-out patterns, or event-driven architectures.

110. `vercel-sandbox`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/vercel-sandbox/LICENSE.txt
   - Evidence: Embedded license file: skills/vercel-sandbox/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when executing user-generated or AI-generated code in isolation.

111. `vercel-services`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/vercel-services/LICENSE.txt
   - Evidence: Embedded license file: skills/vercel-services/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when working with Vercel Services — deploy multiple services within a single Vercel project. Use for monorepo layouts or when combining a backend (Python, Go) with a frontend (Next.js, Vite) in one deployment

112. `vercel-storage`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/vercel-storage/LICENSE.txt
   - Evidence: Embedded license file: skills/vercel-storage/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when choosing, configuring, or using data storage with Vercel applications.

113. `verification`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/verification/LICENSE.txt
   - Evidence: Embedded license file: skills/verification/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when verifying the full user-facing flow end-to-end across browser, API, database, deployment, or telemetry layers.

114. `verification-before-completion`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always

115. `web-artifacts-builder`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/web-artifacts-builder/LICENSE.txt
   - Evidence: Embedded license file: skills/web-artifacts-builder/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/anthropics/skills
   - Description: Use when creating elaborate multi-component HTML artifacts with modern frontend tooling, rich interactions, or generated visual experiences.

116. `webapp-testing`
   - Source: anthropics/skills example skill
   - License: Apache-2.0, see skills/webapp-testing/LICENSE.txt
   - Evidence: Embedded license file: skills/webapp-testing/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/anthropics/skills
   - Description: Use when testing local web applications with Playwright, browser automation, screenshots, console logs, or interaction checks.

117. `workflow`
   - Source: vercel/vercel-plugin skill
   - License: Apache-2.0, see skills/workflow/LICENSE.txt
   - Evidence: Embedded license file: skills/workflow/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/vercel/vercel-plugin
   - Description: Use when building durable workflows, long-running tasks, API routes or agents that need pause/resume, retries, step-based execution, or crash-safe orchestration with Vercel Workflow.

118. `writing-plans`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when you have a spec or requirements for a multi-step task, before touching code

119. `writing-skills`
   - Source: superpowers plugin backup promoted from temp
   - License: MIT, from superpowers plugin metadata
   - Evidence: Metadata only from prior manifest/source audit: MIT, from superpowers plugin metadata
   - Audit status: metadata-only-needs-upstream-license-file
   - Origin: local plugin-backup temp promotion; original upstream ref not captured
   - Description: Use when creating new skills, editing existing skills, or verifying skills work before deployment

120. `yeet`
   - Source: github plugin backup promoted from temp
   - License: Apache-2.0, see skills/yeet/LICENSE.txt
   - Evidence: Embedded license file: skills/yeet/LICENSE.txt
   - Audit status: license-file-present
   - Origin: https://github.com/openai/plugins
   - Description: Use when publishing local changes to GitHub by checking scope, committing intentionally, pushing a branch, or opening a draft PR.
