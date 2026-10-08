---
title: OLePFM Session Manager — Institutional Platform Rules
description: Rules that apply only when the OLePFM workflow runs on the institutional platform with its knowledge base. Names the search tools for Prompts S-1 to S-4 (web_search, the app-wide knowledge base search, project_search), the two-pass link verification through web_search that stands in for opening pages, and the Enterprise Document Repository agent as the link source for knowledge-base documents. Adds the index check S-5, applied inside each sourcing prompt to every source as its link is verified, which fills the Status column, lets the user upload what they need and removes the rest; requires the user's must-have sources to be uploaded before Step 1. Sets the citation rules for Steps 1 to 3, the platform readings of the Text readable column, and the items added to the Sources completion gate, Prompt C-01 and Prompt C-09. Skip when the user supplies the documents directly, as in Claude Code.
---

# Institutional Platform Rules: Source Verification

**When this file applies.** Use it when the session runs on the institutional platform, that is, when Setup 1 (`manager-setup.md`) found the Report Template and the Synthesis Handbook in the root of the app-wide knowledge base, in report mode and in workshop mode (`manager-workshop.md`). Skip it when the user supplies the documents directly, as in Claude Code or Claude.ai: the principle holds there too (cite only what you have read), but the rules below are written for the platform's tools. On the platform a source passes two checks in order: the **link check**, a proper link to the document or to a non-empty page, the entry filter in `manager-00-source-prep.md`; and **readability**, checked at the same time by the index check S-5 below. Readability depends on what the link points to. A **web page** is readable on the platform at its link, so it needs no indexing or upload. A **file** (PDF, Word, text, spreadsheet or any other document) is not: the platform's document reader cannot open an `https://` link (it reads only the app-wide knowledge base and the files uploaded to the project), and `web_search` returns snippets, not the file, so an external file becomes readable only once it is indexed in the app-wide knowledge base or uploaded to the project. A link proves that a file exists, not that the platform can read it. A claim resting on text the platform cannot read cannot be checked, so an unindexed source that the user does not upload leaves the table and is never cited. This file adds the search tools and the link source for S-1 to S-4, the index check S-5 with its **Status** column, three citation rules, the platform readings of the Text readable column, and items for the Sources completion gate, Prompt C-01 and Prompt C-09. The prompt files themselves do not change.

| Link check | Readable here? | Action |
|---|---|---|
| Passed | Yes | Enter the source and cite it. |
| Passed | No (a file) | **Upload case.** The user downloads the file from the working link and uploads it; the S-5 index check then confirms that `project_search` returns its text. |
| Failed | Not tested | **Drop it.** A dead link gives nothing to download, so there is nothing to upload. Re-source only with independent reason to believe a correct URL exists. |

---

## Finding sources and their links (Prompts S-1 to S-4)

