---
name: olepfm-session-manager
title: OLePFM Session Manager
description: Orchestration guide for producing a complete OLePFM Sector Reform Design Report in a single AI session. Upload first. Controls stage sequencing (Sources, Steps 1 to 3, Compilation and QA), intervention points, inter-step data recording, and AI behavior rules. Also prepares the Working Tables for a reform design workshop when the user says "start OLePFM workshop preparation" or asks for workshop tables. Use for any OLePFM, outcome-led PFM or sector reform design report or workshop request.
---

# OLePFM Sector Reform Design: Session Manager

This document is the orchestration guide for producing a complete OLePFM Sector Reform Design Report in a single AI session. Upload it together with the ten prompt files and the reference documents at the start of the session.

---

## TWO WAYS TO USE THIS SKILL

| Mode | When | Follow |
|---|---|---|
| **Full report** | The user wants an OLePFM Sector Reform Design Report | This document, from Session Setup through Compilation and QA |
| **Workshop table preparation** | The user says "start OLePFM workshop preparation" or wants the Working Tables for a reform design workshop | `manager-workshop.md` (in `references/`). It reuses Setup 2 (in `manager-setup.md`) and the Sources stage and a subset of the Step 1 and Step 2 prompts, then stops after Table 2.1 and scaffolds the rest blank |

Workshop mode is an overlay on the report workflow, not a separate process: the instructions to the AI below (sequential execution, one prompt at a time, pause at every ✏️ point, never invent placeholder values) apply in both modes.

---

## INSTRUCTIONS TO THE AI

You are assisting with the production of an OLePFM Sector Reform Design Report. Follow these rules throughout the session:

1. **Sequential execution only.** Work through the five stages — Sources, Step 1, Step 2, Step 3, Compilation and QA — in strict order. Do not begin a new stage until the user explicitly says "proceed to Step [n]" (or "proceed to Compilation") or equivalent.

2. **One prompt at a time.** Run each numbered prompt individually; after each output, wait for the user before the next. Do not chain prompts.

3. **Pause at every ✏️ intervention point.** After every prompt that has a ✏️ marker, output a block in this shape before stopping — plain Markdown, not a `>` blockquote (which breaks the checkboxes):

   **✏️ Review the output — focus on these points**

   **[topic]** — [one line on why it matters, drawn from the instruction text before the prompt].

   - [ ] [check 1]
   - [ ] [check 2]
   - [ ] [check 3]

   Say "proceed" when satisfied, or provide corrections.

   Show all checks as one checklist, from the skill's ✏️ block.

4. **Declare stage completion.** At the end of each stage, output:

   > **STEP [n] COMPLETE** (or **SOURCES COMPLETE**, **COMPILATION AND QA COMPLETE**)
   > Please review the completion gate below before I proceed to [next stage].

5. **Record inter-step data.** At the specified points, ask the user to confirm the recorded values before proceeding. These values carry forward across stages.

6. **Do not invent or skip.** If a prompt asks you to fill in a placeholder such as `[number]` or `[paste bottleneck title]`, pause and ask the user for the value rather than inventing one.

7. **Reference check table at the end of each chapter.** When a step's chapters are compiled (Prompts 1-15, 2-10 and 3-14), append to each chapter a table of its cited claims with the source, the document URL and the exact text from the document that supports each one, following `manager-reference-check.md` (in `references/`). Quote verbatim or mark the row not verified; never invent a passage. Every number shown in a chart or chart data table also gets a row; Data360 values with claim tags are treated as verified. The tables are review aids and stay out of the compiled report unless the user asks for them.

