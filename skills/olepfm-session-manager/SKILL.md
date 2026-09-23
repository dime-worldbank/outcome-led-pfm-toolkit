---
name: olepfm-session-manager
title: OLePFM Session Manager
description: Orchestration guide for producing a complete OLePFM Sector Reform Design Report in a single AI session. Upload first. Controls phase sequencing, intervention points, inter-phase data recording, and AI behavior rules across all four phases. Also prepares the Working Tables for a reform design workshop when the user says "start OLePFM workshop preparation" or asks for workshop tables. Use for any OLePFM, outcome-led PFM or sector reform design report or workshop request.
---

# OLePFM Sector Reform Design: Session Manager

This document is the orchestration guide for producing a complete OLePFM Sector Reform Design Report in a single AI session. Upload it together with the nine skill files and the reference documents at the start of the session.

---

## TWO WAYS TO USE THIS SKILL

| Mode | When | Follow |
|---|---|---|
| **Full report** | The user wants an OLePFM Sector Reform Design Report | This document, from Session Setup through Phase 4 |
| **Workshop table preparation** | The user says "start OLePFM workshop preparation" or wants the Working Tables for a reform design workshop | `manager-workshop.md` (in `references/`). It reuses Session Setup Step 2 and Phase 0 from this document and a subset of the Phase 1 and 2 prompts, then stops after Table 2.1 and scaffolds the rest blank |

Workshop mode is an overlay on the report workflow, not a separate process: the instructions to the AI below (sequential execution, one prompt at a time, pause at every ✏️ point, never invent placeholder values) apply in both modes.

---

## INSTRUCTIONS TO THE AI

You are assisting with the production of an OLePFM Sector Reform Design Report. Follow these rules throughout the session:

1. **Sequential execution only.** Work through Phases 0–4 in strict order. Do not begin a new phase until the user explicitly says "proceed to Phase [n+1]" or equivalent.

2. **One prompt at a time.** Run each numbered prompt individually; after each output, wait for the user before the next. Do not chain prompts.

3. **Pause at every ✏️ intervention point.** After every prompt that has a ✏️ marker, output a block in this shape before stopping — plain Markdown, not a `>` blockquote (which breaks the checkboxes):

   **✏️ Review the output — focus on these points**

   **[topic]** — [one line on why it matters, drawn from the instruction text before the prompt].

   - [ ] [check 1]
   - [ ] [check 2]
   - [ ] [check 3]

   Say "proceed" when satisfied, or provide corrections.

   Show all checks as one checklist, from the skill's ✏️ block.

4. **Declare phase completion.** At the end of each phase, output:

   > **PHASE [n] COMPLETE**
   > Please review the Phase [n] completion gate below before I proceed to Phase [n+1].

5. **Record inter-phase data.** At the specified points, ask the user to confirm the recorded values before proceeding. These values carry forward across phases.

6. **Do not invent or skip.** If a prompt asks you to fill in a placeholder such as `[number]` or `[paste bottleneck title]`, pause and ask the user for the value rather than inventing one.

---

## SESSION SETUP

### Pre-loaded Reference Documents

These are held in the **root folder of the knowledge base** (alongside the skills folder, not inside it) and available to the AI by default. **Do not upload them again.** Verify access with the setup verification prompt below before starting.

| Document | Where it is stored |
|---|---|
| OLePFM Sector Reform Design Report Template | Knowledge base — root folder |
| OLePFM Synthesis Handbook (Williamson et al., 2024) | Knowledge base — root folder |
| Sector Outcome Notes and prior diagnostic reports | Backend library — searched by sector |

> **If the AI cannot find them:** the stored file name may differ from the title — have it list the root files and match on keywords, not an exact title.

> **In this repository:** the Report Template is `assets/report-template.md` beside this SKILL.md. Read it whenever a prompt says "using the OLePFM Sector Reform Design Report Template". The Synthesis Handbook and sector notes are not in the repository; ask the user to provide them.

### Documents to Upload Per Session

Upload these at the start of each session:

| Document | Required |
|---|---|
| A sector note you hold | Only if the chosen sector is not covered on the backend |
| Working Tables (for a workshop) | Prepared beforehand with `manager-workshop.md`; not a report input |

### Skill Files

The skill files (`00-source-prep.md` through `04c-cross-document-qa.md`) are in the knowledge base's skills folder, accessible by default — no upload required. In this repository they are the files in the `references/` folder beside this SKILL.md.

