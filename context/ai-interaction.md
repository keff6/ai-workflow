# AI Interaction Guidelines

## Communication

- Be concise and direct
- Explain non-obvious decisions briefly
- Ask before large refactors or architectural changes
- Don't add features not in the project spec
- Never delete files without clarification

## Workflow

This is the common workflow that we will use for every single feature/fix
(the `/feature` skill runs these steps):

1. **Document** - Load the spec into @context/current-feature.md (`/feature load`).
2. **Plan** - Propose a plan and wait for approval (`/feature start`).
3. **Branch** - Full mode: new branch per feature/fix. Lite mode: stay on the current branch.
4. **Implement** - Implement the goals one by one. Run lint/typecheck after each one.
5. **Test** - Write unit tests for new logic (`/feature test`). Verify UI in the browser.
   Run the build and fix any errors.
6. **Review** - Check goals, quality and scope creep (`/feature review`).
7. **Commit** - Only after checks pass and with permission, never auto commit (`/feature complete`).
8. **Merge** - Full mode: merge into the default branch (`main`/`master`) and delete the branch. Lite mode: skip.
9. **Log** - Full mode: add to `context/HISTORY.md`. Lite mode: tick the slice in `context/SPEC.md`.

Do NOT commit without permission and until the checks pass. If they fail, fix the issues first.

## Lite mode (time-boxed work)

When `CLAUDE.md` says **Workflow mode: lite**:

- Keep the time box in mind. Before starting a slice, say if it risks not fitting.
- Prefer the simplest thing that meets the acceptance criteria; note shortcuts in the
  SPEC.md Decisions log instead of polishing.
- Working software at every commit beats a half-finished bigger feature.

## Branching

Full mode: a new branch for every feature/fix, named **feature/[feature]** or
**fix/[fix]**. Ask to delete the branch once merged.

## Commits

- Ask before committing (don't auto-commit)
- Stage files by name; never `git add -A` or `git add .`
- Use conventional commit messages (feat:, fix:, chore:, etc.)
- Keep commits focused (one feature/fix/slice per commit)
- Never put "Generated With Claude" or co-author lines in commit messages

## When Stuck

- If something isn't working after 2-3 attempts, stop and explain the issue
- Don't keep trying random fixes
- Ask for clarification if requirements are unclear

## Code Changes

- Make minimal changes to accomplish the task
- Don't refactor unrelated code unless asked
- Don't add "nice to have" features
- Preserve existing patterns in the codebase

## Code Review

Review AI-generated code periodically, especially for:

- Security (auth checks, input validation)
- Performance (unnecessary re-renders, N+1 queries)
- Logic errors (edge cases)
- Patterns (matches existing codebase?)
