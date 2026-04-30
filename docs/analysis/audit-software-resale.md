# Audit: Software Resale & SaaS Rationalization

**Document Type:** Focused Operational Audit  
**Version:** 3.3 (Corrected AvePoint margin to 29.8%)  
**Date:** April 30, 2026  
**Supersedes:** All prior versions  
**Author:** Manus AI (Strategic Audit Assistant)

---

## A. Objective

This audit addresses the software cost structure, resolving prior mysteries around product resale margins and the "Synnex Black Box." This version incorporates line-item purchase data from TD Synnex and completes the product-level profitability picture for all major software lines.

---

## B. Evidence Reviewed

| Source | Period | Notes |
|--------|--------|-------|
| `P1TDSPurchaseHistoryPULSEONEPOS.xlsx` | CY 2025 | TD Synnex line-item purchase history (SO and CPO tabs) |
| `pulseone-definitive-pl-analysis.md` | CY 2025 | Authoritative corrected P&L |
| `2025 PulseOne Software COGS and Expense.xlsx` | CY 2025 | QB transaction detail |
| `2025PulseOneConsultingServicesCost.xlsx` | CY 2025 | QB Consulting Services Cost detail |
| ConnectWise product revenue data | CY 2025 | From COGS gap analysis cross-reference |

---

## C. Software Product Profitability Summary

### Master Product P&L (CY 2025)

| Product | Revenue (CW) | Total Cost | Gross Margin | Margin % | Classification |
|---|---|---|---|---|---|
| **Barracuda** | $323,737 | $160,781 | $162,956 | **50.3%** | Product Resale |
| **AvePoint** | $165,514 | ~$116,000 | ~$49,500 | **29.8%** | Product Resale |
| **Microsoft M365** | $495,000 | $361,906 | $133,094 | **26.9%** | Agreement License |
| **Adobe** | ~$103,000 | ~$99,000 | ~$4,000 | **~4.3%** | Product Resale (pass-through) |
| **TOTAL** | **$1,087,251** | **~$737,687** | **~$349,564** | **32.2%** | |

**Key insight:** The software resale engine is profitable overall at 32.2% blended margin. Barracuda is the standout performer at 50.3%. AvePoint contributes healthy margin at 29.8%. Adobe is a near-zero-margin pass-through that drags the average down.

---

## D. Major Findings & Corrections

### Finding 1: Barracuda is Highly Profitable (50.3% Margin)
Prior audits flagged a concern that Barracuda costs were escalating without being passed through to clients. The TD Synnex purchase history (SO tab), when correctly calculated at **Net Price × Qty per line** (not the misleading "Total Order" column which shows order-level totals shared across lines), reveals:
- **ConnectWise Revenue:** $323,737
- **TD Synnex Cost (Net Price × Qty):** $160,781 (monthly recurring licenses)
- **Gross Margin:** **$162,956 (50.3%)**

This is a very healthy product margin that significantly exceeds the BiC target of 24-26%. The Barracuda resale business is not a source of margin leakage.

**Important correction:** The earlier v3.0 figure of $209,123 was incorrect — it used the "Total Order" column which double-counts by showing the full order total on every line within that order. The correct method is Net Price × Qty per line = $160,781.

### Finding 2: AvePoint Margin Corrected to 29.8% (Not 66.8%)

AvePoint is both a **client** (PulseOne does projects for AvePoint Inc.) and a **product** (PulseOne resells AvePoint backup/compliance licenses to its own clients). The product resale side:

**Cost breakdown:**
| Source | Amount | Notes |
|---|---|---|
| QB "Purchases - Software for Resale" (direct) | $41,200 | Direct AvePoint billing |
| TD Synnex SO tab (APU_ parts) | $13,035 | AvePoint licenses through Synnex for 11 clients |
| QB CS-Cost (one-off project) | $675 | Georgia Farm backup project |
| Additional cost via Ingram Micro (estimated) | ~$61,000 | Not yet reconciled — see note below |
| **Total AvePoint Cost (estimated)** | **~$116,000** | |

**Revenue:** ConnectWise shows $165,514 in AvePoint product revenue sold to PulseOne's clients, yielding a **29.8% gross margin**.

**CORRECTION (v3.3):** The prior version showed 66.8% margin based only on the $54,910 in directly identifiable AvePoint costs. The archived COGS gap analysis (audit-software-cogs-gap-analysis.md) established a 29.8% margin figure, indicating approximately $61K in additional AvePoint procurement cost flows through Ingram Micro and/or TD Synnex under generic descriptions that are not easily attributed to AvePoint without line-item invoice detail. The owner has confirmed 29.8% is the correct margin assumption until the Ingram data is fully reconciled.

**Open item:** The ~$61K in unreconciled AvePoint cost is part of the broader Ingram Micro $194K gap (see action register). Resolving the Ingram reconciliation will confirm the exact AvePoint cost.

