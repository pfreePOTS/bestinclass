# Software COGS Gap Analysis: What Is in COGS With No Corresponding Sale?

**Date:** April 20, 2026  
**Scope:** QuickBooks Software COGS (Agreement License Cost + Purchases - Software for Resale) vs. ConnectWise Cost/Sell Report CY2025  
**Total QB Software COGS:** $944,985.82  
**Total QB Software Revenue (P&L):** $514,405 (Standalone) + $763,755 (Agreement) = $1,278,160  

---

## A. Objective

The ConnectWise Cost/Sell report shows healthy software margins at the transaction level. The QuickBooks P&L shows a -9.4% loss on Standalone Software Resale. This analysis identifies precisely which QB COGS items have no matching sale in ConnectWise, and why.

---

## B. The Core Finding: Three Vendors Account for the Entire Gap

The cross-reference of every QB software COGS vendor against the CW sell report reveals the following:

| QB Vendor | QB COGS | CW Revenue Found | Gap (Unmatched) | Status |
|---|---|---|---|---|
| **TD Synnex Corp** (both sections) | $552,840 | $6,380 | **$548,327** | ⚠ No line-item sale found |
| **Ingram Micro** | $194,247 | $0 | **$194,247** | ⚠ No sale found in CW |
| Amazon Web Services | $73,982 | $153,714 | -$25,520 | ✓ Sold at 35.3% GM |
| AvePoint | $41,200 | $165,514 | -$74,982 | ✓ Sold at 29.8% GM |
| EFolder (Axcient) | $10,719 | $0 | **$10,719** | ⚠ No sale found |
| ScalePad / WarrantyMaster | $5,988 | $0 | **$5,988** | ⚠ No sale found |
| Atlassian | $2,962 | $0 | **$2,962** | ⚠ No sale found |
| Microsoft (net of rebates) | -$22,896 | $353,829 | — | See below |
| Barracuda | $72,960 | $323,737 | — | ✓ Sold at 25.3% GM |

**Total unmatched COGS (vendors with no CW sale): ~$762,243**

This is the gap. The revenue for these costs is either: (a) billed inside a managed services agreement and not broken out as a product line in CW, (b) billed directly and not captured in the CW Cost/Sell report, or (c) genuinely unbilled.

---

## C. TD Synnex: The Largest Unresolved Item ($552,840)

The Synnex COGS in QuickBooks consists of **two completely different pools**:

**Pool 1 — Agreement License Cost: $301,813 (12 monthly bills)**  
Every transaction is recorded as "Estimate" with no product detail. Monthly amounts range from $22,321 to $30,277 — a 44.5% swing with no explanation in the memo field. This is the consolidated Synnex bill for bundled managed services software (RMM, security stack, etc.). It is **not expected to appear as a product sale in CW** because it is the cost of delivering the managed service, not a resale item. However, it cannot be verified without a line-item invoice from Synnex.

**Pool 2 — Standalone Resale: $251,028 (217 transactions)**  
These transactions have client names in the memo field (ARC, DaighRick, ACT, Calpine, FireSprinkler, etc.) and represent specific software purchased for specific clients. The CW sell report shows only $6,380 in Synnex-matched revenue. This means **$244,648 of client-attributed Synnex purchases have no matching product invoice in CW**. The most likely explanation is that these were billed inside managed services agreement line items, not as separate product invoices.

---

## D. Ingram Micro: $194,247 With Zero CW Revenue Match

Ingram Micro has **no matching product description in the CW sell report** — zero. The QB transactions are all client-attributed:

| Date | Client | Amount |
|---|---|---|
| 2025-08-31 | ARC | $98,222.29 |
| 2025-05-17 | DaighRick | $8,391.70 |
| 2025-03-27 | ACT | $6,861.78 |
| 2025-05-07 | Outside Analytics / AvePoint | $6,629.60 |
| 2025-05-31 | Fire Sprinkler Systems | $6,409.13 |
| 2025-11-11 | **Erroneous charge — credited 11/11/25** | $5,017.80 |
| 2025-07-31 | Turning Point | $4,617.83 |
| 2025-10-07 | Fire Sprinkler | $4,491.21 |
| 2025-09-19 | Calpine | $4,481.90 |
| 2025-06-29 | Calpine | $4,044.62 |
| ... | (129 more rows) | ... |

**Critical item:** The $5,017.80 entry on 2025-11-11 is explicitly labeled "Erroneous charge on 9/17/25. Credited 11/11/25." This means the original charge ($5,017.80) and the credit ($5,017.80) should net to zero — but only if both entries are in the file. If only the charge is present, this is phantom COGS.

