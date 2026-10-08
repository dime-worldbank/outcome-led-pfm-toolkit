---
title: OLePFM Workshop Preparation
description: Produces the Sector Background Information paper a reform design workshop starts from. Chapters 1 and 2 of the Sector Reform Design Report (outcome, public sector results, challenges, and the policy, institutional, public finance and feasibility context, with the financial flows table and two diagrams), Annex Tables 1.1 and 1.2 and Table 2.1 populated from desk research, and Tables 2.2 to 3.5 left blank as workshop exercises with facilitation notes, rendered into the OLePFM Sector Background Information Word template. Establishes context and sources, then reuses the Step 1 and Step 2 generation prompts unchanged. Use when preparing for an upcoming workshop; trigger by saying "start OLePFM workshop preparation" or asking for workshop tables.
---

# OLePFM Workshop Preparation

Use this to produce the **Sector Background Information** paper a reform design workshop starts from: Chapters 1 and 2 of the report drafted from desk research, Annex Tables 1.1 and 1.2 and Table 2.1 populated, and Tables 2.2 to 3.5 left blank as the workshop's own exercises. It reuses the generation prompts in the Step 1 and Step 2 prompt files (`manager-01a-chapters1-2.md`, `manager-01a-section2-3.md`, `manager-01b-annex1.md`, `manager-02-chapter3-annex2.md`) and changes nothing in them. The paper is delivered as a Word document rendered into the OLePFM Sector Background Information Template (step 5), whose Markdown twin `manager-sector-background-template.md` is the structural authority: its headings, bracketed guidance and tables say what goes where. `manager.md` is the session manager's SKILL.md; the AI behaviour rules there (one prompt at a time, pause at every ✏️ point, never invent values, reference check after every cited draft) apply throughout.

The workshop reviews the paper, validates Table 2.1 and fills in 2.2 onward; the completed tables then inform the full report drafted with the standard workflow (`manager.md`).

## Opening prompt

To start, say **start OLePFM workshop preparation** — no need to name the country or sector; the AI will ask. That is equivalent to pasting:

---

I want to prepare the OLePFM Sector Background Information paper and Working Tables for an upcoming reform design workshop. Guide me through it: first ask me for the country and sector, then draft Chapters 1 and 2, populate Annex Tables 1.1, 1.2 and 2.1, and leave Tables 2.2 onward as blank exercises for the workshop.

---

## Steps

1. **Set up and verify the template.** Run Setup 1 in `manager-setup.md`, then paste this extra check before anything else is drafted:

   ---

   Please also confirm you can access the **OLePFM Sector Background Information Template**, the Word file stored in the root folder of the app-wide knowledge base alongside the Report Template. Search that knowledge base with `vector_search` on the title keywords "Sector Background Information" and "Background Information Template", as the stored file name may differ; if a search returns nothing, list the root files and match on those keywords. State whether you can access it, its title and the file name it is stored under, and confirm it is the Word (.docx) file and not a text copy: the paper in step 5 is produced by cloning it. If it is still missing after the searches and the root listing, list the file names you can see at the root, stop and alert the user before proceeding.

   ---

   > **Do not proceed to Setup 2 until the AI confirms the template is accessible and is the Word file.** In Claude Code, ask the user for the `.docx` instead.

   Then establish country, sector and development outcome as in Setup 2 of the same file (including the off-list sourcing order), then run the **full Sources stage exactly as `manager.md` runs it for the report**: Prompts S-1 to S-4 from `manager-00-source-prep.md`, each with its ranking, link check and readability check, and on the institutional platform the rules of `manager-platform.md` in full, which are the four-tool discovery before any filter, the two-pass link verification, the index check S-5 inside each sourcing prompt with its upload requests, the final pass and the must-have sources. Then apply the Sources completion gate in `manager.md`, with the platform's additions, declare **SOURCES COMPLETE** and wait for the user to confirm the sources before any drafting. The paper cites nothing outside the running source table; cite sources as hyperlinked parentheticals.

2. **Draft Chapters 1 and 2.** Run the Step 1 prompts in order, one at a time, pausing at every ✏️ point and appending the reference check table (`manager-reference-check.md`) to every cited draft; resolve every not-readable, not-verified or uncited row before moving on. Each prompt's output fills one part of the template:

   | Template section | Prompt | File |
   |---|---|---|
   | Chapter 1. Introduction | 1-01 | `manager-01a-chapters1-2.md` |
   | 2.1 Outcomes and Public Sector Results | 1-02 | same |
   | 2.2 Key Public Sector Challenges | 1-03 | same |
   | 2.3.1 Policy Framework | 1-04 | `manager-01a-section2-3.md` |
   | 2.3.1 Institutional Architecture | 1-05 | same |
   | Figure 1. Institutional Mapping | 1-06 | same |
   | 2.3.2 Fiscal Policy Context | 1-07 | same |
   | 2.3.2 Main Financial Flows and the Financial Flows Table | 1-08 | same |
   | Figure 2. Mapping Financial Flows | 1-09 | same |
   | 2.3.2 Public Financial Management | 1-10 | same |
   | 2.3.3 Feasibility of Policy and Institutional Capability | 1-11 | same |

   Keep each section to the length the template's bracketed guidance gives: the paper is a background note, not the full report. Write the roadmap paragraph of Chapter 1 as the template says, Chapter 2 covered here and Chapters 3 to 5 to follow the workshop. Pause after Prompt 1-11 for the user to review the two chapters together.

   > **Economic resilience or another cross-cutting fiscal outcome:** replace Prompts 1-04 to 1-10 with ER-1-04 to ER-1-10 from `manager-01a-variant-economic-resilience.md`. The fiscal-cycle narrative (ER-1-08) takes the place of the financial flows table and the fiscal-cycle diagram (ER-1-09) is Figure 2; say so under the heading.

