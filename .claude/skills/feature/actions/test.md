# Test Action

1. Read current-feature.md to understand what was implemented.
2. Identify the logic added or modified for this feature: server actions, API handlers,
   utilities, data transformations, validation.
3. Check if tests already exist for these.
4. For logic without tests, write unit tests:
   - Use the project's test runner (see `CLAUDE.md`). If there is none, propose one and
     stop for approval instead of installing it silently.
   - Focus on logic, not presentational components.
   - Test the happy path, error cases, and the edge cases listed in the spec.
   - Don't write tests just to write them. Use your best judgement.
5. Run the test command from `CLAUDE.md` and make sure everything passes.
6. Report what is now covered and what deliberately isn't.
