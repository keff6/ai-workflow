# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

<!-- New project? Run `/feature kickoff <assignment>` (or `/feature kickoff lite ...` for
     a time-boxed test) and it will fill this file in. Delete sections that don't apply. -->

@AGENTS.md

## <Project Name>

<!-- One or two sentences: what this project is and who it's for. -->

**Workflow mode:** full <!-- full | lite — see .claude/skills/feature/SKILL.md -->

## Context Files

Read the following to get the full context of the project:

- @context/project-overview.md   <!-- full mode: PRD-style summary. Lite mode: replace with @context/SPEC.md -->
- @context/coding-standards.md
- @context/ai-interaction.md
- @context/current-feature.md

Not loaded by default: `context/HISTORY.md` (past features and why), `context/ROADMAP.md`.

## Commands

<!-- Only commands that have actually been run and work. Claude uses these to check its own work. -->

```bash
# npm run dev        # <fill in: start dev server>
# npm run build      # <fill in: production build>
# npm run lint       # <fill in: lint>
# npm run typecheck  # <fill in: e.g. tsc --noEmit>
# npm test           # <fill in: test runner>
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

## Database

<!-- Provider, project/branch identifiers if using a hosted DB (Neon, PlanetScale, Supabase, etc.), which
     branch/environment to target by default when using DB-related MCP tools. -->

## Deployment

<!-- Target platform and any pre-deploy steps (e.g. run migrations before the app starts). -->

## Git

**IMPORTANT:** Do not add Claude attribution or co-author lines to commit messages.
