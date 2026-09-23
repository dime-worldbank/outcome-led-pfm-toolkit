# Skills index

One folder per skill. Each folder contains a `SKILL.md` and, where needed, `scripts/`, `references/` and `assets/`. See [CONTRIBUTING.md](../CONTRIBUTING.md) for how to add one.

| Skill | Description | Status |
|---|---|---|
| [olepfm-session-manager](olepfm-session-manager/) | Orchestrates production of a complete OLePFM Sector Reform Design Report across five stages (Sources, Steps 1 to 3, Compilation and QA), or prepares the Working Tables for a reform design workshop. Controls sequencing, intervention points, inter-step records and completion gates. | draft |

Status values: `stub` (placeholder, not yet usable), `draft` (usable, not yet tested), `stable` (tested on real prompts).

## How the OLePFM skill is put together

```
olepfm-session-manager/
├── SKILL.md                           entry point; picks report mode or workshop mode
├── assets/
│   └── report-template.md             OLePFM Sector Reform Design Report Template: structure and standard text the prompts follow
└── references/
    ├── manager-workshop.md            workshop mode: overlay that reuses the files below, stops after Table 2.1
    ├── 00-source-prep.md              Sources: source preparation (Prompts S-1 to S-4)
    ├── 01a-chapters1-2.md             Step 1: Chapters 1 and 2 (Prompts 1-01 to 1-11)
    ├── 01a-variant-economic-resilience.md  Step 1 variant for cross-cutting fiscal outcomes (Prompts ER-1-04 to ER-1-10, ER-1-Q5)
    ├── 01b-annex1.md                  Step 1: Annex Step 1 and compilation (Prompts 1-12 to 1-14)
    ├── 02-chapter3-annex2.md          Step 2: Chapter 3 and Annex Step 2 (Prompts 2-01 to 2-10)
    ├── 03a-reform-results.md          Step 3: Annex Table 3.1 and Section 4.1 (Prompts 3-01 to 3-05)
    ├── 03b-stakeholders-systems-steps.md  Step 3: Sections 4.2, 4.3 and Annex Table 3.5 (Prompts 3-06 to 3-12)
    ├── 03c-conclusion-compilation.md  Step 3: Chapter 5 and compilation (Prompts 3-13 and 3-14)
    ├── 04a-audit-and-part1.md         Compilation and QA: consistency audit and Main Report Part 1 (Prompts C-01 to C-05)
    ├── 04b-part2-and-annex.md         Compilation and QA: Main Report Part 2 and Annex document (Prompts C-06 to C-13)
    └── 04c-cross-document-qa.md       Compilation and QA: cross-document checks (Prompts QA-1 to QA-5)
```

**Report mode** follows SKILL.md from Session Setup through Compilation and QA, loading one prompt file at a time.

**Workshop mode** is an overlay on the same workflow. `manager-workshop.md` reuses Setup 2 of Session Setup, the Sources stage (`00-source-prep.md`, Prompts S-1 to S-4) and a handful of Step 1 and Step 2 prompts (1-02, 1-03, 1-05, 1-08, 1-13 and 2-02) to pre-populate Tables 1.1 to 2.1, then scaffolds Tables 2.2 to 3.5 blank for the workshop. The AI behaviour rules in SKILL.md apply in both modes. Because everything lives in one folder, there is one copy of each prompt and nothing to keep in sync.

The prompt files are not standalone skills. Each one depends on session context and drafts produced by the stages before it, and the manager calls them by file name. Step 1, Step 3 and Compilation and QA are split into sub-files (a, b, c) only because the original platform limited file size. They remain split here so the same files can be uploaded unchanged.

## Prompt numbering

Every prompt has a unique ID that says which stage it belongs to and where it sits in the sequence. The stages follow the OLePFM five-step process in the Practitioners Toolkit Guidance Note; only Steps 1 to 3 are covered, because Steps 4 and 5 are implementation.

| Stage | Prompt IDs | File(s) |
|---|---|---|
| Sources | S-1 to S-4 | `00-source-prep.md` |
| Step 1 | 1-01 to 1-14 | `01a-chapters1-2.md`, `01b-annex1.md` |
| Step 2 | 2-01 to 2-10 | `02-chapter3-annex2.md` |
| Step 3 | 3-01 to 3-14 | `03a-reform-results.md`, `03b-stakeholders-systems-steps.md`, `03c-conclusion-compilation.md` |
| Compilation | C-01 to C-13 | `04a-audit-and-part1.md`, `04b-part2-and-annex.md` |
| Final QA | QA-1 to QA-5 | `04c-cross-document-qa.md` |