**The ARC concentration:** A single Ingram bill dated 2025-08-31 for ARC totals **$98,222** — more than half of all Ingram Micro spend. This is almost certainly the Adobe Creative Cloud annual renewal for ARC (confirmed by the user as a bundled arrangement). If this cost is being billed to ARC inside a managed services agreement rather than as a product invoice, it will never appear in the CW sell report.

---

## E. Vendors With No CW Sale: Likely Internal Tools Miscategorized as Resale

Three vendors in the "Purchases - Software for Resale" section have zero corresponding CW revenue and are almost certainly **internal tools that were miscategorized**:

| Vendor | Annual Cost | Pattern | Likely Classification |
|---|---|---|---|
| EFolder Systems (Axcient) | $10,719 | $901.93/month recurring | Internal backup/DR platform — should be Service Delivery COGS |
| ScalePad / WarrantyMaster | $5,988 | $499/month recurring | Internal warranty tracking tool — should be SG&A |
| Atlassian | $2,962 | $217-$417/month recurring | Internal Jira/Confluence — should be SG&A |

These three total **$19,669** and are sitting in "Purchases - Software for Resale" but are clearly platform subscriptions, not client resale items. They have no client attribution in the memo field and show a perfectly consistent monthly charge pattern.

---

## F. Microsoft: Confirmed Near-BiC After Rebates

| Metric | Value |
|---|---|
| CW Microsoft Revenue | $353,829 |
| CW Microsoft Cost (gross) | $281,520 |
| CW Microsoft GM% (gross) | 20.4% |
| Microsoft Rebates (QB) | **$11,482** |
| Adjusted Microsoft Cost | $270,037 |
| **Adjusted Microsoft GM%** | **23.7%** |
| BiC Target | 24.3% |
| Gap to BiC | **0.6 pts = $2,189 additional revenue needed** |

Microsoft is **0.6 percentage points below the BiC floor** after rebates. This is not a material problem — it is effectively at parity. The rebates are real and material ($11,482) and must be included in any margin calculation. The gap to BiC is closed by raising prices on approximately $13,000 of Microsoft revenue by ~17%, or by adding a small cloud management fee to any client on M365.

---

## G. The Real Question: Is the Ingram/Synnex Resale Revenue Being Billed?

The data cannot definitively answer whether the $444,875 in Ingram + Synnex standalone resale costs are being billed to clients. There are two possibilities:

**Scenario A — Revenue is being billed inside managed services agreements:**  
The software cost is real, the revenue is real, but the revenue is mapped to "Managed Services" in QuickBooks rather than "Software Resale." This would mean there is no margin problem — just a revenue categorization issue. The P&L would show inflated Managed Services margin and deflated Software margin.

**Scenario B — Some costs are genuinely unbilled:**  
Specific purchases (particularly the large ARC/Ingram items) were procured but not invoiced to the client, or were invoiced under a flat-rate agreement that does not fully recover the cost. This would be a real margin leak.

**The only way to resolve this is to pull the ConnectWise agreement for ARC and cross-reference the $98,222 Ingram purchase against what was billed to ARC in August 2025.**

---

## H. Recommended Actions

| Priority | Action | Owner | Expected Impact |
|---|---|---|---|
| **P1 — Immediate** | Pull the ARC agreement from CW and verify the $98,222 Ingram bill (August 2025) was billed to ARC | Account Manager | Resolves 51% of the Ingram gap |
| **P1 — Immediate** | Request a line-item invoice from TD Synnex for any month and reconcile against CW agreements | Finance | Resolves $301,813 in unverifiable Agreement License cost |
| **P1 — Immediate** | Confirm the $5,017.80 "erroneous charge" (Ingram, 11/11/25) has a matching credit in QB | Finance | Eliminates phantom COGS if credit is missing |
| **P2 — This week** | Reclassify EFolder ($10,719), ScalePad ($5,988), and Atlassian ($2,962) out of "Software for Resale" | Finance | Corrects $19,669 in misclassified COGS |
| **P2 — This week** | Add a $5-10/user/month Cloud Management fee to all M365 clients | Sales/Ops | Closes the 0.6 pt Microsoft BiC gap ($2,189) |
| **P3 — This month** | For all Ingram Micro client-attributed purchases, verify each has a matching CW invoice | Finance | Confirms or denies Scenario A vs. B above |

---

## I. Clarifying Questions

1. **ARC — August 2025 Ingram bill:** Was the $98,222 Adobe/software purchase for ARC billed to ARC in August 2025? If so, under what line item on their invoice?
2. **Synnex Agreement License bill:** Has PulseOne ever received a line-item breakdown from Synnex for the monthly "Estimate" bill? The 44.5% monthly variance ($22,321–$30,277) needs an explanation.
3. **Erroneous Ingram charge:** Is the $5,017.80 credit from 11/11/25 present in the QB file? If not, this is phantom COGS that needs to be entered.
