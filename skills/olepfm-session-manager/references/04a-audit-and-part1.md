---
title: OLePFM Compilation and QA (4a) — Consistency Audit and Main Report Part 1
description: Compilation and QA (file 4a) of the OLePFM report workflow. Runs the pre-compilation consistency audit across all chapters and annexes, then compiles Main Report Part 1 (front matter, Chapter 1, Chapter 2). Continue with 04b-part2-and-annex.md.
---

# Compilation and QA (file 4a): Consistency Audit and Main Report Part 1

**Compilation and QA, file 1 of 3.** Run these prompts after Step 3 (Chapters 4 & 5) is complete and confirmed. The session context and all prior chapter drafts are already in context.

> **Start with Prompt C-01 (consistency audit) before any compilation step.** Resolve all identified discrepancies before proceeding to C-02. Do not skip this step.

Pause at every ✏️ intervention point and wait for user confirmation before proceeding.

**Prerequisites in context:**
- All values recorded in manager (reform result counts, feasibility breakdown, implementation horizon, authors, date)
- Draft Chapters 1–5 and all Annex Step drafts from Steps 1–3

> When Prompt C-05 is complete and confirmed, continue with `04b-part2-and-annex.md`.

---

## PRE-COMPILATION: CONSISTENCY AUDIT

### ✏️ Review the output — focus on these points

**Pre-compilation consistency audit (Prompt C-01)** — the most important step in compilation. Complete the audit and make all corrections to the draft chapters before compiling.

- [ ] Reform result numbers and titles — the connective tissue of the report — are identical wherever they appear
- [ ] Bottleneck codes (e.g. B2.3) match between Chapter 3 and Annex Table 2.2 (a mismatch is a substantive analytical error)
- [ ] Feasibility ratings are stable across Chapter 3, Section 4.1, Annex Table 3.1, and Chapter 5
- [ ] Each public sector challenge title in Section 2.2 appears consistently in Sections 3.2.1, 3.2.2, and 4.1

**Do not proceed to Main Report Part 1 until you have reviewed the audit findings and instructed the AI on how to resolve each inconsistency.**

### Prompt C-01 — Pre-Compilation Consistency Audit

Before beginning compilation, please conduct a systematic consistency audit across all draft chapter and annex documents for the [country] [sector] OLePFM report.

Check the following:

**(i) Reform result codes, titles, and feasibility ratings.** Confirm that every reform result has an identical code, title description, and feasibility rating (H/M/L) in: Section 4.1; the summary reform results table at the end of Section 4.1; Annex Table 3.1; and the feasibility summary in Chapter 5. List any discrepancies.

**(ii) Bottleneck codes and titles.** Confirm that every individual bottleneck code (e.g. B2.3) cited in Sections 3.2.1, 3.2.2, and 4.1 matches identically with the corresponding row in Annex Table 2.2. Confirm that every priority bottleneck in Section 3.2.2 matches identically with Annex Table 2.3. List any discrepancies.

**(iii) Public sector challenge references.** Confirm that the public sector challenges named in Section 2.2 are referred to by exactly the same title or shorthand description in Sections 3.2.1, 3.2.2, 4.1, and 5.2. List any inconsistencies.

**(iv) Stakeholder names.** Confirm that organizations named in Section 4.2 and in Annex Tables 3.2 and 3.3 are referred to by consistent names throughout all chapters and annexes. List any inconsistencies.

**(v) Annex cross-references.** Confirm that every Annex table referenced in the chapter text exists as a table in the relevant draft annex document with the same title and content. List any missing or mismatched references.

**(vi) Citation format.** Confirm that all citations are hyperlinked to their source and follow the form ([World Bank, 2010](url)) consistently. List any citations that are not hyperlinked, deviate from this form, or any factual claims that are uncited.

Present findings as a numbered list of discrepancies with: the location (document, section, paragraph); the nature of the error; and a recommended correction. If no discrepancy is found in a category, state "No discrepancies found."

---

## Main Report Part 1 — Front matter and Chapters 1–2

Compile Part 1 in four sequential prompts (Prompts C-02 through C-05), reviewing the output at each intervention point before proceeding.

### Prompt C-02 — Front Matter: Cover, Table of Contents, Executive Summary, and List of Acronyms

Please compile the front matter for Main Report Part 1 of the [country] [sector] OLePFM Reform Diagnosis and Design Report. Produce the following elements in order:

**(i) Cover page.** Include: the full report title formatted as "[Country]: [Sector] Reform Diagnosis and Design — Outcome-Led PFM Reform"; the sub-title "Outcome-Led PFM Reform Diagnosis and Design"; the authors ([author names and affiliations]); the issuing institution (World Bank, Governance Global Practice); and the date ([date]).

**(ii) Table of contents.** Produce a complete table of contents covering both Main Report Part 1 and Main Report Part 2, with all chapter and section headings, all annex table titles, the list of acronyms, and the bibliography. Use the section numbering and heading titles exactly as they appear in the compiled chapters. Note in the table of contents that the Annex is published as a separate companion volume.

**(iii) Executive summary (approximately 600–800 words)** covering:
- The development outcome and why it matters for [country] (approximately 100 words)
- The [number] public sector challenges preventing progress toward the outcome (approximately 150 words — one to two sentences per challenge)
- The role of public finance and the [number] priority PFM bottlenecks (approximately 150 words — one sentence per bottleneck)
- The reform action plan: the [total number] reform results across the [number] change objectives, with the count of High, Medium, and Low feasibility results (approximately 150 words)
- Implementation horizon and key early actions (approximately 100 words)
- A concluding sentence connecting the reform plan to the development outcome

