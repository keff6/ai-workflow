# AGENTS.md

Use this file for short, load-bearing warnings Claude should see on every session —
things that would otherwise cause it to write code against stale training data (most
commonly: a dependency with recent breaking changes). Keep it short; anything longer
belongs in `context/coding-standards.md` or `context/project-overview.md`. Leave this
file mostly empty until something actually needs flagging.

**Example pattern** — copy this block (uncommented, filled in) when a dependency in
this project has shipped breaking changes recent enough that Claude's training data
won't reflect them:

```markdown
<!-- BEGIN:framework-agent-rules -->
# This is NOT the <Framework> you know

This version has breaking changes — APIs, conventions, and file structure may all
differ from your training data. Read the relevant guide in
`node_modules/<package>/docs/` (or the official docs) before writing any code.
Heed deprecation notices.
<!-- END:framework-agent-rules -->
```
