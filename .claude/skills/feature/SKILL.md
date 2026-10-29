---
name: feature
description: Spec-driven feature workflow - kickoff a new project, generate or load specs, then start, test, review, explain and complete each feature
argument-hint: kickoff [lite]|generate|load|start|test|review|explain|complete
---

# Feature Workflow

Manages a project from kickoff, and each feature from spec to merge.

## Working Files

@context/current-feature.md

- `context/current-feature.md` — the one feature in flight right now. Kept small; it is
  loaded on every session.
- `context/HISTORY.md` — append-only log of completed features. Not loaded by default;
  read it only when you need past decisions.
- `context/features/` — spec files (full mode).
- `context/SPEC.md` — the single spec (lite mode).

### current-feature.md structure

- `# Current Feature` - H1 heading with feature name when active
- `## Status` - Not Started | In Progress | Complete
- `## Goals` - Bullet points of what success looks like
- `## Notes` - Additional context, constraints, or details from spec

## Workflow mode

`CLAUDE.md` states **Workflow mode: full** or **lite**. If it says neither, use full.

- **full:** a branch per feature, merged into the default branch on complete.
- **lite:** no branches. Work on the current branch, one commit per slice, tick the slice
  in `context/SPEC.md` on complete. Never push in lite mode unless asked.

**Default branch:** whatever the repo uses (`main`, `master`, ...). Find it with
`git symbolic-ref --short refs/remotes/origin/HEAD` (strip `origin/`), or, with no
remote, `git config init.defaultBranch` or the branch the first commit is on. In the
action files, `<default>` means that branch.

## Task

Execute the requested action: $ARGUMENTS

| Action | Description |
|--------|-------------|
| `kickoff` | Start a project from an assignment: questions, stack, scaffold, checks, context files. `kickoff lite` for interviews/time boxes |
| `generate` | Draft spec files for a ROADMAP phase (full mode) |
| `load` | Load a spec, a lite slice, or an inline description into current-feature.md |
| `start` | Propose a plan, then (after approval) branch and implement |
| `test` | Write and run unit tests for the feature's logic |
| `review` | Check goals met, code quality, scope creep |
| `explain` | Document what changed and why, file by file |
| `complete` | Run checks, commit, merge (full) or tick slice (lite), log to HISTORY |

See [actions/](actions/) for detailed instructions. Read the matching action file before
doing anything.

If no action provided, explain the available options.
