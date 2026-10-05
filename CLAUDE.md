# CLAUDE.md

This repo is a collection of Agent Skills for outcome-led PFM (Public Financial Management) work. There is no application code. Each `skills/<name>/` folder is a self-contained skill: `SKILL.md` with YAML frontmatter plus optional `scripts/`, `references/` and `assets/`.

## Conventions

- The folder name is the skill name: lowercase, hyphens, no spaces. `SKILL.md` has no `name` field.
- The frontmatter `description` must say what the skill does and when to trigger it. All "when to use" guidance lives there, not in the body.
- Keep `SKILL.md` under 500 lines. Move long material into `references/` and link to it.
- A new skill is a folder under `skills/` with a `SKILL.md` whose frontmatter has `title` and `description`. See CONTRIBUTING.md.
- After adding or editing a skill, run `python3 scripts/validate_skills.py` and update the tables in `README.md` and `skills/README.md`.
- The files in `skills/olepfm-session-manager/references/` (the prompt files plus the `manager-*.md` files) are exported unchanged to another platform that limits file size. Do not merge or rename them; the manager and the files cross-reference each other by those exact names. When a file outgrows the limit, split it at a prompt boundary into a new file beside it (as `01a-section2-3.md` and `04b-render-word-template.md` were), and update the manager's run instructions, the neighbouring files' continue-with notes and the tables in `skills/README.md`. See the mapping in `skills/README.md`.
- Sector variants of a prompt file sit beside it as `<file>-variant-<sector>.md` (for example `01a-variant-economic-resilience.md`), contain only the prompts that differ, keep the standard numbers with a prefix (`ER-1-05`), and are dispatched from SKILL.md by sector. Client material may still use the old letter codes (B1, T1, M1a); translate them with the crosswalk in `skills/README.md` instead of reverting the numbering.
- Rules that apply only on the client's platform (its knowledge base, upload requests, Prompt S-5) live in `skills/olepfm-session-manager/references/manager-platform.md`. Keep SKILL.md and the prompt files platform-neutral: dispatch to that file with a one-line note, as for sector variants, and put any new platform-only rule there.
- `skills/olepfm-joint-action-plan/` was divided from the client's "Joint Action Plan Compiler v5" file into SKILL.md plus references, with its process renumbered Task 1 to 8 to avoid clashing with OLePFM Steps. Its `assets/joint-action-plan-template.md` is the structural authority for a JAP, as `report-template.md` is for the sector report.
- Every `references/*.md` file must start with YAML frontmatter (`---` delimiters) carrying `title` and `description`, as the client's platform requires; the validator fails otherwise. `SKILL.md` carries the same two fields, `title` and `description`, and nothing else in its header.
- Hard limit: `SKILL.md` and every `references/*.md` file must stay under 20,000 characters (the client's platform rejects larger files). Split a file at a prompt boundary instead of trimming it; `scripts/validate_skills.py` fails on any file over the limit. Files in `assets/` are exempt.
- Prompt IDs follow the scheme in `skills/README.md` (S-n, 1-nn, 2-nn, 3-nn, C-nn, QA-n, plus n-Qk for per-step checks). Keep them unique and sequential within a stage; update the sequence summary tables and the manager's run instructions when adding or removing a prompt.

## Git and data

- `.gitignore` ignores everything by default and whitelists by extension. If a new file in a skill does not show up in `git status`, add a rule to the "Agent skills toolkit" section at the bottom of `.gitignore` rather than forcing it with `git add -f`.
- Never commit country data, workshop outputs, reports or credentials. Skill `assets/` are for templates only.
- Word templates (`.docx`) are not committed. The client uploads them to the platform's backend knowledge base; skills refer to them by document title, and the Markdown twin in `assets/` is the committed text version.
