# Skills index

One folder per skill. Each folder contains a `SKILL.md` and, where needed, `scripts/`, `references/` and `assets/`. See [CONTRIBUTING.md](../CONTRIBUTING.md) for how to add one.

| Skill | Description | Status |
|---|---|---|
| [olepfm-session-manager](olepfm-session-manager/) | Orchestrates production of a complete OLePFM Sector Reform Design Report across five stages (Sources, Steps 1 to 3, Compilation and QA), or prepares the Working Tables for a reform design workshop. Controls sequencing, intervention points, inter-step records and completion gates. | draft |
| [olepfm-joint-action-plan](olepfm-joint-action-plan/) | Compiles a Joint Action Plan from two or more sector reports produced by the session manager: extracts and synthesises cross-cutting bottlenecks, selects a PFM reform framework, drafts the plan against the bundled skeleton template, and cross-checks it against the source reports. Eight tasks. | draft |

Status values: `stub` (placeholder, not yet usable), `draft` (usable, not yet tested), `stable` (tested on real prompts).

## How the OLePFM skill is put together

```
olepfm-session-manager/
├── SKILL.md                           entry point; picks report mode or workshop mode
├── assets/
│   └── report-template.md             OLePFM Sector Reform Design Report Template: structure and standard text the prompts follow
└── references/
    ├── manager-setup.md               session setup: document check, country/sector/outcome context, Sector Outcome Reference
    ├── manager-workshop.md            workshop mode: overlay that reuses the files below, stops after Table 2.1
    ├── 00-source-prep.md              Sources: source preparation (Prompts S-1 to S-4)
    ├── 01a-chapters1-2.md             Step 1: Chapters 1 and 2 (Prompts 1-01 to 1-11)
    ├── 01a-variant-economic-resilience.md  Step 1 variant for cross-cutting fiscal outcomes, file 1 (ER-1-04 to ER-1-06)
    ├── 01a-variant-economic-resilience-2.md  file 2 (ER-1-07 to ER-1-10, ER-1-Q5)
    ├── 01b-annex1.md                  Step 1: Annex Step 1 and compilation (Prompts 1-12 to 1-15)
    ├── 02-chapter3-annex2.md          Step 2: Chapter 3 and Annex Step 2 (Prompts 2-01 to 2-10)
    ├── 03a-reform-results.md          Step 3: Annex Table 3.1 and Section 4.1 (Prompts 3-01 to 3-05)
    ├── 03b-stakeholders-systems-steps.md  Step 3: Sections 4.2, 4.3 and Annex Table 3.5 (Prompts 3-06 to 3-12)
    ├── 03c-conclusion-compilation.md  Step 3: Chapter 5 and compilation (Prompts 3-13 and 3-14)
    ├── 04a-audit-and-part1.md         Compilation and QA: consistency audit and Main Report Part 1 (Prompts C-01 to C-05)
    ├── 04b-part2-and-annex.md         Compilation and QA: Main Report Part 2 and Annex document (Prompts C-06 to C-13)
    └── 04c-cross-document-qa.md       Compilation and QA: cross-document checks (Prompts QA-1 to QA-5)
```

**Report mode** follows SKILL.md from Session Setup through Compilation and QA, loading one prompt file at a time.

**Workshop mode** is an overlay on the same workflow. `manager-workshop.md` reuses Setup 2 (in `manager-setup.md`), the Sources stage (`00-source-prep.md`, Prompts S-1 to S-4) and a handful of Step 1 and Step 2 prompts (1-02, 1-03, 1-05, 1-08, 1-13 and 2-02) to pre-populate Tables 1.1 to 2.1, then scaffolds Tables 2.2 to 3.5 blank for the workshop. The AI behaviour rules in SKILL.md apply in both modes. Because everything lives in one folder, there is one copy of each prompt and nothing to keep in sync.

The prompt files are not standalone skills. Each one depends on session context and drafts produced by the stages before it, and the manager calls them by file name. Step 1, Step 3 and Compilation and QA are split into sub-files (a, b, c) only because the original platform limited file size. They remain split here so the same files can be uploaded unchanged.

## Prompt numbering

Every prompt has a unique ID that says which stage it belongs to and where it sits in the sequence. The stages follow the OLePFM five-step process in the Practitioners Toolkit Guidance Note; only Steps 1 to 3 are covered, because Steps 4 and 5 are implementation.

| Stage | Prompt IDs | File(s) |
|---|---|---|
| Sources | S-1 to S-4 | `00-source-prep.md` |
| Step 1 | 1-01 to 1-15 | `01a-chapters1-2.md`, `01b-annex1.md` |
| Step 2 | 2-01 to 2-10 | `02-chapter3-annex2.md` |
| Step 3 | 3-01 to 3-14 | `03a-reform-results.md`, `03b-stakeholders-systems-steps.md`, `03c-conclusion-compilation.md` |
| Compilation | C-01 to C-13 | `04a-audit-and-part1.md`, `04b-part2-and-annex.md` |
| Final QA | QA-1 to QA-5 | `04c-cross-document-qa.md` |

Optional quality checks are numbered by step: 1-Q1 to 1-Q4, 2-Q1 to 2-Q5, 3-Q1 to 3-Q5. Most sit at the end of their step's last file; 3-Q5 sits in the 03a file because it runs right after Table 3.1. Inside each file, prompts sit under a heading naming the guidance-note sub-step they serve (Sub-step 1.4, Sub-step 2.2, and so on), and each prompt heading names the report section or annex table it produces. When adding a prompt, give it the next number in its stage and update the Prompt Sequence Summary table at the end of the file and the manager's run instructions.

