# PulseOne — COGS vs. SG&A Person-by-Person Classification Analysis
**Date:** April 17, 2026  
**Purpose:** Reclassify all labor costs to correct COGS vs. SG&A buckets and rebuild the normalized P&L  
**Prepared by:** Manus (PulseOne BIC Audit)

---

## Context and Methodology

### The Problem
QuickBooks currently shows:
- **Consulting Services – Cost (COGS):** $1,044,424 — this captures contractor/1099 payments routed through QB's COGS account
- **Salary Expense (SG&A):** $1,441,010 — this captures ALL W-2 payroll indiscriminately, regardless of whether the employee is a service delivery technician (COGS) or an overhead/admin person (SG&A)
- **Payroll Taxes (SG&A):** $296,256 — same problem; all payroll taxes sit in SG&A
- **Partner Compensation (SG&A):** $423,000 — partner draws, currently all in SG&A

The Expense Tracker shows total contractor cost of **$1,798,225**, creating a **$753,801 gap** versus what QB reports in Consulting Services – Cost. The most likely explanation is that a portion of contractor payments were coded to Salary Expense or another SG&A line rather than to the COGS account in QB.

### Classification Principles (Service Leadership BIC Standard)
Under Service Leadership Best in Class methodology:
- **COGS** = All costs directly associated with delivering services to clients: technician labor (W-2 and 1099), subcontractors, tools and software used in delivery, and direct project labor
- **SG&A** = Overhead: sales, marketing, executive/owner compensation (to the extent not billable), finance/admin, HR, facilities, and non-delivery software

For **mixed-role individuals** (e.g., a working owner who does some delivery and some management), the correct approach is to split their cost by estimated time allocation between delivery and overhead.

### Key Definitions Used
| Role Category | COGS % | SG&A % | Rationale |
|---|---|---|---|
| Pure service delivery technician (HD/field/NOC) | 100% | 0% | Entirely billable delivery labor |
| Service delivery with some admin duties | 80–90% | 10–20% | Primarily delivery, minor overhead |
| Service manager / team lead (hands-on) | 70–80% | 20–30% | Delivery + supervision |
| Sales / BizDev | 0% | 100% | Pure SG&A |
| Marketing | 0% | 100% | Pure SG&A |
| Operations / Admin | 0–20% | 80–100% | Overhead, unless directly supporting delivery |
| Finance / Accounting | 0% | 100% | Pure SG&A |
| Executive / Owner (non-billable) | 0–30% | 70–100% | Depends on delivery involvement |
| POC (PulseOne Communications) | Separate entity — allocate by function |

---

## PART A: W-2 EMPLOYEES — CLASSIFICATION TABLE

The following table covers every W-2 employee identified in the 2025 payroll reports. Annual cost is estimated as Gross YTD × burden factor (payroll taxes ~10–12%, benefits where applicable). Where the employee was terminated mid-year, the YTD figure is used as-is.

### Group 1: Service Delivery — Technical Staff (Dept: 100 – Services Tech Service)

These are the core service delivery employees. Under BIC standards, their labor cost belongs in COGS.

