# PulseOne Technician Scheduling and Utilization Audit
**Date:** April 21, 2026
**Status:** DEFINITIVE — Incorporating CY 2025 Schedule Data
**Prepared by:** Manus (PulseOne BIC Audit)

---

## A. Objective
To evaluate PulseOne's technician scheduling, time allocation, and labor efficiency against the Service Leadership Best in Class (BIC) framework. This analysis bridges the previously identified gap between known labor costs and actual operational capacity by cross-referencing the newly provided 2025 Services Team Schedule with existing payroll, Upwork, and ConnectWise ticket data.

## B. Evidence Reviewed
*   `ServicesTeamSchedule2025.xlsx` (New evidence: 9 months of daily shift schedules for all technicians)
*   `PulseOne_Definitive_PL_Analysis.md` (Confirmed W-2 and Upwork contractor costs)
*   `PulseOne_Technician_Efficiency_Audit.md` (CY 2025 ConnectWise ticket volumes by technician)
*   `Service Leadership Best in Class (BIC) Framework Reference.md` (Benchmark standards)

## C. Current Understanding
Prior analysis established that PulseOne's Help Desk (Managed Services) was operating at a highly profitable 52.0% gross margin, while the Consulting/Projects division was severely underperforming at 24.2% [1]. However, we lacked the operational denominator—scheduled hours—to determine if the margin drag was caused by low utilization (technicians sitting idle), poor pricing, or unbilled project hours [2]. The 2025 schedule data provides that denominator, allowing us to calculate true capacity, effective hourly costs, and ticket-handling efficiency.

## D. Findings

### 1. Massive "Ghost Worker" Capacity (The Consulting Margin Drag)
The most critical finding from the schedule data is the identification of approximately 10,000 annualized hours of scheduled technician capacity that produced **zero Help Desk tickets** in 2025. 

Six individuals were scheduled for near full-time hours but do not appear in the ConnectWise ticket data under matching accounts:
*   **David:** 1,984 annualized hours
*   **Blain:** 1,965 annualized hours
*   **BJ Snider:** 1,952 annualized hours
*   **Peal:** 1,077 annualized hours
*   **Jeremy:** 997 annualized hours
*   **Basim:** 2,005 annualized hours (Confirmed Upwork contractor for Arc Client Support)

These "ghost workers" represent massive labor capacity. If they are performing project work, their costs are severely dragging down the Consulting gross margin. If they are performing Help Desk work under shared or generic ConnectWise accounts, it completely obscures individual accountability and efficiency metrics. 

### 2. Jim Froio — Pure Overhead Drag
The schedule confirms that Jim Froio was on extended leave or entirely non-operational for the vast majority of 2025. Across the 9 months of available schedule data, he logged **0 scheduled hours and 194 vacation days**. 

Despite this absence, his $112,788 W-2 salary remained on the P&L. Furthermore, 868 tickets were logged under his ConnectWise account (`jfroio`), suggesting either auto-assignment rules are routing tickets to an absent employee, or other technicians are working under his credentials. This salary represents a pure overhead drag on profitability.

### 3. Extreme Variance in Effective Hourly Cost
By dividing confirmed annual costs by annualized scheduled hours, we reveal massive disparities in what PulseOne pays for labor capacity.

| Technician | Classification | Annualized Hours | Annual Cost | Effective Hourly Cost |
| :--- | :--- | :--- | :--- | :--- |
| **Vincent** | Upwork (Escalations) | 1,100 hrs | $104,740 | **$95.22 / hr** |
| **Matthew** | Upwork (Help Desk) | 1,595 hrs | $83,390 | **$52.29 / hr** |
| **Hagen** | W-2 FT (Help Desk) | 1,579 hrs | $50,597 | **$32.05 / hr** |
| **George** | Contractor (Offshore) | 1,941 hrs | $48,000 | **$24.73 / hr** |
| **Charles Castro** | Upwork (Amiri Dedicated) | 2,074 hrs | $38,228 | **$18.43 / hr** |

Vincent and Matthew are exceptionally expensive resources. Vincent's rate ($95.22/hr) may be justified if he is strictly handling high-level network escalations, but Matthew's effective rate ($52.29/hr) for standard Help Desk support is nearly double that of equivalent W-2 or offshore resources.

![Effective Hourly Cost](../charts/chart_effective_hourly_cost.png)

### 4. Ticket Handling Efficiency
When plotting scheduled hours against actual tickets handled, distinct efficiency tiers emerge among the core Help Desk team.

*   **High Efficiency:** Alex Calkins handled 1,892 tickets on just 572 scheduled hours (3.31 tickets/hour). Emily handled 128 tickets on 89 hours (1.44 tickets/hour). 
*   **Core Offshore Efficiency:** George (Contractor) is the most efficient full-time resource, handling 1,545 tickets across 1,941 scheduled hours (0.80 tickets/hour).
*   **Low Efficiency / Project Mix:** Vincent (170 tickets / 1,100 hrs) and Matthew (157 tickets / 1,595 hrs) show very low ticket volume relative to their scheduled time, further indicating they are either performing non-ticketed project work or are severely underutilized.

