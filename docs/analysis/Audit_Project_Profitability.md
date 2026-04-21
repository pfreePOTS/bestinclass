# PulseOne Project Profitability Audit

**Date:** April 20, 2026  
**Status:** DRAFT — Pending ConnectWise Validation  
**Prepared by:** Manus (PulseOne Strategic Audit Assistant)  

---

## A. Objective
Conduct a deep profitability audit of the PulseOne Consulting/Projects division to identify the structural root causes of the segment’s underperformance. The Master Scorecard reports Project/Consulting Gross Margin at 24.2%, which is roughly half of the Service Leadership Best in Class (BiC) target of 48–52%. This audit decomposes revenue, isolates discrete project delivery from staff augmentation, and quantifies the impact of untracked internal W-2 labor on the true cost of project delivery.

## B. Evidence Reviewed
This analysis synthesizes data from the following authoritative project files and knowledge base documents:
- `QuickBase Completed Projects jan 1 2025 to date 4 20 2026.xlsx` (Project-level revenue and subcontractor COGS)
- `Invoice totals by company 2025.xlsx` (Total invoiced revenue by client)
- `Expenses Tracking MASTER 2023.xlsx` (2025 tab for contractor budgets and labor allocations)
- `Upwork - Reports - Time by freelancer 2025.csv` and `2026.csv` (Contractor hours, rates, and task alignment)
- `PulseOne_Definitive_PL_Analysis.md` (Authoritative financial baseline)
- `PulseOne_Corrected_Findings_and_Utilization.md` (Prior utilization hypotheses)

## C. Current Understanding
The Definitive P&L establishes that PulseOne generated $1,175,036 in consulting/project revenue in CY 2025 at a fully-loaded 24.2% gross margin. Concurrently, the total service delivery labor cost across the company is approximately 35.6% of revenue, which is 5–10 points higher than the BiC target of 25–30%. 

However, the operational data in QuickBase logs $1,949,344 in completed project revenue for CY 2025 at a blended direct margin of 45.6%. This massive gap between the operational tracking tool (QuickBase) and the financial reality (P&L) is driven by two structural issues: (1) the inclusion of staff augmentation and managed services revenue in the QuickBase project tracker, and (2) the "invisible subsidy" of untracked internal W-2 labor consumed by projects.

## D. Findings

### 1. The Primary Root Cause: The "Invisible Subsidy" of W-2 Labor
The central finding of this audit is that QuickBase project margins are artificially inflated because they only capture external subcontractor invoices as COGS. When PulseOne deploys internal W-2 staff (e.g., Hagen McDonell, James Froio, Joel Alvarez, Eric Anzalone) to execute project work, their labor cost is not recorded against the project in QuickBase.

This creates an "invisible subsidy":
- **Project margins look artificially high (47.1% in QB)** because they receive "free" labor from the internal W-2 pool.
- **Help Desk/Managed Services margins look artificially low** because that division absorbs the payroll cost for work actually performed for projects.
- **The P&L catches everything**, which is why the fully-loaded project margin drops all the way down to **24.2%**.

The 24.2% is the *real* project margin. The 47.1% in QuickBase is a cash margin that only measures the markup on external subcontractors.

**Quantifying the Hidden Cost:**
There is a pool of approximately $375,000 in W-2 service delivery payroll capable of being deployed to projects. If these internal resources spend just 33% of their time on project delivery, that represents ~$124,000 in hidden project COGS. Adding $124K in hidden labor to the true project base ($691K revenue) drops the direct margin from 47.1% down to 29.1% — very close to the P&L's fully-loaded 24.2%.

### 2. The Three-Segment Reclassification
The $1.95M in QuickBase "project" revenue actually consists of three distinct service delivery models that must be evaluated against different BiC benchmarks:

**Segment 1: Staff Augmentation (ARC Research)**
ARC Research represents a managed pool of contractors provided by PulseOne at a negotiated monthly rate. This is staff augmentation, not project delivery. In CY 2025, ARC generated $1,103,649 (56.6% of the QuickBase total) at a 43.3% direct margin. This represents a 76.3% markup on cost, which is exceptionally strong for staff augmentation (where BiC is typically 15–25% markup).

**Segment 2: True Consulting/Projects (Bunzl Parent, AvePoint, etc.)**
Excluding staff augmentation and recurring managed services, true project delivery generated $690,839 (35.4% of the total) across 61 engagements. These discrete projects operated at a 47.1% direct margin (before internal W-2 labor loading). The Bunzl parent company accounted for 79.4% of this true project revenue ($548,639).

**Segment 3: Managed Services (Bunzl Subsidiaries)**
Work performed for Bunzl subsidiaries (Bunzl De Mexico, Cool Pak, Monte Package, Intergro) consists of recurring managed service relationships, not discrete projects. These engagements generated $154,855 (7.9% of the total) at a 55.8% direct margin.

### 3. Project-Level Margin Failures
Within the $690K true project portfolio, 98% of projects beat their internal target margins. However, the internal targets themselves are set at 35–39%, which is structurally below the BiC target of 48–52%. PulseOne is consistently hitting its goals, but the goals are set too low to achieve Best in Class profitability.

The single failure against internal targets had a disproportionate impact due to its size. The Bunzl AD Migration project was priced at $252,400 but incurred $173,923 in direct subcontractor COGS, yielding a 31.1% direct margin against a 35.6% target. This single 4.5-point miss represented an $11,333 profit shortfall, *before* any internal W-2 labor was applied.