3. **Populate the annex tables.** Generate each with its existing prompt, append its reference check table and resolve every flagged row, then add a short **facilitation note** in italics under the table title:

   | Table | Prompt | Facilitation note |
   |---|---|---|
   | **Annex Table 1.1** Outcomes, Results and Challenges | 1-12 (`manager-01b-annex1.md`) | *Pre-populated by AI. Review; agree preferably three and no more than five challenges — a challenge must not mention money.* |
   | **Annex Table 1.2** Organizational Functions | 1-13 (same file) | *Pre-populated by AI. Validate; add any missing organizations.* |
   | **Annex Table 2.1** Roles of Public Finance | 2-02 (`manager-02-chapter3-annex2.md`) | *Pre-populated by AI. Read before identifying challenges; validate the potential and actual roles.* |

   Table 1.3 is not produced separately: the financial flows table in Section 2.3.2 (Prompt 1-08) carries the same channels, values and problems. Tables 2.2 to 3.5 stay exactly as the template draws them, header rows, preset row labels and exercise notes only, with no AI content. Pause here for the user to review the three populated tables.

4. **Assemble and check.** Assemble the paper in template order: title and "[Country]: [Sector] Sector" line, Chapter 1, Chapter 2 with its figures and flows table, Annex Tables 1.1 and 1.2, then the Working Tables 2.1 to 3.5. Leave the reference check tables out of the paper unless the user asks for a reviewers' annex. Show it for a last content check before rendering.

5. **Render into the Word template and hand off.** The deliverable is a Word file produced from the template, nothing else. Render the way Prompt C-14 (`manager-04b-render-word-template.md`) renders the full report: open the OLePFM Sector Background Information Template confirmed in step 1 with the platform's document tools (in Claude Code, the environment's Word capability), clone it, and write the confirmed content into the clone in place, keeping its heading and body styles, table style, section layout and footers. Never generate a new document from scratch and never convert Markdown, HTML or text to Word. If the template cannot be opened or cloned, stop and tell the user; do not hand over a substitute. The paper is finished only when the `.docx` is presented for download.

   - **Title block.** Keep the title "OLePFM Sector Background Information"; replace "[Country]: [Sector] Sector" with the country and sector and add the workshop date on the next line.
   - **Chapters.** Replace every bracketed guidance paragraph with the confirmed text of its section, in the template's body style, keeping the headings. Keep the two standard paragraphs of Chapter 1 that carry no brackets.
   - **Figures.** Insert the institutional diagram (Prompt 1-06) as a picture where the Figure 1 placeholder sits and the financial flows diagram (1-09) at the Figure 2 placeholder, each above its caption, and delete the placeholder paragraphs. Export each draw.io diagram as a PNG wide enough to fill the text column.
   - **Tables.** Fill the Financial Flows Table (one row per channel, adding or trimming rows to match), Annex Tables 1.1, 1.2 and 2.1 in the template's table style, trimming empty skeleton rows in those tables only. Leave Tables 2.2 to 3.5 untouched, including their exercise notes and preset row labels.
   - **Footer.** Keep the template's footer as it is.
   - **Artefact scan.** Confirm zero of: "[bracketed]" guidance anywhere, "[Country]" or "[Sector]" left unreplaced, "Insert Figure" placeholders, and any AI-written cell in Tables 2.2 to 3.5. Confirm the file still carries the template's heading styles, footer and the landscape section of the Working Tables, which shows it was cloned and not rebuilt. Report the count, which must be 0, then present the `.docx` for download.

   **✏️ Review the output — focus on these points**

   **Word render** — the paper is what participants read and write in, so the chapters must be complete and the blank tables really blank.

   - [ ] The file is a `.docx` produced by cloning the template: its heading styles, footer and landscape tables section are present
   - [ ] Title block shows the country, sector and workshop date; no bracketed guidance remains
   - [ ] Chapters 1 and 2 follow the template headings, with both figures placed above their captions
   - [ ] The Financial Flows Table and Annex Tables 1.1, 1.2 and 2.1 carry the confirmed content in the template's table style
   - [ ] Tables 2.2 to 3.5 are empty apart from header rows, preset row labels and exercise notes
   - [ ] The artefact scan reported 0

   Say "proceed" when satisfied, or provide corrections to re-render.

## Notes

- **Populate only through Table 2.1.** Table 2.2 is the workshop's first live exercise, so the AI stops there; do not pre-fill 2.2 onward.
- **Keep challenges free of money/PFM.** The challenges in Section 2.2 and Table 1.1 must be stated as delivery failures only — no mention of money, public finance or PFM.
- **Draft to refine.** The paper and the populated tables are a starting point for the workshop to review and change, not a final answer.
- **Length.** Follow the template's guidance on paragraph counts; cut rather than pad.
