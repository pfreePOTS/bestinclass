# PulseOne Strategic Audit: Corrected Findings and Utilization Data Assessment

**Objective:**
Re-evaluate PulseOne’s financial performance against the Service Leadership Best in Class (BIC) framework, incorporating the confirmed time allocations for senior leaders (Laura Walsh, Steve Calkins, Jim Froio) and addressing the availability of technician utilization data.

**Evidence Reviewed:**
- Group LLC and PulseOne LLC historical P&Ls (2022–2024)
- 2025 POTS P&L and Balance Sheet
- `ExpensesTrackingMASTER2023.xlsx` and `PayoneerReportingSheet52322.xlsx`
- Confirmed senior leader time splits (Walsh: 20% Sales / 80% Svc Ldr; Calkins: 100% Svc Ldr; Froio: 40% Billable / 40% Int IT / 20% Admin)

---

## 1. The Impact of the Corrected Senior Leader Allocations

Removing the senior leadership overhead from the direct delivery cost pool has a profound impact on the gross margin picture. When Walsh, Calkins, and the non-billable portions of Froio are correctly classified as SG&A rather than COGS, the margins improve significantly, though Consulting remains a major problem area.

### Revised Service Line Margins vs BIC Target
| Service Line | Previous Estimate (All in COGS) | **Corrected Margin** | BIC Target | Status |
|---|---|---|---|---|
| **Managed Services** | 48.7% | **52.0%** | 48-52% | **AT TARGET** |
| **Consulting** | 7.8% | **24.2%** | 48-52% | **BELOW** |
| **Product (HW+SW)** | 11.9% | **11.9%** | 24-27% | **BELOW** |
| **Blended Total** | 28.6% | **36.0%** | 44.0%+ | **BELOW** |

![Corrected Margins](chart_final_margins.png)

### Key Takeaways from the Correction
1. **Managed Services is highly efficient.** At 52.0% gross margin, the Help Desk team is operating at the absolute top end of the Service Leadership BIC target range. This confirms that the core recurring business model is structurally sound.
2. **Consulting is still severely underperforming.** While removing the senior leadership overhead improved the consulting margin from 7.8% to 24.2%, it is still operating at half the profitability it should be (BIC target: 48-52%).
3. **SG&A Overhead is higher than previously thought.** With the senior leaders correctly classified as overhead, SG&A now consumes 88.3% of gross margin dollars (BIC target: 58.0%). The business is top-heavy relative to its gross margin generation.

![SG&A Breakdown](chart_final_sga.png)

---

## 2. Utilization Data Assessment

You asked: *"Do you have enough information to gauge utilization rates for technicians?"*

**The short answer is no.** 

None of the uploaded financial documents, P&Ls, or expense tracking spreadsheets contain the operational data required to calculate actual technician utilization rates.

### What We Have
We have the **denominator** (cost and available hours). The `ExpensesTrackingMASTER2023.xlsx` tells us the headcount, the hourly rate, and the expected weekly hours (usually 40) for each technician.

### What We Are Missing
We do not have the **numerator** (billable hours). To gauge whether the Help Desk and Consulting teams are truly healthy from an operational standpoint, we must know how many of those 40 hours per week are actually being logged against client agreements or billed to projects.

### The Critical Data Gap
Service Leadership defines Best in Class technician utilization as **65% to 75% billable**. 

Because we know Managed Services is generating a 52.0% gross margin, we can *infer* that the Help Desk technicians (Dare, George, etc.) must be operating at a reasonably high utilization rate, or the margin would be lower. 

However, because Consulting is only generating a 24.2% gross margin, we can infer that either:
1. The subcontractors (Basim, David, Blue Pisces) are logging hours that are not being billed to clients.
2. The W2 consulting staff are sitting idle (low utilization).
3. Projects are severely underpriced (fixed fee projects where hours overrun the budget).

### Required ConnectWise Follow-Up

To definitively answer the utilization question and solve the Consulting margin problem, please retrieve the following from the ConnectWise AI interface:

**1. Technician Utilization Report**
> "Pull a technician utilization report for the last 6 months. What is the billable utilization percentage for each technician in the Help Desk and Services departments?"

**2. Project Profitability by Subcontractor**
> "Run a project profitability report for the last 6 months. For projects involving Basim Mashni, David Fredrick, or Blue Pisces, what was the ratio of subcontractor cost to billed revenue?"

**3. Agreement vs. Project Hours**
> "What percentage of total logged technician hours in the last 6 months were applied to Managed Services agreements versus Consulting projects?"

Without this ConnectWise data, the financial model shows *where* the margin is leaking (Consulting), but cannot definitively prove *why* (utilization vs. pricing).
