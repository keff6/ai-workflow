# Kickoff Action

Takes a project from "here is the assignment" to "scaffolded, checks running, context
files written". Run it once, at the start of a project. Two modes:

- **full** (default): writes the PRD, coding standards and a phased ROADMAP. For real
  projects that will last weeks.
- **lite**: writes a single `context/SPEC.md`. For time-boxed work — interview take-homes,
  live coding tests, spikes. Usage: `/feature kickoff lite <assignment>`.

Stop at every **STOP** below and wait for the user. Do not batch past a STOP, even if the
answers seem obvious: in an interview the user may need to check them with the interviewer.

## 0. Check where you are

- Read $ARGUMENTS after "kickoff". If it starts with `lite`, use lite mode; strip the word.
- Look at the current directory:
  - **Empty (or only this kit's files):** you will scaffold in step 4.
  - **Existing project** (`package.json`, `pyproject.toml`, `go.mod`, etc.): skip
    scaffolding, but still do steps 1–3 and 5–6 against the real code.
- If `CLAUDE.md` or the context files already contain real (non-placeholder) content,
  stop and ask before overwriting anything.

## 1. Get the assignment

- If the remaining arguments name a file, read it. If they are text, use that.
- If there is nothing, ask the user to paste the assignment. **STOP.**

## 2. Understand it — STOP for answers

Reply with, in this order:

1. **Restatement:** the problem in 3–5 lines, in your own words.
2. **Requirements found:** a numbered list of every explicit requirement.
3. **Ambiguities and questions:** at most 5, most important first. For each, give the
   assumption you would make if nobody answers, so the user can just say "go with your
   assumptions".
4. **Lite only:** ask how much time is available, if the assignment doesn't say.

**STOP.** Wait for answers before going on.

## 3. Propose stack and slices — STOP for approval

- **Stack:** if the assignment or user fixes it, use that. Otherwise recommend one, with a
  one-line reason tied to *this* assignment and one alternative you considered. Prefer
  the boring, well-known option; in an interview, prefer what the user knows best.
- **Slices:** break the work into vertical slices, each one demoable end to end (data →
  logic → UI), ordered so the most important requirement works first.
  - Lite: 3–6 slices that fit the time box, with a rough time each. Mark which are
    "must" and which are "if time".
  - Full: group slices into phases (Phase 0 = foundation).
- **Test plan:** what will be tested automatically (usually the core logic) and how.

**STOP.** Wait for approval or changes.

## 4. Scaffold (empty directory only)

- Use the official generator, non-interactively, into the current directory (e.g.
  `npx create-next-app@latest . --ts --eslint --app --use-npm --yes`, `npm create vite@latest`,
  `uv init`). Check the generator's current flags with `--help` rather than guessing.
  Never hand-write boilerplate a generator produces.
- If the generator refuses a non-empty directory, scaffold into a temp folder and move the
  files in, without overwriting this kit's files.
- `git init` if needed.

## 5. Build the feedback loop

The goal is that Claude can check its own work from the first feature on.

- Make sure there are working commands for: dev, build, lint, typecheck, test.
- If there is no test runner, propose the standard one for the stack (e.g. Vitest for
  Vite/Next) and install it after the user agrees; add one trivial passing test.
- Run each command once. Record the exact commands that work. Fix anything broken now,
  not later.
- Check installed major versions of the main framework. If one is likely newer than your
  training data, fill in the warning block in `AGENTS.md`.

## 6. Write the context

Fill in `CLAUDE.md` in both modes:
- Project name and a one-line description.
- **Workflow mode:** `full` or `lite`.
- The verified commands from step 5 (uncommented).
- The real stack with versions, and the architecture you expect (where things will live).
- Delete sections that don't apply (e.g. Database, Deployment) instead of leaving placeholders.

**Full mode**, also:
- `context/project-overview.md` — fill from steps 2–3. Put unanswered questions under
  Open questions, with the assumption taken.
- `context/coding-standards.md` — only conventions actually decided; delete the rest.
- `context/ROADMAP.md` — phases and slices from step 3. Spec files themselves come later
  via `/feature generate`.

**Lite mode**, also write `context/SPEC.md`:

```markdown
# Spec: <project name>

**Time box:** <e.g. 90 min> · **Started:** <time>

## Goal
<1–2 sentences>

## Requirements
1. <from the assignment, numbered>

## Assumptions
- <every question that wasn't answered, with the assumption taken>

## Out of scope
- <what we are deliberately not doing>

## Acceptance criteria
- [ ] <checkable statements, linked to requirement numbers>

## Slices
- [ ] 1. <slice> (must, ~20 min)
- [ ] 2. <slice> (must, ~20 min)
- [ ] 3. <slice> (if time)

## Decisions log
- <decision> — <why> (append as you go; this becomes the README's "Decisions" section)
```

In `CLAUDE.md`'s Context Files list, replace `@context/project-overview.md` with
`@context/SPEC.md` so the spec loads on every session.

Do not delete the unused full-mode templates in lite mode; just say they aren't used.

## 7. Commit and hand over

- Show `git status`, propose the commit `chore: scaffold project and add AI context`, and
  ask before committing (per `ai-interaction.md`).
- End with: the stack, the verified commands, and the next step:
  - Full: `/feature generate phase-0`.
  - Lite: `/feature load slice 1`.
