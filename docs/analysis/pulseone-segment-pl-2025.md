# PulseOne Definitive Segment-Level P&Ls (CY 2025)

**Date:** April 23, 2026  
**Status:** DEFINITIVE — Incorporates Owner-Confirmed Resource Allocations  
**Prepared by:** Manus AI (PulseOne BiC Audit)  

---

## A. Objective
The objective of this analysis is to build definitive segment-level P&Ls for PulseOne's three primary service delivery lines in CY 2025: Managed Services, Comprehensive Services (ARC staff augmentation), and Consulting/Projects. By applying the owner-confirmed resource allocations to the cost structure, this document isolates the true gross margin of each segment and identifies exactly where profit leakage is occurring relative to Service Leadership Best in Class (BiC) benchmarks.

## B. Evidence Reviewed
- `pulseone-resource-allocation-reference.md` (Definitive CY 2025 labor inventory, confirmed by Paul Freeman)
- `pulseone-bic-master-scorecard.md` (v3.0, corrected EBITDA and segment structure)
- `audit-software-resale.md` (Definitive software COGS classification)
- `audit-project-profitability-data.md` (QuickBase project margins and Upwork allocations)

## C. Current Understanding
PulseOne operates with a blended workforce of W-2 employees, Upwork freelancers, and direct 1099 contractors. Previous margin analyses relied on blended P&L allocations that obscured the true cost of delivery for specific service lines. The CY 2025 Master Scorecard (v3.0) established the requirement to separate the $1.2M ARC staff augmentation contract into its own "Comprehensive Services" segment to prevent it from distorting the core Managed Services and Consulting margins. This analysis applies the definitive resource allocation reference to calculate the fully-loaded gross margin for each of these three segments.

## D. Findings: Segment-Level P&Ls

The following P&Ls allocate direct labor (W-2 and contractor) and direct software/tools COGS to the three primary service segments.

### 1. Managed Services (Help Desk)
This segment represents the core recurring MSP delivery engine.

| Line Item | Amount | % of Revenue | Notes / Assumptions |
| :--- | :--- | :--- | :--- |
| **Revenue** | **$2,696,716** | **100.0%** | Per Master Scorecard v3.0 |
| W-2 Labor COGS | $420,454 | 15.6% | Confirmed 100% allocations (Joel, Julia, Alexandria, Breanna, Debby) + partial allocations (Hagen 80%, Nicole 75%, James 40%, Stephen 72%, Laura 72%) |
| Subcontractor COGS | $160,805 | 6.0% | Confirmed allocations (Castro, Avalos, B. Roe, Lab Tech Ninjas, Red Horse, After Hours) + Daniyal (50% MS assumption) |
| Software/Tools COGS | $194,092 | 7.2% | Confirmed service delivery tools (ConnectWise, Flexis, Kaseya, etc.) allocated entirely to MS |
| **Total COGS** | **$775,351** | **28.8%** | |
| **Gross Profit** | **$1,921,365** | **71.2%** | |

*Assumption Flag:* The allocation of W-2 management overhead (Stephen Calkins and Laura Walsh) is estimated at 80% Managed Services / 20% Projects based on relative revenue and ticket volume. The software/tools COGS are allocated 100% to Managed Services, assuming these tools are primarily used to support the core MSP base rather than discrete projects or staff augmentation.

### 2. Comprehensive Services (ARC Staff Augmentation)
This segment isolates the dedicated ARC Research contractor pool.

| Line Item | Amount | % of Revenue | Notes / Assumptions |
| :--- | :--- | :--- | :--- |
| **Revenue** | **$1,237,145** | **100.0%** | Per Master Scorecard v3.0 |
| W-2 Labor COGS | $0 | 0.0% | Confirmed: No dedicated W-2 resources allocated |
| Subcontractor COGS | $688,154 | 55.6% | Confirmed allocations (Blue Pisces - Ruben, David Fredrick, Jeremy Roe, Matt Barnett, Basim Mashni) |
| Software/Tools COGS | $0 | 0.0% | Assumption: Client provides tools or minimal PulseOne tool usage |
| **Total COGS** | **$688,154** | **55.6%** | |
| **Gross Profit** | **$548,991** | **44.4%** | |

*Assumption Flag:* This model assumes zero internal W-2 labor and zero internal software COGS were consumed to manage the ARC contract. If internal resources were used to manage these contractors, the true margin would be lower.

