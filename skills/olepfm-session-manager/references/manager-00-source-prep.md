---
title: OLePFM Sources — Source Preparation
description: Sources stage of the OLePFM report workflow, run once before any chapter drafting. Identifies all sources needed across the full report (analytical, fiscal, political economy, digital systems), ranks them by relevance and popularity, and checks each one's link and readability together before it enters the running source table: only those with a live, correct link to the document file or to a non-empty page are entered, and a source whose text cannot be read is flagged for upload.
---

# Sources: Source Preparation

This skill is run once at the start of the session (the Sources stage, before Step 1). It identifies all sources needed across the full report — analytical, fiscal, political economy, and systems. Complete and confirm all four prompts before proceeding to Step 1.

**The running table.** Every source is entered into a **single running numbered table** — columns **No. | Author | Year | Title | Relevance | Link | Download | Verified**. **Link** is the URL the in-text citation points to (the page where the source is published); citations hyperlink to it (see S-1). **Download** is a direct link to the document file itself (usually a PDF) or, for an online database, to a data export or API query that returns the data; for a web page that is itself the source (an official website, a data portal), it is the page's URL; for a document the user has supplied to the session, it is the file name. **Verified** holds the link-check evidence for each URL in the row: the status and the exact title and year the URL returned, so a mismatch cannot hide. Numbering starts at 1 in S-1 and continues unbroken through S-2, S-3 and S-4 — never restarted per prompt — so each source keeps one stable number for the rest of the session.

**How a source enters: rank, then check link and readability together.** For each prompt, gather every candidate the searches return and rank them by relevance and popularity, without regard to whether a link has been found yet: relevance to the prompt's topics and to [country] and [sector] first, then popularity, meaning how widely the source is cited and relied on (an official government document, a World Bank, IMF or PEFA report or a national statistics release ranks above a working paper, a news item or a blog). Then take the ranked list source by source: run the link check and, the moment a link passes, the readability check on the same source, and enter the row with both results, in ranked order so that the numbering follows the ranking. The two checks are never run as separate rounds. A verified link is the condition of entry: a source that fails is dropped, not demoted, however relevant it looks, because its document cannot be obtained, uploaded or checked; mention it, if at all, in one line beneath the table as *not listed: no link*, so the user can look for it elsewhere. Never fill a Link or Download cell with a placeholder, a URL from memory or one built from a pattern: a plausible link that does not open is worse than none. Re-check a link whenever its row is edited.

**The link check.** Every Link and Download URL must be **live, non-empty and correct**, and all three are judged on what actually came back, never on the fact that something came back.

- *Live*: open it where the environment can fetch pages and read the HTTP status. Only a 2xx response passes. A 404, 403, 410 or 5xx fails even when the server sends a full page with it, which many sites do; so does a login wall or a redirect to a generic home, search or listing page.
- *Non-empty*: the page's main body holds the document's own text or data. Site chrome is not content: navigation menus, headers, footers, cookie banners, sidebars and lists of other pages can add up to a long page that says nothing, so look for at least one substantive paragraph, table or file about the named document. Read the page title and the main body in the page's own language, translating if needed: a not-found or error page is usually phrased in the site's language ("the content you are looking for was not found", "try again or use the navigation menu") and carries the site's full menu and footer, so it looks populated. Any such message, an empty page, a placeholder, a cookie or script shell with no content, or a zero-length file fails exactly as an error status does. A Download link must return the file itself, of the expected type and a plausible size, opening to the document's title page, not an HTML page in its place.
- *Correct*: a content match, not a liveness test. The title that opens matches the row's title, and the year or the author matches too; a different title or year means a different document, and the link fails. The Download link opens the file itself, not a landing page.

Record the evidence in the Verified column, one entry per URL: the status and the exact title and year it returned, for example *200; returned «Health Sector Strategic Plan 2023–2027», 2023*. Every distinct URL in a row is checked on its own: the Download link never inherits the Link's result, even for the same source. A URL found in a source map, an earlier list or table, a summary or another document's bibliography is a discovery candidate only, never verified by that fact, and is checked like any other. Where pages cannot be fetched, a link counts as checked only when a web search in this session returned that URL for that document with a snippet whose words come from the document's content; a title alone, menu text or a not-found message is no evidence that the page has content. On the institutional platform, which cannot open pages, `manager-platform.md` names the search tools to run for each prompt, the two-pass link verification that replaces opening the URL, and where the link of a document found in the knowledge base comes from.

**The readability check, with the link check.** A live link says nothing about whether the text can be read: a search result is a title and a snippet, not the document. For every source whose link has just passed, open the page or file and read it in this session before entering the row. Where that is not possible, enter the row flagged **Upload needed** in the Relevance column and, below the table, ask the user to upload the document using its Download link. A flagged source is not cited until the user has uploaded it or it is found in the knowledge base. The reference check (`manager-reference-check.md`) repeats this readability test for every cited passage at every draft. On the institutional platform, the index check S-5 (`manager-platform.md`), applied to each file source as its link is verified, replaces this flag with the Status column and the formal upload request; a web page is read at its link there.
---

## Prompt S-1 — General Analytical Sources

Search for and identify the most relevant and recent sources from the intranet and web covering: (i) public expenditure and public finance overall and in [sector] in [country]; (ii) PFM systems and their relationship to [sector] regulation, infrastructure, and/or service delivery; (iii) sector performance data and delivery challenges; and (iv) institutional and governance arrangements for [sector] delivery.

This should include analytical reports as well as official government websites, including those which provide sector and fiscal information. Project documents count too: a Project Appraisal Document (PAD), an Implementation Completion and Results Report or a programme document is an analytical source for its sector context, institutional analysis, results data and fiduciary or PFM assessment, and is cited for that diagnostic content, not for the project's design. Do not leave such documents out as operational.

Present the sources as a **numbered table** with columns **No. | Author | Year | Title | Relevance | Link | Download | Verified**, numbered sequentially from 1 in ranked order, with Link and Download as Markdown links that have passed the link check above; a source without one is left out and at most noted in one line beneath the table. Keep one running table; S-2–S-4 add rows and continue the same numbering rather than starting over.

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

Add the new sources as rows in the running table from S-1 (same columns: **No. | Author | Year | Title | Relevance | Link | Download | Verified**), numbering each from the last row used, in ranked order.

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