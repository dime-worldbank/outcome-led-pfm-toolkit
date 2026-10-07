---
title: OLePFM Sources — Source Preparation
description: Sources stage of the OLePFM report workflow, run once before any chapter drafting. Identifies all sources needed across the full report (analytical, fiscal, political economy, digital systems), ranks them by relevance and popularity, and enters in the running source table only those with a live, correct link to the document file or to a non-empty page; a source whose text cannot be read is flagged for upload.
---

# Sources: Source Preparation

This skill is run once at the start of the session (the Sources stage, before Step 1). It identifies all sources needed across the full report — analytical, fiscal, political economy, and systems. Complete and confirm all four prompts before proceeding to Step 1.

**The running table.** Every source is entered into a **single running numbered table** — columns **No. | Author | Year | Title | Relevance | Link | Download**. **Link** is the URL the in-text citation points to (the page where the source is published); citations hyperlink to it (see S-1). **Download** is a direct link to the document file itself (usually a PDF) or, for an online database, to a data export or API query that returns the data; for a web page that is itself the source (an official website, a data portal), it is the page's URL; for a document the user has supplied to the session, it is the file name. Numbering starts at 1 in S-1 and continues unbroken through S-2, S-3 and S-4 — never restarted per prompt — so each source keeps one stable number for the rest of the session.

**How a source enters: rank, then check the link.** For each prompt, gather every candidate the searches return and rank them by relevance and popularity, without regard to whether a link has been found yet: relevance to the prompt's topics and to [country] and [sector] first, then popularity, meaning how widely the source is cited and relied on (an official government document, a World Bank, IMF or PEFA report or a national statistics release ranks above a working paper, a news item or a blog). Then run the link check on the ranked list, and enter the sources that pass in ranked order, so that the numbering follows the ranking. A verified link is the condition of entry: a source that fails is dropped, not demoted, however relevant it looks, because its document cannot be obtained, uploaded or checked; mention it, if at all, in one line beneath the table as *not listed: no link*, so the user can look for it elsewhere. Never fill a Link or Download cell with a placeholder, a URL from memory or one built from a pattern: a plausible link that does not open is worse than none. Re-check a link whenever its row is edited.

**The link check.** Every Link and Download URL must be **live, non-empty and correct**. Live: open it where the environment can fetch pages and confirm it resolves without an error page, a login wall or a redirect to a generic home or search page. Non-empty: what opens actually holds the document's text or data; a page that answers successfully (HTTP 200) but shows an empty page, a "text not found" or "page not found" message, a placeholder, a cookie or script shell with no content, or a zero-length file, fails exactly as an error page does. Correct: what opens is the named document, with the row's title, author and year, and the Download link opens the file itself, not a landing page. Where pages cannot be fetched, a link counts as checked only when a web search in this session returned that URL for that document together with a snippet of the page's text; a title with no text is no evidence that the page has content. Say in the Relevance column how the link was checked. On the institutional platform, `manager-platform.md` names the search tools to run for each prompt and where the link of a document found in the knowledge base comes from.

**The readability check, after entry.** A live link says nothing about whether the text can be read: a search result is a title and a snippet, not the document. For every external source, open the page or file and read it in this session. Where that is not possible, flag the row with **Upload needed** in the Relevance column and, below the table, ask the user to upload the document using its Download link. A flagged source is not cited until the user has uploaded it or it is found in the knowledge base. On the institutional platform, Prompt S-5 (`manager-platform.md`) turns these flags into the Status column and the formal upload request.
---

## Prompt S-1 — General Analytical Sources

Search for and identify the most relevant and recent sources from the intranet and web covering: (i) public expenditure and public finance overall and in [sector] in [country]; (ii) PFM systems and their relationship to [sector] regulation, infrastructure, and/or service delivery; (iii) sector performance data and delivery challenges; and (iv) institutional and governance arrangements for [sector] delivery.

This should include analytical reports as well as official government websites, including those which provide sector and fiscal information.

Present the sources as a **numbered table** with columns **No. | Author | Year | Title | Relevance | Link | Download**, numbered sequentially from 1 in ranked order, with Link and Download as Markdown links that have passed the link check above; a source without one is left out and at most noted in one line beneath the table. Keep one running table; S-2–S-4 add rows and continue the same numbering rather than starting over.