**Top AvePoint clients by Synnex billing:** CT Legal Services, New Haven Legal Assist, Statewide Legal Services, Talus Ag, CHW, Fagen Friedman.

**Note:** AvePoint as a CLIENT generated $67,250 in project/T&M revenue (12 projects at 68.8% margin in QuickBase). This is separate from the product resale and belongs in the True Projects segment.

### Finding 3: Skout is an Internal Tool, Not a Resale Product
The $72,960 paid directly to Barracuda/Skout (previously assumed to be part of the product cost) has been confirmed by the owner as an internal Help Desk SOC tool. 
- **Action Taken:** This $72,960 has been reclassified from Product COGS to Managed Services (Help Desk) COGS.
- **Open Question for Team:** The Skout cost grew 87% during 2025 ($48K → $90K annualized run rate). Was this expected due to client onboarding, or was it an uncontrolled cost increase?

### Finding 4: The Microsoft Rebate Risk
Microsoft 365 margin appears healthy at 26.9% ($495K revenue vs $362K cost through Synnex), but this includes **$22K in backend rebates**. Without rebates, the operational margin drops to ~22.5%. If Microsoft alters its rebate program, this margin is at risk and would fall below the BiC 24-26% floor.

### Finding 5: Adobe is a Near-Zero-Margin Pass-Through
Adobe licensing ($99K cost, ~$103K revenue, ~4.3% margin) was primarily a large pass-through sale to ARC Research. This is not a sustainable product line at current pricing. A procurement fee or markup should be attached to any future Adobe pass-through arrangements.

### Finding 6: The Product Resale "Loss" is an Accounting Artifact
The QuickBooks P&L shows a negative margin on Product Resale. This is an artifact of how revenue is recognized — much of the software cost (e.g., $10,719 for Axcient/EFolder backups, Skout) is bundled into Managed Services agreements. The clients pay for the software via their monthly MS fee, but the cost remains in the Product COGS line. 
- **Conclusion:** The underlying software resale engine is profitable at 32.2% blended margin when properly matched.

---

## E. The Synnex Black Box — RESOLVED

The TD Synnex purchase history, when correctly calculated at the line level (Net Price × Qty), reconciles closely to QuickBooks:

| Category | TD Synnex (Net Price × Qty) | Notes |
|---|---|---|
| Barracuda (EP/DP/BBS/BAR) | $160,781 | Product resale COGS |
| Microsoft CSP (318Z/CFQ/C0L) | $361,906 | Agreement License Cost |
| AvePoint (APU_) | $13,035 | Product resale (partial — $41K more billed direct) |
| Hardware/Other | $28,314 | Misc resale |
| **TOTAL** | **$564,036** | |
| **QB Total Synnex** | **~$553,000** | ($251K Resale + $302K Agreement) |
| **Variance** | **$11,036 (2.0%)** | Likely timing differences |

The prior "$4.55M mystery" was caused by using the "Total Order" column, which shows the order-level total on every line within an order (causing massive double-counting). The correct line-level calculation produces $564K — which reconciles within 2% of what QuickBooks shows.

**Status: RESOLVED.** PulseOne is NOT being overbilled by Synnex. The $553K in QB accurately reflects PulseOne's actual cost.

---

## F. SaaS Tool Sprawl & SGA Misclassification

*(Note: These findings remain unchanged from v2.0 but are preserved here for completeness).*

1. **$194,092 Misclassified:** Service delivery tools (ConnectWise, Flexis, Kaseya, Wasabi, Duo, etc.) were misclassified in QB as "Computer and Internet Expenses" (SGA). They have been correctly moved to COGS in the definitive P&L.
2. **True SGA Software:** Genuine internal SGA software spend is only **$58,539**.
3. **Immediate Cancellations:** $1,561/year can be saved by cancelling redundant tools (Replit, Calendy, Claude.AI, Patreon, etc.).

---

## G. Recommended Actions

1. **Reclassify Skout:** Ensure the bookkeeper permanently maps the direct Skout payments to Managed Services COGS, not Product Resale.
2. **Investigate Skout Growth:** Determine whether the 87% cost increase was driven by client onboarding (justified) or uncontrolled pricing (needs action).
3. **Attach Procurement Fee to Adobe:** The 4.3% margin on $99K is not sustainable. Add a minimum procurement/management fee for pass-through software.
4. **Monitor Microsoft Rebates:** The M365 margin depends on $22K in rebates. Build a contingency plan for rebate reduction.
5. **Consolidate AI Tools:** Standardize on Cursor (IDE) + one primary LLM API (OpenAI or Anthropic). Cancel redundant subscriptions.
6. **Protect AvePoint Margin:** At 29.8%, AvePoint is a healthy but not exceptional margin product. Monitor cost increases from Ingram/Synnex and ensure pricing passes through any vendor cost increases to maintain margin.
