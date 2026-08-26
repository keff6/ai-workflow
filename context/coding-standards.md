# Coding Standards

<!--
  Skeleton carried over from real project use. Fill in the bracketed prompts with
  this project's actual conventions — delete sections that don't apply (e.g. no
  "Styling" section for a backend-only service), add sections this stack needs that
  aren't listed here (e.g. "Concurrency", "CLI/Args").
-->

## Language

- [ ] Type-checking mode (strict? loose?) and how strict
- [ ] Rules on `any` / untyped escape hatches
- [ ] Where types/interfaces for data models, API payloads, props live

## Framework conventions

- [ ] Component/module style (functional vs. class, hooks vs. other state patterns, etc.)
- [ ] Where business logic lives vs. where UI/presentation logic lives
- [ ] When to reach for a heavier tool (e.g. an API route) vs. the framework's lighter default

## File organization

- [ ] Directory layout convention (feature folders? layer folders?)
- [ ] Naming: components, files, functions, constants, types

## Styling

- [ ] Styling approach (CSS framework, CSS-in-JS, design tokens) and where theme
      config lives
- [ ] Any version-specific gotchas (e.g. "this major version moved config from JS to CSS")

## Data / validation

- [ ] ORM/query layer conventions
- [ ] Migration workflow (e.g. always use the dev-migration command, never push
      schema changes directly)
- [ ] Input validation approach and where schemas live

## Error handling

- [ ] Standard error/result shape for actions or API responses
- [ ] How user-facing error messages get surfaced

## Code quality

- [ ] No commented-out code / no unused imports — call out if this differs from defaults
- [ ] Function/file size guidance if any