Optional quality checks at the end of a step are numbered by step: 1-Q1 to 1-Q4, 2-Q1 to 2-Q5, 3-Q1 to 3-Q4. Inside each file, prompts sit under a heading naming the guidance-note sub-step they serve (Sub-step 1.4, Sub-step 2.2, and so on), and each prompt heading names the report section or annex table it produces. When adding a prompt, give it the next number in its stage and update the Prompt Sequence Summary table at the end of the file and the manager's run instructions.

## Sector variants

The standard prompts are written for service-delivery sectors. Where a sector needs different prompts, a variant file sits beside the standard file, named `<file>-variant-<sector>.md`, and contains only the prompts that change. Variant prompts keep the standard number with a prefix, so ER-1-05 replaces 1-05. The manager decides by sector when to use a variant and says where to switch out and back in.

| Variant | Applies to | Replaces | Adds |
|---|---|---|---|
| `01a-variant-economic-resilience.md` | Economic resilience and other cross-cutting fiscal outcomes (macro-fiscal stability, fiscal or debt sustainability) | Prompts 1-04 to 1-10 (Section 2.3) | Check ER-1-Q5 and a three-item deviation register for the compilation audit |

## Crosswalk from the previous prompt codes

Earlier versions of these files, and material the client may still send, use letter codes that restart in every file. Translate them with this table rather than reverting the numbering.

| File | Previous code | Current ID |
|---|---|---|
| 00 | S1 to S4 | S-1 to S-4 |
| 01a | A1; B1; B2; B3a, B3b, B3c; B4a, B4b, B4c, B4d; B5 | 1-01; 1-02; 1-03; 1-04, 1-05, 1-06; 1-07, 1-08, 1-09, 1-10; 1-11 |
| 01a | QA1, QA3, QA4 | 1-Q1, 1-Q3, 1-Q4 |
| 01b | C1; C2; D1; QA2 | 1-12; 1-13; 1-14; 1-Q2 |
| 02 | B1 to B9; C1; QA1 to QA5 | 2-01 to 2-09; 2-10; 2-Q1 to 2-Q5 |
| 03a | B1; T1; T2; C1; C2 | 3-01; 3-02; 3-03; 3-04; 3-05 |
| 03b | D1, D2, D3; E1, E2; F1, F2 | 3-06, 3-07, 3-08; 3-09, 3-10; 3-11, 3-12 |
| 03c | G1; H1; QA1 to QA4 | 3-13; 3-14; 3-Q1 to 3-Q4 |
| 04a | A1; M1a to M1d | C-01; C-02 to C-05 |
| 04b | M2a to M2d; AN1 to AN4 | C-06 to C-09; C-10 to C-13 |
| 04c | QA1 to QA5 | QA-1 to QA-5 |
| manager | Phase 0; Phase 1 to 3; Phase 4; Session Setup Step 1 and 2 | Sources; Step 1 to 3; Compilation and QA; Setup 1 and 2 |

## Platform file names

The files are also used on a platform that keeps all of them in one flat skills folder. Mapping:

| Platform file | Repository path |
|---|---|
| `manager.md` | `olepfm-session-manager/SKILL.md` |
| `manager-workshop.md` | `olepfm-session-manager/references/manager-workshop.md` |
| `00-source-prep.md` to `04c-cross-document-qa.md` | `olepfm-session-manager/references/<same name>` |
| `01a-variant-economic-resilience.md` | `olepfm-session-manager/references/01a-variant-economic-resilience.md` |
| OLePFM Sector Reform Design Report Template (knowledge base root) | `olepfm-session-manager/assets/report-template.md` |

The Synthesis Handbook (Williamson et al., 2024) and the sector notes are not kept in this repository. On the platform they are pre-loaded in the knowledge base; in Claude Code, provide them in the session.

To export for that platform, copy SKILL.md as `manager.md` and the `references/` files as they are. The `name:` line in the SKILL.md frontmatter is required by the Agent Skills format and can be left in place.
