---
title: OLePFM Session Manager — Institutional Platform Rules
description: Rules that apply only when the OLePFM workflow runs on the institutional platform with its knowledge base. Adds Prompt S-5, run after S-4, which checks that every source in the running table is indexed in the knowledge base or uploaded to the session and asks the user to upload the rest; the citation rules that follow for Steps 1 to 3; what makes a source's text reachable on the platform (indexed in the internal knowledge base or returned by project_search); and the items it adds to the Sources completion gate and the consistency audit (Prompt C-01). Skip when the user supplies the documents directly, as in Claude Code.
---

# Institutional Platform Rules: Source Verification

**When this file applies.** Use it when the session runs on the institutional platform, that is, when Setup 1 (`manager-setup.md`) found the Report Template and the Synthesis Handbook in the root of the knowledge base. Skip it when the user supplies the documents directly, as in Claude Code or Claude.ai: the principle still holds there (cite only what you have read), but the verification prompt below is written for the platform's knowledge base. It applies in report mode and in workshop mode (`manager-workshop.md`), since both run the Sources stage.

**Why it exists.** On the platform, Prompts S-1 to S-4 (`manager-00-source-prep.md`) find sources in two ways: through web searches, and in the bibliographies of documents that are already indexed in the knowledge base. Neither means the source itself is indexed. A web search result gives a title and a snippet; a bibliography entry shows only that another document cited the work. If the full text is not indexed, the AI cannot read it, any claim attributed to it cannot be checked, and the citation is unreliable. Prompt S-5 checks every source, asks the user to upload what is missing, and marks what remains unavailable so that it is never cited.

**What it adds, and where.** One prompt, S-5, run after S-4 and before the Sources completion gate; a **Status** column in the running source table, which carries through the rest of the session; three citation rules for Steps 1 to 3; extra items for the Sources completion gate in `manager.md`; and one extra item each for the consistency audit (Prompt C-01) and the bibliography (Prompt C-09). The prompt files themselves do not change.

---

## Prompt S-5 — Reachability Verification of the Source List (adds the Status column)

Run after Prompt S-4 has been reviewed and approved, on the complete running table.

---

For every source in the running table from Prompts S-1 to S-4, check whether the document itself is indexed in the knowledge base. Search the knowledge base for each source on its title keywords first, then on author and year, since the stored file name may differ from the title. Count a source as indexed only if a knowledge base search or `project_search` returns the document's own text now; a file whose text the search does not return (a scanned PDF, an image) is Not indexed, and you say why. A web search result, a web page whose content you cannot read, or an entry in the bibliography or reference list of another indexed document, does not count: it shows that the document exists or was cited, not that you can read it. Carry every row flagged Upload needed in S-1 to S-4 over as Not indexed unless the knowledge base or `project_search` returns its text.

Add a **Status** column to the running table, so the columns are **No. | Author | Year | Title | Relevance | Link | Download | Status**, and fill it for every row with one of:

- **Indexed** — the document is in the knowledge base. Give the file name it is stored under, for example `Indexed (stored as: xyz.pdf)`.
- **Uploaded** — the user has uploaded the document to the project or session and `project_search` returns its text.
- **Not indexed** — neither. The source is known only from a web search or from another document's bibliography.

Keep every source's number as it is: do not remove, reorder or renumber rows.

Below the table, list the **Not indexed** sources as an **upload request**: for each, give its number, author, year and title, and repeat its verified Download link so the user can fetch the file, and say where else the document can be obtained if you know. Ask the user to upload to this session the documents they can obtain, and say that you will re-check them once uploaded. Treat a web page, online database or data portal as a document: its Download link is the data export or file to upload, since that is what will be cited.

Then stop and wait for the user.

---

### ✏️ Review the output — focus on these points

**Reachability verification (Prompt S-5).** Every citation in the report will rest on this column, so check it before Step 1.

- [ ] Every row has a Status, and every Indexed entry names the file it is stored under
- [ ] No source is marked Indexed only because a web search found it or another document cites it
- [ ] The upload request gives enough detail to find each Not indexed document, with its Download link wherever a file exists
- [ ] The sources the report depends on most (the main analytical reports, the budget documents, the PEFA or public expenditure review) are Indexed or about to be uploaded; where one cannot be obtained, the gap is flagged