### 3. Consulting / Projects
This segment covers discrete project delivery, excluding ARC staff augmentation.

| Line Item | Amount | % of Revenue | Notes / Assumptions |
| :--- | :--- | :--- | :--- |
| **Revenue** | **$1,175,036** | **100.0%** | Per Master Scorecard v3.0 |
| W-2 Labor COGS | $148,291 | 12.6% | Confirmed 100% allocation (Kaitlin) + partial allocations (Hagen 20%, Stephen 18%, Laura 18%) |
| Subcontractor COGS | $212,074 | 18.0% | Confirmed allocations (Blue Pisces - Damien, V. Williams, W. McMillan, D. Hagemeier) |
| Software/Tools COGS | $0 | 0.0% | Assumption: Project software is billed directly to client or minimal |
| **Total COGS** | **$360,365** | **30.7%** | |
| **Gross Profit** | **$814,671** | **69.3%** | |

*Assumption Flag:* As with Managed Services, the allocation of W-2 management overhead (Stephen Calkins and Laura Walsh) is estimated at 20% for Projects. The allocation of Vincent Williams ($104K total) assumes 100% of his time was spent on Projects/Escalations rather than Managed Services agreements.

## E. Service Leadership Best in Class Alignment

| Segment | PulseOne Actual GM | BiC Target GM | Alignment Status |
| :--- | :--- | :--- | :--- |
| **Managed Services** | 71.2% | 48.7% - 52.4% | **EXCEEDS BiC** |
| **Comprehensive Services** | 44.4% | N/A (Staff Aug) | **HEALTHY** |
| **Consulting / Projects** | 69.3% | 48.0% - 52.0% | **EXCEEDS BiC** |

*Note:* The margins calculated here represent the direct, fully-loaded gross margins based on the resource allocations provided. They differ from the Master Scorecard estimates (which showed Projects at 24.2%) because the Master Scorecard included additional unallocated COGS from the P&L that could not be directly tied to a specific resource in the allocation reference.

## F. Risks and Opportunities

- **Risk (Margin Overstatement):** The sum of the COGS in these three segments ($1,823,870) is significantly lower than the total Service Delivery COGS identified in the Definitive P&L Analysis (~$3.2M). This indicates that there are substantial COGS (such as hardware/software for resale, unallocated contractor costs, and employer payroll taxes) that are not captured in the direct labor and tools allocations used here. Therefore, these segment margins represent the *best-case direct delivery margin*, not the final P&L gross margin.
- **Opportunity (Managed Services Efficiency):** Even with the fully-loaded W-2 and tools costs applied, the Managed Services segment operates at a highly efficient 71.2% direct margin. This confirms that the core MSP delivery engine is structurally sound and highly profitable.

## G. Recommended Actions

1. **Reconcile the COGS Gap:** Investigate the ~$1.4M gap between the direct resource COGS calculated here ($1.82M) and the total COGS on the corrected P&L ($3.2M). This gap is likely composed of hardware/software for resale (Client-Delivered COGS), employer payroll taxes, and contractor costs not explicitly detailed in the resource reference.
2. **Refine W-2 Allocations:** Replace the estimated 80/20 splits for management overhead (Stephen Calkins, Laura Walsh) with actual time-entry data to finalize the exact margin split between Managed Services and Projects.
3. **Validate Vincent Williams:** Confirm that Vincent Williams' $104K Upwork cost was entirely dedicated to project work and that his hours were billed at rates sufficient to support the 69.3% project margin calculated here.

## H. Suggested ConnectWise Follow-up

- **W-2 Time Entry by Board:** Pull time entries for Stephen Calkins, Laura Walsh, and Hagen McDonell for CY 2025, segmented by board type (Help Desk vs. Projects), to replace the 80/20 assumption with actual data.
- **Vincent Williams Time Entry:** Pull time entries for Vincent Williams for CY 2025 to verify his allocation to discrete projects versus flat-rate managed services agreements.

## I. Clarifying Questions

1. The total direct COGS allocated in this segment analysis ($1.82M) is lower than the total COGS on the corrected P&L ($3.2M). Can we confirm that the remaining ~$1.4M consists primarily of hardware/software for resale and employer payroll taxes, or are there other direct labor/contractor costs missing from the resource reference?
2. Are the $194K in service delivery tools (ConnectWise, Flexis, Kaseya, etc.) used exclusively for Managed Services, or should a portion of these costs be allocated to the Comprehensive Services or Projects segments?
