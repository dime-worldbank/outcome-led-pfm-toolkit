# CLAUDE.md

This repo is a collection of Agent Skills for outcome-led PFM (Public Financial Management) work. There is no application code. Each `skills/<name>/` folder is a self-contained skill: `SKILL.md` with YAML frontmatter plus optional `scripts/`, `references/` and `assets/`.

## Conventions

- Folder name equals the `name` field in `SKILL.md` frontmatter: lowercase, hyphens, no spaces.
- The frontmatter `description` must say what the skill does and when to trigger it. All "when to use" guidance lives there, not in the body.
- Keep `SKILL.md` under 500 lines. Move long material into `references/` and link to it.
- A new skill is a folder under `skills/` with a `SKILL.md` whose frontmatter has `name` and `description`. See CONTRIBUTING.md.
- After adding or editing a skill, run `python3 scripts/validate_skills.py` and update the tables in `README.md` and `skills/README.md`.
- The files in `skills/olepfm-session-manager/references/` (ten phase files plus `manager-workshop.md`) are exported unchanged to another platform that limits file size. Do not merge, split or rename them; the manager and the files cross-reference each other by those exact names. See the mapping in `skills/README.md`.

## Git and data

- `.gitignore` ignores everything by default and whitelists by extension. If a new file in a skill does not show up in `git status`, add a rule to the "Agent skills toolkit" section at the bottom of `.gitignore` rather than forcing it with `git add -f`.
- Never commit country data, workshop outputs, reports or credentials. Skill `assets/` are for templates only.