| # | Name | QB Dept | Status | Gross YTD | Est. Annual Burden | COGS % | SG&A % | Rationale |
|---|---|---|---|---|---|---|---|---|
| 1 | **Eric Anzalone** | 100 – Services Tech Service | Active, FT | $76,718 | ~$85,000 | **100%** | 0% | Full-time service delivery technician. Expense Tracker confirms "Services" dept, W2 ADP. |
| 2 | **James Froio** | 100 – Services Tech Service | Active, FT | $112,788 | ~$126,000 | **100%** | 0% | Full-time service delivery. Expense Tracker: "Help Desk" dept. Senior tech. |
| 3 | **Kaitlin Harris** | 100 – Services Tech Service | Active, FT | $79,040 | ~$88,000 | **100%** | 0% | Full-time service delivery. Expense Tracker: "Services" dept. |
| 4 | **Laura Walsh** | 100 – Services Tech Service | Active, FT | $108,186 | ~$121,000 | **100%** | 0% | Full-time service delivery. Expense Tracker: "Services" dept. |
| 5 | **Stephen Calkins** | 100 – Services Tech Service | Active, FT | $148,960 | ~$164,000 | **90%** | 10% | Senior/lead technician. Expense Tracker rate of $71.62/hr suggests senior role with some supervisory overhead. |
| 6 | **Hagen McDonell** | 100 – Services Tech Service | Active, FT | $50,597 | ~$56,000 | **100%** | 0% | Full-time service delivery. Expense Tracker: "Help Desk" dept. |
| 7 | **Alexandria Calkins** | 100 – Services Tech Service | Active, PT | $17,258 | ~$19,000 | **100%** | 0% | Part-time service delivery. Expense Tracker: "Services" dept. |
| 8 | **Nicole Goodwin** | 100 – Services Tech Service (also POC) | Active, PT | $51,100 | ~$56,000 | **80%** | 20% | Split between Services delivery and POC (PulseOne Communications). Expense Tracker shows dual allocation: POC + Services 2025 addition. |
| 9 | **Julia Morte** | 100 – Services Tech Service | Active, PT | $20,322 | ~$22,000 | **100%** | 0% | Part-time service delivery. Expense Tracker: "Help Desk" dept. |
| 10 | **Joel Alvarez** | 100 – Services Tech Service | Active, PT | $25,068 | ~$27,000 | **100%** | 0% | Part-time service delivery. Expense Tracker: "Help Desk" dept. |
| 11 | **Emily Acker** | 100 – Services Tech Service | Terminated | $9,690 | $9,690 | **100%** | 0% | Service delivery, terminated. YTD cost is actual. |
| 12 | **Debby Brooke** | 100 – Services Tech Service | Terminated | $7,928 | $7,928 | **100%** | 0% | Service delivery, terminated. YTD cost is actual. |
| 13 | **Breanna Copeland** | 100 – Services Tech Service | Terminated | $11,444 | $11,444 | **100%** | 0% | Service delivery, terminated. YTD cost is actual. |

**Group 1 Subtotals (W-2 Service Delivery):**

| Metric | Amount |
|---|---|
| Total Gross YTD (Group 1) | ~$918,099 |
| Estimated Annual Burden (Group 1) | ~$1,008,000 |
| Amount to COGS (weighted avg ~99%) | ~$995,000 |
| Amount to SG&A (supervisory/admin) | ~$13,000 |

---

### Group 2: Sales, Marketing, and Business Development (Dept: 200 – Marketing)

Under BIC standards, all sales and marketing labor is SG&A. No portion belongs in COGS.

| # | Name | QB Dept | Status | Gross YTD | COGS % | SG&A % | Rationale |
|---|---|---|---|---|---|---|---|
| 14 | **Kyle Carey** | 200 – Marketing | Active, FT | $51,800 | 0% | **100%** | Sales/BizDev role. Expense Tracker: "MKTG" dept. Pure SG&A. |
| 15 | **Chad Wiggins** | 200 – Marketing | Terminated, FT | $95,000 | 0% | **100%** | Business Development. Expense Tracker: "Biz Dev" dept. Pure SG&A. |
| 16 | **Heather Kohler** | 200 – Marketing | Terminated, FT | $13,200 | 0% | **100%** | Marketing. Pure SG&A. |
| 17 | **Dana Rankin** | 200 – Marketing | Terminated, FT | $9,200 | 0% | **100%** | Marketing. Pure SG&A. |
| 18 | **Anneliese Rivera** | 200 – Marketing | Terminated, PT | $4,100 | 0% | **100%** | Marketing. Pure SG&A. |
| 19 | **Marcello Rocha Moreira** | 200 – Marketing | Terminated, FT | $33,280 | 0% | **100%** | Marketing. Expense Tracker also shows Payoneer contractor version. Pure SG&A. |
| 20 | **Andrea Carcamo (Lucy)** | 200 – Marketing | Active, FT | $7,492 | 0% | **100%** | Marketing. Expense Tracker: "MKTG" dept. Pure SG&A. |

**Group 2 Subtotals:** Total Gross YTD ~$214,072 → 100% SG&A

---

### Group 3: Operations and Administration (Dept: 300 – Operations)

Operations staff are primarily overhead. Some may support service delivery coordination (dispatch, scheduling), which could warrant a partial COGS allocation, but the default is SG&A unless confirmed otherwise.

| # | Name | QB Dept | Status | Gross YTD | COGS % | SG&A % | Rationale |
|---|---|---|---|---|---|---|---|
| 21 | **Aimee Brock** | 300 – Operations | Active, PT | $23,300 | 0% | **100%** | Operations/admin. Expense Tracker: "Operations" dept, 2025 addition. Pure SG&A. |
| 22 | **Emily Wolf** | 300 – Operations | Active, PT | $18,400 | 0% | **100%** | Operations/admin. Expense Tracker: "Operations" dept, 2025 addition. Pure SG&A. |
| 23 | **Jamie Davin** | 300 – Operations | Terminated, PT | $9,800 | 0% | **100%** | Operations/admin. Terminated 2025. Pure SG&A. |
| 24 | **Juliet Simpson** | 300 – Operations | Terminated, PT | $9,263 | 0% | **100%** | Operations/admin. Terminated 2025. Pure SG&A. |
| 25 | **Mariette Wingard** | 300 – Operations | Terminated, PT | $0 | 0% | **100%** | Operations/admin. No 2025 payroll recorded. |
| 26 | **Ashley Holmes** | 300 – Operations | Terminated, PT | $725 | 0% | **100%** | Operations/admin. Very brief tenure 2025. Pure SG&A. |