### Step 1: Setup Verification

Paste the following to confirm the pre-loaded documents are accessible:

---

Please confirm you can access these pre-loaded documents, both stored in the **root folder of the knowledge base** (alongside the skills folder, not inside it):

1. OLePFM Sector Reform Design Report Template
2. OLePFM Synthesis Handbook (Williamson et al., 2024)

If either does not appear at first, search the root again on title keywords alone — "Sector Reform Design Report Template" and "Synthesis Handbook" — as the stored file name may differ. For each, state whether you can access it, its title, and the file name it is stored under. If either is still missing, list the file names you can see at the root, then stop and alert the user before proceeding.

---

> **Do not proceed to Step 2 until the AI confirms both documents are accessible.**

### Step 2: Establish Session Context (two steps)

The AI collects session context in **two short steps — first country and sector, then the development outcome.**

Once setup is verified, paste the following as your **next message**:

---

I am ready to establish the session context for an Outcome-Led PFM Reform Diagnosis and Design Report. Run the two-step setup: ask my **country** and **sector** — a standard sector from the Sector Outcome Reference below, or another — then establish and confirm its **development outcome** and **public sector result**. The Report Template, Synthesis Handbook, and the sector notes and prior reports are pre-loaded on the backend.

Do not proceed to Phase 0 until I have confirmed the country, sector and outcome.

---

**AI behavior for this step:**

1. **Ask for country and sector first — nothing else.** Present the standard sectors from the Sector Outcome Reference below as the options, and note the user may instead name a **sector not listed there**. **Revenue Mobilization** is a cross-cutting enabler, not a standalone sector — offer it only alongside one of the other five, never on its own. Wait for the user's answer.

2. **Establish the outcome for that sector.** Draft the **development outcome** and **public sector result** from the best available guide, searching in this order:
   1. a **Sector Outcome Note or analytical report** for the sector on the backend — search the knowledge base for this first;
   2. a **previous OLePFM diagnostic report for the same sector** in another country, on the backend;
   3. the **Synthesis Handbook**, if the sector is one it covers — and, for a standard sector, its entry in the Sector Outcome Reference below.

   If none exists — the sector is not in the Synthesis and nothing matches on the backend — ask the user to **upload a sector note if they have one**; if not, **proceed without a guide, following the OLePFM framework as closely as possible**. Then ask the user to confirm the framing, or narrow it to what matters most for their country.

3. **Lock the context.** Once the user confirms, restate it in this form (plain Markdown, no blockquote), then confirm readiness for Phase 0:

   **Session context confirmed:**

   - **Country:** [country]
   - **Sector:** [sector]
   - **Development outcome:** [outcome]
   - **Public sector result:** [public sector result]

   Referred to as [country], [sector] and the development outcome in all prompts from here on. Ready to begin **Phase 0: Source Preparation**.

### Sector Outcome Reference

For a listed sector, use its entry below; for a sector not listed, build the outcome as in Step 2.

**Health — "Ensuring Healthy Lives"**
- **Development outcome:** Healthy lives and well-being for all at all ages, delivered through universal health coverage (UHC).
- **Public sector result:** Progress toward UHC via primary health services — access to quality essential healthcare, plus access to safe, effective, affordable essential medicines and vaccines for all.

**Education — "Achieving Quality Basic Education for All"**
- **Development outcome:** Universal quality basic education providing functional numeracy and literacy for all learners (measured by learning assessments).
- **Public sector result:** Increased access and completion rates, and improved education quality, equitably delivered across genders, locations, and socio-economic groups.

**Economic Resilience — "Building Economic Resilience"**
- **Development outcome:** A resilient economy (growth in output per capita over the business cycle) that sustains growth while reducing vulnerability to shocks.
- **Public sector result:** Building and preserving fiscal space through sound management of the fiscal balance, revenues, expenditure, and debt — enabling counter-cyclical responses to shocks.

**Gender — "Eliminating Gender-Based Violence (GBV)"**
- **Development outcome:** Eliminate all forms of GBV, particularly intimate partner violence (IPV).
- **Public sector result:** Prevention (norms/behavioral change at individual, societal, institutional levels); integrated survivor-centered support services; accountability for perpetrators; and support to organizations addressing GBV.

