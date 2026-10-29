# Start Action

1. Read current-feature.md and verify Goals are populated.
   If empty, error: "Run /feature load first".
2. Read the spec file named in Notes, if there is one.
3. **Propose a plan and stop:** the files you expect to create or change, the order,
   how each goal will be verified (test, typecheck, or browser check), and any
   ambiguity left in the spec. Wait for approval.
4. After approval, set Status to "In Progress".
5. Full mode: create and check out the feature branch (`feature/<slug>` from the H1).
   Lite mode: stay on the current branch.
6. Implement the goals one by one. After each goal, run the project's lint/typecheck
   (and tests, if the goal touches tested logic) from `CLAUDE.md`, and fix failures
   before moving on.
7. When done, list each goal with how it was verified, then suggest `/feature review`.
