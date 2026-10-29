# PRD: <Project Name>

**Status:** Draft
**Owner:** <you>
**Last updated:** <date>

---

## 1. Summary

<One or two sentences: what this system does and who it's for.>

## 2. Problem statement

<What's broken or missing without this, in concrete terms.>

## 3. Goals

- ...

## 4. Non-goals (explicitly out of scope for v1)

- ...

## 5. Target user

<Who this is built for — one person, a team, the public. This shapes how much
"security boundary" auth needs to be vs. a convenience gate.>

## 6. Scope / Feature list

| Area | Description | Auth required |
|---|---|---|
| ... | ... | ... |

## 7. User stories

- As a <user>, I can <do X> so that <outcome>.

## 8. Functional requirements

<Broken out by feature area, as detailed as needed for specs to be written against it.>

## 9. Data model (summary)

<High-level entities and relationships; point at the actual schema file as source of truth.>

## 10. Non-functional requirements

- **Stack:** <fill in — this should match CLAUDE.md's Stack section>
- **Performance:** <any real target, or explicitly "none, at this scale">
- **Accessibility:** <bar, if any>
- **Deployment:** <target platform>

## 11. Success criteria

<How you'll know v1 is done — concrete and checkable, not aspirational.>

## 12. Open questions

<Track unresolved decisions here; strike them through with a resolution note once
settled, rather than deleting — it's useful history for later.>

## 13. Milestones

See `ROADMAP.md` for the full phased task breakdown.

## 14. References

- `CLAUDE.md` — repo conventions and stack
- `ROADMAP.md` — phased task breakdown
- `SPEC_TEMPLATE.md` — spec format for individual features
- `context/features/*.md` — per-feature implementation specs
- `context/HISTORY.md` — completed features and why