Conversely, small projects (under $5K) are highly efficient. The 42 projects in this tier generated $91,050 in revenue at an 82.8% direct margin, demonstrating that the pricing and delivery model works well for discrete, transactional scopes.

### 4. Contractor Efficiency and Escalation Dependency
PulseOne relies heavily on external contractors. The CY 2025 Expenses Tracker budgets $560,236 annually for the four core COGS contractors dedicated to the ARC staff augmentation pool. QuickBase recorded $625,919 in ARC COGS, which aligns closely with the budget plus Matthew Barnett's $74K net cost.

However, the Upwork analysis identified Vincent Williams billing $104,740 (1,706 hours at $61/hr) for IT/Network escalations and ITMS projects. His cost is not explicitly tracked in QuickBase COGS. If his escalation hours are not being billed to clients at $150+/hr, or if they are being absorbed into flat-rate agreements, he represents a significant, untracked margin leak outside the QuickBase system.

## E. Service Leadership Best in Class Alignment

| Metric | PulseOne Actual | BiC Target | Alignment Status |
|---|---|---|---|
| **Staff Augmentation Markup** | 76.3% (ARC) | 15–25% | **Exceeds Benchmark** |
| **Consulting/Project Gross Margin** | 24.2% (Fully Loaded) | 48–52% | **Severely Below Benchmark** |
| **Total Service Delivery Labor** | ~35.6% of Revenue | 25–30% | **Below Benchmark** (Costs too high) |
| **Client Concentration (Projects)** | 79.4% in Single Client (Bunzl) | <20% in Top Client | **High Risk** |
| **Project Pricing Discipline** | Internal Targets 35–39% | Consistent >50% | **Below Benchmark** |

*Note: Benchmark alignment remains provisional pending ConnectWise validation of billable utilization and P&L revenue classification.*

## F. Risks and Opportunities

**Risks:**
- **The Invisible Subsidy:** The use of internal W-2 staff on projects without tracking their cost in QuickBase means project pricing is structurally flawed. If project quotes are built expecting a 35% margin based *only* on subcontractor costs, the fully-loaded margin will always be severely below BiC when W-2 labor is applied.
- **P&L Classification Dependency:** If the highly profitable ARC staff augmentation revenue ($1.1M) is mapped to the Consulting line on the P&L, it is masking deep losses in true project delivery. If ARC is removed, the remaining true projects may be operating at a negative fully-loaded margin.
- **Escalation Dependency:** Vincent Williams costs $104K/year at $61/hr. If his escalation hours are not being billed to clients at sufficient rates, he represents a major margin leak.

**Opportunities:**
- **Target Margin Recalibration:** QuickBase data proves PulseOne consistently hits its internal margin targets (98% success rate). Simply raising the internal pricing target to the BiC standard of 50% (and accounting for W-2 labor in the quote) would likely result in execution at that higher level.
- **Small Project Expansion:** True projects under $5K operate at 83% direct margin. Standardizing and increasing the volume of these transactional projects could rapidly lift the segment average.

## G. Recommended Actions

1. **Implement Fully-Loaded Project Costing:** QuickBase (or ConnectWise) must be updated to track internal W-2 labor hours applied to projects. Every hour a W-2 employee works on a project must carry a burdened hourly cost rate to calculate true project margin.
2. **Recalibrate Project Pricing Targets:** Update the quoting and estimation tools to require a minimum 50% target gross margin on all true project work, abandoning the current 35–39% baseline. Quotes must include the estimated cost of internal W-2 labor.
3. **Reconcile the Revenue Classification:** Finance must definitively map the $1.1M ARC staff augmentation revenue to the P&L to determine if it is inflating the Consulting margin or the Managed Services margin.
4. **Audit Vincent Williams' Billing:** Trace the 1,706 hours billed by Vincent Williams in CY 2025 to specific client invoices to ensure his $61/hr cost is generating at least $125/hr in revenue.

## H. Suggested ConnectWise Follow-Up

To definitively resolve the "invisible subsidy" and prove exactly how much W-2 labor is consumed by projects, the following specific data pulls are required from the ConnectWise AI interface:

1. **Technician Time Entries by Board Type** (Updates CW-05)
   *Request:* "For CY 2025, pull time entries for all internal W-2 technicians (e.g., Hagen McDonell, James Froio, Joel Alvarez, Eric Anzalone, Kaitlin Harris). Break down their total logged hours by board type: Help Desk/ITMS (agreements) versus Projects versus Internal/Admin. Include the burdened hourly cost for each technician."
   *Why:* This will precisely quantify the "invisible subsidy" — the exact dollar amount of W-2 labor that projects consumed but did not pay for.

2. **Agreement vs. Project Revenue Classification**
   *Request:* "For CY 2025, please provide the total revenue billed under Managed Services Agreements versus the total revenue billed under discrete Projects. Specifically, how is the ARC Research monthly revenue classified in ConnectWise?"
   *Why:* Determines whether ARC staff augmentation is masking losses in true projects or inflating the Managed Services margin.

3. **Vincent Williams Time Entries** (Updates CW-03)
   *Request:* "For CY 2025, how many of Vincent Williams' hours were billed to clients as T&M project work versus how many were applied to fixed-fee Managed Services agreements?"
   *Why:* Determines if the highest-cost Upwork contractor is a profit center or a margin leak.

## I. Clarifying Questions

1. Is the ARC staff augmentation revenue ($1.1M) currently mapped to the "Consulting Services" revenue line on the P&L, or is it mapped to Managed Services?
2. When quoting a new project for a client, does the sales team currently include the estimated cost of internal W-2 labor in the margin calculation, or do they only calculate margin based on external subcontractor costs?
