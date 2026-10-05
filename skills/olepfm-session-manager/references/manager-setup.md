---
title: OLePFM Session Manager — Session Setup
description: Session setup for the OLePFM session manager, run before the Sources stage: verify the pre-loaded documents (Setup 1), establish and lock the session context of country, sector, development outcome and public sector result (Setup 2), and the Sector Outcome Reference for the standard sectors. Return to manager.md for the stage sequence and completion gates.
---

# Session Setup

Complete Setup 1 and Setup 2 below before starting the Sources stage, then return to `manager.md` (the SKILL.md of this skill) for the stage sequence. The AI behaviour rules in `manager.md` apply throughout.

### Pre-loaded Reference Documents

These are held in the **root folder of the knowledge base** (alongside the skills folder, not inside it) and available to the AI by default. **Do not upload them again.** Verify access with the setup verification prompt below before starting.

| Document | Where it is stored |
|---|---|
| OLePFM Sector Reform Design Report Template | Knowledge base — root folder |
| OLePFM Synthesis Handbook (Williamson et al., 2024) | Knowledge base — root folder |
| Sector Outcome Notes and prior diagnostic reports | Backend library — searched by sector |

> **If the AI cannot find them:** the stored file name may differ from the title — have it list the root files and match on keywords, not an exact title.

> **In this repository:** the Report Template is the file `manager-report-template.md` in this skill. Read it whenever a prompt says "using the OLePFM Sector Reform Design Report Template". The Synthesis Handbook and sector notes are not in the repository; ask the user to provide them.

### Documents to Upload Per Session

Upload these at the start of each session:

| Document | Required |
|---|---|
| A sector note you hold | Only if the chosen sector is not covered on the backend |
| Working Tables (for a workshop) | Prepared beforehand with `manager-workshop.md`; not a report input |

### Setup 1: Verify the Pre-loaded Documents

Paste the following to confirm the pre-loaded documents are accessible:

---

Please confirm you can access these pre-loaded documents, both stored in the **root folder of the knowledge base** (alongside the skills folder, not inside it):

1. OLePFM Sector Reform Design Report Template
2. OLePFM Synthesis Handbook (Williamson et al., 2024)

If either does not appear at first, search the root again on title keywords alone — "Sector Reform Design Report Template" and "Synthesis Handbook" — as the stored file name may differ. For each, state whether you can access it, its title, and the file name it is stored under. If either is still missing, list the file names you can see at the root, then stop and alert the user before proceeding.

---

> **Do not proceed to Setup 2 until the AI confirms both documents are accessible.**

### Setup 2: Establish Session Context (two parts)

The AI collects session context in **two short parts — first country and sector, then the development outcome.**

Once setup is verified, paste the following as your **next message**:

---

I am ready to establish the session context for an Outcome-Led PFM Reform Diagnosis and Design Report. Run the two-step setup: ask my **country** and **sector** — a standard sector from the Sector Outcome Reference below, or another — then establish and confirm its **development outcome** and **public sector result**. The Report Template, Synthesis Handbook, and the sector notes and prior reports are pre-loaded on the backend.

Do not proceed to the Sources stage until I have confirmed the country, sector and outcome.

---

**AI behavior for this setup:**

1. **Ask for country and sector first — nothing else.** Present the standard sectors from the Sector Outcome Reference below as the options, and note the user may instead name a **sector not listed there**. **Revenue Mobilization** is a cross-cutting enabler, not a standalone sector — offer it only alongside one of the other five, never on its own. Wait for the user's answer.

2. **Establish the outcome for that sector.** Draft the **development outcome** and **public sector result** from the best available guide, searching in this order:
   1. a **Sector Outcome Note or analytical report** for the sector on the backend — search the knowledge base for this first;
   2. a **previous OLePFM diagnostic report for the same sector** in another country, on the backend;
   3. the **Synthesis Handbook**, if the sector is one it covers — and, for a standard sector, its entry in the Sector Outcome Reference below.

   If none exists — the sector is not in the Synthesis and nothing matches on the backend — ask the user to **upload a sector note if they have one**; if not, **proceed without a guide, following the OLePFM framework as closely as possible**. Then ask the user to confirm the framing, or narrow it to what matters most for their country.

