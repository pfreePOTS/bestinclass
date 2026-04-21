# PulseOne Project Profitability Audit — Step-by-Step Derivation

**Date:** April 20, 2026  
**Status:** DRAFT — Pending ConnectWise Validation  
**Prepared by:** Manus (PulseOne Strategic Audit Assistant)  

---

## A. Objective
This audit rebuilds the PulseOne Consulting/Projects margin from the ground up, relying only on confirmed data sources rather than blended P&L allocations. The objective is to cleanly separate staff augmentation from discrete project delivery, quantify the cash margin of true projects, and define exactly what data is needed to calculate the fully-loaded gross margin against Service Leadership Best in Class (BiC) standards.

## B. Evidence Reviewed
This analysis relies exclusively on the following authoritative sources:
- `QuickBase Completed Projects jan 1 2025 to date 4 20 2026.xlsx` (Project-level revenue and out-of-pocket subcontractor COGS)
- `Expenses Tracking MASTER 2023.xlsx` (2025 tab for contractor budgets and W-2 classifications)
- `Upwork - Reports - Time by freelancer 2025.csv` (Contractor hours and task alignment)
- `PulseOne_Definitive_PL_Analysis.md` (Total W-2 service delivery labor pool)

*Note: Previous versions of this audit cited a 24.2% consulting margin on $1,175,036 in revenue. That margin was an artifact of P&L allocation logic, not a direct measurement of project performance. This version discards that allocation and measures direct performance.*

## C. Current Understanding: The QuickBase Baseline
In CY 2025, the QuickBase project tracker recorded 97 completed engagements totaling **$1,949,344** in revenue and **$1,059,830** in Cost of Goods Sold (COGS). 

**Critical Constraint:** The COGS tracked in QuickBase represents *only* out-of-pocket subcontractor invoices. It does not include any internal W-2 labor, payroll taxes, or Upwork contractors unless specifically invoiced to a project. Therefore, the margins calculated from QuickBase are **cash margins**, not fully-loaded gross margins. 

## D. Step-by-Step Findings

### Step 1: Cleanly Separating ARC Staff Augmentation
The ARC Research relationship is a managed pool of contractors billed at a negotiated monthly rate. This is staff augmentation, not discrete project delivery, and must be evaluated separately.

**What we know about ARC (CY 2025):**
- **Revenue:** $1,103,649 (56.6% of all QuickBase project revenue)
- **QuickBase COGS:** $625,919 (subcontractor invoices for David Fredrick, Blue Pisces, Basim Mashni, etc.)
- **Cash Margin:** $477,730 (43.3%)
- **Markup on Cost:** 76.3%

**Insight:** ARC is highly profitable as a staff augmentation play. A 76.3% markup on external contractors significantly exceeds the typical 15–25% markup seen in BiC staffing models. Assuming no internal W-2 labor was required to manage this pool, the 43.3% cash margin is effectively the true gross margin for this segment.

### Step 2: Isolating True Project Delivery
After removing ARC staff augmentation ($1.1M) and Bunzl subsidiary managed services ($155K) from the QuickBase data, we are left with the true discrete project delivery segment.

**What we know about True Projects (CY 2025):**
- **Project Count:** 61 discrete engagements
- **Revenue:** $690,839
- **QuickBase COGS:** $365,526 (out-of-pocket subcontractor invoices only)
- **Cash Margin:** $325,313 (47.1%)

**Insight:** On a cash basis, true projects are operating near the BiC target of 48–52%. For every $1.00 of project revenue billed, PulseOne pays $0.53 in external subcontractor invoices and keeps $0.47. The Bunzl parent company accounted for 79.4% of this true project revenue ($548,639).

### Step 3: The "Invisible Subsidy" of W-2 Labor
The 47.1% cash margin on true projects is the absolute ceiling. The true, fully-loaded gross margin is lower. How much lower depends entirely on how much internal W-2 labor was consumed by these projects.

PulseOne employs a pool of service delivery W-2 staff (e.g., Hagen McDonell, James Froio, Joel Alvarez, Eric Anzalone, Kaitlin Harris) totaling approximately **$708,879** in burdened payroll. When these employees work on a project, their cost is absorbed by the general payroll (or Help Desk margin) and is never charged to the project in QuickBase.

This creates an "invisible subsidy" where projects borrow labor from the Help Desk to appear profitable. 

**Sensitivity Analysis on True Projects ($690K Revenue):**
- If $0 of W-2 labor went to projects → True Margin = **47.1%**
- If $50K of W-2 labor went to projects → True Margin = **39.9%**
- If $100K of W-2 labor went to projects → True Margin = **32.6%**
- If $150K of W-2 labor went to projects → True Margin = **25.4%**
- If $200K of W-2 labor went to projects → True Margin = **18.1%**

Without knowing exactly how much W-2 time was spent on projects, it is impossible to calculate the true project margin.

### Step 4: The Upwork Escalation Leak
In addition to W-2 labor, Vincent Williams billed $104,740 (1,706 hours at $61/hr) on Upwork for IT/Network escalations and ITMS projects. His cost is not explicitly tracked in QuickBase COGS. If his hours were applied to true projects rather than flat-rate agreements, his cost represents another hidden margin leak that would further depress the true project margin.

## E. Risks and Opportunities

**Risks:**
- **False Margin Signals:** Because QuickBase only tracks subcontractor invoices, the company believes it is operating at a 47% project margin. If W-2 labor and Upwork escalations are heavily utilized, the true margin could be below 25%, meaning projects are destroying value.
- **Client Concentration:** 79.4% of true project revenue comes from a single client (Bunzl).
- **Pricing Targets:** QuickBase data shows projects are consistently hitting their internal margin targets. However, the internal targets are set at 35–39% (cash basis), which guarantees a fully-loaded margin well below the BiC 50% standard once W-2 labor is applied.

**Opportunities:**
- **Target Recalibration:** By simply requiring project quotes to include the estimated cost of internal W-2 labor and raising the target margin to 50%, PulseOne can structurally fix project profitability at the quoting stage.
- **Small Project Efficiency:** Projects under $5,000 operate at an 83% cash margin. Standardizing and increasing the volume of these transactional projects is a clear path to margin expansion.

## F. Required ConnectWise Follow-Up

The profitability of the project division cannot be finalized until the "invisible subsidy" is quantified. This requires three specific data pulls from the ConnectWise AI interface:

1. **W-2 Technician Time by Board Type**
   *Request:* "For CY 2025, pull time entries for all internal W-2 technicians (Hagen McDonell, James Froio, Joel Alvarez, Eric Anzalone, Kaitlin Harris, Laura Walsh). Break down their total logged hours by board type: Help Desk/ITMS (agreements) versus Projects versus Internal/Admin. Include the burdened hourly cost for each technician."
   *Why:* This is the only way to calculate the true W-2 labor cost consumed by projects.

2. **Vincent Williams Project Allocation**
   *Request:* "For CY 2025, how many of Vincent Williams' 1,706 hours were logged to discrete Project boards versus Help Desk/Managed Services agreement boards?"
   *Why:* Determines if his $104K cost belongs in the project margin calculation or the agreement margin calculation.

3. **P&L Revenue Classification for ARC**
   *Request:* "How is the ARC Research monthly revenue classified in the ConnectWise GL mapping? Does it flow to Managed Services revenue or Consulting revenue in QuickBooks?"
   *Why:* We must know where the highly profitable ARC revenue sits to understand which P&L segment it is subsidizing.
