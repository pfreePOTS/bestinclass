# PulseOne Audit Continuation: Open Items Analysis

**Date:** May 1, 2026
**Prepared by:** Manus (PulseOne Strategic Audit Assistant)

## A. Objective
This document addresses the four open items from the current state of the PulseOne Best in Class (BiC) Audit: validating labor allocation estimates, itemizing the $286,697 G&A operating expenses, investigating the negative gross margin in the Projects segment, and outlining a path to 40% margin for the Comprehensive segment. The analysis is grounded in the corrected v7.1 P&L model and QuickBase project data [1] [2].

## B. Evidence Reviewed
- `scripts/build_pl_v7_corrected.py` (Canonical P&L build script)
- `PulseOne_Definitive_PL_Evaluation_2025.md` (Master P&L document)
- `pulseone-resource-allocation-reference.md` (Authoritative labor allocation)
- `PulseOne_Four_Questions_Analysis_Revised.md` (Revised project profitability analysis)
- `2025 Profit and Loss POTS_analysis.xlsx` (QuickBooks source detail)

## C. Findings

### 1. G&A Itemization: Resolving the $286,697 Gap
The previous P&L model accurately identified a $286,697 gap between the model's sourced expenses and the QuickBooks total. This gap represents real G&A operating expenses that were not individually modeled [3].

By extracting the unitemized lines from the QuickBooks P&L, we can now categorize these expenses according to Best in Class standards. The total unitemized lines actually sum to $349,568, but this includes ~$63K in mapping overlap where QuickBooks aggregate lines (like "Agreement License Cost") contain costs we have already modeled separately (like Skout/Barracuda) [4].

The scaled itemization of the $286,697 gap is as follows:

| Category | Scaled Amount | % of Revenue | Key Components |
| :--- | :--- | :--- | :--- |
| **Insurance & Taxes** | $130,553 | 2.5% | Insurance ($106K), CA Tax ($14.6K), Interest ($9.3K) |
| **Facilities** | $41,241 | 0.8% | Rent ($32.5K), Utilities ($7K), Janitorial ($1.6K) |
| **Marketing / Advertising** | $42,623 | 0.8% | Advertising and Promotion ($42.6K) |
| **Office & Admin** | $41,544 | 0.8% | Telephone ($16.5K), Office Supplies ($8.7K), Bank Fees ($6.8K) |
| **Professional Development** | $19,287 | 0.4% | Training and Development ($19.3K) |
| **Professional Services** | $11,439 | 0.2% | Professional Fees ($12K) |
| **Total Unitemized G&A** | **$286,687** | **5.5%** | |

*Note: The $42,623 in Advertising and Promotion is currently sitting in G&A but should structurally be reclassified to Marketing SG&A.*

### 2. Projects Segment Investigation: The Revenue Discrepancy
The Projects segment shows a -4.6% gross margin in the P&L model (revenue of $432,343 against COGS of $452,365). However, QuickBase tracks $690,839 in "true project" revenue for 2025 [5].

This **$258,496 revenue discrepancy** is the critical factor in evaluating the segment. If the QuickBase revenue figure is correct, and the model's COGS is accurate, the segment would be operating at a 34.5% gross margin. 

The likely explanation is that QuickBooks is misclassifying project revenue. The QuickBooks "Consulting Income" line ($1.8M) is split between Comprehensive staffing ($1.38M) and Projects ($420K). The remaining ~$260K of project revenue tracked in QuickBase is almost certainly being booked into "IT Managed Services" or "Sales - Hardware/Software" in QuickBooks.

### 3. Labor Allocation Sensitivity
The model relies on estimated allocations for four key W-2 employees (Calkins, Froio, Walsh, Harris). To test the fragility of the -4.6% margin conclusion, a sensitivity analysis was performed [6].

Even in the most optimistic scenario—where all four individuals spend 10% less time on projects than estimated—the segment only reaches a 9.7% gross margin. The fixed contractor costs (Upwork and BILL) alone consume 51% of the $432K QuickBooks revenue. 

Therefore, the exact W-2 percentages matter for precision, but the conclusion is robust: the Projects segment is unprofitable at the current QuickBooks revenue level. The fix requires resolving the revenue discrepancy (Section 2) and enforcing fully-loaded pricing.

### 4. Comprehensive Segment: Path to 40% Margin
The Comprehensive Services segment (ARC and Bunzl staff augmentation) operates at a 35.2% gross margin, falling short of the ~40% target. This represents a $66,541 profit gap [7].

The segment is bifurcated:
- **ARC:** $1.1M revenue, $667K contractor cost (39.5% GM)
- **Bunzl Staffing:** $280K revenue, $230K contractor cost (18.1% GM)

ARC is performing at target. The Bunzl staffing engagements (e.g., Path to Cloud, Elsabon HR) are the drag on the segment. Because Bunzl is a massive growth engine with an active pipeline of new subsidiaries, PulseOne should focus on pricing new engagements correctly rather than disrupting existing ones.

To close the $66K gap, PulseOne can execute a combination strategy:
- A 5% rate increase on all contract renewals
- Negotiating a 2-3% rate reduction with Blue Pisces and other primary BILL contractors

## D. Recommended Actions

1. **Reclassify Advertising:** Move the $51,970 QuickBooks Advertising line from G&A to Marketing SG&A to accurately reflect customer acquisition costs.
2. **Resolve Project Revenue:** Pull ConnectWise invoices tagged to project boards for CY2025 to determine whether true project revenue is $432K (QuickBooks) or $691K (QuickBase). This will definitively answer whether the Projects segment is a loss-leader or a victim of accounting misclassification.
3. **Validate Labor via ConnectWise:** Pull 2025 ConnectWise time entries by board for Calkins, Froio, Walsh, and Harris to replace the estimated allocation percentages with hard data.
4. **Target Bunzl Pricing:** Ensure all net-new Bunzl staffing proposals are priced to achieve a minimum 40% gross margin against the Blue Pisces contractor costs.

## References
[1] `scripts/build_pl_v7_corrected.py`
[2] `PulseOne_Definitive_PL_Evaluation_2025.md`
[3] `PulseOne_Definitive_PL_Evaluation_2025.md` (Section D.7)
[4] `scripts/itemize_ga_opex.py` output
[5] `PulseOne_Four_Questions_Analysis_Revised.md` (Section 2)
[6] `scripts/projects_cogs_reconcile.py` output
[7] `pulseone-resource-allocation-reference.md` (Section E)