3. **Lock the context.** Once the user confirms, restate it in this form (plain Markdown, no blockquote), then confirm readiness for the Sources stage:

   **Session context confirmed:**

   - **Country:** [country]
   - **Sector:** [sector]
   - **Development outcome:** [outcome]
   - **Public sector result:** [public sector result]

   Referred to as [country], [sector] and the development outcome in all prompts from here on. Ready to begin **Sources: Source Preparation**.

### Sector Outcome Reference

For a listed sector, use its entry below; for a sector not listed, build the outcome as in Setup 2.

**Health — "Ensuring Healthy Lives"**
- **Development outcome:** Healthy lives and well-being for all at all ages, delivered through universal health coverage (UHC).
- **Public sector result:** Progress toward UHC via primary health services — access to quality essential healthcare, plus access to safe, effective, affordable essential medicines and vaccines for all.

**Education — "Achieving Quality Basic Education for All"**
- **Development outcome:** Universal quality basic education providing functional numeracy and literacy for all learners (measured by learning assessments).
- **Public sector result:** Increased access and completion rates, and improved education quality, equitably delivered across genders, locations, and socio-economic groups.

**Economic Resilience — "Building Economic Resilience"**
- **Development outcome:** A resilient economy (growth in output per capita over the business cycle) that sustains growth while reducing vulnerability to shocks.
- **Public sector result:** Building and preserving fiscal space through sound management of the fiscal balance, revenues, expenditure, and debt — enabling counter-cyclical responses to shocks.
- **Prompt variant:** cross-cutting fiscal outcome. In Step 1, Prompts 1-04 to 1-10 are replaced by ER-1-04 to ER-1-10 from `manager-01a-variant-economic-resilience.md` and `manager-01a-variant-economic-resilience-2.md` (see the Step 1 instructions in `manager.md`). The same applies to any other macro-fiscal outcome, such as fiscal or debt sustainability.

**Gender — "Eliminating Gender-Based Violence (GBV)"**
- **Development outcome:** Eliminate all forms of GBV, particularly intimate partner violence (IPV).
- **Public sector result:** Prevention (norms/behavioral change at individual, societal, institutional levels); integrated survivor-centered support services; accountability for perpetrators; and support to organizations addressing GBV.

**Energy — "Accelerating the Transition to Renewable Energy"**
- **Development outcome:** Adequate, accessible, and affordable power supply generated primarily through renewable sources.
- **Public sector result:** Timely, adequate public or private investment to achieve renewable generation, transition, accessibility, and affordability that can be sustained.

**Revenue Mobilization — "Mobilizing Revenue in Support of Policy Objectives"** *(enabler for the others, not a standalone sector)*
- **Development outcome:** Sufficient revenues raised in ways that support the government's broader economic and social policy objectives.
- **Public sector result:** Tax administration that raises adequate resources efficiently and equitably, with the capacity to forecast and manage revenue so budgets are realistic.

---

---

## Prompt numbering

Prompts are numbered by stage and run in order: S-1 to S-4 (Sources), 1-01 to 1-15 (Step 1), 2-01 to 2-10 (Step 2), 3-01 to 3-14 (Step 3), C-01 to C-14 (Compilation) and QA-1 to QA-5 (final cross-document checks). Optional quality checks at the end of a step are numbered 1-Q1, 2-Q1 and so on. Inside each file, prompts are grouped under the OLePFM sub-step they serve (for example Sub-step 1.4, Map the sector policy, institutional and public finance context). A sector variant of a prompt keeps the standard number with a prefix: ER-1-05 is the economic-resilience variant of Prompt 1-05. The prompt files are listed in `manager.md` under each stage; where a stage's file was split for the platform's file-size limit (`manager-01a-chapters1-2.md` and `manager-01a-section2-3.md`; `manager-04b-part2-and-annex.md` and `manager-04b-render-word-template.md`), the manager names both and each file says which prompts it holds.