The executive summary should be written for a senior government official or development partner who will not necessarily read the full report. Use plain language. Avoid PFM jargon where a plain English equivalent exists. Write in flowing paragraphs — no bullet points.

**(iv) List of acronyms.** Produce a clean alphabetical table of all acronyms used in the report with their full expansions. Confirm that every acronym used in Chapters 1–5 and the Annexes appears in the list and that no acronym in the list is unused.

---

### ✏️ Review the output — focus on these points

**Executive summary (Prompt C-02)** — the most widely read section; review it with particular care.

- [ ] The challenges are described as frontline service delivery failures — not in PFM or financial terms
- [ ] The bottleneck descriptions are concise but analytically precise — the specific nature of each failure, not a generic "weak PFM"
- [ ] The reform results count and feasibility breakdown are accurate
- [ ] The early actions named are genuinely the most critical steps from Annex Table 3.5 — not the easiest or most visible
- [ ] The final connecting sentence is specific to the country context and the outcome

Revise before proceeding.

---

### Prompt C-03 — Chapter 1: Introduction

Please compile the final version of Chapter 1 — Introduction — for the [country] [sector] OLePFM Reform Diagnosis and Design Report, using the draft Chapter 1 document and applying the corrections identified in the consistency audit (Prompt C-01).

Apply the following editorial instructions:
(i) Confirm the opening paragraph situates [country]'s [sector] performance in its development context with specific, current data.
(ii) Confirm the OLePFM methodology description correctly references the Williamson et al. (2024) Synthesis Handbook and accurately describes the backward-mapping approach.
(iii) Confirm the purpose statement names the report's specific intended uses.
(iv) Confirm the section-by-section road map accurately describes what each section contains and uses the correct section numbers.

Present the final compiled Chapter 1 in full.

---

### Prompt C-04 — Chapter 2: Outcome and Public Sector Context

Please compile the final version of Chapter 2 — Outcome and Public Sector Context — for the [country] [sector] OLePFM Reform Diagnosis and Design Report, using the draft Chapter 2 document and applying the corrections identified in the consistency audit (Prompt C-01).

Apply the following editorial instructions:
(i) **Section 2.1:** Confirm that outcome data cited is consistent with the executive summary and Chapter 5. Standardize any figures that appear with different values in different locations.
(ii) **Section 2.2:** Confirm that each challenge is described in terms of observable frontline service delivery failures — without reference to money or PFM. Confirm challenge titles and numbers are identical to those used in Sections 3.2.1, 3.2.2, 4.1, and 5.2. Add a cross-reference at the end of Section 2.2 directing readers to Annex Table 1.1.
(iii) **Section 2.3.1:** Confirm key policy documents and legislative instruments are referenced with correct titles, years, and act numbers.
(iv) **Section 2.3.2:** Confirm a cross-reference to Annex Table 1.2 appears at the end of Section 2.3.2. Confirm the financial flows sub-section names and describes all main financing channels; each channel description notes its approximate size in the most recent available year; and a cross-reference to Annex Table 1.3 appears in that sub-section. Confirm the PFM sub-section covers budget formulation, budget execution (wages and non-wage), procurement, audit and accountability, and digital financial management systems — in that order.
(v) **Section 2.3.3:** Confirm the three feasibility dimensions are each addressed with specific [country] evidence and are consistent with the feasibility ratings used in Chapters 3 and 4.

Present the final compiled Chapter 2 in full.

---

### ✏️ Review the output — focus on these points

**Main Report Part 1 (Prompt C-04).** Read Chapters 1 and 2 consecutively before finalizing Part 1.

- [ ] The opening of Chapter 2 flows naturally from the end of Chapter 1
- [ ] The public sector challenges in Section 2.2 are specific and vivid — a reader unfamiliar with [country]'s [sector] understands what is actually going wrong at the frontline
- [ ] The institutional architecture in Section 2.3.1 and the PFM description in Section 2.3.2 are correctly cross-referenced to Annex Table 1.2, and the financial flows to Annex Table 1.3
- [ ] The financial flows section gives enough analytical context for the Chapter 3 bottleneck analysis without pre-empting it

Make any editorial adjustments before producing the final Part 1 document.

---

### Prompt C-05 — Compile Main Report Part 1

Please compile the final Main Report Part 1 document for the [country] [sector] OLePFM Reform Diagnosis and Design Report, combining in order: (i) the front matter from Prompt C-02; (ii) Chapter 1 from Prompt C-03; and (iii) Chapter 2 from Prompt C-04.

Apply the following final formatting instructions:
- All section and sub-section headings must be consistently formatted and numbered.
- All cross-references to Part 2 must use the phrase "see Main Report Part 2" or "discussed in Section [number] of Part 2."
- All cross-references to the Annex must use the phrase "see Annex Table [number]."
- The final paragraph of Chapter 2 should serve as a bridge to Chapter 3.
- Add a footer on each page: "[Country] [Sector] OLePFM Reform Diagnosis and Design — Main Report Part 1."
- Add a note after the table of contents: "This document is Part 1 of a two-part main report. It should be read together with Main Report Part 2 (Chapters 3–5 and Bibliography) and the companion Annex volume (Annex Steps 1–3)."

---

## Prompt Sequence Summary

| Prompt | Output | Document |
|---|---|---|
| C-01 | Cross-chapter consistency audit with correction list | — |
| C-02 | Cover, ToC, executive summary, acronym list | Part 1 |
| C-03 | Final compiled Chapter 1 | Part 1 |
| C-04 | Final compiled Chapter 2 | Part 1 |
| C-05 | Full Main Report Part 1 | Part 1 |

Continue with `04b-part2-and-annex.md`.