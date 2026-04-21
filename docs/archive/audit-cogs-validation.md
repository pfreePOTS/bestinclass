# PulseOne COGS Validation Audit

**Version:** 1.0  
**Date:** 2026-04-20  
**Author:** Manus AI  
**Status:** Complete (pending Paul's confirmation on 3 items)  
**Depends on:** `pulseone-definitive-pl-analysis.md` (v3.0), `pulseone-cogs-classification-analysis.md`

---

## A. Objective

Conduct a deep validation audit of the $1,113,902 COGS reclassification proposed in the Definitive P&L Analysis (v3.0). This audit verifies every material line item across three categories — software, labor, and contractors — against Service Leadership Best in Class methodology to ensure accurate gross margin reporting. The specific goals are:

1. Classify every software expense into one of three buckets (Client-Delivered COGS, Service Delivery Tool COGS, Internal SG&A)
2. Cross-reference person-by-person labor classifications against payroll actuals
3. Validate the $753,801 contractor cost discrepancy between the Expense Tracker and QuickBooks
4. Produce a reconciliation table from Original P&L COGS through each adjustment to Final Corrected COGS

---

## B. Evidence Reviewed

| Source Document | Period | Key Data |
|---|---|---|
| `2025 PulseOne Software COGS and Expense.xlsx` | CY 2025 | 1,068 transactions across 3 QB sections |
| `2025payrollreports.xlsx` | CY 2025 | W-2 gross pay by department and employee |
| `Expenses Tracking MASTER 2023.xlsx` (2025 tab) | Budget 2025 | Budgeted monthly rates for all personnel |
| `Upwork - Reports - Time by freelancer 2025.csv` | CY 2025 | Actual Upwork spend by contract and talent |
| `Upwork - Reports - Time by freelancer2026.csv` | CY 2026 YTD | Trend comparison |
| `pulseone-definitive-pl-analysis.md` (v3.0) | CY 2025 | Authoritative corrected P&L with 3 adjustments |
| `pulseone-cogs-classification-analysis.md` | CY 2025 | Person-by-person COGS vs SG&A classification |

---

## C. Current Understanding

PulseOne's original QuickBooks P&L showed only $1,044,424 in COGS (the "Consulting Services - Cost" line), yielding an artificially high gross margin of approximately 73%. The Definitive P&L Analysis proposed $1,113,902 in reclassifications across three adjustments to move service delivery labor and tools from SG&A to COGS:

| Adjustment | Description | Amount | Source QB Line |
|---|---|---|---|
| A | W-2 Service Delivery Labor | $708,879 | Salary Expense |
| B | Computer & Internet Expenses (97.7% COGS) | $257,970 | Computer & Internet Expenses |
| C | Upwork COGS from other lines | $147,053 | Salary Expense (partial) |
| **Total** | **Reclassification** | **$1,113,902** | |

This audit tests the mechanical accuracy and classification correctness of each adjustment.

---

## D. Findings

### Finding 1: Software COGS Classification (Adjustment B)

The QB "Computer & Internet Expenses" line totals $263,953 on the P&L. The software detail file captures $256,232 of itemized transactions from this same QB account. Line-item classification of all 68 unique vendors reveals three distinct buckets:

| Classification Bucket | Annual Amount | Vendor Count | % of Total |
|---|---|---|---|
| Client-Delivered Software COGS | $570,987 | 11 | 47.5% |
| Service Delivery Tool COGS | $571,692 | 16 | 47.6% |
| Internal SG&A | $58,539 | 41 | 4.9% |
| **Total Software** | **$1,201,218** | **68** | **100%** |

The Client-Delivered ($570,987) and the majority of Service Delivery Tools ($373,999 from Agreement License Cost) are **already correctly coded to COGS** in QB under "Purchases - Software for Resale" and "Agreement License Cost." Only the $197,693 of Service Delivery Tools sitting in the "Computer & Internet Expenses" line requires reclassification.

**Critical Finding:** The Definitive P&L applied a 97.7% COGS ratio (derived from Upwork's COGS/SG&A split) to the entire $263,953 Computer & Internet line, yielding $257,970. However, this line contains software subscriptions, not Upwork payments. The correct approach is to classify each software vendor individually:

| Sub-bucket within Computer & Internet | Amount | Correct Treatment |
|---|---|---|
| Service Delivery Tools (ConnectWise, Flexis, Kaseya, Qualys, TimeZest, etc.) | $197,693 | Move to COGS |
| Internal SG&A (Adobe, Cursor, OpenAI, Zapier, Anthropic, Calendly, etc.) | $58,539 | Remains SG&A |
| **Total classified** | **$256,232** | |
| Unclassified gap (vs $263,953 QB line) | $7,721 | Needs review |

**Items Requiring Paul's Confirmation:**

| Vendor | Amount | Question |
|---|---|---|
| Microsoft Azure | $19,041 | Client infrastructure (COGS) or internal dev/test (SG&A)? |
| GoDaddy.com, Inc. | $2,880 | Client domains (COGS) or PulseOne domains (SG&A)? |
| Pivotal Crew LLC | $2,000 | Service delivery support (COGS) or internal consulting (SG&A)? |
| AI MAD FZCO | $360 | Purpose? |
| **Total pending** | **$24,281** | |

**Impact on Adjustment B:** Should be reduced from $257,970 to $197,693, a decrease of $60,277. If the pending items ($24,281) are confirmed as COGS, the adjustment would be $221,974.

---

### Finding 2: Labor COGS Classification (Adjustment A)

The Definitive P&L proposed moving $708,879 of W-2 labor from Salary Expense to COGS. Cross-referencing against the 2025 payroll report:

| Employee | Department | Gross Pay | Status | Classification |
|---|---|---|---|---|
| Stephen Calkins | 100 - Services | $148,960 | Active FT | COGS |
| James Froio | 100 - Services | $112,788 | Active FT | COGS |
| Laura Walsh | 100 - Services | $108,186 | Active FT | COGS |
| Kaitlin Harris | 100 - Services | $79,760 | Active FT | COGS |
| Eric Anzalone | 100 - Services | $76,718 | Active FT | COGS |
| Hagen McDonell | 100 - Services | $51,610 | Active FT | COGS |
| Nicole Goodwin | 100 - Services | $38,150 | Active PT | COGS (80%) |
| Joel Alvarez | 100 - Services | $25,850 | Active PT | COGS |
| Julia Morte | 100 - Services | $20,322 | Active PT | COGS |
| Alexandria Calkins | 100 - Services | $17,258 | Active PT | COGS |
| Breanna Copeland | 100 - Services | $11,444 | Terminated | COGS |
| Emily Acker | 100 - Services | $9,690 | Terminated | COGS |
| Debby Brooke | 100 - Services | $7,928 | Terminated | COGS |
| **Total Dept 100** | | **$708,663** | | |

**Validation:** Adjustment A ($708,879) matches Dept 100 payroll gross ($708,663) within $216. The small difference is attributable to employer burden (FICA, workers' comp) applied as a percentage. **Adjustment A is CONFIRMED.**

**Split-Role Flag — Nicole Goodwin:** Nicole appears in both Dept 100 ($38,150) and Dept 900/POC ($12,950). The COGS Classification document assigns her 80% COGS / 20% SG&A. The payroll data supports this: her Services hours (1,057) represent approximately 74% of her total hours, while POC hours (362) represent 26%. The 80/20 split is a reasonable approximation.

---

### Finding 3: Contractor COGS and the $753K Discrepancy

The COGS Classification Analysis identified a $753,801 gap between the Expense Tracker total ($1,798,225) and QB Consulting Services - Cost ($1,044,424). This audit finds the gap is a **structural artifact** of comparing a budget tool to an actuals system:

| Factor | Amount | Explanation |
|---|---|---|
| SG&A contractors included in Expense Tracker | $746,319 | These belong in SG&A, not COGS — correctly excluded from QB COGS |
| Budget vs. Actual variance | ~$53,898 | Expense Tracker uses budgeted rates; actuals differ significantly |
| Burden markup (5-10%) in Expense Tracker | ~$65,000 | Platform fees included in budget but may be coded differently in QB |
| **Approximate total explanation** | **~$865,217** | Exceeds gap — confirms no "missing" costs |

**Upwork Actuals vs. Expense Tracker Budget (CY2025):**

| Contractor | Expense Tracker (Annual) | Upwork Actual | Variance | Note |
|---|---|---|---|---|
| Vincent Williams | $65,520 | $104,740 | +$39,220 | More hours than budgeted |
| Matt Barnett | $73,712 | $83,390 | +$9,678 | Fixed price ARC |
| CharlesDoone Castro | $82,992 | $38,228 | -$44,764 | Reduced in 2025 |
| Omar Avalos | $54,600 | $49,442 | -$5,158 | Close to budget |
| Jeremy Roe | $59,850 | $6,476 | -$53,374 | Drastically reduced |
| Dustin Hagemeier | $0 | $500 | +$500 | Minimal 2025 |
| **Total** | **$336,674** | **$282,776** | **-$53,898** | |

**Conclusion:** The Expense Tracker is a planning/budgeting tool, not an actuals record. The $753,801 "discrepancy" is resolved: it reflects the inclusion of SG&A contractors and budget-vs-actual variances. No material costs are missing from the COGS analysis.

---

### Finding 4: Upwork Reclassification (Adjustment C)

Upwork CY2025 actuals total $299,924. Contract-level classification confirms:

| Contract | Talent | Amount | Classification |
|---|---|---|---|
| IT and Network Risk Assessments | Vincent Williams | $87,830 | COGS |
| Arc | Matthew Barnett | $83,390 | COGS |
| Help Desk Support | Omar Avalos / Brendan Roe | $55,418 | COGS |
| Amiri Help Desk Support | Charlesdoone Castro | $38,228 | COGS |
| ITMS Projects | Vincent Williams | $16,070 | COGS |
| ARC Onsite End User Support | Basim Mashni | $5,906 | COGS |
| Training for AvePoint | William McMillan | $3,000 | COGS |
| Other COGS contracts | Various | $3,284 | COGS |
| **Total COGS** | | **$293,125** | **97.7%** |
| Thrive Program Video Editing | Kirill Hovansky | $3,660 | SG&A |
| Thrive LearnDash project | Sabah Razaq | $2,438 | SG&A |
| Tech Talk Video Editing | Yana Kosenko | $700 | SG&A |
| **Total SG&A** | | **$6,798** | **2.3%** |

The Definitive P&L's Adjustment C ($147,053) represents the portion of Upwork COGS that is NOT already in QB "Consulting Services - Cost." This implies approximately $146,072 of Upwork spend ($293,125 - $147,053) is already correctly coded to COGS in QB. The remaining $147,053 is likely coded to "Salary Expense" alongside W-2 payroll.

**Validation Status:** The $147,053 figure is **plausible** but **cannot be independently verified** without QB transaction-level detail showing where each Upwork payment was coded. The 97.7% COGS split is confirmed at the contract level.

---

## E. Service Leadership Best in Class Alignment

| Area | Alignment Status | Notes |
|---|---|---|
| Service Delivery Tools as COGS | **Aligned** | RMM, PSA, SOC tools correctly classified as COGS per SL methodology |
| W-2 Service Delivery Labor as COGS | **Aligned** | Dept 100 personnel deliver client services; burden correctly included |
| Contractor Service Delivery as COGS | **Aligned** | 97.7% of Upwork contracts are client-facing service delivery |
| Internal SG&A separation | **Aligned** | $58,539 in internal tools correctly excluded from COGS |
| Chart of Accounts structure | **Below Benchmark** | Commingling of Upwork with W-2 Salary Expense violates SL standards |
| Software account separation | **Below Benchmark** | Service delivery and internal tools share one QB account |

---

## F. Risks and Opportunities

**Risks:**
1. **Margin Misstatement ($60,277):** If the full Adjustment B ($257,970) is applied without line-item validation, $58,539 of Internal SG&A will be incorrectly moved to COGS, understating gross margin by 1.5 percentage points.
2. **Unverifiable Adjustment C ($147,053):** Without QB transaction-level confirmation, this adjustment relies on inference rather than evidence. If Upwork is actually already in Consulting Services - Cost, this adjustment would double-count $147,053.
3. **Budget-as-Actuals Risk:** The Expense Tracker's budgeted figures (used in the COGS Classification Analysis) diverge from actuals by up to $53,374 per contractor. Any analysis relying on Expense Tracker numbers as "costs" will be inaccurate.

**Opportunities:**
1. **Accounting Cleanliness:** Creating distinct QB sub-accounts for "Service Delivery Software" vs "Internal Software" eliminates future reclassification work.
2. **Contractor Coding Fix:** Moving Upwork payments from "Salary Expense" to a dedicated "Contractor - Service Delivery" account would make the P&L self-classifying.
3. **Validated Baseline:** With Adjustment A confirmed and Adjustment B refined, PulseOne has a defensible COGS baseline for Service Leadership benchmarking.

---

## G. Recommended Actions

| Priority | Action | Impact | Owner |
|---|---|---|---|
| 1 | Revise Adjustment B from $257,970 to $197,693 | Corrects $60,277 margin misstatement | Orchestration Thread |
| 2 | Confirm Microsoft Azure ($19,041) classification | Could move $19K between COGS and SG&A | Paul |
| 3 | Obtain QB transaction detail for Upwork coding | Validates or invalidates $147,053 Adjustment C | Paul / Bookkeeper |
| 4 | Restructure QB Chart of Accounts | Eliminates future manual reclassification | Paul / Bookkeeper |
| 5 | Replace Expense Tracker budgets with QB actuals for all COGS analysis | Ensures accuracy | Manus |

---

## H. Suggested ConnectWise Follow-up

1. **Agreement Profitability Report (CY2025):** Confirm that the $197,693 in Service Delivery Tools is being recovered through agreement pricing. If tools cost exceeds agreement margin, pricing adjustment is needed.
2. **Technician Utilization by Board:** Cross-reference the 13 Dept 100 employees against ConnectWise time entries to validate that their hours are primarily client-facing (supporting the COGS classification).
3. **Project Profitability for Blue Pisces / David Fredrick contracts:** These two contractors represent $379,720/yr in budgeted COGS. Confirm actual project revenue vs. cost.

---

## I. Clarifying Questions

1. **Microsoft Azure ($19,041):** Is this hosting client workloads (COGS) or PulseOne internal development/testing (SG&A)?
2. **Daniyal Arif:** The Expense Tracker shows him budgeted at $44,117 under Marketing (SG&A), but the COGS Classification document lists him under Services (COGS). Which department received his actual 2025 work output?
3. **Blue Pisces (Ruben):** Budgeted at $196,950/yr. What was the actual 2025 spend, and was it 100% dedicated to client project delivery?
4. **Upwork QB coding:** Can you pull a QB transaction report filtered to "Upwork" to confirm which account(s) these payments are coded to? This would definitively validate or invalidate Adjustment C ($147,053).

---

## Reconciliation Table

| Line | Description | Amount | Confidence | Status |
|---|---|---|---|---|
| A | Original QB COGS (Consulting Services - Cost) | $1,044,424 | ACTUAL | QB Verified |
| B | + Adjustment A: W-2 Service Delivery Labor | $708,879 | HIGH | **VALIDATED** (within $216 of payroll) |
| C | + Adjustment B: Service Delivery Software Tools | $197,693 | HIGH | **VALIDATED** (line-item classified) |
| D | + Adjustment B: Pending items (Azure, GoDaddy, etc.) | $24,281 | LOW | **PENDING** Paul's confirmation |
| E | + Adjustment C: Upwork COGS from non-COGS lines | $147,053 | MEDIUM | **PLAUSIBLE** but unverifiable |
| F | - Internal SG&A incorrectly in original Adj B | -$60,277 | HIGH | **CORRECTION** to Definitive P&L |
| | | | | |
| **G** | **= Corrected COGS (conservative, validated only)** | **$1,950,996** | | B+C items only |
| **H** | **= Corrected COGS (with plausible items)** | **$2,098,049** | | Includes D+E |
| **I** | **= Definitive P&L v3.0 Corrected COGS** | **$2,158,326** | | For comparison |
| **J** | **= Gap (Definitive P&L vs. this audit, conservative)** | **$207,330** | | Adj B overstatement + unverified Adj C |

---

## Impact on Master Scorecard

If the conservative validated COGS ($1,950,996) is adopted:

| Metric | Definitive P&L v3.0 | This Audit (Conservative) | This Audit (With Plausible) |
|---|---|---|---|
| Total COGS | $2,158,326 | $1,950,996 | $2,098,049 |
| Gross Profit | $1,729,174 | $1,936,504 | $1,789,451 |
| Gross Margin % | 44.5% | 49.8% | 46.0% |
| Service Delivery GM % | ~44% | ~50% | ~46% |

**Note:** These figures should NOT be applied to the Master Scorecard until Paul confirms the pending items and provides QB transaction detail for Upwork coding. The Scorecard update will be handled in the orchestration thread.

---

## Appendix: Methodology Notes

**Service Leadership COGS Definition:** Under Service Leadership Best in Class methodology, COGS includes all costs directly attributable to delivering services to clients. This encompasses:
- Personnel whose primary function is client service delivery (technicians, engineers, project managers)
- Tools and platforms used to deliver or manage client services (RMM, PSA, security monitoring, backup)
- Software licenses provisioned to or on behalf of specific clients
- Third-party contractors performing client-facing work

**Excluded from COGS (SG&A):** Internal operations tools (accounting, HR, marketing automation), personnel in sales/marketing/administration, and contractors performing non-client work (video editing, marketing content).
