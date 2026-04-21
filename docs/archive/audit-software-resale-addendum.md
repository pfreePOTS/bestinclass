# Audit Addendum: Software Resale Margin Mystery Resolution

**Date:** April 20, 2026  
**Subject:** Reconciliation of QuickBooks Software COGS (-9.4% Margin) vs. ConnectWise Cost/Sell Report (68.1% Margin)

## 1. The Core Mystery

Prior analysis of the 2025 QuickBooks P&L and transaction detail showed a **critical failure in Standalone Software Resale**: $514,405 in revenue against $570,987 in cost, yielding a **-9.4% gross margin** (a $56,582 loss).

However, an analysis of the ConnectWise Cost/Sell report for the same period reveals a completely different picture. The CW report shows 6,704 software/subscription line items generating **$2,978,392 in revenue against $949,040 in cost**, yielding a **healthy 68.1% gross margin**.

## 2. The Root Cause: Unbilled COGS vs. Aggregated Invoicing

The discrepancy is caused by two intersecting accounting/billing practices:

1. **Aggregated Invoicing:** The CW Cost/Sell report shows that the vast majority of software is being sold as part of larger managed services agreements or bundled invoices. QuickBooks is only seeing the "Standalone Software Resale" revenue line ($514k), while the actual software revenue ($2.97M) is being mapped to other revenue accounts (likely Managed Services or Project revenue).
2. **Unbilled COGS:** The CW report shows $949k in software cost, while QuickBooks shows $570k in the Standalone Resale COGS account (plus more in Agreement License COGS). This means costs are correctly hitting the P&L, but the revenue they generate is not being matched to them in the chart of accounts.

**Conclusion:** PulseOne does not have a -9.4% software margin problem. It has a **revenue mapping problem**. The software margin is actually highly profitable (68.1%) when viewed at the transaction level, but the revenue is hiding in the Managed Services lines on the P&L.

## 3. The Structural Margin Issue: Microsoft and Adobe

While the overall software margin is healthy, the transaction data reveals a structural problem with two major vendors that are dragging down profitability and failing to meet the Service Leadership Best-in-Class (BiC) floor of 24.3%:

### Microsoft (M365 Products)
- **Total Cost:** $220,220
- **Total Revenue:** $263,554
- **Blended Margin:** 16.4% ⚠
- **The Issue:** Microsoft CSP margins are structurally capped around 16-17%. Selling raw Microsoft licenses without a service wrap mathematically guarantees failure against the BiC 24% target.
- **Top Offender:** Microsoft 365 Business Premium Annual ($48,482 cost, 17.3% GM).

### Adobe (Creative Cloud)
- **Total Cost:** $126,961
- **Total Revenue:** $132,625
- **Blended Margin:** 4.3% ⚠
- **The Issue:** Adobe margins are near-zero. This volume is heavily concentrated in a single client (Bunzl).
- **Top Offender:** Adobe CC License - 1 Year/ 10-49 Users ($45,417 cost, 3.1% GM).

## 4. Client Concentration: The Bunzl Group

The data reveals extreme concentration in a single corporate group. The "Bunzl" entities (Bunzl, Cool Pak, Bunzl De Mexico, Tingley Rubber, Steiner Industries, Cordova Safety, MCR Safety) account for:
- **Total Cost:** $344,551
- **Total Revenue:** $1,525,125
- **Blended Margin:** 77.4%

Bunzl represents 29.5% of all invoiced revenue in the Cost/Sell report.

## 5. Negative Margin Transactions

There are 105 specific invoice lines where the cost exceeded the price, resulting in a direct loss of $25,096. 

The top structural losses are:
1. **Arc Research Institute:** $3,920 loss on a credit ("Credit for David being out the first 2 weeks") mapped against cost.
2. **Santa Barbara Sky Football Club:** Consistent negative margins on hardware (Dell Inspiron, Cisco Switches) and services.
3. **Malenfant Technical Services:** Negative margins on Barracuda products.

## 6. Recommended Actions

1. **Re-map P&L Revenue:** Stop trying to manage "Standalone Software Resale" as a P&L line item. The CW data proves it is a fiction. Software revenue is hopelessly blended with Managed Services revenue. Manage software margin at the ConnectWise agreement level, not the QuickBooks P&L level.
2. **Bundle Microsoft:** Immediately stop selling raw Microsoft 365 licenses. They must be bundled into a per-user managed service seat, or have a "Cloud Management" fee attached to bridge the gap from 16% to the 24% BiC floor.
3. **Review Adobe Pricing:** The 4.3% margin on $126k of Adobe spend is unacceptable. If this is a pass-through for Bunzl, it needs a procurement fee attached.
4. **Investigate Santa Barbara Sky Football Club:** Review the pricing model for this client. They appear repeatedly in the negative margin hardware/software transaction list.
