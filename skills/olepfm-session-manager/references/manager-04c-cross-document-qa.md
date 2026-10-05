---
title: OLePFM Compilation and QA (4c) — Cross-Document Quality Assurance
description: Compilation and QA (file 4c) of the OLePFM report workflow. Runs the five cross-document quality assurance checks (Prompts QA-1 to QA-5) over Main Report Parts 1 and 2 and the Annex before the report is released. Run after manager-04b-part2-and-annex.md and the draft render in manager-04b-render-word-template.md.
---

# Compilation and QA (file 4c): Cross-Document Quality Assurance

**Compilation and QA, file 4 of 4.** Run these prompts after all three final documents have been compiled in `manager-04a-audit-and-part1.md` and `manager-04b-part2-and-annex.md`. If any check changes content, re-run Prompt C-14 in `manager-04b-render-word-template.md` afterwards so the delivered `.docx` carries the corrections.

Pause at every ✏️ intervention point and wait for user confirmation before proceeding.

**Prerequisites in context:**
- Compiled Main Report Part 1 (step 4a)
- Compiled Main Report Part 2 and Annex document (step 4b)

---

## Cross-document quality assurance

Run QA-1 through QA-5 in sequence after all three documents are compiled. Resolve all identified issues before releasing the final report.

### ✏️ Review the output — focus on these points

**Cross-document QA (Prompts QA-1 to QA-5)** — these catch issues that only appear when the three documents are read as a whole.

- [ ] A final correction list has been compiled from QA-1 through QA-5
- [ ] The AI has applied every correction to the relevant document(s)

**Do not release any document for external review until all QA findings have been resolved.**

---

### Prompt QA-1 — Cross-Document Consistency: Reform Results

Please check for consistency across Main Report Part 1, Main Report Part 2, and the Annex with respect to reform result codes, titles, and feasibility ratings.

Specifically: (i) list every reform result code that appears in any of the three documents; (ii) for each code, confirm that the title and feasibility rating are identical in Section 4.1, the Section 4.1 summary table, Annex Table 3.1, and Chapter 5; and (iii) confirm that the total count of reform results stated in the executive summary matches the count in the Section 4.1 summary table and Annex Table 3.1. List all discrepancies with the recommended correction.

---

### Prompt QA-2 — Cross-Document Consistency: Public Sector Challenges

Please check that the public sector challenges are referred to by exactly the same title or shorthand in every location across the three compiled documents: the executive summary; Section 2.2; Section 3.2.1; Section 3.2.2; Section 4.1 (in each change objective opening paragraph); Section 5.2; Annex Table 1.1; Annex Table 2.2; and Annex Table 2.3.

List any inconsistencies in challenge title, numbering, or characterisation across locations.

---

### Prompt QA-3 — Cross-Document Consistency: Outcome and Spending Data

Please check that all quantitative outcome and spending data cited across the three compiled documents are internally consistent.

Check that: (i) key outcome indicators appear with the same value, year, and source citation in every location where they are cited across the executive summary, Chapter 2, Chapter 5, and Annex Table 1.1; and (ii) financial flows data appear with the same value, year, and source citation in every location where they are cited across the executive summary, Section 2.3.2, Sections 3.1 and 3.2, and Annex Tables 1.3 and 2.1.

List any inconsistencies with the recommended correction and the most reliable source.

---

### Prompt QA-4 — Annex Completeness Check

Please confirm that: (i) every Annex table referenced in the main report chapters exists in the Annex document with the correct title and number — list any missing tables; (ii) every organization named in any Annex table is also named in the main report (either in Section 2.3.2 or Section 4.2) — list any organizations that appear in the Annex but not in the main report; and (iii) the Annex Table of Contents is complete and accurate.

List all gaps or inconsistencies.

---

### Prompt QA-5 — Plain Language and Accessibility Check

Please review the executive summary and Chapter 5 conclusion and identify:

(i) any sentence that uses PFM jargon where a plain English equivalent exists — suggest a plain English reformulation;
(ii) any sentence that refers to an analytical concept (such as a bottleneck code, OLePFM methodology step, or taxonomy category) that would be unintelligible to a senior government official unfamiliar with the OLePFM framework — suggest how to make it accessible without losing precision; and
(iii) any passage in the executive summary that a reader could interpret as inconsistent with the body of the report — either because it overstates the reform plan's ambition or understates the political economy challenges.

Flag and suggest revisions for each.

---

---

## Compilation and QA Prompt Sequence Summary (all three files)

| Prompt | Skill file | Output | Document |
|---|---|---|---|
| C-01 | 04a | Cross-chapter consistency audit with correction list | — |
| C-02 | 04a | Cover, ToC, executive summary, acronym list | Part 1 |
| C-03 | 04a | Final compiled Chapter 1 | Part 1 |
| C-04 | 04a | Final compiled Chapter 2 | Part 1 |
| C-05 | 04a | Full Main Report Part 1 | Part 1 |
| C-06 | 04b | Final compiled Chapter 3 | Part 2 |
| C-07 | 04b | Final compiled Chapter 4 | Part 2 |
| C-08 | 04b | Final compiled Chapter 5 | Part 2 |
| C-09 | 04b | Full Main Report Part 2 + bibliography | Part 2 |
| C-10 | 04b | Annex Step 1 (Tables 1.1 to 1.3) | Annex |
| C-11 | 04b | Annex Step 2 (Tables 2.1, 2.2, 2.3) | Annex |
| C-12 | 04b | Annex Step 3 (Tables 3.1–3.5) | Annex |
| C-13 | 04b | Full Annex document | Annex |
| QA-1 to QA-5 | 04c | Cross-document QA findings and corrections | All |