# Review Action

1. Read current-feature.md and the spec it points to, to understand the goals and
   acceptance criteria.
2. Review all code changes made for this feature (find them as in
   [explain.md](explain.md): `git diff <default>` in full mode; uncommitted changes plus
   untracked files in lite mode).
3. Run the checks from `CLAUDE.md` (lint, typecheck, test) rather than trusting earlier
   runs.
4. Check for:
   - ✅ Goals met — and how each was verified
   - ❌ Goals missing or incomplete
   - ⚠️ Code quality issues or bugs
   - 🚫 Scope creep (code beyond goals)
5. Final verdict: Ready to complete or needs changes.