## How the joint action plan skill is put together

```
olepfm-joint-action-plan/
├── SKILL.md                           the eight tasks, documents needed, edge cases, terminology
├── assets/
│   └── joint-action-plan-template.md  OLePFM Joint Action Plan Annotated Skeleton Template: the structure every JAP follows
└── references/
    ├── reform-frameworks.md           Framework 1 (service delivery) and Framework 2 (jobs and resilience), selection rules
    └── task-checklists.md             extraction map keyed to the report's sections and tables, synthesis table, gap-analysis formats, finalisation checklist
```

This skill runs after the session manager: its inputs are the Sector Reform Design Reports that skill produces, and its extraction map names the report sections and annex tables to read. Its process is numbered Task 1 to Task 8 so it is never confused with the OLePFM Steps. It was divided from the client's "Joint Action Plan Compiler v5" file; when the client sends a new version, divide it the same way rather than pasting it whole.

## Sector variants

The standard prompts are written for service-delivery sectors. Where a sector needs different prompts, a variant file sits beside the standard file, named `<file>-variant-<sector>.md`, and contains only the prompts that change. Variant prompts keep the standard number with a prefix, so ER-1-05 replaces 1-05. The manager decides by sector when to use a variant and says where to switch out and back in.

| Variant | Applies to | Replaces | Adds |
|---|---|---|---|
| `01a-variant-economic-resilience.md` and `-2.md` | Economic resilience and other cross-cutting fiscal outcomes (macro-fiscal stability, fiscal or debt sustainability) | Prompts 1-04 to 1-10 (Section 2.3) | Check ER-1-Q5 and a three-item deviation register for the compilation audit |

## Crosswalk from the previous prompt codes

Earlier versions of these files, and material the client may still send, use letter codes that restart in every file. Translate them with this table rather than reverting the numbering.

| File | Previous code | Current ID |
|---|---|---|
| 00 | S1 to S4 | S-1 to S-4 |
| 01a | A1; B1; B2; B3a, B3b, B3c; B4a, B4b, B4c, B4d; B5 | 1-01; 1-02; 1-03; 1-04, 1-05, 1-06; 1-07, 1-08, 1-09, 1-10; 1-11 |
| 01a | QA1, QA3, QA4 | 1-Q1, 1-Q3, 1-Q4 |
| 01b | C1; C2; (none); D1; QA2 | 1-12; 1-13; 1-14 (Annex Table 1.3, added to match the template); 1-15; 1-Q2 |
| 02 | B1 to B9; C1; QA1 to QA5 | 2-01 to 2-09; 2-10; 2-Q1 to 2-Q5 |
| 03a | B1; T1; T2; C1; C2 | 3-01; 3-02; 3-03; 3-04; 3-05 |
| 03b | D1, D2, D3; E1, E2; F1, F2 | 3-06, 3-07, 3-08; 3-09, 3-10; 3-11, 3-12 |
| 03c | G1; H1; QA1 to QA4 | 3-13; 3-14; 3-Q1 to 3-Q4 |
| 04a | A1; M1a to M1d | C-01; C-02 to C-05 |
| 04b | M2a to M2d; AN1 to AN4 | C-06 to C-09; C-10 to C-13 |
| 04c | QA1 to QA5 | QA-1 to QA-5 |
| manager | Phase 0; Phase 1 to 3; Phase 4; Session Setup Step 1 and 2 | Sources; Step 1 to 3; Compilation and QA; Setup 1 and 2 |

## Platform file names

The files are also used on a platform that keeps all of them in one flat skills folder and **limits each skill file to 20,000 characters**. `SKILL.md` and every file in `references/` must stay under that limit (the validator checks it); split a file rather than trimming its content, as was done for `01a-variant-economic-resilience.md` and for the a/b/c phase files. The templates in `assets/` are knowledge-base documents on the platform and are not subject to the limit. Mapping:

| Platform file | Repository path |
|---|---|
| `manager.md` | `olepfm-session-manager/SKILL.md` |
| `manager-workshop.md` | `olepfm-session-manager/references/manager-workshop.md` |
| `manager-setup.md` | `olepfm-session-manager/references/manager-setup.md` |
| `00-source-prep.md` to `04c-cross-document-qa.md` | `olepfm-session-manager/references/<same name>` |
| `01a-variant-economic-resilience.md`, `01a-variant-economic-resilience-2.md` | `olepfm-session-manager/references/<same name>` |
| OLePFM Sector Reform Design Report Template (knowledge base root) | `olepfm-session-manager/assets/report-template.md` |
| Skill: OLePFM Joint Action Plan Compiler v5 | `olepfm-joint-action-plan/SKILL.md` plus its two `references/` files (content divided, tasks renumbered) |
| OLePFM Joint Action Plan Annotated Skeleton Template | `olepfm-joint-action-plan/assets/joint-action-plan-template.md` |

The Synthesis Handbook (Williamson et al., 2024) and the sector notes are not kept in this repository. On the platform they are pre-loaded in the knowledge base; in Claude Code, provide them in the session.

To export for that platform, copy SKILL.md as `manager.md` and the `references/` files as they are. The `name:` line in the SKILL.md frontmatter is required by the Agent Skills format and can be left in place.
