# Skills index

One folder per skill. Each folder contains a `SKILL.md` and, where needed, `scripts/`, `references/` and `assets/`. Every file in `references/` and `assets/` starts with the skill's prefix (`manager-`, `joint-action-plan-`) because the client's platform keeps all skill files in one flat folder; see [Platform file names](#platform-file-names) below. See [CONTRIBUTING.md](../CONTRIBUTING.md) for how to add one.

| Skill | Description | Status |
|---|---|---|
| [olepfm-session-manager](olepfm-session-manager/) | Orchestrates production of a complete OLePFM Sector Reform Design Report across five stages (Sources, Steps 1 to 3, Compilation and QA), or prepares the Working Tables for a reform design workshop. Controls sequencing, intervention points, inter-step records and completion gates. | draft |
| [olepfm-joint-action-plan](olepfm-joint-action-plan/) | Compiles a Joint Action Plan from two or more sector reports produced by the session manager: extracts and synthesises cross-cutting bottlenecks, selects a PFM reform framework, drafts the plan against the bundled skeleton template, and cross-checks it against the source reports. Eight tasks. | draft |

Status values: `stub` (placeholder, not yet usable), `draft` (usable, not yet tested), `stable` (tested on real prompts).

## How the OLePFM skill is put together

```
olepfm-session-manager/
├── SKILL.md                                   entry point; picks report mode or workshop mode (exported as manager.md)
├── assets/
│   ├── manager-report-template.md             OLePFM Sector Reform Design Report Template: structure and standard text the prompts follow
│   └── manager-sector-background-template.md  OLePFM Sector Background Information Template: Chapters 1 and 2, Annex Tables 1.1 and 1.2 and the Working Tables 2.1 to 3.5; the paper a workshop starts from
└── references/
    ├── manager-setup.md                       session setup: document check, country/sector/outcome context, Sector Outcome Reference
    ├── manager-workshop.md                    workshop mode: overlay that drafts Chapters 1 and 2 and Tables 1.1, 1.2 and 2.1 with the files below, leaves 2.2 to 3.5 blank, renders into the Sector Background template
    ├── manager-platform.md                    institutional platform only: search tools, link source, index check S-5 inside each sourcing prompt (Status column, upload request), citation rules
    ├── manager-reference-check.md             reference check table after every cited draft (claim, source, document URL, text readable, exact text), merged per chapter at Prompts 1-15, 2-10, 3-14
    ├── manager-00-source-prep.md              Sources: source preparation (Prompts S-1 to S-4)
    ├── manager-01a-chapters1-2.md             Step 1: Chapter 1 and Sections 2.1 to 2.2 (Prompts 1-01 to 1-03)
    ├── manager-01a-section2-3.md              Step 1: Section 2.3 (Prompts 1-04 to 1-11) and the Step 1 quality checks
    ├── manager-01a-variant-economic-resilience.md    Step 1 variant for cross-cutting fiscal outcomes, file 1 (ER-1-04 to ER-1-06)
    ├── manager-01a-variant-economic-resilience-2.md  file 2 (ER-1-07 to ER-1-10, ER-1-Q5)
    ├── manager-01b-annex1.md                  Step 1: Annex Step 1 and compilation (Prompts 1-12 to 1-15)
    ├── manager-02-chapter3-annex2.md          Step 2: Chapter 3 and Annex Step 2 (Prompts 2-01 to 2-10)
    ├── manager-03a-reform-results.md          Step 3: Annex Table 3.1 and Section 4.1 (Prompts 3-01 to 3-05)
    ├── manager-03b-stakeholders-systems-steps.md  Step 3: Sections 4.2, 4.3 and Annex Table 3.5 (Prompts 3-06 to 3-12)
    ├── manager-03c-conclusion-compilation.md  Step 3: Chapter 5 and compilation (Prompts 3-13 and 3-14)
    ├── manager-04a-audit-and-part1.md         Compilation and QA: consistency audit and Main Report Part 1 (Prompts C-01 to C-05)
    ├── manager-04b-part2-and-annex.md         Compilation and QA: Main Report Part 2 and Annex document (Prompts C-06 to C-13)
    ├── manager-04b-render-word-template.md    Compilation and QA: render the compiled report into the OLePFM Word template (Prompt C-14)
    └── manager-04c-cross-document-qa.md       Compilation and QA: cross-document checks (Prompts QA-1 to QA-5)
```

**Report mode** follows SKILL.md from Session Setup through Compilation and QA, loading one prompt file at a time. After every prompt whose output cites a source, `manager-reference-check.md` adds a reference check table (claim, source, document URL, whether the source's text could be retrieved in this session, exact text from the document) so the user can check the references at that prompt's ✏️ point; the compilation prompts merge them into one table per chapter before the completion gate, and the tables stay out of the compiled report unless asked for. The workshop overlay and the joint action plan skill apply the same rule to their cited tables and sections.

**Workshop mode** is an overlay on the same workflow. `manager-workshop.md` reuses Setup 2 (in `manager-setup.md`), the Sources stage (`manager-00-source-prep.md`, Prompts S-1 to S-4), the Step 1 prompts 1-01 to 1-13 and Prompt 2-02 to draft Chapters 1 and 2 and populate Annex Tables 1.1, 1.2 and 2.1, and leaves Tables 2.2 to 3.5 blank for the workshop. Its step 5 renders the paper into the OLePFM Sector Background Information Word template (Markdown twin `manager-sector-background-template.md`), the same way Prompt C-14 renders the report. The AI behaviour rules in SKILL.md apply in both modes. Because everything lives in one folder, there is one copy of each prompt and nothing to keep in sync.

The prompt files are not standalone skills. Each one depends on session context and drafts produced by the stages before it, and the manager calls them by file name. Step 1, Step 3 and Compilation and QA are split into sub-files (a, b, c), and the 01a and 04b files are split once more (`manager-01a-section2-3.md`, `manager-04b-render-word-template.md`), only because the platform limits each file to 20,000 characters. They remain split here so the same files can be uploaded unchanged; each file says which prompts it holds and which file comes next.

## Prompt numbering

Every prompt has a unique ID that says which stage it belongs to and where it sits in the sequence. The stages follow the OLePFM five-step process in the Practitioners Toolkit Guidance Note; only Steps 1 to 3 are covered, because Steps 4 and 5 are implementation.

| Stage | Prompt IDs | File(s) |
|---|---|---|
| Sources | S-1 to S-4 | `manager-00-source-prep.md` |
| Sources, institutional platform only | S-5, inside each of S-1 to S-4 | `manager-platform.md` |
| Step 1 | 1-01 to 1-15 | `manager-01a-chapters1-2.md`, `manager-01a-section2-3.md`, `manager-01b-annex1.md` |
| Step 2 | 2-01 to 2-10 | `manager-02-chapter3-annex2.md` |
| Step 3 | 3-01 to 3-14 | `manager-03a-reform-results.md`, `manager-03b-stakeholders-systems-steps.md`, `manager-03c-conclusion-compilation.md` |
| Compilation | C-01 to C-14 | `manager-04a-audit-and-part1.md`, `manager-04b-part2-and-annex.md`, `manager-04b-render-word-template.md` |
| Final QA | QA-1 to QA-5 | `manager-04c-cross-document-qa.md` |

Optional quality checks are numbered by step: 1-Q1 to 1-Q4, 2-Q1 to 2-Q5, 3-Q1 to 3-Q5. Most sit at the end of their step's last prompt file (the Step 1 checks in `manager-01a-section2-3.md`); 3-Q5 sits in the 03a file because it runs right after Table 3.1. Inside each file, prompts sit under a heading naming the guidance-note sub-step they serve (Sub-step 1.4, Sub-step 2.2, and so on), and each prompt heading names the report section or annex table it produces. When adding a prompt, give it the next number in its stage and update the Prompt Sequence Summary table at the end of the file and the manager's run instructions.

## How the joint action plan skill is put together

```
olepfm-joint-action-plan/
├── SKILL.md                                   the eight tasks, documents needed, edge cases, terminology (exported as joint-action-plan.md)
├── assets/
│   └── joint-action-plan-template.md          OLePFM Joint Action Plan Annotated Skeleton Template: the structure every JAP follows
└── references/
    ├── joint-action-plan-reform-frameworks.md Framework 1 (service delivery) and Framework 2 (jobs and resilience), selection rules
    └── joint-action-plan-task-checklists.md   extraction map keyed to the report's sections and tables, synthesis table, gap-analysis formats, finalisation checklist
```

This skill runs after the session manager: its inputs are the Sector Reform Design Reports that skill produces, and its extraction map names the report sections and annex tables to read. Its process is numbered Task 1 to Task 8 so it is never confused with the OLePFM Steps. It was divided from the client's "Joint Action Plan Compiler v5" file; when the client sends a new version, divide it the same way rather than pasting it whole.

## Word templates

Every deliverable is handed over as a Word document rendered into its official template by cloning the `.docx` and filling it in place, never by converting Markdown. The templates are not committed; the Markdown twins in `assets/` carry their text.

Each workflow verifies that its template is accessible, and is the Word file, before anything is drafted.

| Deliverable | Word template | Verified at | Render instructions |
|---|---|---|---|
| Sector Reform Design Report (Main Report Parts 1 and 2 and the Annex, delivered as one file) | OLePFM Sector Reform Design Report Template | Setup 1 in `manager-setup.md` | Prompt C-14 in `manager-04b-render-word-template.md` |
| Sector Background Information paper for a workshop (Chapters 1 and 2, Annex Tables 1.1 and 1.2, Working Tables 2.1 to 3.5) | OLePFM Sector Background Information Template | Step 1 of `manager-workshop.md`, which runs Setup 1 and adds this template to the check | Step 5 in `manager-workshop.md` |
| Joint Action Plan | OLePFM Joint Action Plan Template | The Setup section of `olepfm-joint-action-plan/SKILL.md` | Output section and Task 8 in `olepfm-joint-action-plan/SKILL.md` |

## Sector variants

The standard prompts are written for service-delivery sectors. Where a sector needs different prompts, a variant file sits beside the standard file, named `<file>-variant-<sector>.md`, and contains only the prompts that change. Variant prompts keep the standard number with a prefix, so ER-1-05 replaces 1-05. The manager decides by sector when to use a variant and says where to switch out and back in.

| Variant | Applies to | Replaces | Adds |
|---|---|---|---|
| `manager-01a-variant-economic-resilience.md` and `-2.md` | Economic resilience and other cross-cutting fiscal outcomes (macro-fiscal stability, fiscal or debt sustainability) | Prompts 1-04 to 1-10 (Section 2.3) | Check ER-1-Q5 and a three-item deviation register for the compilation audit |

## Platform-specific rules

Rules that apply only on the institutional platform (where the knowledge base holds the pre-loaded documents and indexes what the user uploads) live in `manager-platform.md`, not in the prompt files or in SKILL.md. The manager dispatches to it with a one-line note, as it does for sector variants, so the prompt files stay platform-neutral and run unchanged in Claude Code. The file names the platform's search tools, the two-pass link verification through web_search (the platform cannot open pages) and the Enterprise Document Repository agent as the link source for knowledge-base documents, requires the user's must-have sources to be uploaded before Step 1, and holds the index check S-5, applied inside each of S-1 to S-4 to every source as its link is verified, which checks that it is indexed in the knowledge base or uploaded to the session, lets the user choose what to upload, removes the rest, and sets the citation rules that follow (cite only Indexed, Uploaded or Web page sources; cite the document read, not the one it cites; verify a new source before citing it). It also adds items to the Sources completion gate and to the consistency audit (Prompt C-01), and defines readability on the platform: a source's text is readable only when the app-wide knowledge base or `project_search` returns it, which is what the reference check tests. Put any future platform-only rule in the same file.

## Crosswalk from the previous prompt codes

Earlier versions of these files, and material the client may still send, use letter codes that restart in every file. Translate them with this table rather than reverting the numbering.

| File | Previous code | Current ID |
|---|---|---|
| 00 | S1 to S4 | S-1 to S-4 |
| 01a | A1; B1; B2 | 1-01; 1-02; 1-03 (`manager-01a-chapters1-2.md`) |
| 01a | B3a, B3b, B3c; B4a, B4b, B4c, B4d; B5 | 1-04, 1-05, 1-06; 1-07, 1-08, 1-09, 1-10; 1-11 (now in `manager-01a-section2-3.md`) |
| 01a | QA1, QA3, QA4 | 1-Q1, 1-Q3, 1-Q4 |
| 01b | C1; C2; (none); D1; QA2 | 1-12; 1-13; 1-14 (Annex Table 1.3, added to match the template); 1-15; 1-Q2 |
| 02 | B1 to B9; C1; QA1 to QA5 | 2-01 to 2-09; 2-10; 2-Q1 to 2-Q5 |
| 03a | B1; T1; T2; C1; C2 | 3-01; 3-02; 3-03; 3-04; 3-05 |
| 03b | D1, D2, D3; E1, E2; F1, F2 | 3-06, 3-07, 3-08; 3-09, 3-10; 3-11, 3-12 |
| 03c | G1; H1; QA1 to QA4 | 3-13; 3-14; 3-Q1 to 3-Q4 |
| 04a | A1; M1a to M1d | C-01; C-02 to C-05 |
| 04b | M2a to M2d; AN1 to AN4 | C-06 to C-09; C-10 to C-13 (C-14, the Word render, sits in `manager-04b-render-word-template.md`) |
| 04c | QA1 to QA5 | QA-1 to QA-5 |
| manager | Phase 0; Phase 1 to 3; Phase 4; Session Setup Step 1 and 2 | Sources; Step 1 to 3; Compilation and QA; Setup 1 and 2 |

## Platform file names

The files are also used on a platform that keeps every skill file in **one flat folder with no sub-folders** and **limits each skill file to 20,000 characters**. Two rules follow.

- **Prefix.** Every file in a skill's `references/` and `assets/` starts with the skill's prefix, the tail of the folder name, so a flat listing shows which workflow a file belongs to: `manager-` for olepfm-session-manager, `joint-action-plan-` for olepfm-joint-action-plan. `SKILL.md` is exported as `<prefix>.md`. The validator checks the prefix.
- **No folder paths.** SKILL.md and the `references/` files refer to other files by file name only (`manager-setup.md`, not `references/manager-setup.md`), because the folders do not exist on the platform. The validator fails on any `references/`, `assets/` or `scripts/` path inside those files.

`SKILL.md` and every file in `references/` must stay under the character limit (the validator checks it); split a file rather than trimming its content, as was done for `manager-01a-section2-3.md` and `manager-04b-render-word-template.md`. The templates in `assets/` are knowledge-base documents on the platform and are not subject to the limit. Mapping:

| Platform file | Repository path |
|---|---|
| `manager.md` | `olepfm-session-manager/SKILL.md` |
| `manager-setup.md`, `manager-workshop.md`, `manager-platform.md`, `manager-reference-check.md` | `olepfm-session-manager/references/<same name>` |
| `manager-00-source-prep.md` to `manager-04c-cross-document-qa.md`, including `manager-01a-section2-3.md`, `manager-01a-variant-economic-resilience.md` and `manager-04b-render-word-template.md` | `olepfm-session-manager/references/<same name>` |
| OLePFM Sector Reform Design Report Template (knowledge base root) | `olepfm-session-manager/assets/manager-report-template.md` |
| OLePFM Sector Background Information Template (knowledge base root) | `olepfm-session-manager/assets/manager-sector-background-template.md` |
| `joint-action-plan.md` | `olepfm-joint-action-plan/SKILL.md` (divided from the client's "Skill: OLePFM Joint Action Plan Compiler v5" file, tasks renumbered) |
| `joint-action-plan-reform-frameworks.md`, `joint-action-plan-task-checklists.md` | `olepfm-joint-action-plan/references/<same name>` |
| OLePFM Joint Action Plan Annotated Skeleton Template | `olepfm-joint-action-plan/assets/joint-action-plan-template.md` |

The Synthesis Handbook (Williamson et al., 2024) and the sector notes are not kept in this repository. On the platform they are pre-loaded in the knowledge base; in Claude Code, provide them in the session.

To export for that platform, copy each SKILL.md as `<prefix>.md` (`manager.md`, `joint-action-plan.md`) and the `references/` files as they are. Every file, SKILL.md included, carries the same header: `title` and `description`.
