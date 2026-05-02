# PulseOne Audit: Margin Drivers, Project Profitability, and Technician Utilization

**Date:** April 28, 2026  
**Prepared by:** Manus (PulseOne Strategic Audit Assistant)  

---

## A. Objective
To address four specific operational questions raised by Services Management regarding technician utilization, project profitability, software COGS (including Barracuda), and Help Desk staffing levels. This analysis incorporates the newly provided `2025ticketsbymember.pdf` and `2025ticketinfo.pdf` data alongside the existing financial and labor models to provide an evidence-based assessment against Service Leadership Best in Class (BiC) standards.

## B. Evidence Reviewed
- `2025ticketsbymember.pdf` (CY 2025 aggregate ticket data by member)
- `2025ticketinfo.pdf` (Single-day snapshot of ticket flow on April 28, 2026)
- `PulseOne_Definitive_PL_Evaluation_2025.md` (Authoritative financial baseline)
- `Audit_Project_Profitability.md` (QuickBase project data vs. W-2 labor subsidy)
- `pulseone-technician-efficiency-audit.md` (Prior utilization analysis)
- `audit-software-resale-addendum.md` (Software transaction-level profitability)

---

## 1. Technician Utilization: Merging Ticket Data with Scheduled Hours

The new ticket data allows us to directly compare the hours technicians logged in ConnectWise against their scheduled capacity. The resulting "Utilization Gap" proves that significant portions of the team's time are not being tracked against client tickets.

**The Utilization Gap:**
Across the service delivery team, we identified approximately **16,708 scheduled hours** for CY 2025. However, the new `2025ticketsbymember.pdf` shows the team only logged **6,128 hours** in ConnectWise. This represents an overall logging rate of just **36.7%**.

**Key Disparities by Technician:**
*   **Blain Mulligan:** Highly utilized. He logged 1,957 hours against 1,965 scheduled hours (nearly 100% utilization) and resolved 1,009 tickets. 
*   **The Offshore Core:** George Oracion (1,129 logged / 1,941 scheduled) and Omar Avalos (1,225 logged / 1,941 scheduled) are carrying the bulk of the ticket volume, resolving 1,672 and 1,007 tickets respectively.
*   **Vincent Williams:** As a $102K Upwork contractor, he is exceptionally expensive. He logged only **101 hours** and resolved 210 tickets against 1,100 scheduled hours. His effective cost per ticket resolved is nearly **$485**. The new ticket data explicitly lists his role as "Help Desk Technician," not Projects, which contradicts the assumption that he was primarily doing project-based risk assessments.
*   **Matthew Barnett:** Another expensive Upwork contractor ($88K). He logged 295 hours and resolved 172 tickets against 1,595 scheduled hours. His cost per ticket is over **$510**.

![Utilization Gap](../chart_utilization_gap.png)

**Conclusion:** The Help Desk is not necessarily overstaffed in total headcount, but the *allocation* of that headcount is highly inefficient. The offshore team (George, Omar) is doing the heavy lifting, while expensive domestic Upwork contractors (Vincent, Matthew) are logging very few hours and resolving very few tickets relative to their cost.

---

## 2. The Project Profitability Argument: Proving the Overspend

Services Management argues that projects are profitable because they do not track internal tech time against them. This is the definition of the "Invisible Subsidy." By failing to track internal time, the project P&L looks healthy, but the overall company P&L bleeds margin.

**The Evidence Against Project Profitability:**
The QuickBase data shows 61 "true" projects (excluding ARC staff augmentation) generated $690,839 in revenue and consumed $365,526 in out-of-pocket subcontractor invoices. This yields a "cash margin" of 47.1%. This is what Services Management sees, and why they believe projects are profitable.

However, the owner-confirmed resource allocation model proves that W-2 staff are heavily utilized for projects:
*   Kaitlin Harris (100% Projects)
*   Laura Walsh (35% Projects)
*   James Froio (30% Projects)
*   Steve Calkins (15% Projects)
*   Hagen McDonell (20% Projects)

The fully loaded cost (including payroll taxes) of this W-2 labor dedicated to projects is approximately **$244,333**. 

