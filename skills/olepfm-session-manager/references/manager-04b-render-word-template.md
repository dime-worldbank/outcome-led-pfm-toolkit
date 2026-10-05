---
title: OLePFM Compilation and QA (4b, continued) — Rendering to the Word Template
description: Compilation and QA (file 4b, second of two) of the OLePFM report workflow. Prompt C-14 pours the confirmed content of Main Report Parts 1 and 2 and the Annex into the branded OLePFM Sector Reform Design Report Word template, so the delivered .docx carries the template's cover, table of contents, styles, landscape annex tables and footers with no placeholder text. Run after manager-04b-part2-and-annex.md (as a draft render if QA has not yet run); re-run after the QA corrections from manager-04c-cross-document-qa.md.
---

# Compilation and QA (file 4b, continued): Rendering to the Word Template

**Compilation and QA, file 3 of 4.** Run this prompt after Prompts C-06 to C-13 in `manager-04b-part2-and-annex.md` are complete and confirmed. The compiled Main Report Part 1 (step 4a), Part 2 and Annex are already in context.

Pause at the ✏️ intervention point and wait for user confirmation before proceeding.

> When Prompt C-14 is complete and confirmed, continue with `manager-04c-cross-document-qa.md` (Prompts QA-1 to QA-5). If QA then changes any content, re-run Prompt C-14 so the delivered `.docx` carries the corrections.

---

## Rendering to the Word template

After Prompts C-06 to C-13 (`manager-04b-part2-and-annex.md`) have produced and the user has confirmed the final *content* of the three documents (Main Report Part 1 from step 4a, Main Report Part 2, and the Annex), the report is delivered as a single Word document that follows the official OLePFM template. This is Prompt C-14.

### The template

- **Asset:** `OLePFM xxxxx - Sector Reform Design Report Template (1).docx`
  - Institutional platform: knowledge base root folder / backend library. Resolve it the same way Setup 1 resolves the Report Template — match on the title keywords "Sector Reform Design Report Template", as the stored file name may differ.
  - Repository (Claude Code): ask the user to provide the `.docx` template if it is not supplied.
- **Why render into the actual `.docx`, not convert from Markdown.** The template carries a branded cover page, an automatic Table of Contents, a defined style system (Heading 1/2/3, Para, Body, the `Grid Table` annex-table styles, Caption), a portrait main-report section and a **landscape** annex section, and page footers. Converting Markdown to Word loses all of this. Cloning the template and filling it in place preserves every element.
- **Method:** clone the template, remove its placeholder guidance, and write the confirmed content into the matching headings and tables **using the template's own styles**. Do not rebuild the document from scratch.

### Prompt C-14 — Render the compiled report into the OLePFM Word template

> **Run only after** the content of Part 1 (step 4a), Part 2 (Prompt C-09) and the Annex (Prompt C-13) has been compiled and confirmed, and all C-01 and QA corrections (if QA has already run) are applied. If QA (`04c`) has not yet run, render a **draft** here and re-render once QA corrections are in.

Please render the confirmed [country] [sector] OLePFM report into the official OLePFM Word template and produce a single downloadable `.docx`. Follow this procedure exactly, and **leave no placeholder text behind**.

**1. Locate and clone the template.** Find `OLePFM xxxxx - Sector Reform Design Report Template (1).docx` (match on the title keywords if the stored name differs; ask the user for it if it cannot be found). Work on a **copy** — never overwrite the template.

**2. Cover page.** Replace the placeholder title lines. Specifically: replace the line reading "Report Template" with "[Sector] Sector", and immediately after the title block insert two lines — "[Country]" and the report date (e.g. "[Month Year]"). Keep the branding images on the cover unchanged. The word "Template" must not appear anywhere on the cover.

**3. Acronyms table.** Replace the placeholder rows (which read "XXXX" / "xxxxxxxxxxxxxxxx") with the report's actual acronym list, derived from the acronym list compiled in Prompt C-02 (Part 1 front matter). One acronym per row; remove any surplus blank rows.

**4. Remove all authoring guidance.** The template contains grey instructional paragraphs (the "Instructions" style) and instructional captions/tables that tell an author what to write. Remove **every** one, including:
- all paragraphs in the "Instructions" style;
- the instructional "Fiscal Analysis" data-collection table (its header reads "Data To be collected" / "Stories that can be told from the data") — delete the whole table;
- leftover bracketed guidance in body text, e.g. "[Sector/policy area context]", "[policy/outcome area]", "[describe …]", "[Country]";
- standalone guidance lines such as "Source:", "etc", and empty "Figure:" captions that have no accompanying figure.

