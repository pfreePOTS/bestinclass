# PulseOne Project Profitability Audit

**Date:** April 20, 2026  
**Status:** DRAFT — Pending ConnectWise Validation  
**Prepared by:** Manus (PulseOne Strategic Audit Assistant)  

---

## A. Objective
Conduct a deep profitability audit of the PulseOne Consulting/Projects division to identify the structural root causes of the segment’s underperformance. The Master Scorecard reports Project/Consulting Gross Margin at 24.2%, which is roughly half of the Service Leadership Best in Class (BiC) target of 48–52%. This audit decomposes revenue, allocates project-related labor costs, and reclassifies engagements into three distinct service delivery models—Staff Augmentation, True Consulting/Projects, and Managed Services—to determine the exact source of margin leakage.

## B. Evidence Reviewed
This analysis synthesizes data from the following authoritative project files and knowledge base documents:
- `QuickBase Completed Projects jan 1 2025 to date 4 20 2026.xlsx` (Project-level revenue and subcontractor COGS)
- `Invoice totals by company 2025.xlsx` (Total invoiced revenue by client)
- `Expenses Tracking MASTER 2023.xlsx` (2025 tab for contractor budgets and labor allocations)
- `Upwork - Reports - Time by freelancer 2025.csv` and `2026.csv` (Contractor hours, rates, and task alignment)
- `PulseOne_Definitive_PL_Analysis.md` (Authoritative financial baseline)
- `PulseOne_Corrected_Findings_and_Utilization.md` (Prior utilization hypotheses)

## C. Current Understanding
The Definitive P&L establishes that PulseOne generated $1,175,036 in consulting/project revenue in CY 2025 at a 24.2% gross margin. Concurrently, the total service delivery labor cost across the company is approximately 35.6% of revenue, which is 5–10 points higher than the BiC target of 25–30%. 

However, the operational data in QuickBase logs $1,949,344 in completed project revenue for CY 2025 at a blended direct margin of 45.6%. This $774K revenue gap and 21.4-point margin paradox is driven by classification differences between the operational tracker (QuickBase) and the financial system (P&L). To resolve this, this audit reclassifies the QuickBase data into three distinct business models based on the nature of the engagements.

## D. Findings

### 1. The Three-Segment Reclassification
The $1.95M in QuickBase "project" revenue actually consists of three distinct service delivery models that must be evaluated against different BiC benchmarks:

**Segment 1: Staff Augmentation (ARC Research)**
ARC Research represents a managed pool of contractors (David Fredrick, Blue Pisces/Ruben, Basim Mashni, and Matthew Barnett) provided by PulseOne at a negotiated monthly rate. This is staff augmentation, not project delivery. In CY 2025, ARC generated $1,103,649 (56.6% of the QuickBase total) at a 43.3% direct margin. This represents a 76.3% markup on cost, which is exceptionally strong for staff augmentation (where BiC is typically 15–25% markup).

**Segment 2: True Consulting/Projects (Bunzl Parent, AvePoint, etc.)**
Excluding staff augmentation and recurring managed services, true project delivery generated $690,839 (35.4% of the total) across 61 engagements. These discrete projects operated at a 47.1% direct margin (before internal W-2 labor loading). The Bunzl parent company accounted for 79.4% of this true project revenue ($548,639).

**Segment 3: Managed Services (Bunzl Subsidiaries)**
Work performed for Bunzl subsidiaries (Bunzl De Mexico, Cool Pak, Monte Package, Intergro) consists of recurring managed service relationships, not discrete projects. These engagements generated $154,855 (7.9% of the total) at a 55.8% direct margin.

### 2. The True Margin Paradox
The P&L reports a fully-loaded consulting/project margin of 24.2% on $1.175M in revenue. If the $1.1M in highly profitable ARC staff augmentation revenue is included in that P&L consulting line, the remaining $75,000 in true project revenue must be operating at a deeply negative margin to drag the blended average down to 24.2%. 

Conversely, if ARC is classified as Managed Services in the P&L, then the 24.2% margin applies primarily to the $690K in true projects. Because these true projects achieved a 47.1% direct margin in QuickBase using only subcontractor COGS, the 22.9-point drop to 24.2% in the P&L means that massive amounts of unbilled or untracked internal W-2 labor are being consumed by these projects.

### 3. Project-Level Margin Failures
Within the $690K true project portfolio, 98% of projects beat their internal target margins. However, the single failure had a disproportionate impact due to its size. The Bunzl AD Migration project was priced at $252,400 but incurred $173,923 in direct COGS, yielding a 31.1% margin against a 35.6% target. This single 4.5-point miss represented an $11,333 profit shortfall.

