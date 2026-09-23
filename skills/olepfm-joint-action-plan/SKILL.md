---
name: olepfm-joint-action-plan
title: OLePFM Joint Action Plan Compiler
description: Compiles a Joint Action Plan (JAP) from two or more OLePFM sector diagnostic reports (the reports produced by the olepfm-session-manager skill), following the bundled OLePFM Joint Action Plan Annotated Skeleton Template and one or both PFM reform frameworks. Use this whenever the user asks to compile, draft, synthesise or structure a joint action plan, joint reform agenda, joint reform plan or multi-sector reform strategy from OLePFM sector diagnoses, even if they do not say "JAP". Trigger phrases include "compile a joint action plan from these diagnostic reports", "synthesise these OLePFM reports into a joint strategy", "draft a joint reform agenda from these sector diagnoses" and "prepare a multi-sector action plan using the OLePFM approach".
---

# OLePFM Joint Action Plan Compiler

Based on the OLePFM Joint Action Plan Compiler, version 5 (September 2026).

## What this skill does

This skill guides the compilation of a Joint Action Plan (JAP) from multiple OLePFM (Outcome-Led PFM Reform) sector diagnostic reports. It follows an eight-task process and produces a document that:

- synthesises the bottlenecks and reform actions from multiple sector diagnostics into a single, jointly-owned reform agenda;
- follows the structure and formatting conventions set out in the **OLePFM Joint Action Plan Annotated Skeleton Template** (bundled in `assets/`);
- uses one or both of two PFM reform frameworks to organise its objectives and reform results, depending on the sectors and outcomes in scope;
- is grounded in evidence and language from the sector diagnostics, so that stakeholders who participated in those processes recognise their work in the joint document.

It sits downstream of the `olepfm-session-manager` skill: that skill produces one Sector Reform Design Report per sector; this one compiles several of them into the joint plan (sub-step 3.3 of the OLePFM process, for a multi-sector engagement).

**Two vocabularies, by design.** The sector reports speak of *change objectives*, *reform results* and *key steps*. The JAP speaks of *Objectives*, *Reform Results* and *Actions*. Keep each document's own terms; do not "correct" one into the other.

## Documents

| Document | Where | Role |
|---|---|---|
| Annotated Skeleton Template | `assets/joint-action-plan-template.md` (bundled) | The master guide for structure, section content, length and formatting. Every section of the JAP follows it. Read the annotation for a section before drafting that section. |
| Sector diagnostic reports (two or more) | Provided by the user | The evidence base. Normally OLePFM Sector Reform Design Reports produced with the `olepfm-session-manager` skill. |
| OLePFM Synthesis Handbook (*Making Public Resources Count for Development*) | Provided by the user | The methodological backbone: outcome-led framing, theory of change concepts and reform design principles. |

If the reports or the Handbook are not in the conversation, ask for them. Do not begin extraction or drafting until all source reports are confirmed.

## Reference files

- `references/reform-frameworks.md`: the two PFM reform frameworks, how to choose between them and how to combine them. Read it at Task 4.
- `references/task-checklists.md`: the extraction map keyed to the report's sections and annex tables, the bottleneck synthesis table, the gap-analysis formats and the finalisation checklist. Read the relevant section at Tasks 1, 3, 6 and 8.

## The eight tasks

The tasks are numbered Task 1 to Task 8 so they cannot be confused with the OLePFM Steps 1 to 5 used by the sector reports.

### Task 1 — Gather and extract from the source reports

Confirm with the user before starting:

- which sector diagnostic reports are available, and ask for any not yet in the conversation;
- the country or region, and the name of the national PFM strategy or reform process the JAP should feed into;
- whether supplementary sources should be searched (the World Bank intranet where available, and the web) or whether to work from the provided documents only.

Then read each report and extract the items in the extraction map (`references/task-checklists.md`, section 1): outcomes and public sector results, the challenges, the priority bottlenecks with their causes, ratings, stakeholders and change objective, the change objectives with their reform results and reforms, the Annex Table 3.1 matrix, the Annex Table 3.5 key steps, and the systems, capacity and TA content. Produce a structured internal summary of each sector's content before proceeding. Keep it internal unless the user asks to see it.

### Task 2 — Search for supplementary context (only if authorised in Task 1)

Search for: recent PFM assessments for the country (PEFA, public expenditure reviews, fiduciary risk assessments); intergovernmental fiscal transfer and local government financing data; local authority performance assessments or equivalent; the national development strategy and PFM strategy; and relevant World Bank project documentation (local governance, service delivery, fiscal management operations). Summarise the findings for the user, saying which sources will be drawn on and for which sections. These sources mainly ground Sections A and B: the introduction, reform context and problem statement.