**Energy — "Accelerating the Transition to Renewable Energy"**
- **Development outcome:** Adequate, accessible, and affordable power supply generated primarily through renewable sources.
- **Public sector result:** Timely, adequate public or private investment to achieve renewable generation, transition, accessibility, and affordability that can be sustained.

**Revenue Mobilization — "Mobilizing Revenue in Support of Policy Objectives"** *(enabler for the others, not a standalone sector)*
- **Development outcome:** Sufficient revenues raised in ways that support the government's broader economic and social policy objectives.
- **Public sector result:** Tax administration that raises adequate resources efficiently and equitably, with the capacity to forecast and manage revenue so budgets are realistic.

---

## PHASE 0: Source Preparation

**Skill file:** `00-source-prep.md`

Run prompts S1 through S4 from `00-source-prep.md` in sequence.

### Phase 0 Completion Gate

Before advancing to Phase 1, confirm all of the following:

- [ ] The most important recent analytical reports for [country] and [sector] are included
- [ ] Official government budget documents and sector strategy documents are identified
- [ ] International data sources (WHO, World Bank, IMF) are included
- [ ] Budget and expenditure data — including subnational data — are identified
- [ ] Political economy and reform history sources are identified (relevant to Phase 3)
- [ ] Capacity and digital systems sources are identified (relevant to Phase 3)
- [ ] Every source sits in a single running table, numbered sequentially and unbroken across S1–S4
- [ ] Any significant source gaps are flagged before proceeding

> **PHASE 0 COMPLETE — confirm sources before proceeding to Phase 1.**

---

## PHASE 1: Chapters 1 & 2 and Annex Step 1

**Skill files:** `01a-chapters1-2.md`, then `01b-annex1.md`

Run all prompts in `01a-chapters1-2.md` in sequence (A1 through B5), then continue with `01b-annex1.md` (C1, C2 and D1).
### Phase 1 Completion Gate

Before advancing to Phase 2, confirm all of the following:

**Chapter 1**
- [ ] Outcome is framed at the right level of specificity for the country context
- [ ] Purpose statement correctly describes the process and intended use of the report
- [ ] Section structure roadmap matches the structure to be produced

**Section 2.1 — Outcomes and Public Sector Results** *(KEY)*
- [ ] Headline development outcome indicators are accurate and sourced from authoritative data
- [ ] Public sector results reflect actual delivery system performance in [country]
- [ ] Framing is consistent with government's stated policy objectives

**Section 2.2 — Public Sector Challenges** *(MOST CRITICAL in Phase 1)*
- [ ] Challenges are the most structurally important constraints — not symptoms
- [ ] Each challenge is distinct and covers a different dimension of the delivery problem
- [ ] Challenges progress from the point of delivery upward through the system
- [ ] No challenge mentions public finance or PFM
- [ ] Number of challenges (3–5) is appropriate for the complexity of the sector
- [ ] Final challenge titles confirmed

**Section 2.3 — Context**
- [ ] All significant organizations are included at correct levels; diagram reviewed
- [ ] All significant financing channels are identified; data is accurate; diagram reviewed
- [ ] PFM systems description covers all six dimensions (budget formulation, wage execution, non-wage execution, intergovernmental transfers, procurement, audit/accountability, digital systems)
- [ ] Feasibility assessment addresses financial affordability, institutional capability, and stakeholder commitment with specific evidence

**Annex Tables 1.1 and 1.2**
- [ ] Table 1.1 consistent with Sections 2.1 and 2.2
- [ ] Table 1.2 covers all organizations; no significant actor omitted

### Inter-Phase Record — Phase 1 → Phase 2

Record the confirmed challenge titles before proceeding:

```
Challenge 1: 
Challenge 2: 
Challenge 3: 
Challenge 4: 
Challenge 5 (if applicable): 
```

> **PHASE 1 COMPLETE — confirm challenges recorded before proceeding to Phase 2.**

---

## PHASE 2: Chapter 3 and Annex Step 2

**Skill file:** `02-chapter3-annex2.md`

Run all prompts in `02-chapter3-annex2.md` in sequence.
> Note: The session context and source list are already in context — begin directly with Prompt B1.

### Phase 2 Completion Gate

Before advancing to Phase 3, confirm all of the following:

**Section 3.1 — Role of Public Finance**
- [ ] Four-role assessment is specific to [country]'s delivery model — not generic
- [ ] Actual role descriptions are analytically honest and supported by evidence
- [ ] Section correctly foreshadows the bottlenecks that follow

