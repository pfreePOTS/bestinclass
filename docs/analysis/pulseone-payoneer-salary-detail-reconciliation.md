# PulseOne Payoneer & Salary Detail Reconciliation

**Date:** May 4, 2026
**Version:** 1.0
**Status:** FINDINGS DOCUMENTED — Identities Confirmed, Segment Allocation Pending for 2 Resources
**Prepared by:** Manus (PulseOne BiC Audit)
**Confirmed by:** Paul Freeman (CMO / Partner) — verbal, May 4, 2026

---

## A. Objective

Reconcile Payoneer contractor payments against the QuickBooks Salary Detail check register to identify previously unnamed contractors, confirm payment amounts, and validate the P&L model's Payoneer assumptions.

## B. Evidence Reviewed

- **2025PulseOneSalaryDetail.xlsx** — QB check register for the "Salary Expense" GL line ($1,441,010 total)
- P&L model build script (v7.1) — Payoneer total of $194,687 across 5 named contractors
- Resource Allocation Reference (v4.5 → updated to v4.6)
- Paul Freeman verbal confirmations (May 4, 2026)

---

## C. QB Salary Expense Structure ($1,441,010)

The Salary Detail spreadsheet reveals three sub-sections within the QB "Salary Expense" line:

| Section | QB Total | Description |
|---|---|---|
| 401K Employee Contribution | $39,862 | Employee 401K deductions |
| Upwork Outsourced Labor | $323,971 | All Upwork contractor payments (single recurring payee) |
| Salary Expense - Other | $1,077,177 | W-2 net checks + Payoneer + direct contractors |
| **Total Salary Expense** | **$1,441,010** | Matches QB exactly |

---

## D. Salary Expense - Other Composition ($1,077,177)

All entries in this section are individual disbursements. The section total equals the sum of all transaction rows (confirmed: $1,077,176.84).

### W-2 Employees (Net Pay — 24 individuals)

| Employee | Net Pay (26 checks) | Notes |
|---|---|---|
| Stephen Calkins | $114,102 | Gross: $148,960 (23.4% effective deduction rate) |
| James Froio | $83,944 | Gross: $112,788 (25.6%) |
| Laura Walsh | $78,140 | Gross: $108,186 (27.8%) |
| Chad Wiggins | $60,528 | Gross: $95,000 (est.) |
| Kaitlin Harris | $57,670 | Gross: $79,760 (27.7%) |
| Roe Tech LLC (Jeremy Roe) | $54,465 | See contractor section |
| Eric Anzalone | $53,878 | Gross: $76,718 |
| Hagen McDonell | $39,523 | Gross: $51,611 (23.4%) |
| Nicole Goodwin | $37,350 | |
| Kyle Carey | $33,780 | |
| Marcello Rocha Moreira | $25,974 | Partial Payoneer — see below |
| Joel Alvarez | $21,231 | |
| Aimee Brock | $19,507 | |
| Julia Morte | $17,244 | |
| Emily Wolf | $16,574 | |
| Alexandria Calkins | $14,679 | |
| Breanna Copeland | $10,060 | Terminated 8/1/2025 |
| Heather Kohler | $9,850 | Terminated 2/24/2025 |
| Jamie Davin | $8,270 | Terminated 2/27/2025 |
| Juliet Simpson | $8,247 | Terminated 2/24/2025 |
| Emily Acker | $7,621 | |
| Dana Rankin | $7,139 | Terminated 1/29/2025 |
| Andrea Carcamo | $6,659 | |
| Marcy Brooke Chandler | $6,590 | |
| Ashley Holmes | $661 | Terminated 2/27/2025 |
| Debby Brooke | $91 | Terminated 11/12/2025 |
| **W-2 Subtotal** | **~$713,338** | Net pay only |

### Contractors in Salary Expense - Other

| Payee | Amount | Payments | Identity (Confirmed May 4, 2026) |
|---|---|---|---|
| **My IT Services** | **$155,980** | 48 | **AJ + Blaine** — two help desk technicians billing together. 100% MS. |
| **Payoneer** | **$114,425** | 63 | Mixed: Daniel (~$63K), Badar (~$38K), Peal Miah (partial), others |
| **Roe Tech LLC** | **$54,465** | 30 | **Jeremy Roe + Brendan Roe** (son). Already in BILL/CS-Cost ($100,097). |
| **Marcello Rocha Moreira** | **$25,974** | 16 | Same Marcello — partial Payoneer coded to Salary. Rest in CS-Cost. |
| **Infinite Ideas IT Inc** | **$6,400** | 1 | BJ Sinder — already in BILL ($132,390). |
| **Blue Pisces Consulting** | **$1,620** | 1 | Ruben Cortez entity — already in BILL ($193,246). |
| **Tracy Freeman** | **$1,860** | 31 | POC/Non-Operating |
| **Contractor Subtotal** | **~$360,724** | | |

### Other (No Payee)

| Type | Amount | Payments | Description |
|---|---|---|---|
| Child support garnishments | $3,115 | 28 | Court-ordered deductions paid to agency |

---

## E. Payoneer Payment Detail ($114,425 in Salary)

### Payment Band Analysis

The 63 Payoneer entries break into identifiable clusters:

| Band | Payments | Total | Avg/Payment | Annualized | **Identity** |
|---|---|---|---|---|---|
| $2,020–$2,101 | 31 | $63,479 | $2,048 | ~$53K | **Daniel** |
| $1,616–$1,838 | 23 | $38,471 | $1,673 | ~$43K | **Badar** |
| Tagged "Badar - Marketing" | 3 | $3,414 | $1,138 | — | **Badar** (marketing work) |
| $1,893–$1,939 | 3 | $5,752 | $1,917 | — | Likely Badar (variable hours) |
| Other/small | 3 | $3,310 | — | — | Peal Miah or misc |

### Timeline Pattern

- **Jan–Feb 2025:** 1 payment per period (Daniel only, ~$2,020)
- **Mar 2025 onward:** 2 payments per period (Daniel + Badar join)
- **Aug 28, 2025:** Rate increase for Daniel ($2,020 → $2,101)
- **Sep 2025 onward:** 3 payments per period (third contractor added — possibly rate change or new person)

---

## F. Reconciliation: Model vs. Salary Detail

### Payoneer Total Reconciliation

| Source | Model Amount | In Salary Detail | In CS-Cost | Gap |
|---|---|---|---|---|
| Marcello Moreira | $42,645 | $25,974 | ~$16,671 | $0 (split coding) |
| George Oracion | $43,020 | — | — | Coded elsewhere in QB |
| Dare Olusanjo | $50,175 | — | — | Coded elsewhere in QB |
| Daniyal Arif | $52,997 | — | — | Coded elsewhere in QB |
| Peal Miah | $5,850 | ~$3,310 (est.) | — | Partial |
| **Daniel** | Not in model | $63,479 | — | **NEW — needs model inclusion** |
| **Badar** | $30,300 (model) | $41,885 actual | — | **+$11,585 vs model** |
| **TOTAL** | $194,687 | $114,425 | — | See notes |

### Key Findings

1. **George Oracion ($43,020) and Dare Olusanjo ($50,175)** are NOT in the Salary Detail. They are likely coded to a different QB expense line (possibly "Computer and Internet Expenses" or paid via a different payment method that QB categorizes separately).

2. **Daniyal Arif ($52,997)** is also absent from the Salary Detail, suggesting his Payoneer payments are coded to a non-Salary QB line.

3. **Daniel (~$63,479)** was previously unidentified in the model. His payments appear as the $2,020–$2,101 band. He is a service delivery resource — segment allocation (MS vs Projects) pending owner confirmation.

4. **Badar (~$41,885 actual vs $30,300 model)** was previously classified as 100% RepScheduler/Non-Op. The salary detail reveals he is primarily a service delivery resource with only $3,414 tagged as marketing. The model understated his cost by ~$11,585 and misallocated his segment.

5. **AJ + Blaine / "My IT Services" ($155,980)** — not Payoneer, but a direct contractor payee in the Salary line. Both are help desk resources, 100% MS. Already captured in the model's contractor pool but not previously identified by name.

6. **Roe Tech ($54,465 in Salary)** = Jeremy Roe + Brendan Roe. This is a subset of the $100,097 total in BILL/CS-Cost. The same entity is paid through two QB channels — no double-counting in the model.

---

## G. Model Impact Assessment

### Does This Change the P&L Model Totals?

**No.** The QB total expense ($4,950,980) and net income ($217,774) remain unchanged. The Salary Expense line ($1,441,010) is already fully captured in the model. This reconciliation provides **identity and allocation clarity**, not new dollars.

### What DOES Change

| Item | Previous | Corrected | Impact |
|---|---|---|---|
| Badar allocation | $30,300 / 100% Non-Op | ~$41,885 / primarily Service Delivery | Shifts ~$38K from Non-Op to COGS (MS or Projects). Improves operating income by ~$38K but increases COGS. |
| Daniel | Not identified | ~$55K+ / Service Delivery | Already in model as part of Payoneer pool. Now named. |
| My IT Services | Not identified by name | AJ + Blaine / $156K / 100% MS | Already in model. Now named. |

### Badar Reallocation Impact on P&L

If Badar's ~$38,471 service delivery portion is moved from Non-Op to MS COGS:
- Non-Op expenses decrease by ~$38K → Net Income increases by ~$38K
- MS COGS increases by ~$38K → MS Gross Margin decreases slightly
- **Net effect:** Operating income improves; MS margin drops from 48.4% to ~46.3%

**However:** This requires confirming whether the model currently has Badar's $30,300 in Non-Op (it does — line 142-143 of build script). The correction would be:
- Remove $30,300 from Non-Op
- Add ~$41,885 to MS (or split MS/Projects per owner direction)
- Net model expense change: +$11,585 (increases total identified expenses)

---

## H. Open Items Requiring Owner Confirmation

1. **Daniel's segment allocation:** 100% MS, 100% Projects, or a split?
2. **Badar's service delivery segment:** 100% MS, 100% Projects, or a split?
3. **Badar's total:** Is $41,885 (from salary detail) the correct annual total, or are there additional Payoneer payments coded elsewhere?
4. **George, Dare, and Daniyal:** Where are their Payoneer payments coded in QB? (Not in Salary Expense — possibly C&I or another line.)

---

## I. Relationship to Other Documents

This document updates:
- **pulseone-resource-allocation-reference.md** → v4.6 (updated same date)
- **PulseOne_Definitive_PL_Evaluation_2025.md** → v7.2 data integrity note added
- **build_pl_v7_corrected.py** → Badar line needs updating (pending segment confirmation)

This document does NOT change:
- Total QB expenses ($4,950,980)
- Total revenue ($5,168,754)
- Net income ($217,774)
- The build script's output totals (pending Badar reallocation)
