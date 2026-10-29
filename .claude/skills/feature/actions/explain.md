# Explain Action

1. Read current-feature.md to understand what was implemented.
2. Get the list of changed files:
   - Full mode: `git diff <default> --name-only` (default branch: see SKILL.md).
   - Lite mode (no feature branch): uncommitted changes (`git diff HEAD --name-only`
     plus untracked files), or the last slice commit if everything is committed.
3. For each file created or modified:
   - Show the file path
   - Give a 1-2 sentence explanation of what it does / what changed
   - Highlight any key functions, components, or patterns used
4. End with a brief summary of how the pieces fit together.

## Output Format

## Files Changed

**path/to/file.ts** (new)
Brief explanation of what this file does and why it was added.

**path/to/other.ts** (modified)
What changed and why.

## How It All Connects

Brief summary of the data/control flow between these files.