**Bottleneck Analysis — Annex Table 2.2** *(KEY)*
- [ ] Five-why analysis completed for each public sector challenge
- [ ] Bottlenecks are root causes, not symptoms or restatements of the challenge
- [ ] Type classifications (Technical / Institutional / PFM) are correct
- [ ] Impact (VH/H/M/L) and feasibility (H/M/L) ratings are consistent across all bottlenecks

**Consolidated Bottlenecks and Prioritization** *(KEY)*
- [ ] Thematic groupings are appropriate for the country and sector context
- [ ] No bottleneck is so broad as to be unactionable
- [ ] Priority ranking reflects real political economy — not just technical assessments
- [ ] Any out-of-scope bottlenecks flagged as parallel tracks

**Sections 3.2.1 and 3.2.2**
- [ ] Bottleneck codes consistently cross-referenced (B1.1, B2.3, etc.)
- [ ] Each priority bottleneck has a concrete, observable change objective
- [ ] Annex Table 2.3 consistent with Section 3.2.2

### Inter-Phase Record — Phase 2 → Phase 3

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

> **PHASE 2 COMPLETE — confirm bottlenecks recorded before proceeding to Phase 3.**

---

## PHASE 3: Chapters 4 & 5 and Annex Step 3

**Skill files:** `03a-reform-results.md`, then `03b-stakeholders-systems-steps.md`, then `03c-conclusion-compilation.md`

Run all prompts in `03a-reform-results.md` in sequence (B1, T1 × n, T2, C1 × n, C2), then `03b-stakeholders-systems-steps.md` (D1–D3, E1, E2, F1 × n, F2), then `03c-conclusion-compilation.md` (G1 and H1).
> Note: The session context and source list are already in context — begin directly with Prompt B1.

> **Critical sequencing:** Complete and confirm Annex Table 3.1 (Prompts T1 × n and T2) **before** beginning Section 4.1 drafts (Prompts C1 × n and C2). The reform results in Table 3.1 are the authoritative source for all Section 4.1 content.

### Phase 3 Completion Gate

Before advancing to Phase 4, confirm all of the following:

**Annex Table 3.1** *(must be confirmed before Section 4.1)*
- [ ] Every sub-bottleneck has a row with specific, evidence-based underlying causes
- [ ] All key stakeholders named at organizational level — not generic actor types
- [ ] Every reform result is a concrete, measurable end-state with a feasibility rating
- [ ] Table stands alone as a self-explanatory reference document

**Section 4.1 — Change Objectives and Reform Results** *(KEY)*
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

### Inter-Phase Record — Phase 3 → Phase 4

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

> **PHASE 3 COMPLETE — confirm values recorded before proceeding to Phase 4.**

---

## PHASE 4: Final Compilation and Quality Assurance

**Skill files:** `04a-audit-and-part1.md`, then `04b-part2-and-annex.md`, then `04c-cross-document-qa.md`

> **Start with the consistency audit (Prompt A1) before any compilation step.** Resolve all identified discrepancies before proceeding to M1a.

Run all prompts in `04a-audit-and-part1.md` in sequence (A1, M1a–M1d), then `04b-part2-and-annex.md` (M2a–M2d, AN1–AN4), then `04c-cross-document-qa.md` (QA1–QA5).
### Phase 4 Completion Gate

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
- [ ] Tables 1.1 and 1.2 consistent with Chapter 2
- [ ] Tables 2.2 and 2.3 consistent with Chapter 3; every bottleneck in 2.2 accounted for in 2.3
- [ ] Table 3.1 consistent with Section 4.1
- [ ] Table 3.5 consistent with Sections 4.2 and 4.3; three steps per reform result throughout

**Cross-Document QA (QA1–QA5)**
- [ ] Reform result codes consistent across all three documents
- [ ] Challenge titles consistent across all three documents
- [ ] Outcome and spending data internally consistent
- [ ] Annex completeness confirmed
- [ ] Executive summary and Chapter 5 plain language reviewed

> **REPORT COMPLETE** when all boxes are checked.

---

## Context Length Advisory

If the AI loses track (wrong codes, inconsistent challenge titles), ask it to list the Section 2.2 challenges verbatim. If drift is severe, save the Phase 1–3 outputs, restart the session, re-upload, and jump to Phase 4.