![Hours vs Tickets](../charts/chart_hours_vs_tickets.png)

### 5. Section Allocation: Help Desk Dominance
The schedule is divided into three primary sections: Help Desk, Dispatch, and Management Team. 
*   **Help Desk** consumes 83.4% of all scheduled hours (24,241 annualized hours across 17 technicians).
*   **Dispatch** consumes 27.3% of scheduled hours (7,919 annualized hours across 7 technicians, with some overlap).
*   **Management Team** (Laura Walsh, Steve Calkins) are listed on the schedule but log 0 scheduled shift hours, confirming their roles as overhead/leadership rather than direct service delivery.

![Section Allocation](../charts/chart_section_allocation.png)

## E. Service Leadership Best in Class Alignment

| Metric | PulseOne Performance | BIC Target | Alignment |
| :--- | :--- | :--- | :--- |
| **Technician Utilization (Billable %)** | **Unknown** (Schedule tracks presence, not billable time) | 65% to 75% | **Cannot Assess** |
| **Service Multiple of Labor** | **Unknown** (Requires billable hours confirmation) | > 2.8x | **Cannot Assess** |
| **Managed Services Gross Margin** | **52.0%** (From prior P&L analysis) | 48% to 52% | **Aligned** |
| **Project/Consulting Gross Margin** | **24.2%** (From prior P&L analysis) | > 24.6% | **Below Target** |

*Note: While the schedule provides total capacity, it does not distinguish between billable client work, internal admin, or idle time. Therefore, true BIC utilization cannot be calculated without ConnectWise time-entry data.*

## F. Risks and Opportunities

**Risks:**
1.  **The "Ghost Worker" Black Hole:** ~10,000 hours of scheduled time with no corresponding ticket data represents a massive visibility gap. If these resources are performing project work, their unbilled or under-billed time is the root cause of the 24.2% Consulting margin.
2.  **Upwork Premium Rates:** Matthew Barnett ($83K) and Vincent Williams ($104K) are operating at effective hourly rates far above the rest of the team. If their output is standard Help Desk or unbilled project work, they are destroying margin.
3.  **Jim Froio's Salary:** Carrying a $112K salary for an employee with 0 scheduled hours and 194 vacation days is a direct hit to EBITDA. 

**Opportunities:**
1.  **Offshore Leverage:** George and Omar Avalos demonstrate that the offshore contractor model can deliver high ticket volume at highly efficient effective rates ($24/hr). Shifting volume from expensive Upwork contractors to this model would immediately boost margins.
2.  **Accountability Enforcement:** Forcing all "ghost workers" to log time against specific ConnectWise tickets or project phases will immediately illuminate where the Consulting margin is leaking.

## G. Recommended Actions

1.  **Audit the "Ghost Workers":** Immediately determine what David, Blain, BJ Snider, Peal, and Jeremy are doing during their scheduled shifts. If they are doing project work, ensure their time is being billed. If they are doing Help Desk work, ensure they are using their own ConnectWise accounts.
2.  **Evaluate Upwork ROI:** Conduct a strict ROI review of Vincent Williams and Matthew Barnett. Their effective hourly rates ($95/hr and $52/hr) require them to be performing high-value, highly billable work. If they are performing standard support, replace them with offshore contractors.
3.  **Resolve Jim Froio's Status:** Address the $112K salary drag. If he is on permanent leave, the cost should be removed from the operating P&L to reflect true business performance. 
4.  **Investigate Auto-Routing:** Determine why 868 tickets were assigned to Jim Froio's account while he was on extended leave.

## H. Suggested ConnectWise Follow-Up

To definitively solve the utilization and margin puzzle, the following data MUST be retrieved from the ConnectWise AI interface:

1.  **Time Entry by "Ghost Workers":** 
    > *"Run a time entry report for CY 2025 for David, Blain, BJ Snider, Peal, and Jeremy. How many total hours did each log, and what percentage of those hours were billed to clients versus marked as internal/unbillable?"*
2.  **Upwork Contractor Billing:**
    > *"For CY 2025, how many billable hours were logged by Vincent Williams and Matthew Barnett? What was the total revenue billed to clients specifically for their time?"*
3.  **Project Profitability (The Margin Drag):**
    > *"Run a project profitability report for all projects completed in CY 2025. Which specific projects had the lowest gross margin, and which technicians logged the most hours against those unprofitable projects?"*

## References
[1] PulseOne_Corrected_Findings_and_Utilization.md
[2] PulseOne_Billing_Efficiency_Report.md
