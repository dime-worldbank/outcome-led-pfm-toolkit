---
title: OLePFM Step 1 (1a, continued) — Section 2.3
description: Step 1 (file 1a, second of two) of the OLePFM report workflow. Generates Section 2.3 (Policy, Institutional and Public Finance Context, and the Feasibility Assessment), Prompts 1-04 to 1-11, with the chart interaction workflow for the fiscal charts and the Step 1 quality checks. Run after manager-01a-chapters1-2.md; for a cross-cutting fiscal outcome, Prompts 1-04 to 1-10 are replaced by the economic-resilience variant. Continue with manager-01b-annex1.md.
---

# Step 1 (file 1a, continued): Section 2.3

**Step 1, file 2 of 3.** Run these prompts after Prompts 1-01 to 1-03 in `manager-01a-chapters1-2.md` are complete and the challenge titles are confirmed. Those drafts are already in context — begin directly with Prompt 1-04.

Pause at every ✏️ intervention point and wait for user confirmation before proceeding.

> When Prompt 1-11 is complete and confirmed, continue with `manager-01b-annex1.md` (Prompts 1-12 to 1-15).

---

## Sub-step 1.4 — Map the sector policy, institutional and public finance context (Sections 2.3.1 and 2.3.2)

> **Economic resilience or another cross-cutting fiscal outcome?** Use Prompts ER-1-04 to ER-1-10 from `manager-01a-variant-economic-resilience.md` and `manager-01a-variant-economic-resilience-2.md` in place of Prompts 1-04 to 1-10 below, then continue with Prompt 1-11. Everything else in this file is unchanged.

### Prompt 1-04 — Section 2.3.1: Policy Framework

Please set out the relevant public sector policies for [sector] in [country], covering: the overarching policy framework and legislation; sector strategy documents and their key commitments; and any specific policies governing service delivery standards, decentralization, and regulation.

Keep the description to approximately 300 words.

---

### Prompt 1-05 — Section 2.3.1: Institutional Architecture

Please describe the institutions for [sector] in [country], including: (i) public and private sector delivery modalities (direct provision, funding and regulation, decentralization arrangements, digital systems); (ii) organizations involved at all levels of government and outside it; and (iii) the links and hierarchical relationships between organizations.

Keep the description to approximately 300 words.

---

### ✏️ Review the output — focus on these points

**Section 2.3.1 — Institutional Architecture and Diagram (Prompts 1-05, 1-06).** Review the description and diagram carefully before the financial flows analysis.

- [ ] All significant organizations are included at the correct level of government
- [ ] Hierarchical relationships between organizations are correctly described and drawn
- [ ] Non-government actors (private sector, faith-based, NGOs, development partners) are included where significant
- [ ] The diagram's swim lane assignments (Central Government / Local Government / Facilities / Communities) are correct
- [ ] No significant delivery or financing actor has been omitted

You can add missing nodes, correct level assignments, adjust relationship lines, or change colour coding. **Confirm the organizational map is accurate before proceeding, as it forms the basis for the financial flows analysis.**

### Prompt 1-06 — Section 2.3.1: Institutional Diagram (draw.io)

Please prepare an editable diagram using draw.io / diagrams.net showing the organizations involved in [sector] service delivery in [country] and the hierarchical relationships between them, from national level down to the point of service delivery.

Organize the diagram into clearly labelled horizontal bands representing: Central Government | Local/Regional Government | Facilities | Communities.

Use colour-coding to distinguish: core public sector bodies; local government; facilities; community/point of delivery; and non-government actors (private sector, faith-based, NGOs, development partners).

Include external actors such as development partners, faith-based providers, and NGOs where relevant. Use solid lines for hierarchical authority and resource flows and dashed lines for coordination and support relationships.

Caption the figure **Figure: Organizational Map** with a Source line, as in the template.

---

### ✏️ Review the output — focus on these points

**Financial Flows Description and Diagram (Prompts 1-07 to 1-09)** — a critical review point for the financial analysis, before the PFM systems description.

- [ ] All significant financing channels are identified — common omissions include intergovernmental transfers, facility-retained revenues, off-budget donor flows, and social insurance mechanisms
- [ ] Data on flow sizes is accurate and from authoritative sources
- [ ] Relative sizes of flows are correctly represented in the diagram
- [ ] Bottleneck descriptions for each channel are specific and evidence-based rather than generic
- [ ] Channel descriptions accurately reflect the organizational flow path at each stage

You can add a missing channel, correct flow-size data, adjust bottleneck descriptions, or ask for the diagram to be revised. **Confirm the financing channel analysis is accurate and complete before proceeding to the PFM systems description.**