8. **Chart interaction.** For every data chart produced anywhere in the report:
   - Show **both** the interactive chart and its underlying data table, with the table directly beneath the chart; never show one without the other.
   - Render the chart interactively with a fenced ` ```chart ` block using a **Chart.js schema** (`type` / `data.labels` / `data.datasets` / `options`); supported types are line, bar, pie and scatter. Do not use Recharts-style keys or a ` ```recharts ` fence (they render empty); Mermaid is for diagrams, not data charts. Produce a data-exact matplotlib PNG for the file area when the user wants a report-ready figure.
   - Take every value from the Data360 API (or another cited source), never from memory; each value in the table carries its Data360 **claim tag**, and the chart numbers match the table exactly.
   - Cite the source under each table: indicator name + code + source database, plus the Data360 explorer link (`https://data360.worldbank.org`) when reachable (otherwise name/code/database with the API query URL as backup, upgraded in one pass when the explorer is back).
   - **Never treat a chart as final until the user explicitly locks it in.** Present every chart as a draft, ask the user to confirm or change it (type, series, years, titles, colours), and wait — exactly as at a ✏️ point.

---

## SESSION SETUP

Complete the two setup parts in `manager-setup.md` (in `references/`) before starting the Sources stage. **Setup 1** verifies that the Report Template and the Synthesis Handbook are accessible. **Setup 2** establishes and locks the session context (country, sector, development outcome and public sector result), using the Sector Outcome Reference in that file; it also says when a sector uses variant prompts. Do not begin Sources until the context is confirmed.

### Skill Files

The skill files (`00-source-prep.md` through `04c-cross-document-qa.md`) are in the knowledge base's skills folder, accessible by default — no upload required. In this repository they are the files in the `references/` folder beside this SKILL.md.

**Prompt numbering.** Prompts are numbered by stage and run in order: S-1 to S-4 (Sources), 1-01 to 1-15 (Step 1), 2-01 to 2-10 (Step 2), 3-01 to 3-14 (Step 3), C-01 to C-13 (Compilation) and QA-1 to QA-5 (final cross-document checks). Optional quality checks at the end of a step are numbered 1-Q1, 2-Q1 and so on. Inside each file, prompts are grouped under the OLePFM sub-step they serve (for example Sub-step 1.4, Map the sector policy, institutional and public finance context). A sector variant of a prompt keeps the standard number with a prefix: ER-1-05 is the economic-resilience variant of Prompt 1-05.

## SOURCES: Source Preparation

**Skill file:** `00-source-prep.md`

Run Prompts S-1 through S-4 from `00-source-prep.md` in sequence.

> **Institutional platform (knowledge base present):** after Prompt S-4, run Prompt S-5 from `manager-platform.md` to check that every listed source is indexed in the knowledge base, and ask the user to upload any that are not. That file also adds items to the Sources completion gate below and to the consistency audit (Prompt C-01). Skip it when the user supplies the documents directly, as in Claude Code.

### Sources Completion Gate

Before advancing to Step 1, confirm all of the following:

- [ ] The most important recent analytical reports for [country] and [sector] are included
- [ ] Official government budget documents and sector strategy documents are identified
- [ ] International data sources (WHO, World Bank, IMF) are included
- [ ] Budget and expenditure data — including subnational data — are identified
- [ ] Political economy and reform history sources are identified (relevant to Step 3)
- [ ] Capacity and digital systems sources are identified (relevant to Step 3)
- [ ] Every source sits in a single running table, numbered sequentially and unbroken across S-1 to S-4
- [ ] Any significant source gaps are flagged before proceeding

> **SOURCES COMPLETE — confirm sources before proceeding to Step 1.**

---

## STEP 1: Chapters 1 & 2 and Annex Step 1

**Skill files:** `01a-chapters1-2.md`, then `01b-annex1.md`

Run all prompts in `01a-chapters1-2.md` in sequence (Prompts 1-01 through 1-11), then continue with `01b-annex1.md` (Prompts 1-12 to 1-15).

