# PulseOne Audit: Margin Drivers, Project Profitability, and Technician Utilization
*(Revised based on Paul Freeman Annotations — April 29, 2026)*

**Date:** April 29, 2026  
**Prepared by:** Manus (PulseOne Strategic Audit Assistant)  

---

## A. Objective
To address four specific operational questions raised by Services Management regarding technician utilization, project profitability, software COGS (including Barracuda), and Help Desk staffing levels. This revised analysis incorporates Paul Freeman's April 29, 2026 corrections to the Upwork contractor allocations, providing a definitive, evidence-based assessment against Service Leadership Best in Class (BiC) standards.

## B. Evidence Reviewed
- `2025ticketsbymember.pdf` (CY 2025 aggregate ticket data by member)
- `2025ticketinfo.pdf` (Single-day snapshot of ticket flow on April 28, 2026)
- `PulseOne_Audit_Margin_Drivers,_Project_Profitability,_and_Technician_Utilization.pdf` (Annotated with Paul Freeman's corrections)
- `PulseOne_Definitive_PL_Evaluation_2025.md` (Authoritative financial baseline)
- `Audit_Project_Profitability.md` (QuickBase project data vs. W-2 labor subsidy)

---

## 1. Technician Utilization: Merging Ticket Data with Scheduled Hours

The ticket data reveals a **massive utilization gap**. The team was scheduled for ~16,700 hours in CY 2025 but only logged **6,128 hours** in ConnectWise (36.7% logging rate). The offshore team carried the bulk of the ticket volume efficiently, while the two most expensive Upwork contractors were utilized differently than their "Help Desk" titles implied.

**Key Disparities by Technician (Revised):**
*   **Blain Mulligan:** Highly utilized. He logged 1,957 hours against 1,965 scheduled hours (nearly 100% utilization) and resolved 1,009 tickets. 
*   **The Offshore Core:** George Oracion (1,129 logged / 1,941 scheduled) and Omar Avalos (1,225 logged / 1,941 scheduled) are carrying the bulk of the ticket volume, resolving 1,672 and 1,007 tickets respectively. Per Paul Freeman, Omar was 100% Help Desk in 2025 but moved to Projects in 2026.
*   **Dare Olusanjo:** Confirmed by Paul as 100% Help Desk. He logged 300 hours and resolved 650 tickets. At his $48K cost, he is highly efficient at ~$74/ticket.
*   **Vincent Williams:** Paul clarified Vincent was actually **80% Projects / 20% Help Desk**, specifically handling Barracuda implementations. His effective Help Desk cost is ~$21K (yielding a ~$100/ticket cost for his 210 HD tickets). Paul also noted margin compression: Vincent was scheduled at $95/hr but only billed at $65/hr.
*   **Matthew Barnett:** Paul clarified Matt handles **all ticket escalations** and is allocated **25% to Projects**. His high cost-per-ticket ($364 for his HD portion) is driven by complex, multi-hour server troubleshooting tickets rather than volume Help Desk work.

**Conclusion:** The Help Desk is not overstaffed in total headcount, but the *allocation* of that headcount is highly stratified. The offshore team (George, Omar, Dare) handles the volume efficiently, while expensive domestic contractors (Vincent, Matthew) handle escalations and projects.

---

## 2. The Project Profitability Argument: Proving the Overspend

Services Management argues that projects are profitable because they do not track internal tech time against them. This is the definition of the "Invisible Subsidy." By failing to track internal time, the project P&L looks healthy, but the overall company P&L bleeds margin.

**The Evidence Against Project Profitability (Strengthened by Paul's Notes):**
The QuickBase data shows 61 "true" projects (excluding ARC staff augmentation) generated $690,839 in revenue and consumed $365,526 in out-of-pocket subcontractor invoices. This yields a "cash margin" of 47.1%. This is what Services Management sees.

However, the resource allocation model proves that internal labor is heavily utilized for projects. With Paul's corrections, the "Invisible Subsidy" is even larger than previously estimated:

1.  **W-2 Labor Subsidy:** $244,333 (Fully loaded cost of Kaitlin, Laura, James, Steve, and Hagen's project time)
2.  **Upwork Labor Subsidy:** $104,640 (Vincent's 80% + Matt's 25% allocation)
3.  **Total Invisible Subsidy:** **$348,973** (an increase of $55K from prior estimates)

When you apply this $349K internal labor cost to the $690K in project revenue, the true fully-loaded gross margin collapses from 47.1% down to **-3.4% (a net loss)**. 

![Revised Invisible Subsidy](../chart_revised_subsidy.png)

**Conclusion:** We have definitive evidence that projects are not profitable. The 47% margin Services Management sees is an illusion created by borrowing $349K of free labor from the general payroll. If that labor had been properly quoted and billed to the client, PulseOne would have captured an additional ~$350K in gross profit. The failure to track internal time is exactly what caused the overspending.

---

## 3. Software COGS Profitability and Barracuda Overbilling

The assertion that the adjusted Software COGS shows a profit is **correct**, but it comes with critical caveats regarding vendor concentration and billing pass-throughs.

**The Revenue Mapping Reality:**
The QuickBooks P&L showed a -9.4% margin on Standalone Software Resale. However, the ConnectWise Cost/Sell report proves this is a revenue mapping error. The CW report shows 6,704 software transactions generating $2.97M in revenue against $949K in cost, yielding a healthy **68.1% gross margin** at the transaction level. The revenue is simply being booked to Managed Services in QuickBooks rather than the Software Resale line.

**The Barracuda and Adobe Problems:**
While the aggregate margin is 68%, specific vendors are destroying value:
*   **Adobe:** Cost $126,961 against $132,625 revenue (a **4.3% margin**). This is heavily concentrated in the Bunzl client. PulseOne is acting as a pass-through entity for Bunzl's Adobe licensing and making almost zero margin for the effort.
*   **Barracuda:** The transaction data shows 105 specific invoice lines where cost exceeded price, resulting in a direct loss. Furthermore, Barracuda costs escalated by 87% throughout 2025 (reaching an $89K annualized run rate by December). There is no evidence in the P&L that this cost increase was passed through to clients. 
*   **Vincent's Barracuda Projects:** Paul noted Vincent handled all Barracuda projects in 2025 (costing ~$84K). If these projects were absorbed into Managed Services agreements rather than billed separately at his $65/hr rate, PulseOne lost an additional $84K in uncaptured margin on Barracuda implementations alone.

**Conclusion:** The software business as a whole is profitable, but PulseOne is leaking tens of thousands of dollars by failing to enforce a minimum 24% BiC margin floor on Microsoft and Adobe, and by absorbing Barracuda cost increases rather than passing them through to the client.

---

## 4. Help Desk Overstaffing vs. Project Subsidization

Are Help Desk resources underutilized and subsidizing projects? The evidence suggests **yes**.

**The Ticket Flow Reality:**
The `2025ticketinfo.pdf` snapshot from April 28, 2026, shows 113 tickets opened that day. Of those, only 3 (2.7%) were assigned to the "Internal Projects Team." The vast majority (97%) were Help Desk, NOC, or Dispatch. This confirms that the primary operational volume is Help Desk support.

**The Subsidization Dynamic:**
Because the Help Desk volume is handled so efficiently by the offshore team (George, Omar, Dare), it creates excess capacity among the domestic staff. 

When a project is sold without enough margin to hire a dedicated subcontractor, Services Management pulls from this domestic excess capacity (e.g., Steve Calkins, James Froio, Hagen McDonell, Vincent Williams, Matt Barnett) to deliver the project. Because their salaries/retainers are already paid by the Help Desk budget, the project looks profitable.

**Conclusion:** PulseOne does not necessarily have too many Help Desk resources; it has the *wrong mix* of resources. The company is paying premium rates for domestic staff while relying on them to quietly deliver underpriced projects. 

## Recommended Actions

1.  **Mandate Time Tracking:** The "Invisible Subsidy" argument ends the day W-2 staff and contractors are required to log their time against specific project boards in ConnectWise.
2.  **Reprice Projects:** No project quote should be approved unless it includes the fully loaded hourly cost of internal W-2 labor and Upwork project specialists (like Vincent and Matt).
3.  **Audit Barracuda Project Billing:** Determine if Vincent's $84K in Barracuda project work was billed separately to clients or absorbed into existing agreements. If absorbed, this is a massive source of margin leakage.
4.  **Pass Through Barracuda Costs:** Immediately audit all clients with Barracuda licensing to ensure the 87% cost escalation has been reflected in their monthly billing.
 billing.