### Prompt 1-07 — Section 2.3.2: Fiscal Policy Context

Using the sources identified, please provide an analysis of the overall revenues and expenditures for [sector] in [country]. Tell a story from the data which includes:

(i) Overall sector spending and sources of revenue in the sector, including where relevant: total sector spending over time, real, per capita; composition of sector revenue by source; spending by function/level of service/major policy program; national/subnational and organizational share of spending.

(ii) Analysis of financing and spending on the public sector results/programs in focus, including: resources available by major financing channel; share by economic categories (salaries, non-salary, capital); per capita spending on key service delivery budget lines — salaries, operational inputs, infrastructure, and key expenditures on drivers of quality; disparity analysis via per capita analysis of spending across space/regions/local governments; and/or frontline provider analysis.

Use the table "Figures: Fiscal Analysis" from the template for further guidance on this analysis.

Where data is available, also generate the charts that tell this story: pie / composition charts for the most recent year and line or column charts for trends. Present the charts under the template heading **Figures: Fiscal Analysis**, within the Fiscal Policy Context part of Section 2.3.2, following the **chart interaction workflow** below.

#### Chart interaction workflow (applies to every chart in this prompt)

1. **Pull the data from a cited source, not from memory.** Take every value from the Data360 API (or another identified source in the running table). Never hand-type an estimate. Each value a tool returns carries a verifiable **claim tag** — keep it with the value.
2. **Show BOTH the table and the chart, together.** For each figure output, in this order: (a) the **interactive chart**, then (b) its **underlying data table** directly beneath, showing every value with its year/category label, units and source. The table is the verifiable record; the chart is the visual. Never show a chart without its table.
3. **Render the chart interactively.** Use a fenced ` ```chart ` block containing a **Chart.js schema**: `{ "type": …, "data": { "labels": [...], "datasets": [{ "label", "data", … }] }, "options": {…} }`. Supported types: line, bar, pie, scatter. Do **not** use Recharts-style keys (`xKey`, `yKey`, `series`, `dataKey`) and do **not** use a ` ```recharts ` fence — those render empty. Use quoted string labels on the x-axis. (Mermaid is for diagrams, not data charts.) When the user asks for a report-ready artifact, additionally produce a data-exact matplotlib PNG saved to the file area; the inline chart is the preview, the PNG is the document figure.
4. **In the data table, each figure carries its Data360 claim tag**, so the platform can verify it against the source.
5. **Cite the source under each table:** indicator name + indicator code + source database (for example, *Government expenditure on education, total (% of government expenditure)* — WDI, `WB_WDI_SE_XPD_TOTL_GB_ZS`), plus the Data360 explorer link (`https://data360.worldbank.org`) when the site is reachable. When the explorer is down, give the indicator name/code/database and keep the API query URL as a machine-verifiable backup; do a single link-upgrade pass once the explorer is back rather than pasting a guessed deep-link that may 404.
6. **Never auto-lock a chart.** Present every chart as a **draft for review**. After the chart + table + source, ask the user to confirm it or to change type, series, years, titles or colours, and **wait**. Do not treat any chart as final, and do not move to the next figure, until the user explicitly locks it in. This is a ✏️ pause: the chart review below is the intervention point.

Prepare a data table for each chart generated, including the data source.

---

### ✏️ Review the output — focus on these points

**Fiscal charts (Prompt 1-07).** Each chart is a draft until you lock it in — review before moving on.