Search exhaustively with all three tools for every prompt in `manager-00-source-prep.md`: `web_search` for published reports, official websites and databases; the **app-wide knowledge base search** (the platform's shared backend library, the one Setup 1 searches, also called the internal knowledge base) for the sector notes, prior diagnostic reports and other documents indexed there; and `project_search` for the documents uploaded to this project or session. Run each tool on each prompt's topics, and keep searching on new keywords, authors and years until the searches stop returning new documents. Bibliographies and reference lists of indexed documents are leads to search for, not sources. Rank the candidates and apply the link check as `manager-00-source-prep.md` says. Because the platform cannot open pages, the check is run as a **two-pass link verification** through `web_search`, and no link enters the running table until it has passed both passes:

- **Pass 1, discovery.** The URL appears in a `web_search` result for that document.
- **Pass 2, confirmation.** A separate, targeted `web_search` call that names the exact URL(s) and asks what document each returns. Batch several URLs into one call so the double-check is routine, but every distinct URL in the table, in the Link column and in the Download column alike, gets its own Pass 2 result: a URL never inherits verification from another URL verified in the same batch, even for the same source. Pass 2 is a content-match test, not a liveness test. The link is **Verified** only if the tool confirms that the URL returns the expected document, with the returned title matching the row's title and the year or the author matching too; menu, title-only or error text, or a different title or year, means **Failed**: the link is not entered, and a source with no Verified link is noted beneath the table as *not listed: no link*. A URL that merely appears in one search result is not verified; a dead page often returns a full HTML body of menus and footer. Record the evidence in the Verified column, per URL: *Pass 2: returned «exact title», «year» ✓*.
- **Carried-over links are candidates only.** A URL surfaced in a source map, an earlier session's table, a summary or another document's bibliography is never authoritative and passes its own Pass 2 before use.
- **The Enterprise Document Repository agent.** For a document found in the knowledge base or by `project_search`, or whose search result gives no usable link, query the Enterprise Document Repository agent (the platform's Databricks SQL agent over the document repository) on the document's title, author and year, and take the link from the record it returns, exactly as returned. That record is the evidence: write in the Verified column *repository record: «exact title», «year»*.

**Every link shows its Pass 2 result, from this turn.** For every link in the table, the Verified column shows the Pass 2 result next to it. If there is no verification result from this turn, the link does not go in: a result from an earlier turn, an earlier table or memory does not count, and the row is left out until the link has been verified again in the current output. Re-run both passes whenever a row's link is edited or a replacement URL is found; a row whose link fails on re-check is removed and its number retired. As soon as a link is Verified, run the index check (S-5 below) on that source and enter its row with its Status: the two checks are done together, source by source, within the prompt, never as a separate round afterwards. A dead link has nothing to upload: the upload request covers only rows whose link is Verified.

---

## S-5 — Index Verification, inside each sourcing prompt (adds the Status column)

Not a separate prompt: apply this inside each of Prompts S-1 to S-4, to every source the moment its link is Verified and before its row is entered, so that the table each prompt presents already carries the Status column and the upload request. Its review items join that prompt's ✏️ checklist.

---

For every source whose link has just been Verified, before entering its row, decide first what the link points to. A web page (an HTML page, including an official website or a data portal's own pages) is readable at its link: give it Status **Web page** and skip the index search. Never give Web page to a link that returns a file: a URL ending in .pdf, .docx, .xlsx, .txt or another file extension, or one whose Pass 2 result shows a document download, is a file even when it sits on a website, and goes through the index check. For a file (PDF, Word, text, spreadsheet or any other document), check whether the document's own text is indexed, so that the platform can read its text chunks in this session; this is the readability check of `manager-00-source-prep.md`, run with the platform's two indexes. Search the knowledge base for each source on its title keywords first, then on author and year, since the stored file name may differ from the title; then run `project_search` on the same terms. Count a source as indexed only if one of them returns the document's own text chunks now. A file whose text the search does not return (a scanned PDF, an image) is Not indexed, and you say why; so is a source known only from a link, a search result, a repository record or another document's bibliography, which show that it exists, not that you can read it. On the platform this check replaces the Upload needed flag of `manager-00-source-prep.md`: the Status column carries the result instead.

The running table carries a **Status** column from S-1 onwards, so the columns are **No. | Author | Year | Title | Relevance | Link | Download | Verified | Status**, filled for every row as it is entered with one of:

- **Indexed** — the knowledge base search returns the document's text. Give the file name it is stored under, for example `Indexed (stored as: xyz.pdf)`.
- **Uploaded** — the user has uploaded the document to the project or session and `project_search` returns its text.
- **Web page** — the source is an HTML page whose text the platform reads at its link. No indexing or upload needed. Never for a link to a PDF or any other file, whatever site hosts it.
- **Not indexed** — a file that neither index returns. It has a link, but the platform cannot read its text.

Keep every source's number as it is: do not remove, reorder or renumber rows at this point.

Below the prompt's table, list its **Not indexed** sources as an **upload request**, in table order so the most relevant come first: for each, its number, author, year and title, its verified link so the user can fetch the file, and where else the document can be obtained if you know. The user decides which of them the session needs: ask them to upload those, say that you will re-check each once uploaded, and that whatever stays Not indexed will be removed from the table. Do not group, rank or recommend; the Relevance column already says what each source is for. For an online database or data portal whose figures come as a file export, the export is the file to upload, since that is what will be cited; the portal's own pages are web pages.

The upload request goes in the same output as the prompt's table, before its ✏️ block.

---

### ✏️ Items added to each sourcing prompt's checklist

**Link verification and index verification (S-5).** Every citation in the report will rest on these columns, so check them before saying proceed.

- [ ] Every link in the table has a Pass 2 result from this turn in the Verified column; no link appears without one
- [ ] Every new row has a Status, and every Indexed entry names the file it is stored under
- [ ] No source is marked Indexed only because a link, a search result or another document's bibliography shows that it exists
- [ ] The upload request lists every Not indexed source in table order with a verified link, and leaves the choice of what to upload to you
- [ ] You have decided which Not indexed sources the session needs; where one of them cannot be obtained, the gap is flagged

Upload the sources you need, then say "uploaded" to have them re-checked; say "proceed" to drop the rest from the table, or "later" to carry them forward as Not indexed and decide at the final pass.

### After the user uploads

Re-check only the rows in the upload request. Set each one whose text `project_search` now returns to **Uploaded** (or **Indexed**, if it turns out to be in the knowledge base after all) and present the full table again, numbering unchanged. Repeat for as long as the user keeps uploading. A row deferred with "later" stays Not indexed and is listed again in a **final pass** after S-4 is approved, before the Sources completion gate, with the same choices. When the user says "proceed", at any sourcing prompt or at the final pass, **remove every row still marked Not indexed** from the list in question and list each removed source in one line beneath the table as *not listed: not indexed, not uploaded*, with its number, author, year, title and link, so the gap stays visible and the file can still be fetched later. A removed source's number is retired: never reuse it, and give the next new source the number after the highest ever used, so every remaining source keeps its number. A removed source can be restored, with its old number, if the user uploads it later and `project_search` returns its text. After the final pass, apply the Sources completion gate, with the additions below.

---

## Citation rules for Steps 1 to 3 (platform)

These apply to every prompt from Step 1 onward, in addition to the hyperlink rule in `manager-00-source-prep.md`.

1. **Cite only sources in the running table.** After S-5 every row is Indexed, Uploaded or Web page. Never cite a source listed beneath the table as not listed, or a document absent from the table.
2. **Cite the document you read, not the one it cites.** If a fact is known only because an indexed document cites another work, cite the indexed document, adding "citing [author, year]" where useful.
3. **Verify before citing anything new.** A source found later in the session (while drafting, or when the user asks for an additional search at a review point) is entered only once its link has been Verified and its index check (S-5) done, as above, and gets the next number before it is cited. Say that you are adding it; do not cite it silently.

## Text readable on the platform

The reference check (`manager-reference-check.md`) retrieves each cited document's text again at every draft and records the result in its Text readable column. On the platform there are three routes: the two indexes the index check S-5 uses, and reading a web page at its link, so the column reads *Yes: knowledge base (stored as …)*, *Yes: project_search (uploaded as …)*, *Yes: web page content read* or *No: not indexed in the knowledge base or project_search*; a search that returns only a title, a file name or a bibliography entry is *No*, and for a file a link or the Status column never makes it *Yes*. A row whose Source is not in the running table (removed as Not indexed, or never listed), or whose Text readable column reads *No*, must be re-sourced, uploaded or removed before the step's completion gate.

**Must-have sources.** The user names the sources the session must have, at any sourcing prompt or at the final pass. Each must be Indexed, Uploaded or a Web page before any Step 1 drafting begins: for a file, a Verified link is not enough, because the platform cannot read a file at its link. A must-have that stays Not indexed is flagged as a gap at the Sources completion gate, and the user decides whether Step 1 starts without it.

---

## Additions to the Sources completion gate

Add these items to the Sources completion gate in `manager.md`:

- [ ] Every row of the running table has a Status of Indexed, Uploaded or Web page
- [ ] The upload request has been answered: every must-have source the user named is Indexed, Uploaded or a Web page, or its absence is flagged as a gap, and every source still Not indexed has been removed from the table and listed beneath it
- [ ] The only gaps in the numbering are the numbers retired for removed sources; no number has been reused
- [ ] Each of the four coverage areas (analytical, budget and expenditure, political economy, digital systems and capacity) still has at least one source in the table; where one does not, the gap is flagged before Step 1

---

## Additions to Compilation and QA

Hand these to the AI when the Compilation and QA stage begins, as the economic-resilience variant hands over its deviation register.

**Prompt C-01, add item (vii) — Source availability.** Confirm that every citation in every chapter and annex points to a source in the running source table, whose Status is Indexed, Uploaded or Web page; that none points to a source removed as Not indexed, listed beneath the table as not listed, or absent from the table; and that no fact is attributed to a work known only through another document's bibliography. List each violation with its location, and name the document that was actually read, if there is one.

**Prompt C-09, bibliography.** The bibliography lists only sources in the running table, all Indexed, Uploaded or Web page; a source removed as Not indexed does not appear in it.
