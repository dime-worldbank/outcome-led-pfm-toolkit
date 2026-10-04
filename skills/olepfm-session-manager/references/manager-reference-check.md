---
title: OLePFM Session Manager — Reference Check Tables
description: Rule applied at the end of every chapter of the OLePFM Sector Reform Design Report. When a step's chapters are compiled (Prompts 1-15, 2-10 and 3-14), append to each chapter a table listing every cited claim, its source, the document URL and the exact text from the document that supports it, so the user can check the references. Defines the columns, the quotation rules and what to write when a document has not been read. The tables are review aids and stay out of the compiled report unless the user asks for them.
---

# Reference Check Tables

**What this is.** A table at the end of each chapter that lets the user check every reference without opening the chapter's sources one by one. Each row pairs a claim as written in the report with the document it rests on, the URL of that document, and the exact passage in it that supports the claim. A reference that cannot be traced to a passage is shown as unverified rather than hidden.

**When to produce it.** At each step's compilation prompt, where a chapter is assembled in full for the first time: Prompt 1-15 (Chapters 1 and 2), Prompt 2-10 (Chapter 3) and Prompt 3-14 (Chapters 4 and 5). Append one table to each chapter, after its last section, under the heading **Reference check: Chapter [n]**. If the user revises a chapter afterwards, update its table with it. The tables cover the chapters only; annex tables carry their own source rows and citations. Workshop mode (`manager-workshop.md`) compiles no chapters, so it produces no reference check tables unless the user asks for one on the Working Tables.

## Columns

| Column | What goes in it |
|---|---|
| **Section** | The section number where the claim appears, for example 2.3.2 |
| **Claim in the report** | The sentence or figure as written in the chapter, verbatim and kept short. If one sentence makes two claims from two sources, give each its own row |
| **Source** | The source's number in the running source table and the citation as it appears in the text, for example 7, (MoH, 2023). *Uncited* where the text has no citation |
| **Document URL** | The Download link from the running source table where there is one, otherwise its Link. For a document read from a file rather than a URL, give the file name (on the institutional platform, the name it is stored under) |
| **Exact text from the document** | The shortest verbatim passage that supports the claim, in quotation marks, usually one or two sentences, with the page, table or figure number where the document has one. For a data point from a database, the indicator name, value and year as displayed. If the document is not in English, quote the original and add an English translation in brackets |

## Rules for the quotations

1. **Verbatim only.** Copy the passage exactly as it appears in the document, with its figures and units. Never paraphrase, reconstruct, tidy or shorten a quotation in your own words. Use an ellipsis (…) only to drop words from the middle of one passage, never to join sentences from different places.
2. **Never invent a passage.** If you have not read the document, or cannot find a passage that supports the claim, write **Not verified: document not read** or **Not verified: passage not found** in the Exact text column, without quotation marks. An unverified row is useful to the user; an invented quotation is worse than no citation.
3. **The passage must support the claim as written.** If it supports only part of the claim, or a weaker version of it, quote it and add *(supports partially: …)* with a few words on what the document does not say, so the user can decide whether to soften the claim.
4. **One row per claim.** Every parenthetical citation in the chapter has a row. So does every number, date, named law, programme or policy, and every statement about performance that has no citation; its Source column reads *Uncited*, and the user decides whether to add a source or qualify the claim.
5. **Chart and table data.** Every number shown in a chart or in a chart's underlying data table has a reference-check row in the chapter where the chart appears — one row per data-point family (for example, per series or per year block), consistent with rule 4's requirement that every number gets a row. For a value taken from Data360 (or another structured database):
   - **Source column** — the running-table source number and the in-text citation, plus the indicator name, value and year as displayed and the indicator code (for example, *Government expenditure on education, total (% of government expenditure)* — WDI, `WB_WDI_SE_XPD_TOTL_GB_ZS`, 2024).
   - **Document URL column** — the Data360 source link: the explorer link (`https://data360.worldbank.org`) where the site is reachable, otherwise the Data360 API query URL, or the indicator code if neither is available.
   - **Exact text column** — the indicator name, value and year exactly as returned by the source. Because Data360 values carry verifiable claim tags, these rows are treated as **verified**, not "not verified", provided the value in the table matches the value returned by the source.
   A chart value whose figure cannot be matched to a returned source value is marked **Not verified: passage not found**, exactly as for prose claims.

## After each table

Below the table give a one-line tally: rows in total, verified, partially supported, not verified, uncited. The user reviews the tables before the step's completion gate, which asks for it. Resolve every row that is not verified, partially supported or uncited before the gate: find the passage, re-source the claim, soften it or remove it.

## In Compilation and QA

The tables are review aids, not part of the report. Leave them out of the compiled chapters and documents (Prompts C-02 to C-13) unless the user asks to keep them, for example as a reviewers' annex. The consistency audit (Prompt C-01, item (vi) on citations) can start from the tallies: any row still not verified or partially supported is a citation to settle before compilation.
