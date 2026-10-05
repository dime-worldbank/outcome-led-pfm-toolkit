---
title: OLePFM Workshop Table Preparation
description: Produces the Working Tables document a reform design workshop starts from. Establishes context and sources, then pre-populates the framing tables through 2.1 — Outcomes/Results/Challenges (1.1), Organizational Functions (1.2), Main Financing Channels (1.3), Roles of Public Finance (2.1) — using the standard generation prompts, and lays out 2.2 through 3.5 as blank exercise tables with facilitation notes for the workshop to complete, then renders the whole set into the OLePFM Sector Reform Design Report Word template so the handout carries the template's cover, landscape annex tables and footer. Use when preparing tables for an upcoming workshop; it reuses the Step 1 and Step 2 generation prompts and changes nothing in them. Trigger by saying "start OLePFM workshop preparation".
---

# OLePFM Workshop Table Preparation

Use this to produce the **Working Tables** document a reform design workshop starts from. The AI pre-populates the framing tables **through 2.1** from desk research; **2.2 onward are left blank** — those are the workshop's own exercises. It reuses the generation prompts in the Step 1 and Step 2 prompt files (`01a`, `01b`, `02`) and changes nothing in them. The handout is delivered as a Word document rendered into the Report template's annex section (step 5), the same way Prompt C-14 renders the full report. `manager.md` is the session manager's SKILL.md; the prompt files are the `manager-00` to `manager-04c` files beside it.

The workshop reviews 1.1–2.1 and fills in 2.2 onward; the completed tables then inform the report drafted with the standard workflow (`manager.md`).

## Opening prompt

To start, say **start OLePFM workshop preparation** — no need to name the country or sector; the AI will ask. That is equivalent to pasting:

---

I want to prepare the OLePFM Working Tables for an upcoming reform design workshop. Guide me through it: first ask me for the country and sector, then pre-populate the framing tables through 2.1 and leave 2.2 onward as blank exercises for the workshop.

---

## Steps

1. **Set up.** Run Setup 1 in `manager-setup.md` first and stop if it fails: it confirms that the Report Template Word file, which step 5 clones, and the Synthesis Handbook are accessible. Then establish country, sector and development outcome as in Setup 2 of the same file (including the off-list sourcing order), then run source preparation (`manager-00-source-prep.md`, Prompts S-1 to S-4). On the institutional platform, also run Prompt S-5 from `manager-platform.md` and apply its citation rules. Cite sources as hyperlinked parentheticals.

2. **Populate 1.1–2.1.** Generate each table with the existing prompt, append its reference check table (`manager-reference-check.md`) and resolve every not-reachable, not-verified or uncited row, then lay it out in the Working Tables format with a short **facilitation note** for the workshop:

   | Table | Columns | Generate with | Facilitation note |
   |---|---|---|---|
   | **1.1 Outcomes, Public Sector Results and Challenges** | stacked blocks — Development Outcome · Public Sector Results · Selected Public Sector Challenges | Prompts 1-02 (Section 2.1) + 1-03 (Section 2.2) | *Pre-populated by AI. Review; agree preferably three and no more than five challenges — a challenge must not mention money.* |
   | **1.2 Organizational Functions in Policy, Delivery and PFM** | Organization · Level of Government · Policy & Delivery Functions · PFM Functions | Prompt 1-13 (with 1-05) | *Pre-populated by AI. Validate; add any missing organizations.* |
   | **1.3 Main Financing Channels** | Financing Channel · Description & Purpose · Organizations (flow of funds) · Relative Value · Key Problems | Prompt 1-14 (from the Section 2.3.2 flows table, Prompt 1-08) | *Pre-populated by AI. Review the channels, values and problems.* |
   | **2.1 Roles of Public Finance** | Role · Potential Role · Actual Role | Prompt 2-02 (the four roles) | *Pre-populated by AI. Read before identifying challenges; validate the potential and actual roles.* |

   Pause here for the user to review the populated 1.1–2.1 and their reference check tables before the blank scaffold is added.

3. **Scaffold 2.2 onward (blank).** Add the remaining sections as **empty tables — column headers and a workshop-exercise note only, no AI content:**

   | Table | Columns | Workshop exercise note |
   |---|---|---|
   | **2.2 Public Sector Challenges and Bottlenecks** | Public Sector Challenges · Bottlenecks which Contribute to Public Sector Challenges · Type of Bottleneck · Impact on Service Delivery (H/M/L) · Feasibility of Reform (H/M/L) | *For each challenge, identify the bottlenecks that cause it (five-why).* |
   | **2.3 Priority PFM Bottlenecks** | Bottleneck · Impact on Delivery (contribution to public sector challenges) · Feasibility of Change (rating + description) · Relevant Bottlenecks (from Table 2.2) | *Consolidate and prioritize the bottlenecks.* |
   | **3.1 Causal Analysis of Bottlenecks and Proposed Reforms** | Sub-Bottlenecks (problems) · Underlying Causes · Stakeholders · Reform Result (Resolved Problem) · Reforms Required (which address causes) | *For each priority bottleneck, analyse causes and propose reforms.* |
   | **3.2 Key Stakeholders in Reform** | Type · Members · Role | *Map authorizers, team leaders, results team, coalition.* |
   | **3.3 Stakeholder Management Strategy** | Stakeholder · Change Objective(s) · Commitment (H/M/L) · Power to Block (H/M/L) · Source of Interest or Resistance · Motivation Strategy | *Plan how to move each key stakeholder.* |
   | **3.4 Technical Assistance, Digital Systems and Capacity Support** | Name · Description of Changes Required to Address Bottlenecks · Lead Organization · Relevant Change Objectives · Timeframe | *List the systems, capacity and TA each reform needs.* |
   | **3.5 Key Steps to Achieve Results (Action Plan)** | Reform Result · Key Steps to Achieve Results · Timing · Responsible | *Three key steps per reform result, sequenced with timing.* |

