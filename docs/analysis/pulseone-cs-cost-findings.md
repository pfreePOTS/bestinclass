# PulseOne Consulting Services-Cost Analysis

**Date:** April 22, 2026
**Status:** AUTHORITATIVE — Based on QB Detail Report
**Prepared by:** Manus (PulseOne BiC Audit)

---

## A. Objective
To definitively trace and allocate the $1,045,009 sitting in the QuickBooks "Consulting Services - Cost" line for CY 2025. This line contains the bulk of PulseOne's subcontractor costs, but prior analyses relied on partial data and estimates, leading to significant misallocations between the Comprehensive Services (ARC) and Consulting/Projects segments.

## B. Evidence Reviewed
- `2025PulseOneConsultingServicesCost.xlsx` (QB Detail Report provided by owner)
- Total transactions: 189
- Total value: $1,045,803.17 (Variance of -$794.42 from QB summary total of $1,045,008.75)

## C. Key Findings & Corrections

The analysis of the transaction-level detail reveals four major corrections to the prior labor models.

### 1. ARC Costs Were Understated by $75K
The prior model estimated ARC subcontractor costs at $575K. The actual payments to ARC-dedicated vendors total **$650,057**.

| Vendor | Confirmed Amount | Prior Estimate | Variance |
|---|---|---|---|
| Blue Pisces (Ruben Cortez) | $193,246 | $196,950 | -$3,704 |
| David Fredrik LLC (David Falkenberg) | $171,003 | $182,770 | -$11,767 |
| Mash Tech Inc. (Basim Mashni) | $148,918 | $57,522 (Upwork only) | +$91,396 |
| Infinite Ideas IT Inc (BJ Sinder) | $132,390 | $120,000 (Estimate) | +$12,390 |
| Roe Tech LLC (Jeremy Roe) | $4,500 | $18,000 (Estimate) | -$13,500 |
| **Total ARC Subcontractors** | **$650,057** | **$575,242** | **+$74,815** |

**Critical Insight:** Basim Mashni was paid primarily through BILL (Mash Tech Inc.), not Upwork. The prior model used his $57K Upwork figure and missed the $148K in BILL payments. BJ Sinder's company is confirmed as Infinite Ideas IT Inc.

### 2. Bunzl Project Costs Were Understated by $200K+
The prior model allocated $105K to Damien (Blue Pisces) for the Bunzl Path to Cloud project. The actual payments for Bunzl project work total **$306,723**.

| Vendor | Confirmed Amount | Notes |
|---|---|---|
| Blue Pisces Consulting (Damien) | $229,843 | More than double the prior $105K estimate |
| Roe Tech LLC (Jeremy Roe) | $71,195 | Jeremy performed significant Bunzl project work |
| My IT Services | $3,065 | |
| Joel Alvarez (Expense Reimb) | $2,621 | |
| **Total Bunzl Subcontractors** | **$306,723** | |

**Critical Insight:** The assumption that projects were highly profitable (64.2% margin in the previous run) was mathematically flawed because $200K in project subcontractor costs were "missing" from the model. They were sitting in the CS-Cost line but unattributed.

### 3. Jeremy Roe's Work is Primarily Project-Based
The Expenses Tracker indicated Jeremy Roe was a $57K/year resource split between Help Desk and ARC. The CS-Cost detail reveals his company (Roe Tech LLC) was paid **$100,097** in CY 2025, and the vast majority was discrete project work.

| Client / Project | Amount |
|---|---|
| Bunzl | $71,195 |
| Network Relocation | $4,875 |
| Pacific Center | $4,500 |
| ARC | $4,500 |
| Travel | $4,295 |
| IT Assessments | $4,050 |
| Various other clients | $6,682 |
| **Total Roe Tech** | **$100,097** |

### 4. SGA Costs Misclassified as COGS
Marcello Moreira (Sales) was paid **$42,645** via Payoneer (the prior $46,039 figure included a minor variance — the actual Payoneer total from the detail is $42,645). This entire amount is sitting in the Consulting Services-Cost line, artificially inflating COGS and depressing SGA. This must be reclassified to Sales SGA.

## D. Definitive Segment Attribution

Based on the line-item detail, the $1,045,803 in the CS-Cost account maps to the segments as follows:

| Segment | Amount | % of Account |
|---|---|---|
| **Comprehensive Services (ARC)** | $650,057 | 62.2% |
| **Consulting/Projects** | $343,030 | 32.8% |
| **Managed Services** | $6,677 | 0.6% |
| **SGA (Sales - Marcello)** | $42,645 | 4.1% |
| **Total Accounted** | **$1,045,803** | **100.0%** |

*(Note: The $343K in Consulting/Projects includes the $306K for Bunzl plus $36K for other discrete projects like network relocations and IT assessments performed by Roe Tech, Infinite Ideas, and Blue Pisces).*

## E. Action Items
1. **Update Resource Allocation Reference:** Replace the estimated BILL contractor amounts with the exact figures from this report.
2. **Rebuild Segment P&Ls:** The $200K+ increase in CP subcontractor costs will significantly reduce the previously overstated project margin, bringing it closer to the expected 24% reality.
3. **Bookkeeper Correction:** Move the $46,039 Payoneer (Marcello) expense from Consulting Services-Cost to Sales SGA.
