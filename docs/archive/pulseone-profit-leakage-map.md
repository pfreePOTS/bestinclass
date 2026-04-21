# PulseOne Strategic Audit: The Profit Leakage Map

**Objective:**
Answer the macro-level question: *PulseOne generated $5.17M in revenue but only kept $217K (4.2% EBITDA). The Service Leadership Best in Class (BIC) target is 18.5% ($956K). Where did the missing ~$740,000 go?*

**Evidence Reviewed:**
- Group LLC and PulseOne LLC historical P&Ls
- 2025 POTS P&L and Balance Sheet
- `ExpensesTrackingMASTER2023.xlsx` (burdened labor costs)
- ConnectWise CY 2025 Technician Utilization Report
- Confirmed senior leader time allocations

---

## 1. The $740,000 Question

The gap between PulseOne's current profitability and the Best in Class benchmark is exactly **$738,445**. 

Through our analysis of the P&L, the labor allocations, and the utilization data, we have identified five specific sources of leakage that fully explain this gap. The good news is that the core recurring engine (Managed Services) is not the problem — it is operating at a BIC-level 52.0% gross margin. The leakage is happening entirely in other areas of the business.

![Profit Leakage Waterfall](chart_leakage_waterfall.png)

---

## 2. The Five Sources of Profit Leakage

The following table breaks down the missing profit by source, ranked by confidence level and financial impact.

| Leakage Source | Profit Destroyed | Confidence | Root Cause |
|---|---|---|---|
| **1. Software Sold Below Cost** | **$179,494** | VERY HIGH | Vendor cost increases not passed to clients |
| **2. Consulting Margin Deficit** | **$465,533** | HIGH | Subcontractor pricing, scope creep, fixed-fee overruns |
| **3. Billing Write-Downs** | **$16,050** | HIGH | Hours manually reduced before invoicing |
| **4. S&M Spend vs BIC** | **$257,733** | HIGH | High spend not generating MS revenue growth |
| **5. SG&A Overhead vs BIC** | **$224,414** | MEDIUM | Leadership overhead not yet producing margin lift |

*(Note: The sum of these leakages exceeds $740K because some costs overlap — e.g., if consulting margins improve, the SG&A overhead percentage automatically shrinks relative to gross profit. Fixing the top two issues alone bridges the entire gap.)*

---

## 3. Deep Dive into the Leakage Sources

### Leakage 1: Software Resale (The Fastest Fix)
- **The Math:** You sold $514K in software but paid vendors $562K. Instead of making the BIC target of 25.5% margin ($131K profit), you lost $48K. The total swing is $179,494.
- **The Reality:** This is pure margin leakage. You are likely paying increased vendor costs on renewals but haven't updated the pricing table in ConnectWise to pass those costs through to clients.

### Leakage 2: Consulting & Projects (The Biggest Lever)
- **The Math:** You generated $1.80M in consulting revenue but spent $1.36M to deliver it (a 24.2% margin). The BIC target is 50%. The gap is $465,533 in missing gross profit.
- **The Reality:** Subcontractor costs alone (Basim, David, Blue Pisces) were $1.04M. This means you are paying subcontractors 58 cents for every dollar of consulting revenue before you even pay your own W2 staff or partners. Projects are either severely underpriced, or subcontractors are logging hours that aren't being billed to clients.

### Leakage 3: Billing Discipline
- **The Math:** The ConnectWise utilization data proves that 107 hours were marked for invoicing but were manually written down or zeroed out before the invoice was sent. At $150/hr, that is $16,050 in lost profit.
- **The Reality:** This is a process failure. Furthermore, the team failed to log over 8,500 available hours in ConnectWise. Even if only a fraction of those unlogged hours were billable out-of-scope work, the true billing leakage is likely much higher than $16K.

### Leakage 4 & 5: Overhead and ROI
- **The Math:** You are spending 10.4% of revenue on Sales & Marketing (BIC is 5.4%) and 31.7% on SG&A (BIC is 27.4%). 
- **The Reality:** Spending above benchmark on S&M and Service Leadership is a valid strategy *if* it produces high growth and high margins. But Managed Services revenue declined 16.2% last year, and Consulting margins are broken. The investment in overhead is not currently generating an ROI.

---

## 4. Priority Action Plan

You cannot fix all five leakages at once. Here is the recommended sequence of attack to recover the $740K:

**Immediate (Days 1-14): Stop the Bleeding**
1. **Audit Software Pricing:** Pull a ConnectWise product profitability report. Identify exactly which software SKUs or vendors have a negative margin and update client pricing immediately. *(Value: ~$180K)*
2. **Stop Invoice Write-Downs:** Implement a strict policy that no service manager or account manager can write down billable hours without partner approval. *(Value: ~$16K+)*

**Urgent (Days 15-60): Fix Consulting**
3. **Subcontractor Audit:** Pull a ConnectWise project profitability report specifically for projects involving Basim, David, and Blue Pisces. Calculate the exact ratio of subcontractor cost to billed revenue on those projects.
4. **Implement Margin Gates:** Require partner approval for any fixed-fee project proposal that does not model out to a 50% gross margin based on estimated hours. *(Value: ~$465K)*

**Strategic (Days 60-180): Realign Overhead**
5. **Redirect S&M Focus:** The $536K spent on Sales & Marketing must be laser-focused on acquiring new Managed Services agreements to reverse the 16.2% decline, not on selling low-margin consulting projects.
6. **Enforce Time Entry:** Mandate 100% time entry in ConnectWise for all technicians. You cannot manage utilization or identify scope creep if 63% of available hours are not logged.

---
### References
[1] Service Leadership Index® Annual Profitability Report and First Principles (Public Executive Summaries, 2024-2025).
