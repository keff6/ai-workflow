# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENTS.md

## <Project Name>

<!-- One or two sentences: what this project is and who it's for. -->

## Context Files

Read the following to get the full context of the project:

- @context/project-overview.md   <!-- PRD-style summary: goals, non-goals, scope. Write this per project. -->
- @context/coding-standards.md
- @context/ai-interaction.md
- @context/current-feature.md

## Commands

```bash
# npm run dev      # <fill in: start dev server>
# npm run build     # <fill in: production build>
# npm run lint       # <fill in: lint>
# npm test              # <fill in: test runner, or remove if none configured yet>
```

## Stack

<!-- List the real stack once decided, e.g.:
- Next.js 16 (App Router) — breaking changes vs. older training data, read the docs before writing framework-specific code
- TypeScript 5
- <ORM/DB>
- <styling>
-->

## Architecture

<!-- Where things live: routing convention, component layout, server/client boundary rules. -->

**IMPORTANT:** Do not add Claude to commit messages

## Database

<!-- Provider, project/branch identifiers if using a hosted DB (Neon, PlanetScale, Supabase, etc.), which
     branch/environment to target by default when using DB-related MCP tools. -->

## Deployment

<!-- Target platform and any pre-deploy steps (e.g. run migrations before the app starts). -->
