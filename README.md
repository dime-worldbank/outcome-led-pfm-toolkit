# outcome-led-pfm-toolkit

A toolkit of outcome-led PFM (Public Financial Management) skills for AI assistants. Each skill packages a repeatable workflow, such as preparing a diagnostic workshop or generating a structured, outcome-focused report, so Claude can run it consistently across countries and engagements.

Skills follow the [Agent Skills](https://agentskills.io) format: a folder with a `SKILL.md` file plus optional `scripts/`, `references/` and `assets/`. They work in Claude Code, Claude.ai and the Claude API.

## Skills

| Skill | What it does | Status |
|---|---|---|
| [olepfm-session-manager](skills/olepfm-session-manager/) | Produce a complete OLePFM Sector Reform Design Report in one session (Sources, Steps 1 to 3, Compilation and QA), or, in workshop mode, the Working Tables a reform design workshop starts from | draft |
| [olepfm-joint-action-plan](skills/olepfm-joint-action-plan/) | Compile a Joint Action Plan from two or more sector reports produced by the session manager, following the bundled JAP skeleton template and the PFM reform frameworks | draft |

OLePFM stands for Outcome-Led Public Financial Management. The session manager has two modes. Report mode runs five stages, Sources, Steps 1 to 3 and Compilation and QA, loading one prompt file at a time from `references/`. Workshop mode is an overlay on the same workflow: it reuses the setup, the Sources stage and a subset of the Step 1 and Step 2 prompts, then stops after Table 2.1 and leaves the remaining tables blank for the workshop.

See [skills/README.md](skills/README.md) for the full index and conventions.

## Install

### Claude Code (as a plugin)

```
/plugin marketplace add dime-worldbank/outcome-led-pfm-toolkit
/plugin install outcome-led-pfm-toolkit@outcome-led-pfm-toolkit
```

To enable it for everyone working in a given project rather than just yourself, install from the CLI with project scope. This records the plugin in that project's `.claude/settings.json`:

```
claude plugin install outcome-led-pfm-toolkit@outcome-led-pfm-toolkit --scope project
```

### Claude Code (single project, no plugin)

Clone the repo and symlink the skill folder into `.claude/skills/` in your project:

```
git clone https://github.com/dime-worldbank/outcome-led-pfm-toolkit.git
mkdir -p .claude/skills
ln -s "$(pwd)/outcome-led-pfm-toolkit/skills/olepfm-session-manager" .claude/skills/
```

### Claude.ai

Zip a single skill folder (the folder containing `SKILL.md`) and upload it under Settings > Capabilities > Skills.

## Repository layout

```
.
├── skills/                     # one folder per skill (SKILL.md + bundled resources)
├── scripts/validate_skills.py  # checks every skill's frontmatter and layout
├── .claude-plugin/             # plugin + marketplace manifests for Claude Code
└── .github/workflows/          # runs the validator on every push and PR
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add or change a skill. Run the validator before opening a PR:

```
python3 scripts/validate_skills.py
```

## Data handling

This repository holds workflows and templates only. Never commit country data, workshop transcripts, draft reports or anything else that is confidential. The `.gitignore` ignores everything by default and only whitelists code, markdown and skill resources.
