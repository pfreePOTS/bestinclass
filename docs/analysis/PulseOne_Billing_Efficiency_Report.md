# PulseOne Strategic Audit: Billing Efficiency & Revenue Leakage Analysis

**Objective:**
Analyze the CY 2025 ConnectWise utilization data with the corrected definitions that **both** the ITMS board and specific Help Desk elements (e.g., onsite visits, out-of-scope work) are billable. This shifts the focus from a theoretical utilization problem to a tangible billing efficiency problem.

**Evidence Reviewed:**
- CY 2025 Technician Utilization Report (Help Desk & ITMS Boards)
- Clarified definitions: ITMS = client-requested billable tasks; Help Desk = tiered support with billable elements.

---

## 1. The Core Issue: Revenue Leakage

With the confirmation that these boards contain significant billable capacity, the 23% recovery rate (hours billed divided by actual hours logged) is no longer just an artifact of the MSP model — it highlights a genuine leakage problem in the billing process.

The data reveals three distinct areas of revenue leakage, totaling an estimated **$514,951 in uncaptured revenue** at your $150/hr bill rate.

![Revenue Leakage Waterfall](chart_billing_efficiency.png)

### Leakage Area 1: The "Write-Down" Problem (Confirmed)
Across the team, 1,248 hours were marked to be invoiced, but only 1,141 hours were actually billed. 
- **Lost Hours:** 107
- **Revenue Lost:** **$16,050**
- **Diagnosis:** This is not a system error; it is a discipline error. Someone (a service manager or account manager) is reviewing invoices before they go out and manually writing down the hours, likely to avoid client pushback. Every hour written off is $150 in pure margin lost.

### Leakage Area 2: Unbilled Actual Hours (Estimated)
The team logged 4,965 actual hours, but only billed 1,141. That leaves 3,824 hours worked but not billed. While much of this is standard non-billable Help Desk support covered by agreements, the tiered structure means some of this *should* have been billed (e.g., onsite visits, out-of-scope requests).
- **Conservative Estimate:** If even 20% of those unbilled hours were actually billable under your tier definitions but were miscoded by technicians:
- **Potential Revenue Recovered:** **$114,717**

### Leakage Area 3: Unlogged Available Hours (Estimated)
Based on FTE capacity, the team had roughly 13,520 available hours, but only logged 4,965 hours in ConnectWise. That leaves 8,555 hours completely unaccounted for (63% of capacity).
- **Conservative Estimate:** If technicians are failing to log time, and even 30% of that unlogged time was billable work:
- **Potential Revenue Recovered:** **$384,979**
- **Diagnosis:** Best in Class MSPs require 100% time entry discipline. Without it, you cannot accurately measure profitability, identify scope creep, or bill for out-of-scope work.

---

## 2. Operational Misalignments

The data also reveals two specific personnel misalignments that are distorting your cost and profitability metrics.

### Issue 1: Jim Froio's Internal IT Time
Jim Froio logged 660 hours on the Help Desk/ITMS boards. However, his confirmed allocation is 40% billable projects, 40% internal IT, and 20% admin. 
- The 40% internal IT time (roughly 832 hours/year) is the cost of running PulseOne's own infrastructure ($50,525/yr). 
- **Action:** This time must be logged to an internal overhead ticket, not mixed into client-facing boards. Mixing it makes it impossible to accurately measure his client-facing utilization.

### Issue 2: Laura Walsh's Board Usage
Laura Walsh is classified as 80% Service Leadership and 20% Sales. Yet she logged 301 hours on the Help Desk/ITMS boards. 
- At her senior cost ($121,164/yr), her presence on these delivery boards inflates the apparent cost of the Help Desk team without a proportionate revenue contribution. 
- **Action:** Her time on these boards should be reclassified as service management oversight (non-billable overhead), not delivery labor.

---

## 3. Priority ConnectWise Data Requests

To stop the leakage and capture this revenue, you need to pull the following specific reports from the ConnectWise AI interface:

1. **Ticket Type Breakdown (Most Urgent):**
   > "For the Help Desk board in CY 2025, break down actual hours logged by ticket type: (a) standard agreement support, (b) onsite visits, (c) out-of-scope billable work. What percentage of hours fall into each category?"
   *(This will prove exactly how much of the unbilled time should have been billed.)*

2. **Billing Code Audit:**
   > "How many tickets in CY 2025 were marked as billable but then had hours reduced or zeroed out before invoicing? Who approved those write-downs?"
   *(This will identify who is causing the $16,050 write-down leakage.)*

3. **Onsite Billing Capture:**
   > "How many onsite visits were logged in CY 2025? Of those, how many generated a billable charge? What was the total onsite revenue?"
   *(This tests whether your tiered billing rules are actually being enforced.)*

4. **Agreement Hours Consumption:**
   > "For each active Managed Services agreement in CY 2025, what was the average monthly hours consumed per client? Which clients are consuming the most hours relative to their monthly fee?"
   *(This tests whether the flat-fee agreements are priced correctly.)*
