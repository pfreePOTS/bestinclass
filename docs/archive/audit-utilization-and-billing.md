# PulseOne Strategic Audit: Utilization & Billing Efficiency

## A. Objective

The objective of this audit is to quantify billing leakage, evaluate time entry discipline, and measure realization rates across PulseOne's service delivery teams. This document consolidates previous fragmented analyses into a single view of uncaptured revenue and operational friction within the time entry and invoicing processes.

## B. Evidence Reviewed

The findings in this audit are derived from the following sources:
*   ConnectWise Help Desk board volume and time entry logs (CY 2025)
*   ConnectWise ITMS board volume and time entry logs (CY 2025)
*   Invoice realization data (logged vs. billed hours)
*   Service Leadership Best in Class (BiC) Framework Reference [1]
*   PulseOne Definitive P&L Analysis (v3.0)

## C. Current Understanding

PulseOne's Help Desk and ITMS teams operate with a high degree of leverage, achieving a 5.41x Service Multiple of Labor (MoL) against a BiC target of 2.80x [1]. However, this high multiple masks significant operational friction in how time is recorded, approved, and billed. The overall "billable recovery rate" across the service delivery team is currently tracking at 23.0%. While a low billable percentage is expected in a Managed Services model (where most work is covered by flat-fee agreements rather than hourly T&M billing), the absolute volume of unlogged time and written-down invoices indicates structural profit leakage.

## D. Findings

The analysis reveals three distinct areas of billing leakage and capacity mismanagement that collectively represent an estimated $514,951 in uncaptured revenue potential (calculated at a standard $150/hour rate).

### Leakage Area 1: The Write-Down Problem
In CY 2025, technicians logged 1,248 hours that were explicitly marked to be invoiced as T&M work. However, only 1,141 of those hours were actually billed to clients. This represents an 8.5% leakage rate (107 hours) where billable work was performed but written down or zeroed out during the invoicing approval process. This direct leakage destroyed $16,050 in high-margin T&M revenue.

### Leakage Area 2: Unbilled Actual Hours
Technicians logged a total of 4,965 actual hours across the Help Desk and ITMS boards, but only 1,141 of those hours were billed. While the majority of the remaining 3,824 hours were correctly applied against flat-fee Managed Services agreements, the lack of strict billing code audits suggests a portion of this time was out-of-scope work that should have been billed as T&M. A conservative estimate assuming just 20% of these unbilled hours were out-of-scope represents $114,717 in potential recovered revenue.

### Leakage Area 3: Unlogged Available Hours
Based on the FTE capacity of the delivery team, there were roughly 13,520 available working hours in the year. Technicians only logged 4,965 actual hours in ConnectWise, leaving 8,555 hours (63% of total capacity) completely unaccounted for. Without 100% time entry discipline, it is impossible to accurately measure utilization, calculate true agreement profitability, or capture out-of-scope project work.

### Misaligned Senior Labor Allocation
Two senior personnel are logging significant time on lower-tier service boards, distorting the cost of delivery:
*   **Jim Froio:** Logged 660 hours on Help Desk/ITMS boards. His confirmed allocation is 40% billable projects, 40% internal IT, and 20% administrative. His internal IT time is currently being mixed into client-facing boards rather than tracked against an internal overhead ticket.
*   **Laura Walsh:** Logged 301 hours on Help Desk/ITMS boards despite being classified as 80% Service Leadership and 20% Sales. This time should be reclassified as non-billable service management oversight rather than direct delivery labor.

## E. Service Leadership BiC Alignment

| Metric | PulseOne Current | BiC Target | Status |
| :--- | :--- | :--- | :--- |
| Time Entry Discipline | 37% (est. logged capacity) | 100% | **BELOW** |
| Billable Recovery Rate | 23.0% | 65% - 75% | **BELOW** |
| Service Multiple of Labor | 5.41x | 2.80x | **AT TARGET** |
| Managed Services GM | 52.0% | 48.0% - 52.4% | **AT TARGET** |

*Note: The BiC billable recovery target of 70% assumes all time (including agreement-covered time) is logged and tracked. PulseOne's 23.0% rate is artificially low due to the 8,555 unlogged hours.*

## F. Risks and Opportunities

The primary risk is **margin erosion through scope creep**. Without 100% time entry discipline, PulseOne cannot accurately measure how much labor is being consumed by flat-fee agreements. This prevents the company from identifying unprofitable clients or justifying rate increases during contract renewals.

The immediate opportunity is **revenue recovery through strict invoice management**. Stopping the 8.5% write-down leakage requires no new sales or marketing effort; it simply requires enforcing a policy that billable time cannot be zeroed out without partner-level approval.

## G. Recommended Actions

1.  **Stop Invoice Write-Downs:** Implement a strict policy requiring partner approval before any hours marked as billable can be reduced or zeroed out prior to invoicing.
2.  **Enforce 100% Time Entry:** Mandate that all technicians log 100% of their available hours in ConnectWise, including administrative time, training, and internal IT work.
3.  **Create Internal Overhead Tickets:** Establish specific internal ConnectWise tickets for Jim Froio's internal IT work and Laura Walsh's service management oversight to remove this overhead from client-facing profitability metrics.
4.  **Audit Out-of-Scope Work:** Implement a secondary review process for all Help Desk tickets exceeding 4 hours to determine if the work constitutes an out-of-scope project that should be billed separately.

## H. Suggested ConnectWise Follow-Up

To refine this analysis, the following specific data pulls are required from the ConnectWise AI interface:

1.  **Billing Code Audit:** A report of all tickets in CY 2025 marked as billable by the technician but reduced or zeroed out before invoicing, including the name of the approver.
2.  **Agreement Hours Consumption:** A report showing the average monthly hours consumed per client for each active Managed Services agreement in CY 2025.
3.  **Technician Utilization Report:** A report showing the billable utilization percentage for each technician in the Help Desk and Services departments over the last 6 months.

## I. Clarifying Questions

1.  Who currently has the authority to write down or zero out billable hours during the invoicing process?
2.  Is there a formal process for identifying when a Help Desk request crosses the threshold into a billable project?
3.  Are technicians currently required to log 8 hours of time per day, or only time spent actively working on client tickets?

## References

[1] Service Leadership, Inc., "The Financial Value To Large MSPs of Implementing a Reference Architecture," 2016. https://www-cdn.webroot.com/6615/0473/1278/SL_MSP_Report_2017.pdf