**Group 3 Subtotals:** Total Gross YTD ~$61,488 → 100% SG&A

---

### Group 4: POC (PulseOne Communications — Dept: 900)

POC is a separate business entity. Tracy Freeman is listed under POC. The classification depends on whether POC revenue and cost are consolidated into the PulseOne P&L or kept separate.

| # | Name | QB Dept | Status | Gross YTD | COGS % | SG&A % | Rationale |
|---|---|---|---|---|---|---|---|
| 27 | **Tracy Freeman** | 900 – POC | Active, PT | $12,889 | **TBD** | **TBD** | POC entity. If POC is consolidated, her cost should be classified by function (service delivery support = COGS; admin = SG&A). Expense Tracker shows "POC" dept at $1,062/mo. **Requires Paul's confirmation on POC consolidation treatment.** |

---

### Group 5: Owner / Partner Compensation

Paul Freeman is listed in payroll (200 – Marketing dept) with $0 gross YTD shown in the payroll extract. Partner Compensation of $423,000 appears as a separate SG&A line in the P&L.

| # | Name | QB Dept | Status | QB Treatment | COGS % | SG&A % | Rationale |
|---|---|---|---|---|---|---|---|
| 28 | **Paul Freeman** | 200 – Marketing | Active, FT | Partner Comp line ($423K total) | **0–20%** | **80–100%** | Owner/CEO. Primarily executive/sales/strategy. Under BIC, owner comp is normalized out of COGS entirely for margin analysis. If Paul does any billable delivery work, a portion could be COGS, but the standard BIC normalization removes owner comp from COGS. |
| 29 | **Charles Batsford** | 300 – Operations | Active, FT | Partner Comp line (included in $423K) | **0–20%** | **80–100%** | Partner. Operations-focused. Similar treatment to Paul. BIC normalization removes from COGS. |
| 30 | **Rod Hare** | Not in payroll | Partner | Included in $423K Partner Comp | 0% | **100%** | Investor/partner. No service delivery role indicated. Pure SG&A/owner comp. |

**Note on Partner Compensation:** The $423,000 Partner Compensation line in the P&L is already in SG&A. Under BIC normalization, this is typically separated out entirely to calculate "normalized" EBITDA. It should not move to COGS.

---

## PART B: CONTRACTORS AND 1099 WORKERS — CLASSIFICATION TABLE

The following are all non-W2 workers identified in the 2025 Expense Tracker. These are the individuals whose costs should be flowing through "Consulting Services – Cost" in QB but may be misclassified.

### Group 6: Service Delivery Contractors (COGS)

| # | Name | Method | Dept | Mo Cost (Net) | Ann Est | COGS % | SG&A % | Rationale |
|---|---|---|---|---|---|---|---|---|
| 31 | **Daniyal Arif** | Payoneer | Services | ~$4,000 | ~$48,000 | **100%** | 0% | Offshore service delivery tech. Expense Tracker: "Services" dept. Core delivery resource. Should be 100% COGS. |
| 32 | **Red Horse (Robyn)** | ACH | Services | ~$2,908 | ~$34,900 | **100%** | 0% | Service delivery contractor. Expense Tracker: "Services" dept. Note: $2,908.80/mo per tracker note. Should be COGS. |
| 33 | **Matt Barnett** | Upwork | Help Desk | ~$5,850 net | ~$70,200 net | **100%** | 0% | Help Desk contractor (Upwork). Expense Tracker shows $7,800/mo gross with a $1,950/mo COGS reimbursement credit (10 hrs/wk). Net cost ~$5,850/mo. Should be COGS. |
| 34 | **Omar Avalos** | Upwork | Help Desk | ~$4,333 | ~$52,000 | **100%** | 0% | Help Desk contractor (Upwork). Should be COGS. |
| 35 | **Vincent Williams** | Upwork | Help Desk | ~$5,200 | ~$62,400 | **100%** | 0% | Help Desk contractor (Upwork). Should be COGS. |
| 36 | **Level 2 Engineer** (Neal, Memphis TN) | W2 ADP | Services | ~$7,453 | ~$89,440 | **100%** | 0% | Planned/budgeted Level 2 engineer. "Laura want Neal in Memphis TN" note. If hired, 100% COGS. |
| 37 | **Technical Staff – After Hours** | W2 ADP | Help Desk | ~$433 | ~$5,200 | **100%** | 0% | On-call after-hours coverage. 100% COGS. |