- [ ] Each figure shows **both** an interactive chart and its underlying data table
- [ ] Every value comes from Data360 (or a cited source) and carries its claim tag; chart numbers match the table exactly
- [ ] Charts render interactively (```chart + Chart.js schema), not as a static spec or empty block
- [ ] Each table has a source line: indicator name + code + database (+ explorer link when reachable)
- [ ] The story the charts tell matches the Section 2.3.2 narrative

Confirm each chart to lock it in, or ask for changes (type, series, years, titles, colours). No chart is final until you lock it.

### Prompt 1-08 — Section 2.3.2: Financial Flows Table and Description

Please provide a table detailing the main financial flows from central government through intermediate organizations to the point of [sector] service delivery in [country], covering:

(i) Each distinct "financing channel."
(ii) A "description" of the channel and its purpose.
(iii) The "organizations" through which funds flow at each stage.
(iv) The relative "value" of each flow.
(v) The key "problems" within each channel (e.g. late releases, low execution rates, off-budget flows).

There should be no more than 250 words per channel/row. Provide a summary narrative description of the main financial flows, of no more than 100 words for each channel.

---

### Prompt 1-09 — Section 2.3.2: Financial Flows Diagram (draw.io)

Please prepare a diagram using draw.io / diagrams.net of the main financial flows from central government through intermediate organizations to the point of [sector] service delivery in [country], showing: (i) each distinct financing channel using a distinct colour; (ii) the organizations through which funds flow at each stage; and (iii) the relative size of each flow encoded in line thickness, with thicker lines representing larger flows.

Include bottleneck indicators (amber diamond nodes) showing the key failure point in each channel. Provide a legend explaining the colour coding, line thickness scale, and bottleneck symbols. Caption it **Figure: Main Financial Flows**, as in the template.

---

### Prompt 1-10 — Section 2.3.2: PFM Systems Description

Please provide a description of the PFM rules and systems in [sector] in [country] and the roles of different organizations in managing funds for service delivery, covering: budget formulation; budget execution for wage and non-wage expenditure; intergovernmental fiscal transfers; procurement; audit and accountability; and digital financial management systems.

Use available diagnostics including PEFA and other reports. Highlight both areas of progress and persistent weaknesses. Keep the description to approximately 300 words.

---

### ✏️ Review the output — focus on these points

**PFM Systems Description (Prompt 1-10).** Review before proceeding to the feasibility assessment.

- [ ] All six PFM dimensions are covered (budget formulation, wage execution, non-wage execution, intergovernmental transfers, procurement, audit and accountability, digital systems)
- [ ] The PEFA and other diagnostic findings are correctly cited and interpreted
- [ ] Areas of genuine progress are acknowledged alongside persistent weaknesses
- [ ] The description is specific to the [sector] context rather than generic

Make corrections before proceeding.

---

## Sub-step 1.5 — Assess institutional capability and policy feasibility (Section 2.3.3)

### Prompt 1-11 — Section 2.3.3: Feasibility Assessment

Please provide a short assessment of approximately 300 words on the feasibility of achieving [sector] policy objectives in [country] from a technical, political, and financial perspective.

Use the descriptions of feasible policy and institutional capability from the OLePFM [sector] Outcome Note or the OLePFM Synthesis as a framing.

Assess: (i) whether policy commitments are fiscally affordable given the available fiscal envelope; (ii) whether the government has the institutional capability to deliver the policy; and (iii) whether there is stakeholder commitment and support for the reforms needed to ensure implementation.

---

### ✏️ Review the output — focus on these points

**Feasibility Assessment (Prompt 1-11).** Review before proceeding to the Annex.

- [ ] The financial affordability assessment reflects the actual fiscal envelope and neither overstates nor understates the financing gap
- [ ] The institutional capability assessment is grounded in the organizational and PFM analysis in Section 2.3
- [ ] The stakeholder commitment assessment reflects the actual political economy, including both supportive and resistant interests

Adjust any dimension that is too optimistic or pessimistic.

---

## Quality checks for Step 1 (optional)

Use these prompts at any stage to check and improve draft outputs.

**1-Q1 — Template Compliance Check**

Please check that the section headings, subheadings, and introductory texts in the draft Chapters 1 and 2 strictly follow the OLePFM Sector Reform Design Report Template. Identify any deviations and correct them.

**1-Q3 — Evidence Check**

Please check that all factual claims in Chapters 1 and 2 are supported by a hyperlinked parenthetical citation, e.g. ([World Bank, 2010](https://…)). Flag any unsupported claims and either add a citation or qualify the claim appropriately.

**1-Q4 — PFM Exclusion Check**

Please review the public sector challenge descriptions in Section 2.2 to confirm that no challenge mentions money, public finance, or PFM. Flag any challenges that violate this rule and suggest a revision.

---

## Prompt Sequence Summary

| Prompt | Output |
|---|---|
| 1-01 to 1-03 | Chapter 1, Sections 2.1 and 2.2 (`manager-01a-chapters1-2.md`) |
| 1-04 | Section 2.3.1: Policy Framework |
| 1-05 | Section 2.3.1: Institutional Architecture |
| 1-06 | Section 2.3.1: Institutional Diagram |
| 1-07 | Section 2.3.2: Fiscal Policy Context and Charts |
| 1-08 | Section 2.3.2: Financial Flows Table and Description |
| 1-09 | Section 2.3.2: Financial Flows Diagram |
| 1-10 | Section 2.3.2: PFM Systems Description |
| 1-11 | Section 2.3.3: Feasibility Assessment |

Continue with `manager-01b-annex1.md`.
