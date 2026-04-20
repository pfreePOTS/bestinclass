# PulseOne Strategic Audit: Software Classification Findings

**Objective:**
Analyze the detailed vendor-level software expense data to identify misclassifications between COGS (client-billable software) and SG&A (internal operational tools), and diagnose the root cause of the negative software resale margin.

**Evidence Reviewed:**
- `2025PulseOneSoftwareCOGSandExpense.xlsx`
- Service Leadership BIC Chart of Accounts Definitions

---

## 1. The Core Problem: The Negative Software Margin is Real

The most important finding from this data is that the negative software margin we saw on the P&L is **not** an accounting error or misclassification. It is a real pricing problem.

### The Math
You have two software revenue streams and two corresponding COGS lines:

**A. Agreement Licenses (Recurring Managed Services Software)**
- Revenue: $763,755
- Cost: $366,527
- **Margin: 52.0%** *(Excellent — beats BIC target)*

**B. Software Resale (One-off or standalone software sales)**
- Revenue: $514,405
- Cost: $562,726
- **Margin: -9.4% (Loss of $48,321)** *(Critical failure — BIC target is 24-27%)*

### The Root Cause
The detailed vendor data shows exactly where this loss is happening. Your Software Resale costs are heavily concentrated in three vendors:
1. **Synnex Corp:** $251,028
2. **Ingram Micro:** $194,247
3. **Amazon Web Services (AWS):** $63,273

These three vendors account for $508,548 of your $562,726 Software Resale cost. Because this category is losing money overall, it means you are consistently underpricing Synnex, Ingram Micro, and AWS consumption when you bill it to clients.

**Immediate Action Required:**
Pull the ConnectWise billing agreements for the top 5 clients consuming AWS, Synnex, and Ingram Micro products. Compare their billed rates against the vendor invoices. You will likely find that vendor costs have increased, but the client billing rates have remained static.

---

## 2. SG&A Tool Sprawl: The $264K Computer & Internet Line

In the previous departmental analysis, we flagged the $263,953 "Computer and Internet Expenses" line item as a major source of G&A bloat. The detailed vendor data reveals exactly what is driving this cost.

### The Big Three Internal Tools ($172,850 / 65% of the total)
1. **ConnectWise:** $89,800
2. **Flexis:** $64,009
3. **Microsoft Azure:** $19,041

These are core operational tools. ConnectWise at $90K/year for a $5M MSP is typical. Flexis (NOC/Help Desk augmentation) at $64K is also a standard delivery cost.

### The "Sprawl" Tail ($91,103 / 35% of the total)
The remaining $91K is spread across **49 different vendors**. This is classic IT tool sprawl. Some of these are clearly redundant or unnecessary for a $5M MSP:

- **AI & Dev Tools (Redundant):** OpenAI ($1,076), Anthropic ($424), Claude.AI ($220), OpenRouter ($27), Cursor ($1,184), Replit ($526), Railway ($823), Scrapfly ($230), Iron Software ($249). You are paying for multiple overlapping LLM and dev environments.
- **Scheduling/CRM (Redundant):** You are paying $39,560 for RepScheduler (in Sales), but also paying for TimeZest ($3,609) and Calendly ($514). Pick one scheduling tool and standardize.
- **Misc SaaS:** Monday.com ($288), Figma ($97), Patreon ($71), Quicken ($72), Vevox ($131), LearnDash ($199).

**Strategic Action:**
While cutting the $91K "tail" won't solve the entire profitability gap, it is the easiest cash to recover. Mandate a zero-based budget review of every SaaS tool under $5,000/year. If it doesn't directly support ConnectWise or service delivery, cancel it.

---

## 3. Misclassifications Identified

There are a few minor misclassifications, but they do not change the macro profitability picture.

### A. Flexis ($64,009)
- **Current Location:** Computer & Internet Expenses (SG&A)
- **BIC Classification:** Flexis provides NOC and Help Desk services. This is direct delivery labor. It should be moved to **Consulting Services - Cost (COGS)** or **Agreement License Cost (COGS)** depending on how it is utilized.
- **Impact:** Moving this $64K to COGS will slightly lower your delivery gross margins (which are currently beating the BIC target) and slightly improve your G&A overhead percentage.

### B. AWS and Microsoft appearing in multiple categories
- **AWS:** Appears in Agreement License Cost ($10,709) and Software Resale ($63,273). This is correct if some AWS is bundled into managed agreements and some is billed standalone.
- **Microsoft:** Appears in Agreement License Cost (negative $11,482 due to rebates), Software Resale ($68), and Computer & Internet ($14,126). This is also correct — you consume Microsoft internally (SG&A) and resell it (COGS).

---

## Summary Conclusion

The detailed software data confirms our previous diagnoses:

1. **The Software Resale loss is real.** You must fix your pricing on Synnex, Ingram Micro, and AWS. This is a ~$180K profit recovery opportunity.
2. **G&A is bloated by tool sprawl.** You have 49 different SaaS vendors in your SG&A tail. Consolidate scheduling tools and cut redundant AI/Dev subscriptions.
3. **Delivery Margins are still healthy.** Even if we move the $64K Flexis cost into COGS, your delivery teams are still operating at or above the BIC targets. The profit leakage remains concentrated in Software Pricing, Marketing overspend, and G&A tool sprawl.
