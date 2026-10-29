# Load Action

1. If current-feature.md already has an active feature (Status is Not Started or
   In Progress), stop and ask before replacing it.

2. Check $ARGUMENTS (after "load"):
   - `slice <n>` (lite mode): take slice n from `context/SPEC.md`, plus the acceptance
     criteria and assumptions that apply to it.
   - A single word with no spaces: look for `context/features/{name}.md` or
     `context/fixes/{name}.md`. Also accept the name without its number prefix
     (`navbar-layout` matches `01-navbar-layout.md`). If nothing matches, list the
     available specs and stop.
   - Multiple words: use as an inline feature description and generate goals.
   - Empty: error — "load needs a spec name, `slice <n>`, or a feature description".

3. Read the spec against the current code. If the spec contradicts itself or the code
   (a field that doesn't exist, conflicting behaviors), list the problems and stop.

4. Update current-feature.md:
   - Update H1 heading to include feature name (e.g., `# Current Feature: Add Navbar`)
   - Write goals as bullet points under ## Goals, taken from the acceptance criteria
   - Write any additional notes/context under ## Notes, including the spec file path
   - Set Status to "Not Started"

5. Confirm the spec loaded and show the feature summary.
