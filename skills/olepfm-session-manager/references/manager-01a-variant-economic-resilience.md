---
title: OLePFM Step 1 (1a) variant — Economic Resilience: Section 2.3 Prompts (file 1 of 2)
description: Drop-in replacements for Prompts 1-04 to 1-10 (Section 2.3) when the outcome is cross-cutting and fiscal — economic resilience, macro-fiscal stability, fiscal or debt sustainability. Replaces the service-delivery institutional tiers, financial-flows table and sector-spending charts with fiscal-outcome tiers, a self-reinforcing fiscal-cycle narrative and diagram, and macro-fiscal charts. Use together with manager-01a-section2-3.md; every other Step 1 prompt is unchanged.
---

# Step 1 (file 1a) variant: Economic Resilience — Section 2.3 prompts (file 2 of 2)

Continue here after Prompts ER-1-04 to ER-1-06 in `manager-01a-variant-economic-resilience.md`, which also holds the purpose, the deviation register and the prompt map for this variant. Pause at every ✏️ intervention point and wait for user confirmation before proceeding.

---

## Sub-step 1.4 (continued) — Public finance context (economic-resilience variant of Section 2.3.2)

### Prompt ER-1-07 — Section 2.3.2: Fiscal Policy Context and Charts (replaces the sector-spending charts)

Using the sources identified, please provide a macro-fiscal analysis for [country] that tells the story of the [fiscal outcome] through the following lenses (omit the standard sector-spending pie/column charts, which do not apply to a cross-cutting fiscal outcome):

(i) Growth and inflation — real GDP growth vs. population growth (per-capita trajectory) and inflation, showing whether growth is strong, stable, and shock-resistant. (Chart: bars + line, multi-year.) (ii) Aggregate fiscal balance — revenue (incl. grants) and expenditure as % of GDP and the resulting overall balance, showing the scale and persistence of deficits. (Chart: grouped bars + balance line.) (iii) Realism of fiscal forecasts / budget credibility — approved vs. actual deficit (or expenditure outturn vs. budget), showing systematic optimism. (Chart: approved vs. actual bars.) (iv) Cyclicality of fiscal policy — primary balance against growth, showing whether policy is counter-cyclical (resilience-building) or pro-cyclical. (Chart: scatter + trend line.) (v) Debt and debt service — gross public debt as % of GDP and interest as a share of domestic revenue, with debt-distress status. (Chart: debt bars + interest/revenue line.) (vi) Spending quality / productive squeeze — economic composition of spending over time (wages, interest, development/capital, other), showing rigid recurrent commitments crowding out productive investment, plus development-budget execution. (Chart: stacked bars.) (vii) Fiscal cost of extra-budgetary institutions — SOE/parastatal debt, guarantees, and contingent-liability estimates (incl. any DSA contingent-liability shock). (Chart: bars, % of GDP.)

For each lens, write a short titled paragraph (bolded lead-in) referencing its figure, and deliver each figure following the **chart interaction workflow** below.

#### Chart interaction workflow (applies to every macro-fiscal chart in this prompt)

1. **Pull the data from a cited source, not from memory.** Take every value from the Data360 API (or another identified diagnostic in the running table). Never hand-type a value. Each value a tool returns carries a verifiable **claim tag** — keep it with the value. Where exact published series are genuinely unavailable, use best-available estimates from the named diagnostics and add the explicit provenance note below.
2. **Show BOTH the table and the chart, together.** For each figure, output: (a) the **interactive chart**, then (b) its **underlying data table** directly beneath, showing every value with its year/category label, units and source. The table is the verifiable record; the chart is the visual. Never show a chart without its table.
3. **Render the chart interactively.** Use a fenced ` ```chart ` block containing a **Chart.js schema** (`type` / `data.labels` / `data.datasets` / `options`); types used here are line, bar (incl. grouped and stacked) and scatter. Do **not** use Recharts-style keys (`xKey`, `yKey`, `series`, `dataKey`) or a ` ```recharts ` fence — those render empty. Use quoted string labels on the x-axis. For report-ready delivery, also produce the charts via a single self-contained generator script (*_charts.py, matplotlib) that writes a 300-dpi PNG per figure and an Excel workbook (one sheet per figure, data + source) to the file area; the inline ` ```chart ` block is the preview, the PNG/Excel are the deliverables.
4. **In the data table, each value carries its Data360 claim tag** (or, for a best-available estimate, the provenance note), so the platform can verify what is verifiable and flag what is not.
5. **Cite the source under each table:** indicator name + indicator code + source database, plus the Data360 explorer link (`https://data360.worldbank.org`) when the site is reachable. When the explorer is down, give name/code/database and keep the API query URL as a machine-verifiable backup; upgrade links in one pass when the explorer is back rather than pasting a guessed deep-link.
6. **Never auto-lock a chart.** Present every figure as a **draft for review**. After the chart + table + source, ask the user to confirm it or to change type, series, years, titles or colours, and **wait**. No figure is final, and you do not move to the next lens, until the user explicitly locks it in. The chart review below is the ✏️ intervention point.

