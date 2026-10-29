# <Project Name> — Roadmap

Spec-driven workflow: every task below gets its own file in `context/features/`, written
*before* any code is touched. Claude Code implements against the spec, not against a
chat message. Use `SPEC_TEMPLATE.md` to write each one, or run `/feature generate
<phase>` to have Claude draft them from this roadmap.

Naming convention: `context/features/<phase>-<slug>.md`, e.g. `context/features/01-navbar-layout.md`.
Load one with `/feature load 01-navbar-layout` (or just `navbar-layout`).

---

## Phase 0 — Foundation

<!-- Goal: whatever needs to exist before any feature work can start — data layer,
     base app shell, auth scaffolding if everything downstream needs it. -->

- [ ] `00-<slug>.md` — ...

**Exit criteria:** <what "done" looks like for this phase, concretely checkable>

---

## Phase 1 — <name>

<!-- Repeat this block per phase. Keep each phase small enough to demo on its own. -->

- [ ] `0N-<slug>.md` — ...

**Exit criteria:** ...

---

## Why this order

<!-- Explain the sequencing logic once specs exist — what blocks what, and why
     pulling something forward or pushing it back would cause rework. This section
     is worth keeping honest and current: it's what future-you (or a reviewer) will
     read to understand *why* the phases are ordered this way, not just what they are. -->

## Decisions locked in

<!-- Cross-cutting decisions made during planning that specs downstream depend on
     (e.g. "auth uses provider X", "a field was added via migration Y"). Update as
     decisions get made — don't let this silently go stale once specs move ahead of it. -->

## Still open

<!-- Small decisions deliberately deferred to individual specs, tracked here so
     they don't get lost. Move items out once resolved (with a note on where they
     were resolved), rather than deleting them. -->
