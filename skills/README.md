# Skills index

One folder per skill. Each folder contains a `SKILL.md` and, where needed, `scripts/`, `references/` and `assets/`. See [CONTRIBUTING.md](../CONTRIBUTING.md) for how to add one.

| Skill | Description | Status |
|---|---|---|
| [olepfm-session-manager](olepfm-session-manager/) | Orchestrates production of a complete OLePFM Sector Reform Design Report across Phases 0 to 4, or prepares the Working Tables for a reform design workshop. Controls sequencing, intervention points, inter-phase records and completion gates. | draft |

Status values: `stub` (placeholder, not yet usable), `draft` (usable, not yet tested), `stable` (tested on real prompts).

## How the OLePFM skill is put together

```
olepfm-session-manager/
├── SKILL.md                           entry point; picks report mode or workshop mode
├── assets/
│   └── report-template.md             OLePFM Sector Reform Design Report Template: structure and standard text the prompts follow
└── references/
    ├── manager-workshop.md            workshop mode: overlay that reuses the files below, stops after Table 2.1
    ├── 00-source-prep.md              Phase 0: source preparation (S1 to S4)
    ├── 01a-chapters1-2.md             Phase 1: Chapters 1 and 2
    ├── 01b-annex1.md                  Phase 1: Annex Step 1 and compilation
    ├── 02-chapter3-annex2.md          Phase 2: Chapter 3 and Annex Step 2
    ├── 03a-reform-results.md          Phase 3: Annex Table 3.1 and Section 4.1
    ├── 03b-stakeholders-systems-steps.md  Phase 3: Sections 4.2, 4.3 and Annex Table 3.5
    ├── 03c-conclusion-compilation.md  Phase 3: Chapter 5 and compilation
    ├── 04a-audit-and-part1.md         Phase 4: consistency audit and Main Report Part 1
    ├── 04b-part2-and-annex.md         Phase 4: Main Report Part 2 and Annex document
    └── 04c-cross-document-qa.md       Phase 4: cross-document QA
```

**Report mode** follows SKILL.md from Session Setup through Phase 4, loading one phase file at a time.

**Workshop mode** is an overlay on the same workflow. `manager-workshop.md` reuses Step 2 of Session Setup, Phase 0 (`00-source-prep.md`, S1 to S4) and a handful of Phase 1 and 2 prompts (`01a` B1, B2, B3b, B4b; `01b` C2; `02` B2) to pre-populate Tables 1.1 to 2.1, then scaffolds Tables 2.2 to 3.5 blank for the workshop. The AI behaviour rules in SKILL.md apply in both modes. Because everything lives in one folder, there is one copy of each prompt and nothing to keep in sync.

The phase files are not standalone skills. Each one depends on session context and drafts produced by the phases before it, and the manager calls them by file name. Phases 1, 3 and 4 are split into sub-files (a, b, c) only because the original platform limited file size. They remain split here so the same files can be uploaded unchanged.

## Platform file names

The files are also used on a platform that keeps all of them in one flat skills folder. Mapping:

| Platform file | Repository path |
|---|---|
| `manager.md` | `olepfm-session-manager/SKILL.md` |
| `manager-workshop.md` | `olepfm-session-manager/references/manager-workshop.md` |
| `00-source-prep.md` to `04c-cross-document-qa.md` | `olepfm-session-manager/references/<same name>` |
| OLePFM Sector Reform Design Report Template (knowledge base root) | `olepfm-session-manager/assets/report-template.md` |

The Synthesis Handbook (Williamson et al., 2024) and the sector notes are not kept in this repository. On the platform they are pre-loaded in the knowledge base; in Claude Code, provide them in the session.

To export for that platform, copy SKILL.md as `manager.md` and the `references/` files as they are. The `name:` line in the SKILL.md frontmatter is required by the Agent Skills format and can be left in place.
