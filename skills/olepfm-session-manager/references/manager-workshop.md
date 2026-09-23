---
title: OLePFM Workshop Table Preparation
description: Produces the Working Tables document a reform design workshop starts from. Establishes context and sources, then pre-populates the framing tables through 2.1 — Outcomes/Results/Challenges (1.1), Organizational Functions (1.2), Main Financing Channels (1.3), Roles of Public Finance (2.1) — using the standard generation prompts, and lays out 2.2 through 3.5 as blank exercise tables with facilitation notes for the workshop to complete. Use when preparing tables for an upcoming workshop; it reuses the phase skills' generation prompts and changes nothing in them. Trigger by saying "start OLePFM workshop preparation".
---

# OLePFM Workshop Table Preparation

Use this to produce the **Working Tables** document a reform design workshop starts from. The AI pre-populates the framing tables **through 2.1** from desk research; **2.2 onward are left blank** — those are the workshop's own exercises. It reuses the generation prompts in the phase skills (`01a`, `01b`, `02`) and changes nothing in them. In this repository, `manager.md` is the SKILL.md of the olepfm-session-manager skill, and the phase skills are the other files in this `references/` folder.

The workshop reviews 1.1–2.1 and fills in 2.2 onward; the completed tables then inform the report drafted with the standard workflow (`manager.md`).

## Opening prompt

To start, say **start OLePFM workshop preparation** — no need to name the country or sector; the AI will ask. That is equivalent to pasting:

---

I want to prepare the OLePFM Working Tables for an upcoming reform design workshop. Guide me through it: first ask me for the country and sector, then pre-populate the framing tables through 2.1 and leave 2.2 onward as blank exercises for the workshop.

---

## Steps

1. **Set up.** Establish country, sector and development outcome as in `manager.md` Step 2 (including the off-list sourcing order), then run source preparation (`00-source-prep.md`, S1–S4). Cite sources as hyperlinked parentheticals.

2. **Populate 1.1–2.1.** Generate each table with the existing prompt, then lay it out in the Working Tables format with a short **facilitation note** for the workshop:

   | Table | Columns | Generate with | Facilitation note |
   |---|---|---|---|
   | **1.1 Outcomes, Public Sector Results and Challenges** | stacked blocks — Development Outcome · Public Sector Results · Selected Public Sector Challenges | `01a` B1 (2.1) + B2 (2.2) | *Pre-populated by AI. Review; agree no more than three challenges — a challenge must not mention money.* |
   | **1.2 Organizational Functions in Policy, Delivery and PFM** | Organization · Level of Government · Policy & Delivery Functions · PFM Functions | `01b` C2 (with `01a` B3b) | *Pre-populated by AI. Validate; add any missing organizations.* |
   | **1.3 Main Financing Channels** | Financing Channel · Description & Purpose · Organizations (flow of funds) · Relative Value · Key Problems | `01a` B4b | *Pre-populated by AI. Review the channels, values and problems.* |
   | **2.1 Roles of Public Finance** | Role · Potential Role · Actual Role | `02` B2 (the four roles) | *Pre-populated by AI. Read before identifying challenges; validate the potential and actual roles.* |

   Pause here for the user to review the populated 1.1–2.1 before the blank scaffold is added.

3. **Scaffold 2.2 onward (blank).** Add the remaining sections as **empty tables — column headers and a workshop-exercise note only, no AI content:**

   | Table | Columns | Workshop exercise note |
   |---|---|---|
   | **2.2 Public Sector Challenges and Bottlenecks** | Public Sector Challenge · Bottleneck · Type · Impact · Feasibility | *For each challenge, identify the bottlenecks that cause it (five-why).* |
   | **2.3 Priority PFM Bottlenecks** | Bottleneck · Impact on delivery (challenges affected) · Feasibility (rating + description) | *Consolidate and prioritize the bottlenecks.* |
   | **3.1 Causal Analysis of Bottlenecks and Proposed Reforms** | Sub-Bottleneck · Underlying Causes · Stakeholders · Reform Result · Reforms Required | *For each priority bottleneck, analyse causes and propose reforms.* |
   | **3.2 Key Stakeholders in Reform** | Type · Members · Role | *Map authorizers, team leaders, results team, coalition.* |
   | **3.3 Stakeholder Management Strategy** | Stakeholder · Commitment · Power to block · Source of interest · Motivation Strategy | *Plan how to move each key stakeholder.* |
   | **3.4 Technical, Systems and Capacity Support** | Name · Description of changes required · Lead Organization · Relevant Change Objectives | *List the systems, capacity and TA each reform needs.* |
   | **3.5 Key Steps to Achieve Results** | Reform Result · Key Steps · Timing · Responsible | *Three key steps per reform result, sequenced with timing.* |

4. **Assemble and hand off.** Output one Working Tables document — **Step 1** (1.1, 1.2, 1.3), **Step 2** (2.1 populated; 2.2, 2.3 blank), **Step 3** (3.1–3.5 blank) — following the OLePFM Working Tables layout. This is the file the workshop fills in and returns.

## Notes

- **Populate only through 2.1.** 2.2 is the workshop's first live exercise, so the AI stops there; do not pre-fill 2.2 onward.
- **Keep challenges free of money/PFM.** The challenges in 1.1 must be stated as delivery failures only — no mention of money, public finance or PFM.
- **Draft to refine.** The populated tables are a starting point for the workshop to review and change, not a final answer.