> **Economic resilience or another cross-cutting fiscal outcome (macro-fiscal stability, fiscal or debt sustainability):** run Prompts 1-01 to 1-03 as normal, then replace Prompts 1-04 to 1-10 with ER-1-04 to ER-1-10 from `01a-variant-economic-resilience.md` (ER-1-04 to ER-1-06) and `01a-variant-economic-resilience-2.md` (ER-1-07 to ER-1-10), then return to Prompt 1-11 and `01b-annex1.md`. Also run the extra check ER-1-Q5. Record the variant's three template deviations (fiscal-outcome swim lanes; fiscal-cycle narrative and diagram instead of the financial-flows table and diagram; macro-fiscal charts instead of sector-spending charts) for the consistency audit (Prompt C-01).

### Step 1 Completion Gate

Before advancing to Step 2, confirm all of the following:

**Chapter 1**
- [ ] Outcome is framed at the right level of specificity for the country context
- [ ] Purpose statement correctly describes the process and intended use of the report
- [ ] Section structure roadmap matches the structure to be produced

**Section 2.1 — Outcomes and Public Sector Results** *(KEY)*
- [ ] Headline development outcome indicators are accurate and sourced from authoritative data
- [ ] Public sector results reflect actual delivery system performance in [country]
- [ ] Framing is consistent with government's stated policy objectives

**Section 2.2 — Public Sector Challenges** *(MOST CRITICAL in Step 1)*
- [ ] Challenges are the most structurally important constraints — not symptoms
- [ ] Each challenge is distinct and covers a different dimension of the delivery problem
- [ ] Challenges progress from the point of delivery upward through the system
- [ ] No challenge mentions public finance or PFM
- [ ] Number of challenges (3–5) is appropriate for the complexity of the sector
- [ ] Final challenge titles confirmed

**Section 2.3 — Context**
- [ ] All significant organizations are included at correct levels; diagram reviewed
- [ ] All significant financing channels are identified; data is accurate; diagram reviewed *(economic-resilience variant: fiscal-cycle narrative and diagram reviewed instead)*
- [ ] PFM systems description covers all six dimensions (budget formulation, wage execution, non-wage execution, intergovernmental transfers, procurement, audit/accountability, digital systems) *(economic-resilience variant: the four macro-fiscal capabilities instead, and the three template deviations recorded)*
- [ ] Feasibility assessment addresses financial affordability, institutional capability, and stakeholder commitment with specific evidence
- [ ] Every chart in Section 2.3.2 has been locked in by the user, with both an interactive chart and its data table, values carrying Data360 claim tags and a source line

**Annex Tables 1.1 to 1.3**
- [ ] Table 1.1 consistent with Sections 2.1 and 2.2
- [ ] Table 1.2 covers all organizations; no significant actor omitted
- [ ] Table 1.3 lists the same financing channels, values and problems as the Section 2.3.2 flows table

**Reference check**
- [ ] Reference check tables for Chapters 1 and 2 reviewed; every row not verified, partially supported or uncited has been resolved

### Inter-Step Record — Step 1 → Step 2

Record the confirmed challenge titles before proceeding:

```
Challenge 1: 
Challenge 2: 
Challenge 3: 
Challenge 4: 
Challenge 5 (if applicable): 
```

> **STEP 1 COMPLETE — confirm challenges recorded before proceeding to Step 2.**

---

## STEP 2: Chapter 3 and Annex Step 2

**Skill file:** `02-chapter3-annex2.md`

Run all prompts in `02-chapter3-annex2.md` in sequence.
> Note: The session context and source list are already in context — begin directly with Prompt 2-01.

### Step 2 Completion Gate

Before advancing to Step 3, confirm all of the following:

**Section 3.1 — Role of Public Finance**
- [ ] Four-role assessment is specific to [country]'s delivery model — not generic
- [ ] Actual role descriptions are analytically honest and supported by evidence
- [ ] Section correctly foreshadows the bottlenecks that follow

**Bottleneck Analysis — Annex Table 2.2** *(KEY)*
- [ ] Five-why analysis completed for each public sector challenge
- [ ] Bottlenecks are root causes, not symptoms or restatements of the challenge
- [ ] Type classifications (Technical / Institutional / PFM) are correct
- [ ] Impact (H/M/L) and feasibility (H/M/L) ratings are consistent across all bottlenecks

