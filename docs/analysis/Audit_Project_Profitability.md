# PulseOne Project Profitability Audit

**Date:** April 20, 2026  
**Status:** DRAFT — Pending ConnectWise Validation  
**Prepared by:** Manus (PulseOne Strategic Audit Assistant)  

---

## A. Objective
Conduct a deep profitability audit of the PulseOne Consulting/Projects division to identify the structural root causes of the segment’s underperformance. The Master Scorecard reports Project/Consulting Gross Margin at 24.2%, which is roughly half of the Service Leadership Best in Class (BiC) target of 48–52%. This audit decomposes revenue, allocates project-related labor costs, analyzes contractor efficiency, and defines the exact ConnectWise data required to resolve the margin gap.

## B. Evidence Reviewed
This analysis synthesizes data from the following authoritative project files and knowledge base documents:
- `QuickBase Completed Projects jan 1 2025 to date 4 20 2026.xlsx` (Project-level revenue and subcontractor COGS)
- `Invoice totals by company 2025.xlsx` (Total invoiced revenue by client)
- `Expenses Tracking MASTER 2023.xlsx` (2025 tab for contractor budgets and labor allocations)
- `Upwork - Reports - Time by freelancer 2025.csv` and `2026.csv` (Contractor hours, rates, and task alignment)
- `PulseOne_Definitive_PL_Analysis.md` (Authoritative financial baseline)
- `PulseOne_Corrected_Findings_and_Utilization.md` (Prior utilization hypotheses)

## C. Current Understanding
The Definitive P&L establishes that PulseOne generated $1,175,036 in consulting/project revenue in CY 2025 at a 24.2% gross margin. Concurrently, the total service delivery labor cost across the company is approximately 35.6% of revenue, which is 5–10 points higher than the BiC target of 25–30%. Because prior audits confirmed the Help Desk (Managed Services) operates efficiently at a 5.41x Service Multiple, the prevailing hypothesis is that the excess labor cost and margin leakage are concentrated in the Consulting/Projects division.

However, the operational data in QuickBase presents a conflicting picture. The QuickBase project tracker logs $1,949,344 in completed project revenue for CY 2025 at a blended gross margin of 45.6%. Reconciling this $774K revenue gap and 21.4-point margin paradox is the central focus of this audit.

## D. Findings

### 1. The Revenue Scope Mismatch ($774K Gap)
The $774K difference between QuickBase project revenue ($1.95M) and P&L consulting revenue ($1.175M) is primarily driven by how recurring monthly engagements are classified. 

QuickBase tracks several large, recurring monthly engagements as "projects," whereas the P&L likely classifies them as Managed Services agreements. Specifically, ARC Research’s "Comprehensive Technical Services Package" is billed monthly ($68K–$95K/month) and generated $1,103,649 in CY 2025. Similarly, Bunzl’s "PM Path to the Cloud" and "Elsabon HR Deployment" are recurring monthly engagements that generated nearly $300K. If these recurring engagements are removed from the QuickBase total, the remaining discrete project revenue aligns much more closely with the P&L’s $1.175M figure.

### 2. The Cost Scope Mismatch (The Margin Paradox)
The 45.6% gross margin reported in QuickBase is an incomplete metric. QuickBase COGS ($1,059,830 for CY 2025) captures only the direct subcontractor costs specifically tagged to those projects. It does not include:
- Internal W-2 service delivery labor allocated to projects.
- Upwork contractors whose time is not explicitly tracked as project COGS in QuickBase.
- Burden and overhead allocations.

The P&L’s 24.2% margin is fully loaded. Therefore, projects appear highly profitable at the subcontractor level in QuickBase (45.6%) but become unprofitable when fully loaded with internal W-2 labor and untracked contractor costs in the P&L (24.2%).

### 3. Extreme Client Concentration
Project revenue is heavily concentrated in two client families, creating significant margin dependency:
- **ARC Research:** Accounted for $1,101,174 (56.5%) of QuickBase project revenue across 18 engagements at a 43.2% direct margin.
- **Bunzl Family:** Accounted for $548,639 (28.1%) of QuickBase project revenue across 13 engagements at a 38.1% direct margin.
- **Combined:** The top two clients represent 84.6% of all project activity. The remaining 57 projects generated just $182,418 but operated at an average direct margin exceeding 80%.

### 4. Contractor Efficiency and Cost Allocation
PulseOne relies heavily on external contractors for project delivery. The CY 2025 Expenses Tracker budgets $560,236 annually for four specific COGS contractors dedicated primarily to ARC Research (David Fredrick, Blue Pisces/Ruben, Basim Mashni, and Jeremy Roe). 

Additionally, the Upwork analysis identified $236,708 in project-attributable Upwork spend in CY 2025:
- **Vincent Williams ($104,740):** Billed 1,706 hours at $61/hr. His work is explicitly tagged to IT/Network escalations, ITMS projects, and named client projects (Cend, Copper Hills, Encore). He is a high-cost escalation resource, not Help Desk.
- **Matthew Barnett ($83,390):** Billed via fixed-price contracts, primarily dedicated to ARC.
- **Charlesdoone Castro ($38,228):** Dedicated to the Amiri Help Desk, which is a single-client dependency risk.

If these contractor costs are not fully captured in QuickBase or are being absorbed by fixed-fee agreements without adequate pricing, they are the primary driver of the margin gap.