### Group 7: Marketing/Sales Contractors (SG&A)

| # | Name | Method | Dept | Mo Cost (Net) | Ann Est | COGS % | SG&A % | Rationale |
|---|---|---|---|---|---|---|---|---|
| 38 | **Marcello Moreira** (contractor version) | Payoneer | MKTG | ~$4,507 | ~$54,080 | 0% | **100%** | Marketing contractor. Pure SG&A. Note: also appears as W-2 terminated employee — confirm if this is the same person or a separate engagement. |
| 39 | **Marcy Dorman-Chandler** | BILL | MKTG | ~$800 | ~$9,600 | 0% | **100%** | Marketing contractor. Pure SG&A. |
| 40 | **Anneliese** (contractor version) | W2 ADP | MKTG | ~$1,083 | ~$13,000 | 0% | **100%** | Marketing. Pure SG&A. |

---

## PART C: ITEMS REQUIRING PAUL'S CONFIRMATION

Before finalizing the reclassification, the following items require your direct input:

### C1 — The $753,801 Gap: Where Did the Contractor Costs Go in QB?

The Expense Tracker shows $1,798,225 in total contractor cost. QB shows only $1,044,424 in Consulting Services – Cost. The $753,801 difference is most likely sitting in one of these QB lines:

| Possible QB Location | Likely Amount | Action Needed |
|---|---|---|
| Salary Expense (SG&A) | Largest portion | Pull QB transaction detail for Salary Expense — look for 1099/contractor payments |
| Computer and Internet Expenses | Some portion | $263,953 in QB — unusually high; may include contractor tool costs |
| Professional Fees | Smaller portion | $14,686 in QB |
| Other SG&A lines | Residual | Review with bookkeeper |

**Question for Paul:** Can you or your bookkeeper pull the QB transaction detail for the Salary Expense line and identify which entries are W-2 payroll vs. contractor/1099 payments? This is the key to closing the gap.

### C2 — Stephen Calkins: Role Confirmation

Stephen Calkins is the highest-paid W-2 employee at ~$149K gross YTD, with an hourly rate of $71.62 in the Expense Tracker. He is in "100 – Services Tech Service" but at this compensation level, he may have a service management or team lead role.

**Question:** Is Stephen purely a delivery technician, or does he have management/oversight responsibilities? This affects whether his split is 100/0 or 90/10 COGS/SG&A.

### C3 — Nicole Goodwin: POC vs. Services Split

Nicole appears in both the POC department and the Services department in the Expense Tracker (a 2025 addition to Services). Her QB department is "900 – POC" in one payroll record and "100 – Services Tech Service" in another.

**Question:** What percentage of Nicole's time is spent on PulseOne managed services delivery vs. POC-related work? Suggested split: 70% COGS (Services), 30% POC/SG&A — confirm.

### C4 — Tracy Freeman: POC Treatment

Tracy is in "900 – POC" and is Paul's wife. Her role appears to be administrative/operational support for PulseOne Communications.

**Question:** Is POC revenue and cost consolidated into the main PulseOne P&L? If yes, what is Tracy's function — service delivery support (COGS) or admin/operations (SG&A)?

### C5 — Daniyal Arif: Full Annual Cost

The Expense Tracker shows Daniyal at ~$4,000/mo for Services. There is also a separate RS (RepScheduler) allocation. His total annual cost needs to be confirmed.

**Question:** What is Daniyal's total 2025 cost across all PulseOne entities (Services + RS + any other allocations)?

### C6 — Paul Freeman: Billable Hours

Paul is listed in QB payroll under "200 – Marketing" with $0 gross YTD (suggesting his compensation runs through the Partner Compensation line). 

**Question:** Does Paul perform any direct billable service delivery work for clients? If yes, what percentage of his time? This determines whether any portion of his comp should be COGS.

### C7 — Charles Batsford: Role and Billable Work

Charlie is in "300 – Operations" with $0 gross YTD in payroll (compensation through Partner Comp line).

**Question:** Does Charlie perform any direct service delivery work? What is his primary function — operations management, client management, technical delivery, or a mix?