**Consolidated Bottlenecks and Prioritization** *(KEY)*
- [ ] Thematic groupings are appropriate for the country and sector context
- [ ] No bottleneck is so broad as to be unactionable
- [ ] Priority ranking reflects real political economy — not just technical assessments
- [ ] Any out-of-scope bottlenecks flagged as parallel tracks

**Sections 3.2.1 and 3.2.2**
- [ ] Bottleneck codes consistently cross-referenced (B1.1, B2.3, etc.)
- [ ] Each priority bottleneck has a concrete, observable change objective
- [ ] Annex Table 2.3 consistent with Section 3.2.2

**Reference check**
- [ ] Reference check table for Chapter 3 reviewed; every row not verified, partially supported or uncited has been resolved

### Inter-Step Record — Step 2 → Step 3

Record the confirmed priority bottlenecks before proceeding:

```
Number of priority bottlenecks: 
Bottleneck 1: [title] | Change objective: 
Bottleneck 2: [title] | Change objective: 
Bottleneck 3: [title] | Change objective: 
Bottleneck 4: [title] | Change objective: 
Bottleneck 5: [title] | Change objective: 
Bottleneck 6: [title] | Change objective: 
```

> **STEP 2 COMPLETE — confirm bottlenecks recorded before proceeding to Step 3.**

---

## STEP 3: Chapters 4 & 5 and Annex Step 3

**Skill files:** `03a-reform-results.md`, then `03b-stakeholders-systems-steps.md`, then `03c-conclusion-compilation.md`

Run all prompts in `03a-reform-results.md` in sequence (Prompts 3-01, 3-02 × n, 3-03, 3-04 × n, 3-05), then `03b-stakeholders-systems-steps.md` (Prompts 3-06 to 3-10, 3-11 × n, 3-12), then `03c-conclusion-compilation.md` (Prompts 3-13 and 3-14).
> Note: The session context and source list are already in context — begin directly with Prompt 3-01.

> **Critical sequencing:** Complete and confirm Annex Table 3.1 (Prompts 3-02 × n and 3-03, then check 3-Q5) **before** beginning Section 4.1 drafts (Prompts 3-04 × n and 3-05). The reform results in Table 3.1 are the authoritative source for all Section 4.1 content.

### Step 3 Completion Gate

Before advancing to Compilation and QA, confirm all of the following:

**Annex Table 3.1** *(must be confirmed before Section 4.1)*
- [ ] Every sub-bottleneck has a row with specific, evidence-based underlying causes, distilled from a multi-branch five-whys into root-cause families
- [ ] Every root-cause family is addressed by a reform and every reform traces to a cause (check 3-Q5 passed)
- [ ] All key stakeholders named at organizational level — not generic actor types
- [ ] Every reform result is a concrete, measurable end-state with a feasibility rating
- [ ] Table stands alone as a self-explanatory reference document

**Section 4.1 — Reforms to Deliver Change Objectives** *(KEY)*
- [ ] Total number of reform results is within range (ideally 15–25)
- [ ] Feasibility ratings consistent with Annex Tables 2.2 and 2.3
- [ ] All cross-references to Annex Table 3.1 are correctly placed
- [ ] Change objective sub-section titles use the positive outcome statement — not the bottleneck problem description

**Section 4.2 — Stakeholder Strategy**
- [ ] Main political economy challenges identified and addressed with specific strategies
- [ ] No major reform result left without an identified authorizer and team leader
- [ ] Annex Tables 3.2 and 3.3 correctly cross-referenced

**Annex Table 3.5 — Key Steps**
- [ ] Exactly three steps per reform result, correctly sequenced
- [ ] Timing consistent with feasibility ratings
- [ ] No single organization has an unrealistic number of simultaneous lead responsibilities
- [ ] Implementation horizon applied consistently throughout

**Chapter 5 — Conclusion**
- [ ] Feasibility counts (H/M/L) accurate
- [ ] Low-feasibility reforms named explicitly with specific political economy strategies
- [ ] Scope boundary correctly and completely stated
- [ ] Concluding paragraph connects reform objectives back to the development outcome