### 5. Project-Level Margin Failures
While 94% of projects in QuickBase beat their target margins, the few that missed had a disproportionate impact due to their size. The most significant failure was the Bunzl AD Migration project. Priced at $252,400, it incurred $173,923 in direct COGS, yielding a 31.1% margin against a 35.6% target. This single 4.5-point miss represented an $11,332 profit shortfall.

Conversely, small projects (under $5K) are highly efficient. The 48 projects in this tier generated $100,442 in revenue at an 84.2% direct margin, demonstrating that the pricing and delivery model works well for discrete, transactional scopes.

## E. Service Leadership Best in Class Alignment

| Metric | PulseOne Actual | BiC Target | Alignment Status |
|---|---|---|---|
| **Consulting/Project Gross Margin** | 24.2% (Fully Loaded) | 48–52% | **Severely Below Benchmark** |
| **Total Service Delivery Labor** | ~35.6% of Revenue | 25–30% | **Below Benchmark** (Costs too high) |
| **Client Concentration (Projects)** | 84.6% in Top 2 Clients | <20% in Top Client | **High Risk** |
| **Project Pricing Discipline** | Variable (31% to 100%) | Consistent >50% | **Inconsistent** |

*Note: Benchmark alignment remains provisional pending ConnectWise validation of billable utilization and agreement profitability.*

## F. Risks and Opportunities

**Risks:**
- **Hidden W-2 Labor Costs:** If QuickBase projects are achieving 45.6% margin using only subcontractor COGS, internal W-2 staff are likely performing unbilled or underpriced project work, dragging the fully-loaded P&L margin down to 24.2%.
- **Fixed-Fee Agreement Bleed:** If the massive ARC and Bunzl monthly engagements are actually managed services agreements, the high dedicated contractor costs (Barnett, Fredrick, Blue Pisces) may be outstripping the fixed monthly revenue.
- **Escalation Dependency:** Vincent Williams costs $104K/year at $61/hr. If his escalation hours are not being billed to clients at $150+/hr, or if they are being absorbed into flat-rate agreements, he represents a significant margin leak.

**Opportunities:**
- **Small Project Expansion:** Projects under $5K operate at 84% direct margin. Standardizing and increasing the volume of these transactional projects could rapidly lift the segment average.
- **Rate Normalization:** The QuickBase data proves PulseOne can track subcontractor COGS accurately. Enforcing a strict 50% markup on all subcontractor labor (e.g., billing Blue Pisces' $125/hr rate at $250/hr) would mathematically guarantee BiC margins on the direct cost portion.

## G. Recommended Actions

1. **Reconcile the Revenue Classification:** Finance must definitively map the $1.95M in QuickBase projects to the P&L to determine which engagements are Consulting (discrete) versus Managed Services (recurring).
2. **Audit Vincent Williams' Billing:** Trace the 1,706 hours billed by Vincent Williams in CY 2025 to specific client invoices to ensure his $61/hr cost is generating at least $125/hr in revenue.
3. **Review the Bunzl AD Migration:** Conduct a post-mortem on the $252K AD Migration to identify why COGS overran the target by $11K. Was it scope creep, underpricing, or inefficient labor?
4. **Evaluate Amiri Profitability:** Charlesdoone Castro costs $38K/year dedicated to Amiri. Confirm the Amiri agreement price adequately covers this dedicated cost plus overhead.

## H. Suggested ConnectWise Follow-Up

To definitively resolve the 24.2% vs 45.6% margin paradox, the following specific data pulls are required from the ConnectWise AI interface:

1. **Agreement vs. Project Revenue Classification**
   *Request:* "For CY 2025, please provide the total revenue billed under Managed Services Agreements versus the total revenue billed under discrete Projects. Specifically, how are the ARC Research 'Comprehensive Technical Services' and Bunzl 'PM Path to the Cloud' engagements classified in ConnectWise?"
   *Why:* Resolves the $774K revenue gap between QuickBase and the P&L.

2. **Project Profitability by Subcontractor** (Updates CW-02)
   *Request:* "Run a project profitability report for CY 2025. For projects involving Basim Mashni, David Fredrick, or Blue Pisces, what was the total billed revenue versus the total labor cost applied?"
   *Why:* Determines if the $560K ARC contractor budget is generating adequate margin.

3. **Vincent Williams Time Entries** (Updates CW-03)
   *Request:* "For CY 2025, how many of Vincent Williams' hours were billed to clients as T&M project work versus how many were applied to fixed-fee Managed Services agreements?"
   *Why:* Determines if the highest-cost Upwork contractor is a profit center or a margin leak.

4. **Technician Utilization by Person** (Updates CW-05)
   *Request:* "Pull a technician utilization report for CY 2025. What is the billable utilization percentage for each internal W-2 technician in the Services/Projects department?"
   *Why:* Identifies if internal staff are sitting idle or performing unbilled project work, which would explain the fully-loaded margin drop.

## I. Clarifying Questions

1. Are the Upwork costs for Matthew Barnett ($83K) and Vincent Williams ($104K) included in the $1.05M QuickBase COGS figure, or are those costs tracked separately?
2. When internal W-2 engineers (e.g., Eric Anzalone, Laura Walsh) work on a QuickBase project, is their labor cost added to the QuickBase COGS column, or does QuickBase only track external subcontractor invoices?