---

## PART D: PRELIMINARY RECLASSIFICATION ESTIMATES

Based on the data extracted, here is a preliminary view of what the reclassification will likely show. **These figures are estimates pending your confirmation of the items in Part C.**

### Current QB Classification (As-Is)

| Line Item | QB Location | Amount |
|---|---|---|
| Consulting Services – Cost | COGS | $1,044,424 |
| Salary Expense | SG&A | $1,441,010 |
| Payroll Taxes | SG&A | $296,256 |
| Partner Compensation | SG&A | $423,000 |
| **Total Labor (all forms)** | | **$3,204,690** |

### Preliminary Reclassification Estimate

| Person/Group | Current QB Location | Estimated Annual Cost | Proposed COGS | Proposed SG&A |
|---|---|---|---|---|
| **W-2 Service Delivery (Group 1)** | Salary Expense (SG&A) | ~$1,008,000 | ~$995,000 | ~$13,000 |
| **W-2 Sales/Marketing (Group 2)** | Salary Expense (SG&A) | ~$235,000 | $0 | ~$235,000 |
| **W-2 Operations/Admin (Group 3)** | Salary Expense (SG&A) | ~$68,000 | $0 | ~$68,000 |
| **Tracy Freeman (POC)** | Salary Expense (SG&A) | ~$14,000 | TBD | TBD |
| **Partner Comp (Paul, Charlie, Rod)** | Partner Comp (SG&A) | $423,000 | $0 | $423,000 |
| **Payroll Taxes (service delivery share)** | Payroll Taxes (SG&A) | $296,256 | ~$175,000 | ~$121,000 |
| **Contractors – Service Delivery** | Consulting Svcs Cost (COGS) | ~$312,000 | ~$312,000 | $0 |
| **Contractors – Marketing/Sales** | Consulting Svcs Cost (COGS) | ~$77,000 | $0 | ~$77,000 |
| **Remaining QB COGS (tools/vendors)** | COGS | ~$655,424 | ~$655,424 | $0 |
| **TOTAL** | | **~$3,088,680** | **~$2,137,424** | **~$937,000** |

### Projected Impact on Gross Margin

| Metric | Current (QB As-Is) | Estimated After Reclassification |
|---|---|---|
| Total Revenue | $5,168,754 | $5,168,754 |
| Total COGS | $2,123,012 | ~$3,132,000 |
| **Gross Profit** | **$3,045,742** | **~$2,037,000** |
| **Gross Margin %** | **58.9%** | **~39%** |
| Total SG&A | $2,827,967 | ~$1,820,000 |
| **Net Income** | **$217,775** | **~$217,000** |

> **Critical Insight:** The net income does not change — reclassification is a presentation correction, not a cash change. However, the gross margin drops from a misleading 58.9% to approximately 39%, which is far below the Service Leadership BIC benchmark of 50%+ for a well-run MSP. This reveals the true profit leakage: **PulseOne's service delivery labor cost is consuming ~61% of revenue before overhead**, leaving insufficient margin to cover SG&A and generate target profitability.

---

## PART E: SERVICE LEADERSHIP BIC ALIGNMENT PREVIEW

| Metric | PulseOne (QB As-Is) | PulseOne (Reclassified Est.) | BIC Benchmark | Gap |
|---|---|---|---|---|
| Gross Margin % | 58.9% | ~39% | 50–55% | **~11–16 pts below BIC** |
| Service Delivery Labor as % of Revenue | ~19% (understated) | ~38–40% | 25–30% | **~10–15 pts above BIC** |
| SG&A as % of Revenue | 54.7% | ~35% | 25–30% | Improving but still elevated |
| Net Income % | 4.2% | ~4.2% | 12–18% | **~8–14 pts below BIC** |

---

## NEXT STEPS

1. **Paul confirms** the items in Part C (7 questions above)
2. **Bookkeeper pulls** QB transaction detail for Salary Expense to identify misclassified contractor payments
3. **Finalize** the reclassification table with confirmed splits
4. **Rebuild** the corrected normalized P&L with:
   - Corrected COGS (service delivery labor moved in)
   - Corrected SG&A (only true overhead)
   - Normalized EBITDA (owner comp added back)
   - BIC benchmark comparison
5. **Identify** specific profit leakage drivers and prioritize corrective actions

---

*This document was prepared using data from: 2025 Profit and Loss POTS_analysis.xlsx, Expenses Tracking MASTER 2023.xlsx (2025 tab), 2025payrollreports.xlsx, and 2025 PulseOne Software COGS and Expense.xlsx.*