4. **Assemble.** Assemble one Working Tables document — **Step 1** (1.1, 1.2, 1.3), **Step 2** (2.1 populated; 2.2, 2.3 blank), **Step 3** (3.1–3.5 blank) — following the OLePFM Working Tables layout, and show it to the user for a last content check before rendering.

5. **Render into the Word template and hand off.** The file the workshop fills in and returns is a Word document on the official OLePFM Sector Reform Design Report template, whose landscape annex section already draws Tables 1.1 to 3.5 in the template's `Grid Table` styles. Render it the way Prompt C-14 (`manager-04b-render-word-template.md`) renders the full report: clone the template and fill it in place, never convert Markdown to Word.

   - **Template.** Use the Report Template Word file confirmed in Setup 1 (step 1); if it is no longer found, match on the title keywords "Sector Reform Design Report Template"; in Claude Code, ask the user for the `.docx`. If the knowledge base holds a dedicated OLePFM Working Tables Word template, use that instead and fill its tables the same way.
   - **Cover.** Replace the line "Report Template" with "[Sector] Sector — Working Tables" and add "[Country]" and the workshop date; keep the branding images. The word "Template" must not appear on the cover.
   - **Strip the report body.** Delete the Acronyms table, Chapters 1 to 5 (the portrait main-report section) and every paragraph in the "Instructions" style. Keep the cover, the table of contents field and the landscape annex section with its Step 1, Step 2 and Step 3 headings.
   - **Fill 1.1 to 2.1.** Write the confirmed content into the template's existing Tables 1.1, 1.2, 1.3 and 2.1, preserving the `Grid Table` styles, and trim fully empty skeleton rows in those four tables only. The reference check tables stay out of the handout unless the user asks for them.
   - **Scaffold 2.2 to 3.5.** Leave the header row and the template's empty rows in place for the workshop to write in; add no AI content. Under every table heading, 1.1 to 3.5, insert the facilitation or exercise note from steps 2 and 3 as one italic paragraph in the template's body style.
   - **Economic-resilience variant.** Where Table 1.3 is replaced by the fiscal-cycle narrative (ER-1-08), put the narrative under the Table 1.3 heading in the body style, delete the empty table and say so in the note.
   - **Footer.** Set the footer to "[Country] [Sector] OLePFM Working Tables".
   - **Artefact scan.** Confirm zero of: "Template" on the cover, "XXXX" placeholders, "Instructions"-style paragraphs, "[bracketed]" guidance, orphan "Figure:" or "Source:" lines, and any pre-filled cell in Tables 2.2 to 3.5. Report the count, which must be 0, then present the `.docx` for download.

   **✏️ Review the output — focus on these points**

   **Word render** — the handout is what participants write in, so the template's tables must be intact and the blank tables really blank.

   - [ ] Cover shows country, sector, "Working Tables" and the workshop date; the word "Template" is gone
   - [ ] Only the annex section follows the cover and table of contents; no report chapters, acronyms table or grey guidance text
   - [ ] Tables 1.1 to 2.1 carry the confirmed content with the `Grid Table` styling and landscape orientation intact
   - [ ] Tables 2.2 to 3.5 are empty apart from header rows, each with its exercise note
   - [ ] Footer reads "[Country] [Sector] OLePFM Working Tables"; the artefact scan reported 0

   Say "proceed" when satisfied, or provide corrections to re-render.

## Notes

- **Populate only through 2.1.** 2.2 is the workshop's first live exercise, so the AI stops there; do not pre-fill 2.2 onward.
- **Keep challenges free of money/PFM.** The challenges in 1.1 must be stated as delivery failures only — no mention of money, public finance or PFM.
- **Draft to refine.** The populated tables are a starting point for the workshop to review and change, not a final answer.
- **Cross-cutting fiscal outcome (economic resilience, fiscal or debt sustainability).** Use the variant prompts in `manager-01a-variant-economic-resilience.md` (ER-1-05, for Table 1.2) and `manager-01a-variant-economic-resilience-2.md` (ER-1-08). Table 1.3 (financing channels) does not apply; replace it with the fiscal-cycle narrative from ER-1-08 and note the substitution in the Working Tables.