When generating every section of the report, cite each source as a Markdown hyperlink to its link — e.g. ([World Bank, 2010](https://example.org/report)) — so the reader can open and verify it. Where a source has no link, cite it in plain text as ([author], [year]).

---

### ✏️ Review the output — focus on these points

**Source list (Prompt S-1).** Review before proceeding to S-2.

- [ ] The most important recent analytical reports for [country] and [sector] are included
- [ ] Official government sector strategy documents are identified
- [ ] Internationally comparable data sources (WHO, World Bank, IMF) are included
- [ ] Any significant gaps in coverage are flagged
- [ ] Every row has a verified Download link that opens the file or a non-empty page; sources without one were left out; no guessed, dead or empty links
- [ ] Every external source whose content could not be read is flagged Upload needed and listed for upload with its Download link

Add any missing sources with an additional search, giving each the next number in the running table — do not renumber sources already listed.

---

## Prompt S-2 — Budget and Expenditure Data Sources

Search for any recent sources of information on the overall budget and [sector] spending in [country], including: official budget documents from the finance ministry website; IMF program documents covering fiscal policy and social spending; civil society and think tank budget analysis; and international databases covering health/education/sector expenditure per capita.

Add the new sources as rows in the running table from S-1 (same columns: **No. | Author | Year | Title | Relevance | Link | Download**), numbering each from the last row used, in ranked order.

Include subnational government budget, revenue and expenditure data in your search.

---

### ✏️ Review the output — focus on these points

**Budget and expenditure sources (Prompt S-2).**

- [ ] The most recent budget documents are identified
- [ ] Both central and subnational spending data sources are covered
- [ ] Any gaps in spending data are flagged for the fiscal analysis in Section 2.3.2
- [ ] Every new row has a verified Download link that opens the file or a non-empty page; sources without one were left out
- [ ] Every new source whose content could not be read is flagged Upload needed and listed for upload

---

## Prompt S-3 — Political Economy and Reform History Sources

Search for any recent sources on the political economy of [sector] reform in [country], including: analyses of stakeholder interests and reform resistance; documentation of previous reform attempts and their outcomes; assessments of institutional relationships and power dynamics in [sector]; and any development partner political economy assessments or country governance analyses.

Add the new sources as rows in the running table from S-2 (same columns), numbering each from the last row used, in ranked order.

---

### ✏️ Review the output — focus on these points

**Political economy and reform history sources (Prompt S-3).** These feed Step 3 (Section 4.2 Stakeholder Strategy).

- [ ] Previous reform attempts (successful and unsuccessful) are documented
- [ ] Known sources of stakeholder resistance are identified
- [ ] Development partner political economy assessments are included where available
- [ ] Every new row has a verified Download link that opens the file or a non-empty page; sources without one were left out
- [ ] Every new source whose content could not be read is flagged Upload needed and listed for upload

Flag any significant gaps now.

---

## Prompt S-4 — Digital Systems and Capacity Sources

Search for any recent sources on digital systems, capacity development, and technical assistance in [sector] in [country], including: assessments of sector information systems and interoperability; capacity development programmes supported by development partners; procurement and supply chain management assessments; and workforce planning systems.

Add the new sources as rows in the running table from S-3 (same columns), numbering each from the last row used, in ranked order.

---

### ✏️ Review the output — focus on these points

**Digital systems and capacity sources (Prompt S-4).** These feed Step 3 (Section 4.3 Systems, Capacity and TA).

- [ ] The main sector information systems (HMIS, IFMIS, payroll systems, etc.) are identified
- [ ] Known digital systems gaps or interoperability failures are documented
- [ ] Active capacity development programmes are noted
- [ ] Every new row has a verified Download link that opens the file or a non-empty page; sources without one were left out
- [ ] Every new source whose content could not be read is flagged Upload needed and listed for upload

Flag any significant gaps now.

---

**Sources complete when all four prompts have been reviewed and approved, every source sits in one continuously numbered table, every row has a verified Download link to its file or to a non-empty page, and every source whose content could not be read is flagged for upload.**