Upload what you can, then say "uploaded" to have those sources re-checked, or "proceed" to mark the rest as not available.

### After the user uploads

Re-check only the rows in the upload request. Set each one whose text `project_search` now returns to **Uploaded** (or **Indexed**, if it turns out to be in the knowledge base after all) and present the full table again, numbering unchanged. Repeat for as long as the user keeps uploading. When the user says "proceed", change every row still marked Not indexed to **Not available: do not cite**, and keep the row in the table so the gap stays visible and the numbering stays stable. Then apply the Sources completion gate, with the additions below.

---

## Link check on the platform

The link check in `manager-00-source-prep.md` asks the AI to open each URL. Where the platform cannot open web pages, a link counts as checked only when this session's web search returned that URL for that document; a URL from memory is never entered. The Download links repeated in the S-5 upload request must have passed that check, because the user will click them to fetch the files.

## Citation rules for Steps 1 to 3 (platform)

These apply to every prompt from Step 1 onward, in addition to the hyperlink rule in `manager-00-source-prep.md`.

1. **Cite only Indexed or Uploaded sources.** Never cite a source marked Not available, and never cite a document that is not in the running table.
2. **Cite the document you read, not the one it cites.** If a fact is known only because an indexed document cites another work, cite the indexed document, adding "citing [author, year]" where useful. Do not cite the other work as if you had read it.
3. **Verify before citing anything new.** A source found later in the session (while drafting a section, or when the user asks for an additional search at a review point) gets the next number in the running table and is checked as in Prompt S-5 before it is cited. Say that you are adding it; do not cite it silently.

## Reachability on the platform

On the platform a source's text is reachable in exactly two ways: it has been **indexed in the internal knowledge base** (the backend library that Setup 1 and Prompt S-5 search), or it is **returned by `project_search`**, the vector search over the documents uploaded to the project or session. The reference check (`manager-reference-check.md`) tests reachability by running a knowledge base search or `project_search` for the passage and quoting from the text the search returns. A search that returns only a title, a file name or a bibliography entry, or no text at all, means the text is not reachable. A URL does not by itself make a source reachable here: a web source counts only once a saved copy of the page has been uploaded and `project_search` returns it. The Text reachable column therefore reads *Yes: knowledge base (stored as …)*, *Yes: project_search (uploaded as …)* or *No: not indexed in the knowledge base or project_search*.

**Reference check tables.** The tables that `manager-reference-check.md` adds after every cited draft, and merges per chapter at compilation, make breaches of these rules visible: a row whose Source is marked Not available in the running table, or whose Text reachable column reads *No*, must be re-sourced, uploaded or removed before the step's completion gate. The reference check retrieves the text again at every draft: Status says where a document is, reachability says that the knowledge base or `project_search` returned its text.

---

## Additions to the Sources completion gate

Add these items to the Sources completion gate in `manager.md`:

- [ ] Every row of the running table has a Status
- [ ] The upload request has been answered: every source the user could obtain is marked Uploaded, and the rest are marked Not available: do not cite
- [ ] Each of the four coverage areas (analytical, budget and expenditure, political economy, digital systems and capacity) still has at least one Indexed or Uploaded source once the unavailable ones are set aside; where one does not, the gap is flagged before Step 1

---

## Additions to Compilation and QA

Hand these to the AI when the Compilation and QA stage begins, as the economic-resilience variant hands over its deviation register.

**Prompt C-01, add item (vii) — Source availability.** Confirm that every citation in every chapter and annex points to a source whose Status in the running source table is Indexed or Uploaded; that no citation points to a source marked Not available or to a document absent from the table; and that no fact is attributed to a work known only through another document's bibliography. List each violation with its location, and name the document that was actually read, if there is one.

**Prompt C-09, bibliography.** The bibliography lists only sources with Status Indexed or Uploaded. A source marked Not available does not appear in it, because nothing in the report may cite it.