Conversely, small projects (under $5K) are highly efficient. The 42 projects in this tier generated $91,050 in revenue at an 82.8% direct margin, demonstrating that the pricing and delivery model works well for discrete, transactional scopes.

### 4. Contractor Efficiency and Cost Allocation
PulseOne relies heavily on external contractors. The CY 2025 Expenses Tracker budgets $560,236 annually for the four core COGS contractors dedicated to the ARC staff augmentation pool. QuickBase recorded $625,919 in ARC COGS, which aligns closely with the budget plus Matthew Barnett's $74K net cost.

However, the Upwork analysis identified Vincent Williams billing $104,740 (1,706 hours at $61/hr) for IT/Network escalations and ITMS projects. His cost is not explicitly tracked in QuickBase COGS. If his escalation hours are not being billed to clients at $150+/hr, or if they are being absorbed into flat-rate agreements, he represents a significant, untracked margin leak.

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
- **Hidden W-2 Labor Costs:** True projects are achieving 47.1% direct margin using only subcontractor COGS. The drop to 24.2% fully-loaded margin means internal W-2 staff are likely performing unbilled or underpriced project work.
- **P&L Classification Dependency:** If ARC staff augmentation revenue is masking deep losses in true project delivery on the P&L, the structural health of the consulting division is much worse than the 24.2% blended margin suggests.
- **Escalation Dependency:** Vincent Williams costs $104K/year at $61/hr. If his escalation hours are not being billed to clients at sufficient rates, he represents a major margin leak outside the QuickBase tracking system.

**Opportunities:**
- **Small Project Expansion:** True projects under $5K operate at 83% direct margin. Standardizing and increasing the volume of these transactional projects could rapidly lift the segment average.
- **Target Margin Recalibration:** QuickBase data proves PulseOne consistently hits its internal margin targets (98% success rate). However, the targets are set at 35–39%. Simply raising the internal pricing target to the BiC standard of 50% would likely result in execution at that higher level.

## G. Recommended Actions

1. **Reconcile the Revenue Classification:** Finance must definitively map the $1.1M ARC staff augmentation revenue to the P&L to determine if it is inflating the Consulting margin or the Managed Services margin.
2. **Audit Vincent Williams' Billing:** Trace the 1,706 hours billed by Vincent Williams in CY 2025 to specific client invoices to ensure his $61/hr cost is generating at least $125/hr in revenue.
3. **Review the Bunzl AD Migration:** Conduct a post-mortem on the $252K AD Migration to identify why COGS overran the target by $11K. Was it scope creep, underpricing, or inefficient labor?
4. **Recalibrate Project Pricing Targets:** Update the quoting and estimation tools to require a minimum 50% target gross margin on all true project work, abandoning the current 35–39% baseline.

## H. Suggested ConnectWise Follow-Up

To definitively resolve the margin paradox and the P&L classification ambiguity, the following specific data pulls are required from the ConnectWise AI interface:

1. **Agreement vs. Project Revenue Classification** (Updates CW-05)
   *Request:* "For CY 2025, please provide the total revenue billed under Managed Services Agreements versus the total revenue billed under discrete Projects. Specifically, how is the ARC Research monthly revenue classified in ConnectWise?"
   *Why:* Determines whether ARC staff augmentation is masking losses in true projects or inflating the Managed Services margin.

2. **Vincent Williams Time Entries** (Updates CW-03)
   *Request:* "For CY 2025, how many of Vincent Williams' hours were billed to clients as T&M project work versus how many were applied to fixed-fee Managed Services agreements?"
   *Why:* Determines if the highest-cost Upwork contractor is a profit center or a margin leak.

3. **Technician Utilization by Person**
   *Request:* "Pull a technician utilization report for CY 2025. What is the billable utilization percentage for each internal W-2 technician in the Services/Projects department?"
   *Why:* Identifies if internal staff are sitting idle or performing unbilled project work, which would explain the massive drop from 47.1% direct margin to 24.2% fully-loaded margin.

## I. Clarifying Questions

1. Is the ARC staff augmentation revenue ($1.1M) currently mapped to the "Consulting Services" revenue line on the P&L, or is it mapped to Managed Services?
2. When internal W-2 engineers (e.g., Eric Anzalone, Laura Walsh) work on a true project, is their labor cost added to the QuickBase COGS column, or does QuickBase only track external subcontractor invoices?