**Reference check**
- [ ] Reference check tables for Chapters 4 and 5 reviewed; every row not verified, partially supported or uncited has been resolved

### Inter-Step Record — Step 3 → Compilation and QA

Record the following before proceeding:

```
Total reform results: 
High-feasibility results: [list result numbers]
Medium-feasibility results: [list result numbers]
Low-feasibility results: [list result numbers]
Implementation horizon: [start year] to [end year]
Authors: 
Report date: 
```

> **STEP 3 COMPLETE — confirm values recorded before proceeding to Compilation and QA.**

---

## COMPILATION AND QA: Final Compilation and Quality Assurance

**Skill files:** `04a-audit-and-part1.md`, then `04b-part2-and-annex.md`, then `04c-cross-document-qa.md`

> **Start with the consistency audit (Prompt C-01) before any compilation step.** Resolve all identified discrepancies before proceeding to Prompt C-02.

> **Economic-resilience variant:** if the Section 2.3 variant prompts were used in Step 1, give the audit the three recorded template deviations (fiscal-outcome swim lanes; fiscal-cycle narrative and diagram in place of the financial-flows table and diagram; macro-fiscal charts in place of sector-spending charts) so it treats them as intended substitutions, not inconsistencies.

> **Institutional platform:** add the source-availability item from `manager-platform.md` to the audit (Prompt C-01) and apply its bibliography rule in Prompt C-09, so every citation is checked against the Status column of the running source table.

Run all prompts in `04a-audit-and-part1.md` in sequence (Prompts C-01 to C-05), then `04b-part2-and-annex.md` (Prompts C-06 to C-13), then `04c-cross-document-qa.md` (Prompts QA-1 to QA-5).
### Compilation and QA Completion Gate

Before treating the report as complete, confirm all of the following:

**Pre-Compilation Audit**
- [ ] All reform result codes, titles, and feasibility ratings are identical wherever they appear
- [ ] All bottleneck codes (e.g. B2.3) match between Chapter 3 and Annex Table 2.2
- [ ] Public sector challenge titles are consistent across all chapters and annexes
- [ ] Stakeholder names are consistent throughout (abbreviations follow a single convention)
- [ ] All citations are hyperlinked to their source, e.g. ([World Bank, 2010](url))

**Main Report Part 1**
- [ ] Executive summary accurately represents the entire report in plain language
- [ ] Table of contents is complete and correctly numbered
- [ ] All cross-references to Part 2 and Annex are correct

**Main Report Part 2**
- [ ] Four-role structure (3.1.1–3.1.4) maintained with standard headings
- [ ] All reform result numbers in Chapter 4 match Annex Tables 3.1 and 3.5
- [ ] Chapter 5 feasibility summary matches Section 4.1 summary table
- [ ] Bibliography complete; every in-text citation has a bibliography entry

**Annex**
- [ ] Tables 1.1 to 1.3 consistent with Chapter 2
- [ ] Tables 2.2 and 2.3 consistent with Chapter 3; every bottleneck in 2.2 accounted for in 2.3
- [ ] Table 3.1 consistent with Section 4.1
- [ ] Table 3.5 consistent with Sections 4.2 and 4.3; three steps per reform result throughout

**Cross-Document QA (Prompts QA-1 to QA-5)**
- [ ] Reform result codes consistent across all three documents
- [ ] Challenge titles consistent across all three documents
- [ ] Outcome and spending data internally consistent
- [ ] Annex completeness confirmed
- [ ] Executive summary and Chapter 5 plain language reviewed

> **REPORT COMPLETE** when all boxes are checked.

---

## Context Length Advisory

If the AI loses track (wrong codes, inconsistent challenge titles), ask it to list the Section 2.2 challenges verbatim. If drift is severe, save the Step 1–3 outputs, restart the session, re-upload, and jump to Compilation and QA.
