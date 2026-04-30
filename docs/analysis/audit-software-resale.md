# Audit: Software Resale & SaaS Rationalization

**Document Type:** Focused Operational Audit  
**Version:** 3.0 (Revised with TD Synnex Purchase Data)  
**Date:** April 30, 2026  
**Supersedes:** All prior versions  
**Author:** Manus AI (Strategic Audit Assistant)

---

## A. Objective

This audit addresses the software cost structure, resolving prior mysteries around product resale margins and the "Synnex Black Box." The primary update in this version incorporates line-item purchase data from TD Synnex, which definitively answers the Barracuda profitability question and reclassifies internal security tools.

---

## B. Evidence Reviewed

| Source | Period | Notes |
|--------|--------|-------|
| `P1TDSPurchaseHistoryPULSEONEPOS.xlsx` | CY 2025 | TD Synnex line-item purchase history (New) |
| `pulseone-definitive-pl-analysis.md` | CY 2025 | Authoritative corrected P&L |
| `2025 PulseOne Software COGS and Expense.xlsx` | CY 2025 | QB transaction detail |

---

## C. Major Findings & Corrections (April 30 Update)

### Finding 1: Barracuda is Highly Profitable (35.4% Margin)
Prior audits flagged a concern that Barracuda costs were escalating without being passed through to clients. The TD Synnex purchase history (SO tab) reveals the true cost of Barracuda licenses billed to clients:
- **ConnectWise Revenue:** $323,737
- **TD Synnex Cost (SO Tab):** $209,123 (monthly recurring licenses)
- **Gross Margin:** **$114,614 (35.4%)**

This is a healthy product margin that exceeds the BiC target of 24-26%. The Barracuda resale business is not a source of margin leakage.

### Finding 2: Skout is an Internal Tool, Not a Resale Product
The $72,960 paid directly to Barracuda/Skout (previously assumed to be part of the product cost) has been confirmed by the owner as an internal Help Desk SOC tool. 
- **Action Taken:** This $72,960 has been reclassified from Product COGS to Managed Services (Help Desk) COGS.

### Finding 3: The Microsoft Rebate Risk
Microsoft 365 margin appears healthy at 43.4% ($495K revenue vs $302K cost), but this relies heavily on **$22K in backend rebates**. Without rebates, the operational margin drops to 39.0%. If Microsoft alters its rebate program, this margin is at risk.

### Finding 4: The Product Resale Loss is an Accounting Artifact
The QuickBooks P&L shows a -9.2% margin on Product Resale. This is an artifact of how revenue is recognized. Much of the software cost (e.g., $10,719 for Axcient/EFolder backups, security tools) is bundled into Managed Services agreements. The clients pay for the software via their monthly MS fee, but the cost remains in the Product COGS line. 
- **Conclusion:** The underlying software resale engine (as evidenced by Barracuda's 35.4% margin and Microsoft's 43.4% margin) is profitable.

---

## D. The Synnex Black Box (Still Open)

While the TD Synnex purchase history provided clarity on Barracuda, the Microsoft CSP billing remains complex. 
- The TD Synnex data shows **$4.55M** in gross Microsoft CSP orders flowing through the tenant.
- QuickBooks only records **$301,813** in Agreement License Cost to Synnex.
- This massive discrepancy indicates that the TD Synnex portal shows the gross retail value of licenses passing through PulseOne's tenant, while QuickBooks only records the net cost (or potentially just the margin/fee). 

**A true line-item invoice from Synnex that reconciles to the $301,813 QuickBooks figure remains the most critical missing piece of financial evidence.**

---

## E. SaaS Tool Sprawl & SGA Misclassification

*(Note: These findings remain unchanged from v2.0 but are preserved here for completeness).*

1. **$194,092 Misclassified:** Service delivery tools (ConnectWise, Flexis, Kaseya, Wasabi, Duo, etc.) were misclassified in QB as "Computer and Internet Expenses" (SGA). They have been correctly moved to COGS in the definitive P&L.
2. **True SGA Software:** Genuine internal SGA software spend is only **$58,539**.
3. **Immediate Cancellations:** $1,561/year can be saved by cancelling redundant tools (Replit, Calendy, Claude.AI, Patreon, etc.).

---

## F. Recommended Actions

1. **Reconcile Microsoft CSP Billing:** The finance team must obtain a line-item invoice from TD Synnex that exactly matches the $301,813 paid in QuickBooks to verify PulseOne is not being overbilled for Microsoft licenses.
2. **Consolidate AI Tools:** Standardize on Cursor (IDE) + one primary LLM API (OpenAI or Anthropic). Cancel redundant subscriptions.
3. **Reclassify Skout:** Ensure the bookkeeper permanently maps the direct Skout payments to Managed Services COGS, not Product Resale.
