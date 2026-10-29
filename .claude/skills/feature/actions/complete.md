# Complete Action

1. **Run the checks** from `CLAUDE.md` (lint, typecheck, build, test). If any fail,
   stop and report — do not commit.
2. **Show what will be committed:** run `git status`. Stage only files that belong to
   this feature, by name — never `git add -A` / `git add .`. Point out any unexpected
   files (env files, logs, build output, scratch files) and leave them unstaged.
3. **Ask before committing.** Propose a conventional commit message
   (`feat: ...`, `fix: ...`) and wait for a yes.
4. Commit.

**Full mode:**

5. Switch to the default branch (see SKILL.md) and merge the feature branch (no push yet). Delete the local branch.
6. Append the feature summary to the END of `context/HISTORY.md` (create it if missing):
   date, feature name, what changed, why, and any confirmed deviations from the spec.
7. Reset current-feature.md: H1 back to `# Current Feature`, Status `Not Started`,
   clear Goals and Notes.
8. Commit: `chore: log [feature] in HISTORY and reset current-feature.md`.
9. Ask before pushing. On yes, push the default branch once; if the feature branch was pushed
   earlier, delete it from origin.

**Lite mode:**

5. Tick the slice in `context/SPEC.md` and append any decisions made to its
   Decisions log. Reset current-feature.md as in full mode. Include these edits in the
   slice commit (amend only if the user agrees) or a small `chore:` commit.
6. Do not merge, delete branches or push. Suggest the next slice.