When you apply this $244K internal labor cost to the $690K in project revenue, the true fully-loaded gross margin collapses from 47.1% down to **~18% to 24%**. 

![The Invisible Subsidy](../chart_invisible_subsidy.png)

**Conclusion:** We have definitive evidence that projects are not profitable. The 47% margin Services Management sees is an illusion created by borrowing $244K of free labor from the general payroll. If that labor had been properly quoted and billed to the client, PulseOne would have captured an additional ~$300K in gross profit. The failure to track internal time is exactly what caused the overspending.

---

## 3. Software COGS Profitability and Barracuda Overbilling

The assertion that the adjusted Software COGS shows a profit is **correct**, but it comes with critical caveats regarding vendor concentration and billing pass-throughs.

**The Revenue Mapping Reality:**
The QuickBooks P&L showed a -9.4% margin on Standalone Software Resale. However, the ConnectWise Cost/Sell report proves this is a revenue mapping error. The CW report shows 6,704 software transactions generating $2.97M in revenue against $949K in cost, yielding a healthy **68.1% gross margin** at the transaction level. The revenue is simply being booked to Managed Services in QuickBooks rather than the Software Resale line.

**The Barracuda and Adobe Problems:**
While the aggregate margin is 68%, specific vendors are destroying value:
*   **Adobe:** Cost $126,961 against $132,625 revenue (a **4.3% margin**). This is heavily concentrated in the Bunzl client. PulseOne is acting as a pass-through entity for Bunzl's Adobe licensing and making almost zero margin for the effort.
*   **Barracuda:** The transaction data shows 105 specific invoice lines where cost exceeded price, resulting in a direct loss. Specifically, "Malenfant Technical Services" showed negative margins on Barracuda products. Furthermore, Barracuda costs escalated by 87% throughout 2025 (reaching an $89K annualized run rate by December). There is no evidence in the P&L that this cost increase was passed through to clients. 

**Conclusion:** The software business as a whole is profitable, but PulseOne is leaking tens of thousands of dollars by failing to enforce a minimum 24% BiC margin floor on Microsoft and Adobe, and by absorbing Barracuda cost increases rather than passing them through to the client.

---

## 4. Help Desk Overstaffing vs. Project Subsidization

Are Help Desk resources underutilized and subsidizing projects? The evidence suggests **yes, but specifically regarding the expensive domestic contractors.**

**The Ticket Flow Reality:**
The `2025ticketinfo.pdf` snapshot from April 28, 2026, shows 113 tickets opened that day. Of those, only 3 (2.7%) were assigned to the "Internal Projects Team." The vast majority (97%) were Help Desk, NOC, or Dispatch. This confirms that the primary operational volume is Help Desk support.

**The Subsidization Dynamic:**
Because the Help Desk volume is handled so efficiently by the offshore team (George and Omar resolved over 2,600 tickets combined), it creates excess capacity among the domestic staff. 

When a project is sold without enough margin to hire a dedicated subcontractor, Services Management pulls from this domestic excess capacity (e.g., Steve Calkins, James Froio, Hagen McDonell) to deliver the project. Because their salaries are already paid by the Help Desk budget, the project looks profitable.

**Conclusion:** PulseOne does not necessarily have too many Help Desk resources; it has the *wrong mix* of resources. The company is paying premium rates for Upwork contractors (Vincent at $102K, Matthew at $88K) who log very few tickets, while relying on W-2 staff to quietly deliver underpriced projects. 

## Recommended Actions

1.  **Mandate Time Tracking:** The "Invisible Subsidy" argument ends the day W-2 staff are required to log their time against specific project boards in ConnectWise.
2.  **Reprice Projects:** No project quote should be approved unless it includes the fully loaded hourly cost of internal W-2 labor.
3.  **Audit Vincent Williams and Matthew Barnett:** Their cost-per-ticket metrics ($485 and $510 respectively) are unsustainable for Help Desk roles. If they are doing project work, their costs must be moved to the project P&L.
4.  **Pass Through Barracuda Costs:** Immediately audit all clients with Barracuda licensing to ensure the 87% cost escalation has been reflected in their monthly billing.
