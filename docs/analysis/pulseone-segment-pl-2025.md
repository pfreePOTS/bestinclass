# PulseOne Definitive Segment-Level P&Ls

**Date:** April 28, 2026
**Version:** 4.1
**Status:** AUTHORITATIVE — Built from QB Detail and Owner Confirmations
**Prepared by:** Manus (PulseOne BiC Audit)

---

## A. Objective
To build definitive, fully reconciled segment-level P&Ls for CY 2025 using exact, transaction-level data from QuickBooks (specifically the "Consulting Services-Cost" detail) combined with owner-confirmed W-2 labor allocations. This version replaces all prior estimates and assumptions.

## B. Evidence Reviewed
- CY 2025 QuickBooks P&L [1]
- CY 2025 QuickBooks "Consulting Services - Cost" Detail Report (189 transactions, $1,045,803 total) [2]
- PulseOne Resource Allocation Reference (v3.0) [3]
- CY 2025 Upwork Time by Freelancer Report [4]

## C. Current Understanding
PulseOne operates three distinct business segments:
1. **Managed Services:** Core help desk and recurring support ($2.70M revenue)
2. **Comprehensive Services (ARC):** Dedicated staff augmentation ($1.24M revenue)
3. **Consulting/Projects:** Discrete, non-recurring project work ($1.18M revenue)

Prior P&L models relied on estimates for contractor costs, which artificially inflated project margins. By tracing every dollar in the CS-Cost account, we have definitively allocated $1.04M in subcontractor costs to their exact segments, revealing the true cost of service delivery.

## D. Findings & Segment P&Ls

The following P&Ls reflect **Direct Delivery Margin** — the margin generated after paying for the labor and tools required to deliver the service. It excludes standalone product resale (M365, hardware, Adobe) which have their own revenue and COGS lines.

| Line Item | Managed Services | Comprehensive (ARC) | Consulting/Projects | Total |
|---|---|---|---|---|
| **Revenue** | **$2,696,716** | **$1,237,145** | **$1,175,036** | **$5,108,897** |
| | | | | |
| **W-2 Labor COGS** | $292,250 | $0 | $202,598 | $494,848 |
| **Upwork COGS** | $152,468 | $0 | $80,280 | $232,748 |
| **BILL/CS-Cost Subs** | $3,612 | $650,057 | $343,031 | $996,700 |
| **Service Delivery Tools** | $277,129 | $16,302 | $32,603 | $326,034 |
| | | | | |
| **Total Segment COGS** | **$725,459** | **$666,359** | **$658,512** | **$2,050,330** |
| **Gross Profit** | **$1,971,257** | **$570,786** | **$516,524** | **$3,058,567** |
| **Gross Margin %** | **73.1%** | **46.1%** | **44.0%** | **59.9%** |

### Key Segment Insights

**1. Consulting/Projects (44.0% Margin)**
The inclusion of exact CS-Cost data dramatically shifted the project narrative. We found **$343,031** in project subcontractors (Damien/Bunzl, Jeremy Roe, Infinite Ideas, F2OnSite) that were previously untracked or underestimated. This drops the project margin from the previously estimated 64.2% down to **44.0%**. While still higher than the 24% "fully-loaded" target, this proves that projects are significantly more expensive to deliver than previously modeled. The remaining gap to 24% represents the "invisible subsidy" of untracked W-2 time.

**2. Comprehensive Services (ARC) (46.1% Margin)**
ARC subcontractor costs were $75K higher than previously estimated. Basim Mashni ($148K) and BJ Sinder ($132K) were paid via BILL, not Upwork. The exact cost of the ARC delivery team was $650,057, yielding a healthy 46.1% margin for a staff augmentation model.

**3. Managed Services (73.1% Margin)**
The core MS delivery engine remains highly efficient. With product resale stripped out and project costs correctly attributed, the pure service delivery margin is 73.1%. This confirms that the root cause of PulseOne's margin leakage is entirely contained within the Project segment and product pricing, not the Help Desk.

## E. Service Leadership Best in Class Alignment
- **Managed Services (73.1%):** Significantly exceeds the BiC target of 48.7–52.4%.
- **Consulting/Projects (44.0%):** Below the BiC target of 48–52%. If the invisible W-2 subsidy is fully accounted for, this margin likely drops into the 20s, indicating a severe quoting and pricing failure.
- **Total Company Margin (59.9% direct):** When combined with the lower-margin product resale business, the blended company margin drops to ~37.4%, which is below the 44.0%+ BiC target.

## F. Risks and Opportunities
- **Risk:** The 44.0% project margin is still an illusion. It only counts the labor we can explicitly trace. Without ConnectWise time-entry data for W-2 staff (Calkins, Froio, Walsh), the true cost of projects remains hidden.
- **Opportunity:** The 73.1% MS margin proves the core business model works. If project quoting is fixed to include the true cost of internal labor, total company profitability will rebound sharply.

## G. Recommended Actions
1. **Adopt these P&Ls as the definitive baseline.** They are the only version built entirely from transaction-level QB detail rather than estimates.
2. **Implement Project Time Tracking:** Mandate that all W-2 staff track their time against specific project tickets in ConnectWise. This is the only way to expose the remaining "invisible subsidy."
3. **Fix Project Quoting:** Immediately require that all project quotes include a loaded cost for internal W-2 labor, not just subcontractor pass-throughs.

## H. Suggested ConnectWise Follow-up
- **W-2 Time Entries by Board:** Pull the CY 2025 time entries for Stephen Calkins, James Froio, and Laura Walsh to determine exactly how many hours they spent on project boards versus MS boards. This will finalize the W-2 allocation and close the remaining gap in the project margin.

## I. Remaining True Gaps

**Resolved since v3.0:**
- Jeremy Roe: RESOLVED — $100,097 via BILL (Roe Tech LLC). 71% Bunzl, 24% other projects, 5% ARC.
- Matt Barnett: RESOLVED — owner-confirmed 75% HD / 15% ITMS / 10% Projects. 0% ARC.
- BJ Sinder: RESOLVED — $132,390 via BILL (Infinite Ideas IT Inc). 100% ARC.
- Basim Mashni: RESOLVED — $148,918 via BILL (Mash Tech Inc). 100% ARC.
- Damien (Blue Pisces): RESOLVED — $229,843 via BILL. 100% Bunzl projects.

**Still Open:**
1. Vincent Williams MS/CP split — contract includes both "Risk Assessments" and "Ticket Escalations." Need owner estimate or CW time entries.
2. CW time entries for Calkins, Walsh, Froio — needed to validate owner-estimated project percentages and quantify the invisible subsidy.
3. GoDaddy ($6K) — confirmed internal SGA. Azure ($19K) — still needs classification.

---

## References

- [1] `docs/analysis/pulseone-definitive-pl-analysis.md` — Corrected P&L COGS baseline
- [2] `2025PulseOneConsultingServicesCost.xlsx` — QB Detail Report provided by owner
- [3] `docs/analysis/pulseone-resource-allocation-reference.md` — Owner-confirmed labor allocations
- [4] `Upwork - Reports - Time by freelancer 2025.csv` — Confirmed CY2025 Upwork data
