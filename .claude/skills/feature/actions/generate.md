# Generate Action

1. Check $ARGUMENTS (after "generate"):
   - If it has text, find the matching Phase or section in `context/ROADMAP.md`.
   - If it is blank, list the ROADMAP phases and ask which one to generate. Don't
     generate anything until the user picks.
2. Read the codebase and `context/ROADMAP.md` (including "Decisions locked in" and
   "Still open") to understand what each item needs.
3. Ask clarifying questions if needed, before writing files.
4. Write one spec per ROADMAP item using `context/SPEC_TEMPLATE.md`, saved as
   `context/features/<phase>-<slug>.md`. Delete template sections that don't apply.
5. If writing the specs changed scope (an item split, cut or added), update
   `context/ROADMAP.md` in the same step so it doesn't drift.
6. List the files created and suggest `/feature load <name>` for the first one.