### Task 3 — Synthesise common bottlenecks

Read across all sector extractions to identify bottlenecks that appear in two or more reports. For each cross-cutting cluster: name it in clear, non-technical language stakeholders will recognise; list the sectors it appears in, with the sector-specific manifestation and precise figures from each report; note the common underlying causes; and note sector-specific bottlenecks that do not cut across sectors, which will become sector-specific reform results or actions rather than cross-sectoral objectives.

Present the synthesis to the user as a table (format in `references/task-checklists.md`, section 2) and invite confirmation that the clustering is correct and complete. This is the foundation of Section B and must be agreed before drafting begins.

### Task 4 — Select the reform framework and design the objective and reform result structure

Read `references/reform-frameworks.md`. Both frameworks use the hierarchy **Objective** (top-level grouping) → **Reform Result** (the specific change sought within it). Choose Framework 1 (PFM for Service Delivery), Framework 2 (PFM for Jobs and Resilience) or a combination according to the sectors in scope, consolidating overlaps when combining. Present the proposed objective and reform result structure to the user for approval before drafting. If the choice is not clear, present both frameworks with a brief explanation and ask.

### Task 5 — Draft the Joint Action Plan

Use the skeleton template in `assets/` as the master guide for every section: structure, content, length and formatting. Read the annotation for each section before drafting it. The document runs cover page, table of contents, abbreviations, Sections A to F and bibliography; it has no annexes.

Rules that go beyond what the template states:

- **Problem paragraphs** in Sections B and D are drawn directly from the sector reports, with precise figures and bracketed citations (for example [MoH 2024], [PEFA 2026]), so that stakeholders recognise their own diagnosis.
- **The reform result** in each Section D block is one bolded sentence stating the desired end-state.
- **Action tables** have four columns: # | Action | Responsible | Timeframe. Cross-sectoral actions are numbered 1.1.1, 1.1.2; sector-specific actions carry a sector suffix such as 1.1.H, 1.1.E, 1.1.A. Timeframes are Year 1, Year 1–2 and so on, never calendar years.
- **Section E.II** (systems, capacity and TA) is drawn from each report's Section 4.3 and Annex Table 3.4, and every item is linked to the reform results it enables. If a report has no such content, infer the requirements from its reform actions.
- **Section E.V** names the actual programmes, strategies and projects the JAP coordinates with; generic language is not sufficient.
- **Section F** uses cross-sectoral indicators only, with every baseline marked TBD and a note that baselines will be established through a joint assessment at the start of implementation.

### Task 6 — Cross-check completeness against the source reports

Before presenting the draft, compare the JAP against each sector report and list: (a) gaps, bottlenecks or problems in the reports that the JAP does not address; (b) missing actions, reforms proposed in the reports that the JAP does not capture; and (c) additions, content in the JAP that is not grounded in the reports, flagged either as an appropriate system-level cross-sectoral enabler to retain or as going beyond the evidence base for the user to decide. Use the formats in `references/task-checklists.md`, section 3. Present the gap analysis with recommendations and wait for the user's decisions before Task 7.

### Task 7 — Revise and iterate

Incorporate the user's decisions and feedback. Edit the draft in place for targeted changes to sections, paragraphs, action rows or indicator rows; redraft from scratch only if the user asks for a reorganisation affecting more than half the document. Track which version is current and confirm the version number with the user after each revision cycle.

### Task 8 — Finalise

Run the finalisation checklist in `references/task-checklists.md`, section 4, before delivering the document.

## Edge cases

| Situation | How to handle |
|---|---|
| Fewer than three sector reports | Proceed, but flag that the synthesis is less robust and that the JAP will need updating as further diagnoses are completed |
| Reports using a different or older OLePFM template | Adapt the extraction to the format used and map everything to the same synthesis framework in Task 3 |
| User wants to include sectors without a completed diagnosis | Note them as "diagnosis in preparation" in Section A and Box 1, and flag that inclusion requires a later update |
| Five or more sector reports | Limit objectives to three or four and reform results to eight to twelve; group closely related bottlenecks rather than creating a reform result for each |
| Framework choice is ambiguous | Present both frameworks with a brief explanation and ask the user to confirm before proceeding |
| A report has no systems, capacity or TA content | Infer the requirements from the reform actions proposed under each change objective and use them for Section E.II |

## Terminology

| Use in the JAP | Do not use |
|---|---|
| Objective | Pillar, Theme |
| Reform Result | Sub-Pillar, Objective (at this level) |
| Action | Reform, Intervention |
| Framework 1 / Framework 2 | MPA 1 / MPA 2 |
