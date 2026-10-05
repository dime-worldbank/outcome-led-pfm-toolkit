# Contributing

## Adding a skill

1. Create a folder with a `SKILL.md` in it:

   ```
   mkdir skills/<skill-name>
   ```

   Start `SKILL.md` with the frontmatter below, then add the body:

   ```yaml
   ---
   title: <Skill title>
   description: What the skill does and when Claude should use it.
   ---
   ```

   Use a short, lowercase, hyphenated folder name that says what the skill does, for example `pfm-budget-credibility-check`; the folder name is the skill's name. The header is the same `title` and `description` pair as every file in `references/`.

2. Fill in `SKILL.md`. The frontmatter `description` is what Claude reads to decide whether to use the skill, so say both what it does and when to use it. Be specific about trigger phrases and contexts. The body holds the instructions, ideally under 500 lines.

3. Put supporting material in the right folder:

   | Folder | Purpose | Loaded when |
   |---|---|---|
   | `scripts/` | Deterministic code Claude runs (Python, shell) | Executed, not read |
   | `references/` | Background docs, checklists, methodology notes | Read on demand |
   | `assets/` | Templates that shape the output, and files copied into it (md, docx, pptx, xlsx, images) | Read or copied when producing output |

   Delete any folder you do not need. Empty folders are kept only via a `.gitkeep` file.

4. Add a row to the table in `skills/README.md` and to the root `README.md`.

5. Run the validator:

   ```
   python3 scripts/validate_skills.py
   ```

6. Open a pull request. Describe the workflow the skill captures and, if you tested it, the prompts you tried.

## Writing guidance

- Start every file in `references/` with YAML frontmatter (`---` delimiters) that has `title` and `description`; the platform the files are exported to requires it, and the validator fails without it.
- Keep `SKILL.md` and every file in `references/` under 20,000 characters. The platform the files are exported to rejects larger files. Split at a prompt boundary rather than trimming; the validator fails on any file over the limit.

- Write instructions in the imperative and explain why a step matters. Claude follows reasoning better than bare rules.
- Keep the skill general. It should work across countries and engagements, not just the example you built it from.
- Prefer a bundled script over prose for anything mechanical (file conversion, table formatting, numbering).
- Point to reference files explicitly and say when to read them, so Claude does not load everything at once.

## Testing a skill

Optional but recommended. Keep test prompts in `skills/<skill-name>/evals/evals.json`:

```json
{
  "skill_name": "pfm-outcome-report",
  "evals": [
    {
      "id": 1,
      "prompt": "A realistic user request",
      "expected_output": "What a good result looks like",
      "files": []
    }
  ]
}
```

Claude Code's `skill-creator` skill can run these prompts with and without the skill and open a side-by-side review.

## What not to commit

No country data, workshop notes, participant lists, draft or final reports, credentials or tokens. The `.gitignore` blocks most of this by default. If you need to whitelist a new file type for a skill, add it to the "Agent skills toolkit" section at the bottom of `.gitignore` and explain why in the PR.