**5. Fill the narrative sections**, writing the confirmed content under each matching heading using the template's own paragraph styles (Para / Body for body text; do not invent new styles):
- Chapter 1 Introduction — the confirmed introduction text (replace the generic methodology boilerplate).
- 2.1 Development Outcomes and Public Sector Results.
- 2.2 — rename the generic "Challenge 1/2/3" headings to the confirmed full challenge titles and add each description.
- 2.3.1 / 2.3.2 / 2.3.3 context.
- 3.1.1–3.1.4 — each role's Potential role and Actual role paragraphs.
- 3.2.1 / 3.2.2 bottleneck narrative and priority bottlenecks.
- 4.1 — rename the generic "Change Objective N:" headings to the confirmed objectives; under each, the contribution statement and every Reform Result (bold lead line with its "[Feasibility: H/M/L]" label, then its description).
- 4.2 Stakeholder Strategy; 4.3 Systems, Capacity Development and TA.
- Conclusion.

**6. Fill every annex table** from the confirmed Annex (Prompt C-13), writing into the template's existing table structures so the `Grid Table` styles are preserved:
- Table 1.1 Outcomes, Public Sector Results and Challenges;
- Table 1.2 Organizational Functions; Table 1.3 Main Financing Channels;
- Table 2.1 Roles of Public Finance (Potential / Actual); Table 2.2 Challenges and Bottlenecks; Table 2.3 Priority Bottlenecks (impact rating/description, feasibility rating/description);
- Table 3.1 causal analysis; Table 3.2 stakeholders; Table 3.3 stakeholder management; Table 3.4 systems/capacity/TA; Table 3.5 action plan (reform result, three key steps, timing, responsible).
After filling, **trim every remaining fully-empty skeleton row** (keep header rows). Remove the empty "Other Bottlenecks" rows in Table 2.3 if the report has no other bottlenecks.

**7. Figures.** For each figure caption retained (Analytical Framework, Organizational Map, Main Financial Flows, fiscal charts), insert the corresponding figure produced during drafting beneath its caption. If a figure was not produced, remove the empty caption rather than leave an orphan "Figure:" line. *(Confirm the figure-handling choice with the user before first use — insert vs. leave manual.)*

**8. Footer.** Set the page footer to "[Country] [Sector] OLePFM Reform Diagnosis and Design" and remove any stray template page-number artefact.

**9. Final artefact scan — must pass before delivery.** Scan the rendered document and confirm **zero** of the following remain: the word "Template" on the cover; any "XXXX"/"xxxx" placeholder; any "Instructions"-style paragraph; any "[bracketed]" guidance; any "Describe:", "Source:", or orphan "Figure:" line; any fully-empty skeleton table row. Report the scan result (count of artefacts found, which must be 0) and the per-table fill count, then present the single compiled `.docx` for download.

> **Implementation note (for the AI).** This render is done programmatically against the `.docx` (e.g. python-docx): clone the file; delete "Instructions"-style paragraphs and the instructional table; set cover/acronym/footer text; insert body paragraphs after the matching headings inheriting the template styles; write and trim table cells. Preserve the cover image, the TOC field, the style definitions and the portrait/landscape section breaks. Do not flatten the document into plain Markdown and re-convert.

---

### ✏️ Review the output — focus on these points

**Word-template render (Prompt C-14).** Open the delivered `.docx` and check:

- [ ] The cover shows the country, sector and date — and the word "Template" is gone
- [ ] The Acronyms table lists the report's real acronyms, no "XXXX" rows
- [ ] No grey guidance text, bracketed placeholders, "Describe:/Source:/etc", or orphan "Figure:" lines anywhere
- [ ] Every annex table is populated with no blank skeleton rows; the `Grid Table` styling and landscape orientation are intact
- [ ] The cover branding image and the Table of Contents are present; the footer reads "[Country] [Sector] OLePFM Reform Diagnosis and Design"
- [ ] The final artefact scan reported 0 artefacts

Say "proceed" when satisfied, or provide corrections to re-render.

---

---

## Prompt Sequence Summary

| Prompt | Output | Document |
|---|---|---|
| **C-14** | **Report rendered into the OLePFM Word template (single `.docx`)** | **All** |

Continue with `manager-04c-cross-document-qa.md`.
