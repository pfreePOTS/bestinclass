# PulseOne Strategic Audit: Technician Utilization Analysis

**Objective:**
Analyze the CY 2025 ConnectWise technician utilization data for the Help Desk and ITMS boards to determine the health, efficiency, and profitability of the Managed Services delivery team relative to Service Leadership Best in Class (BIC) benchmarks.

**Evidence Reviewed:**
- CY 2025 Technician Utilization Report (Help Desk & ITMS Boards)
- PulseOne 2025 POTS P&L (for Managed Services revenue)
- `ExpensesTrackingMASTER2023.xlsx` (for technician burdened costs)
- Service Leadership BIC benchmarks [1]

---

## 1. Executive Summary: The Managed Services Context

The ConnectWise utilization report shows a **23.0% billable recovery rate** (hours billed divided by actual hours logged). At first glance, this appears disastrous compared to the Service Leadership BIC target of 70% utilization. 

However, **this is a classic data trap in Managed Services.**

In a mature Managed Services Provider (MSP), technicians spend the vast majority of their time working on tickets that are covered by flat-fee monthly agreements. This time is "logged" but not separately "billed" because the client has already paid the monthly fee. The 23% recovery rate represents the out-of-scope Time & Materials (T&M) work, project work, or break/fix work billed *on top* of the agreements.

When we combine the T&M revenue with the fixed Agreement revenue, **the Help Desk team is operating at an exceptional level of efficiency.**

### Key Financial Metric: Multiple of Labor (MoL)
Service Leadership measures delivery efficiency using the Multiple of Labor (Revenue divided by Delivery Labor Cost). The BIC target is 2.80x.

- **Total Help Desk / ITMS Team Cost (Annual):** ~$505,608
- **T&M Billed Revenue (from CW Report):** $171,150
- **Managed Services Agreement Revenue (from P&L):** $2,563,441
- **Total Revenue Supported by Team:** $2,734,591
- **True Multiple of Labor:** **5.41x**

At 5.41x, the Help Desk team is generating nearly double the BIC target (2.80x) for revenue per dollar of labor cost. This perfectly aligns with our previous finding that the Managed Services Gross Margin is 52.0% (at the top end of the BIC range).

![Utilization and MoL](chart_utilization.png)

---

## 2. Detailed Findings from the Utilization Data

While the overall financial performance of the team is excellent, the ConnectWise data reveals several operational patterns that require leadership attention.

### Finding 1: Massive Volume Discrepancy Between Boards
The Help Desk board dominates the workload. Across all technicians, Help Desk tickets and hours are 10–15x higher than ITMS tickets. 
- **Help Desk:** 4,374 tickets / 4,743 hours logged
- **ITMS:** 241 tickets / 221 hours logged
- *Action:* Ensure that the ITMS board is being used correctly. If ITMS is meant for proactive maintenance or alerts, the low volume suggests either high automation efficiency or a lack of proactive work being logged.

### Finding 2: Consistent 23% Billable Recovery Across the Team
The billable recovery rate (Hours Billed ÷ Actual Hours Logged) is remarkably consistent across the primary technicians:
- George Oracion: 23%
- AJ Mulligan: 23%
- Omar Avalos: 23%
- *Insight:* This consistency suggests a systemic business rule (e.g., a specific client type or ticket type that is always billed) rather than individual technician performance differences. 

### Finding 3: The "Invoice vs. Billed" Leakage
Across the board, "Invoice Hours" are consistently higher than "Hours Billed." 
- Total Invoice Hours: 1,248
- Total Hours Billed: 1,141
- *Insight:* There is an 8.5% leakage between what technicians mark to be invoiced and what is actually billed to the client. At $150/hr, this represents **$16,050 in lost T&M revenue**. This usually happens when an account manager or service manager writes down the time before the invoice goes out because it took "too long."

![Hours Breakdown](chart_hours_breakdown.png)

---

## 3. The Remaining Blind Spot

The utilization report confirms the T&M billing, but it **does not show total utilization**. We know the team logged 4,964 actual hours. But based on headcount, the team has roughly 13,520 *available* hours per year.

Where are the other 8,500 hours?
1. Are they logged against different boards not included in this report (e.g., Projects)?
2. Are they unlogged (idle time, training, internal meetings)?
3. Are the offshore/contractor hours (Payoneer, BILL, Upwork) not fully captured in ConnectWise?

Because the Multiple of Labor is so high (5.41x), the business is highly profitable even if there is idle time. However, to optimize staffing, you need to know exactly where those 8,500 hours are going.

## 4. Recommended Actions

1. **Investigate the 8.5% Billing Leakage:** Review the ConnectWise invoicing process to understand why 107 hours marked for invoicing were written off or not billed. 
2. **Audit Total Logged Hours:** Pull a report showing *all* logged hours across *all* boards for these technicians to ensure time entry compliance. If technicians are only logging 4,964 hours out of 13,520 available, time entry discipline is broken.
3. **Shift Focus to Consulting:** This data confirms the Help Desk is highly efficient and profitable. The existential threat to PulseOne's EBITDA remains the Consulting/Projects division (24.2% GM). You must run this exact same utilization and profitability exercise for the Project boards and the senior subcontractors (Basim, David, Blue Pisces).

---
### References
[1] Service Leadership Index® Annual Profitability Report and First Principles (Public Executive Summaries, 2024-2025).
