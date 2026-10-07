---
title: OLePFM Session Manager — Institutional Platform Rules
description: Rules that apply only when the OLePFM workflow runs on the institutional platform with its knowledge base. Names the search tools for Prompts S-1 to S-4 (web_search, the internal knowledge base search, project_search) and the Enterprise Document Repository agent as the source of a link for a knowledge-base document; adds Prompt S-5, run after S-4, which checks that each listed source is indexed in the knowledge base or by project_search, lets the user upload what they need and removes the rest; sets the citation rules for Steps 1 to 3, the platform readings of the reference check's Text reachable column, and the items added to the Sources completion gate, the consistency audit (Prompt C-01) and the bibliography (Prompt C-09). Skip when the user supplies the documents directly, as in Claude Code.
---

# Institutional Platform Rules: Source Verification

**When this file applies.** Use it when the session runs on the institutional platform, that is, when Setup 1 (`manager-setup.md`) found the Report Template and the Synthesis Handbook in the root of the knowledge base, in report mode and in workshop mode (`manager-workshop.md`). Skip it when the user supplies the documents directly, as in Claude Code or Claude.ai: the principle holds there too (cite only what you have read), but the rules below are written for the platform's tools. On the platform a source passes two checks in order: **reachability**, a proper link to the document or to a non-empty page, which is the entry filter in `manager-00-source-prep.md`; and **indexing**, the document's text chunks returned by the internal knowledge base search or by `project_search`, checked by Prompt S-5 below. A link proves that a document exists, not that the AI can read it; a claim resting on unindexed text cannot be checked, so an unindexed source that the user does not upload leaves the table and is never cited. This file adds the search tools and the link source for S-1 to S-4, Prompt S-5 with its **Status** column, three citation rules, the platform readings of the Text reachable column, and items for the Sources completion gate, Prompt C-01 and Prompt C-09. The prompt files themselves do not change.

---

## Finding sources and their links (Prompts S-1 to S-4)

Search exhaustively with all three tools for every prompt in `manager-00-source-prep.md`: `web_search` for published reports, official websites and databases; the **internal knowledge base search** for the sector notes, prior diagnostic reports and other documents indexed on the backend; and `project_search` for the documents uploaded to this project or session. Run each tool on each prompt's topics, and keep searching on new keywords, authors and years until the searches stop returning new documents. Bibliographies and reference lists of indexed documents are leads to search for, not sources. Rank the candidates and apply the link check as `manager-00-source-prep.md` says; where the platform cannot open web pages, a link counts as checked only when it came from one of two places:

- **The search result itself.** `web_search` returned that URL for that document in this session, with a snippet of the page's text, not a title alone.
- **The Enterprise Document Repository agent.** For a document found in the knowledge base or by `project_search`, or whose search result gives no usable link, query the Enterprise Document Repository agent (the platform's Databricks SQL agent over the document repository) on the document's title, author and year, and take the link from the record it returns, exactly as returned. Say in the Relevance column that it came from the repository.

A source for which neither yields a link is not reachable and is not listed, as `manager-00-source-prep.md` says.

---

## Prompt S-5 — Index Verification of the Source List (adds the Status column)

Run after Prompt S-4 has been reviewed and approved, on the complete running table, every row of which is reachable.

---

For every source in the running table from Prompts S-1 to S-4, check whether the document's own text is indexed, so that its text chunks can be read in this session. Search the knowledge base for each source on its title keywords first, then on author and year, since the stored file name may differ from the title; then run `project_search` on the same terms. Count a source as indexed only if one of them returns the document's own text chunks now. A file whose text the search does not return (a scanned PDF, an image) is Not indexed, and you say why; so is a source known only from a link, a search result, a repository record or another document's bibliography, which show that it exists, not that you can read it. Carry every row flagged Upload needed in S-1 to S-4 over as Not indexed unless the search returns its text.

Add a **Status** column to the running table, so the columns are **No. | Author | Year | Title | Relevance | Link | Download | Status**, and fill it for every row with one of:

- **Indexed** — the knowledge base search returns the document's text. Give the file name it is stored under, for example `Indexed (stored as: xyz.pdf)`.
- **Uploaded** — the user has uploaded the document to the project or session and `project_search` returns its text.
- **Not indexed** — neither. The document is reachable by its link, but its text cannot be read here.

Keep every source's number as it is: do not remove, reorder or renumber rows at this point.

Below the table, list the **Not indexed** sources as an **upload request**, in table order so the most relevant come first: for each, its number, author, year and title, its verified link so the user can fetch the file, and where else the document can be obtained if you know. The user decides which of them the session needs: ask them to upload those, say that you will re-check each once uploaded, and that whatever stays Not indexed will be removed from the table. Do not group, rank or recommend; the Relevance column already says what each source is for. For a web page, online database or data portal, the file to upload is its data export or a saved copy of the page, since that is what will be cited.

Then stop and wait for the user.

---

### ✏️ Review the output — focus on these points

**Index verification (Prompt S-5).** Every citation in the report will rest on this column, so check it before Step 1.

- [ ] Every row has a Status, and every Indexed entry names the file it is stored under
- [ ] No source is marked Indexed only because a link, a search result or another document's bibliography shows that it exists
- [ ] The upload request lists every Not indexed source in table order with a verified link, and leaves the choice of what to upload to you
- [ ] You have decided which Not indexed sources the session needs; where one of them cannot be obtained, the gap is flagged

Upload the sources you need, then say "uploaded" to have them re-checked, or "proceed" to drop the rest from the table.

### After the user uploads

Re-check only the rows in the upload request. Set each one whose text `project_search` now returns to **Uploaded** (or **Indexed**, if it turns out to be in the knowledge base after all) and present the full table again, numbering unchanged. Repeat for as long as the user keeps uploading. When the user says "proceed", **remove every row still marked Not indexed** and list each removed source in one line beneath the table as *not listed: not indexed, not uploaded*, with its number, author, year, title and link, so the gap stays visible and the file can still be fetched later. A removed source's number is retired: never reuse it, and give the next new source the number after the highest ever used, so every remaining source keeps its number. A removed source can be restored, with its old number, if the user uploads it later and `project_search` returns its text. Then apply the Sources completion gate, with the additions below.

---

## Citation rules for Steps 1 to 3 (platform)

These apply to every prompt from Step 1 onward, in addition to the hyperlink rule in `manager-00-source-prep.md`.

1. **Cite only sources in the running table.** After S-5 every row is Indexed or Uploaded. Never cite a source listed beneath the table as not listed, or a document absent from the table.
2. **Cite the document you read, not the one it cites.** If a fact is known only because an indexed document cites another work, cite the indexed document, adding "citing [author, year]" where useful.
3. **Verify before citing anything new.** A source found later in the session (while drafting, or when the user asks for an additional search at a review point) is entered only once its link has been obtained as above, gets the next number, and is checked for indexing as in Prompt S-5 before it is cited. Say that you are adding it; do not cite it silently.

## Text reachable on the platform

The reference check (`manager-reference-check.md`) retrieves each cited document's text again at every draft and records the result in its Text reachable column. On the platform the only two routes are the ones Prompt S-5 checks, so the column reads *Yes: knowledge base (stored as …)*, *Yes: project_search (uploaded as …)* or *No: not indexed in the knowledge base or project_search*; a search that returns only a title, a file name or a bibliography entry is *No*, and a link or the Status column never makes it *Yes*. A row whose Source is not in the running table (removed at S-5, or never listed), or whose Text reachable column reads *No*, must be re-sourced, uploaded or removed before the step's completion gate.

---

## Additions to the Sources completion gate

Add these items to the Sources completion gate in `manager.md`:

- [ ] Every row of the running table has a Status of Indexed or Uploaded
- [ ] The upload request has been answered: every source the user decided the session needs is marked Uploaded, or its absence is flagged as a gap, and every source still Not indexed has been removed from the table and listed beneath it
- [ ] The only gaps in the numbering are the numbers retired at S-5; no number has been reused
- [ ] Each of the four coverage areas (analytical, budget and expenditure, political economy, digital systems and capacity) still has at least one source in the table; where one does not, the gap is flagged before Step 1

---

## Additions to Compilation and QA

Hand these to the AI when the Compilation and QA stage begins, as the economic-resilience variant hands over its deviation register.

**Prompt C-01, add item (vii) — Source availability.** Confirm that every citation in every chapter and annex points to a source in the running source table, whose Status is Indexed or Uploaded; that none points to a source removed at S-5, listed beneath the table as not listed, or absent from the table; and that no fact is attributed to a work known only through another document's bibliography. List each violation with its location, and name the document that was actually read, if there is one.

**Prompt C-09, bibliography.** The bibliography lists only sources in the running table, all Indexed or Uploaded; a source removed at S-5 does not appear in it.