Provenance rule: where exact published series are unavailable, use best-available estimates from the named diagnostics and add an explicit provenance note that values must be reconciled against exact published series before publication; flag the reconciliation for the Compilation audit. Cite sources as hyperlinked parentheticals.

---

### ✏️ Review the output — focus on these points

**Fiscal Policy Context and Charts (Prompt ER-1-07).** Each chart is a draft until you lock it in — review before the fiscal-cycle narrative.

- [ ] All applicable lenses covered (growth/inflation; balance; forecast realism; cyclicality; debt/service; spending composition; fiscal risk)
- [ ] Each figure shows **both** an interactive chart (```chart + Chart.js schema) and its underlying data table
- [ ] Every value comes from Data360 (or a cited diagnostic) and carries its claim tag; chart numbers match the table exactly
- [ ] Each table has a source line: indicator name + code + database (+ explorer link when reachable)
- [ ] Provenance note present where series are best-available estimates; reconciliation flagged for the Compilation audit
- [ ] Standard sector-spending pie/column charts correctly omitted (with the omission noted as a deviation)
- [ ] Figures are numbered consistently with in-text references

Confirm each chart to lock it in, or ask for changes (type, series, years, titles, colours). No chart is final until you lock it.

---

### Prompt ER-1-08 — Section 2.3.2: Financial Flows as a Self-Reinforcing Fiscal Cycle (replaces the flows table)

For a cross-cutting fiscal outcome, the standard channel-to-frontline financial-flows table does not apply. Instead, please describe [country]'s fiscal dynamics as a self-reinforcing cycle of fiscal indiscipline, in a single narrative of ~200–300 words, identifying the causal loop and the points at which it could be broken:

(i) unrealistic budget assumptions (revenue, growth, inflation) → (ii) budgets that cannot be executed as planned; weak top-down control and ad hoc cash rationing → (iii) in-year overspending and arrears accumulation → (iv) financing gaps closed by expensive domestic (and monetary) borrowing → (v) compounding deficit; debt service + rising wage bill crowd out development spending → (vi) suppressed public investment and weak growth (growth-feedback node) eroding the revenue base and resilience → (vii) inflation and macro-fiscal volatility; absence of buffers leaving the economy exposed when droughts, cyclones, or SOE liabilities strike → forcing abandonment of plans and restarting the cycle.

Weave in the extra-budgetary (SOE) amplifier (unplanned liabilities feeding execution, borrowing, and shocks; cash rationing in turn starving them of legitimate funding) and the exogenous shocks that hit the cycle. Conclude by naming the defined intervention points (credible budgeting; disciplined cash and commitment control; protection of productive investment; pre-arranged disaster-responsive finance). Cite sources as hyperlinked parentheticals.

---

### Prompt ER-1-09 — Section 2.3.2: Fiscal-Cycle Diagram (replaces the financial-flows diagram)

Please prepare an editable diagram using draw.io / diagrams.net depicting the self-reinforcing cycle of fiscal indiscipline in [country]:

- A circular causal loop of the 6–7 core nodes from Prompt ER-1-08, with directional arrows showing the reinforcing direction.
- A growth-feedback node (low public investment → weak growth → eroded revenue base & resilience) closing the loop, colour-coded distinctly (e.g. green).
- An SOE / extra-budgetary amplifier node feeding into the execution and borrowing stages (distinct colour, e.g. orange, with dashed amplifier arrows).
- An exogenous shocks node (droughts, cyclones, terms-of-trade, FX) feeding the volatility/no-buffers stage (grey, dashed).
- A central caption ("Vicious Cycle") and a legend explaining the colour coding.

Provide the diagram as editable draw.io XML and a matplotlib rendering script (*fiscalcycle.py) that writes a 300-dpi PNG.

Record in the caption that this diagram substitutes the standard financial-flows table/diagram (deviation to be recorded for the Compilation audit).

---

### ✏️ Review the output — focus on these points

**Fiscal Cycle Narrative and Diagram (Prompts ER-1-08, ER-1-09).** Review before the PFM systems description.

- [ ] The causal loop is complete and directionally coherent (unrealistic budget → … → restart)
- [ ] Growth-feedback node included and closes the loop
- [ ] SOE/extra-budgetary amplifier and exogenous-shocks nodes are shown feeding the correct stages
- [ ] Defined intervention points are named in the narrative
- [ ] Diagram legend and "substitutes flows table" caption present; deviation recorded for the Compilation audit

Make corrections before proceeding.

---

### Prompt ER-1-10 — Section 2.3.2: PFM Systems for Macro-Fiscal Management (replaces the six-dimension walk)

Please describe [country]'s PFM rules and systems through the lens that matters for a cross-cutting fiscal outcome: their capacity to set a sustainable fiscal course, hold spending to it, manage debt and cash, and contain fiscal risk — rather than the generic six-dimension service-delivery walk. Using PEFA and other diagnostics, cover, each as a short bolded-lead paragraph with the relevant PEFA indicator scores:

(i) The budget as a fiscal-discipline device — medium-term budgeting architecture vs. its bindingness; aggregate expenditure outturn (PI-1) and compositional variance (PI-2); whether the fiscal envelope set at budget time is breached in execution. (ii) Cash and commitment control — treasury single account status, cash forecasting, commitment-ceiling horizon, automated commitment controls (PI-21, PI-25); whether top-down control has been replaced by short-horizon cash rationing that generates arrears. (iii) Arrears as a hidden deficit — whether expenditure arrears are tracked by stock, age, composition (PI-22). (iv) Debt management — recording and MTDS practices and whether they are overwhelmed by the scale of borrowing. (v) Fiscal-risk oversight — EBU/SOE reporting, transfers (PI-7), external audit and legislative scrutiny (PI-30, PI-31) — identify the critical gap. (vi) Digital/systems foundations for fiscal control — IFMIS coverage and integration (with HRMIS, revenue authority), reconciliation limits, and whether the digital backbone can enforce discipline and give a real-time consolidated fiscal position.

State the overall PEFA score and note any deterioration since the previous assessment. Keep to approximately 300–400 words. Cite PEFA and other sources; where a finding comes from an uploaded/backend diagnostic, attribute it (e.g. Country PEFA, 20XX, uploaded).

---

### ✏️ Review the output — focus on these points

**PFM Systems, macro-fiscal lens (Prompt ER-1-10).** Review before proceeding to the feasibility assessment.

- [ ] Framed around the four macro-fiscal capabilities, not the generic six dimensions
- [ ] Correct PEFA indicators cited for each capability (PI-1, PI-2, PI-7, PI-21, PI-22, PI-25, PI-30, PI-31 as relevant)
- [ ] Overall PEFA score and any deterioration since prior assessment stated
- [ ] The critical fiscal-risk-oversight gap is identified
- [ ] Genuine areas of strength (e.g. debt recording, medium-term architecture) acknowledged alongside weaknesses

Make corrections before proceeding.

> **Return to the standard file.** Continue with Prompt 1-11 (Section 2.3.3: Feasibility Assessment) in `manager-01a-section2-3.md`, then `manager-01b-annex1.md` (Prompts 1-12, 1-13 and 1-15; skip 1-14).

---

## Quality check for Step 1 (economic-resilience variant, in addition to 1-Q1, 1-Q3 and 1-Q4)

**ER-1-Q5 — Cross-Cutting Scope Check**

Please review draft Section 2.3 to confirm it treats [fiscal outcome] as a cross-cutting fiscal outcome, not a service-delivery sector. Specifically flag and correct any place where the draft: (i) refers to a service-delivery "facility" or frontline point of delivery as the end of the chain; (ii) uses Central/Local/Facility/Community swim lanes; (iii) presents sector-spending pie/column charts instead of macro-fiscal charts; (iv) analyses revenue policy/mobilization (out of scope) rather than revenue forecasting/reporting; or (v) frames public-sector results as access/quality/coverage rather than fiscal-management performance (balance, expenditure control, debt, fiscal risk). Confirm the three template deviations (swim lanes; fiscal-cycle vs. flows table; macro-fiscal vs. sector charts) are recorded for the Compilation audit (Prompt C-01).

---

## Prompt Sequence Summary (economic-resilience variant)

| Prompt | Output | Source |
|---|---|---|
| 1-01 | Chapter 1: Introduction | standard |
| 1-02 | Section 2.1: Outcomes and Results (fiscal-performance framing) | standard |
| 1-03 | Section 2.2: Key Public Sector Challenges | standard |
| ER-1-04 | Section 2.3.1: Policy Framework (adapted) | this file |
| ER-1-05 | Section 2.3.1: Institutional Architecture (4 fiscal tiers) | this file |
| ER-1-06 | Section 2.3.1: Institutional Diagram (fiscal swim lanes) | this file |
| ER-1-07 | Section 2.3.2: Fiscal Policy Context + macro-fiscal charts | this file |
| ER-1-08 | Section 2.3.2: Self-reinforcing fiscal-cycle narrative | this file |
| ER-1-09 | Section 2.3.2: Fiscal-cycle diagram | this file |
| ER-1-10 | Section 2.3.2: PFM Systems for macro-fiscal management | this file |
| 1-11 | Section 2.3.3: Feasibility Assessment | standard |
| 1-Q1, 1-Q3, 1-Q4, ER-1-Q5 | Quality checks | standard + this file |
| 1-12, 1-13, 1-15 | Annex Tables 1.1, 1.2 and compilation (`manager-01b-annex1.md`); 1-14 replaced by ER-1-08 | standard |
