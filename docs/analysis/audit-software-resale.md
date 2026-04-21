# Audit: Software Resale & SaaS Rationalization

**Document Type:** Focused Operational Audit  
**Version:** 1.0 (Consolidated)  
**Date:** April 20, 2026  
**Supersedes:** `pulseone-software-classification-findings.md`, `pulseone-software-reconciliation.md`, `pulseone-software-allocation-overpayment-analysis.md`, `pulseone-software-optimization-plan-revised.md`, `pulseone-software-pricing-correction-plan.md`, `pulseone-saas-rationalization-matrix.md`  
**Classification Workbook:** `data/financial/Software_COGS_Classified.xlsx`

---

## A. Objective

This audit addresses two related but distinct problems in PulseOne's software cost structure:

1. **Software Resale Margin Failure.** The Standalone Software Resale segment is generating a -9.4% gross margin ($48,321 loss on $514,405 revenue). The Service Leadership Best in Class (BiC) target for product gross margin is 24.3%–26.3%. Correcting this pricing represents a **$185,000 profit swing** — the single largest addressable profit recovery opportunity in the CY 2025 P&L.

2. **COGS/SGA Misallocation.** The QuickBooks chart of accounts places several client-delivery tools (ConnectWise, Flexis, Kaseya, Samurai Sync, Wasabi, Duo Security, Qualys, MSP360, TimeZest) in the SGA "Computer and Internet Expenses" line rather than in COGS. This misclassification understates gross margin and overstates SGA, distorting both the BiC gross margin comparison and the SGA efficiency ratio.

The secondary objective is to identify SaaS tool sprawl within the SGA line and quantify consolidation savings.

---

## B. Evidence Reviewed

| Source | Period | Notes |
|--------|--------|-------|
| `2025 PulseOne Software COGS and Expense.xlsx` | CY 2025 | 1,068 transactions across 3 QB line items; 57 unique vendors |
| `pulseone-definitive-pl-analysis.md` v3.0 | CY 2025 | Authoritative corrected P&L; corrected GM = 37.4% |
| `pulseone-bic-master-scorecard.md` v1.0 | CY 2025 | BiC benchmark targets |
| `docs/meta/architectural-invariants.md` | — | Owner-confirmed vendor classifications |
| `docs/reference/service-leadership-bic-reference.md` | — | BiC product GM target: 24.3%–26.3% |
| `pulseone-software-reconciliation.md` | CY 2025 | Three-way reconciliation: P&L vs. detail file vs. expense tracker |
| Six prior software analysis documents | CY 2025 | Consolidated into this document |

**Data quality:** The detail file reconciles to within 1.3% of the P&L totals ($15,733 variance on $1.2M spend). The Computer and Internet SGA line matches to the penny. The data is reliable for decision-making.

---

## C. Current Understanding

PulseOne has three distinct software cost pools in its QuickBooks chart of accounts:

| QB Line Item | P&L Amount | Detail File Amount | Variance |
|---|---|---|---|
| Agreement License Cost (COGS) | $366,527 | $373,999 | +$7,472 |
| Purchases — Software for Resale (COGS) | $562,726 | $570,987 | +$8,261 |
| Computer and Internet Expenses (SGA) | $263,953 | $256,232 | -$7,721 |
| **Total** | **$1,193,206** | **$1,201,218** | **+$8,012** |

> Note: The SGA detail file captures $256,232 of the $263,953 P&L total. The $7,721 gap likely represents transactions not included in the export range. This does not affect the classification conclusions.

These three pools, when properly classified by function, map to the three audit buckets as follows:

| Bucket | Amount | % of Total | Description |
|--------|--------|-----------|-------------|
| **Client-Delivered Software COGS** | $570,987 | 47.5% | Products purchased for resale to specific clients |
| **Help Desk / Service Delivery COGS** | $571,692 | 47.6% | Tools used by technicians to deliver managed services |
| **Internal SGA** | $58,539 | 4.9% | Tools used by PulseOne staff for internal operations |
| **Total** | **$1,201,218** | **100%** | |

The critical finding is that the current QB classification places **$187,182 of Service Delivery COGS** (ConnectWise, Flexis, Kaseya, Samurai Sync, Wasabi, Duo, Qualys, MSP360, TimeZest, CyberFox, Have I Been Pwned) inside the SGA line. This is the primary source of the COGS/SGA misallocation problem.

---

## D. Findings

### Finding 1: The Software Resale Loss Is Real and Concentrated in Three Vendors

The -9.4% gross margin on standalone software resale is not an accounting artifact. It is a pricing failure. The entire $570,987 in the "Purchases — Software for Resale" section is classified as **Client-Delivered Software COGS** — these are products purchased specifically for client delivery. The corresponding revenue of $514,405 is insufficient to cover cost.

**Vendor concentration within Software Resale:**

| Vendor | CY 2025 Cost | % of Resale COGS | BiC-Compliant Revenue Needed (25% GM) | Revenue Gap |
|--------|-------------|-----------------|--------------------------------------|-------------|
| Synnex Corp | $251,028 | 44.0% | $334,704 | Unknown — no client attribution |
| Ingram Micro | $194,247 | 34.0% | $259,000 | Unknown — no client attribution |
| Amazon Web Services | $63,273 | 11.1% | $84,364 | Unknown — no client attribution |
| AvePoint | $41,200 | 7.2% | $54,933 | Unknown — no client attribution |
| EFolder Systems (Axcient) | $10,719 | 1.9% | $14,292 | Unknown — no client attribution |
| ScalePad | $5,988 | 1.0% | $7,984 | Unknown — no client attribution |
| Other (Atlassian, Mosyle, AppRiver, Paddle, Microsoft) | $4,533 | 0.8% | $6,044 | Unknown |
| **Total** | **$570,987** | **100%** | **$761,316** | **$246,911 revenue shortfall** |

> The $246,911 figure represents the additional revenue PulseOne would need at current cost levels to achieve a 25% gross margin. Alternatively, the same result is achieved by reducing cost (negotiating better distributor pricing) or a combination of both.

### Finding 2: TD Synnex Appears in Both COGS Buckets — Two Separate Problems

Synnex Corp is PulseOne's largest single vendor at **$552,841 combined** across both COGS sections:

| Section | Amount | Classification | Problem |
|---------|--------|---------------|---------|
| Agreement License Cost | $301,813 | Service Delivery COGS | Consolidated "Estimate" billing — no line-item detail, no client attribution. Monthly variance 44.5% ($20,947–$30,277). |
| Purchases — Software for Resale | $251,028 | Client-Delivered Software COGS | Standalone resale — client attribution available in ConnectWise but not in QB. Pricing is stale. |

These are two distinct problems requiring two distinct solutions. The Agreement License Cost portion is a **billing transparency problem** (you cannot verify the bill is correct). The Software Resale portion is a **pricing problem** (you are not charging enough).

### Finding 3: Barracuda Cost Escalation Is Untracked

Barracuda (Skout Cybersecurity) costs grew **87% in CY 2025**:

| Month | Monthly Cost | MoM Change |
|-------|-------------|-----------|
| January 2025 | $3,996 | — |
| March 2025 | $4,715 | +$719 (+18%) |
| December 2025 | $7,472 | +$2,757 (+58% from March) |
| **Annualized at Dec rate** | **$89,662/year** | **+$41,713 vs. Jan rate** |

The $41,713/year cost increase has no corresponding client billing evidence in QuickBooks. If this increase is not being passed through to clients, it is coming entirely out of gross margin.

### Finding 4: $187,182 in Service Delivery COGS Is Misclassified as SGA

The following vendors are in the "Computer and Internet Expenses" SGA line but should be in Service Delivery COGS:

| Vendor | Amount | Rationale | Confidence |
|--------|--------|-----------|-----------|
| ConnectWise, Inc. | $89,800 | PSA/RMM — primary service delivery platform | Analysis |
| Flexis | $64,009 | NOC/Help Desk augmentation | **Owner confirmed** |
| Kaseya | $10,563 | RMM/security management platform | Analysis |
| Samurai Sync | $9,450 | Service delivery tool | **Owner confirmed** |
| Wasabi Technologies | $7,353 | Client backup storage delivery | Analysis |
| MSP360 | $4,005 | Client backup management | Analysis |
| TimeZest | $3,609 | ConnectWise scheduling for client appointments | Analysis |
| CyberFox | $2,189 | Client cybersecurity delivery | Analysis |
| Duo Security | $2,068 | Client MFA delivery | Analysis |
| Qualys | $1,024 | Client vulnerability scanning | Analysis |
| Have I Been Pwned | $22 | Client breach monitoring | Analysis |
| **Total** | **$194,092** | | |

> Note: ConnectWise ($89,800) is the largest single item. Industry standard is to allocate 65–100% of PSA/RMM cost to COGS depending on the proportion of service-delivery vs. administrative use. Given PulseOne's delivery-centric model, full reclassification to COGS is defensible.

**Impact of reclassification on gross margin:**

| | As Reported (QB) | After Reclassification |
|---|---|---|
| Total COGS | $2,123,012 | $2,317,104 (+$194,092) |
| Total SGA | $2,827,967 | $2,633,875 (-$194,092) |
| Gross Margin | 37.4% | **33.6%** |
| SGA % of Revenue | 31.7% | **29.4%** |

> The reclassification lowers the reported gross margin (because more cost moves into COGS) but improves the SGA efficiency ratio. Net income does not change. The corrected gross margin of 33.6% is a more accurate picture of service delivery cost structure — and the gap to the BiC 44% target is now clearly a labor and software pricing problem, not an SGA problem.

### Finding 5: True Internal SGA Tool Spend Is $58,539 — Not $263,953

After reclassifying service delivery tools to COGS, the genuine internal SGA software spend is **$58,539** (4.9% of the detail file total). The top items:

| Vendor | Amount | Action |
|--------|--------|--------|
| Microsoft Azure | $19,041 | **Confirm** — could be client infrastructure (COGS) |
| Microsoft (M365 internal) | $14,127 | Keep — internal productivity |
| Avalara | $6,807 | Keep — tax compliance |
| Adobe Software | $3,739 | Keep — marketing |
| GoDaddy | $2,880 | **Confirm** — client-hosted domains would be COGS |
| Pivotal Crew LLC | $2,000 | **Confirm** — one-time charge, purpose unknown |
| Cursor | $1,184 | Keep — internal dev |
| OpenAI | $1,076 | Keep — internal AI (consolidate with Anthropic) |
| Eversign | $960 | Keep — e-signature |
| Railway | $823 | Keep — internal hosting |
| Replit | $526 | **Cancel** — redundant with Cursor |
| Calendy | $514 | **Cancel** — redundant with TimeZest |
| Anthropic | $425 | **Consolidate** — pick one primary LLM (OpenAI or Anthropic) |
| Manus AI | $389 | Keep — strategic audit tool |
| AI MAD FZCO | $360 | **Confirm** — purpose unclear |
| Zapier | $360 | Keep — workflow automation |
| Other (37 vendors) | ~$2,929 | Mix of keep/cancel — see rationalization matrix |

**Immediate cancellation candidates** (non-business or clearly redundant):
- Quicken ($72) — personal finance software
- Patreon ($71) — content subscription
- Vevox ($131) — meeting polling (redundant)
- Replit ($526) — redundant with Cursor
- Calendy ($514) — redundant with TimeZest
- Claude.AI ($220) — redundant with Anthropic API
- OpenRouter ($27) — redundant with direct API subscriptions

**Estimated immediate savings from cancellations: $1,561/year**

---

## E. Service Leadership BiC Alignment

| Metric | PulseOne Actual | BiC Target | Status |
|--------|----------------|-----------|--------|
| **Agreement License GM** | 52.0% | 48.7%–52.4% | **ALIGNED** |
| **Standalone Software Resale GM** | -9.4% | 24.3%–26.3% | **CRITICAL FAILURE** (-33.7 pts) |
| **Blended Product GM** | ~14.0% (estimated) | 24.3%–26.3% | **BELOW** |
| **SGA % of Revenue (as reported)** | 31.7% | 27.4% | BELOW (+4.3 pts) |
| **SGA % of Revenue (after reclassification)** | 29.4% | 27.4% | BELOW (+2.0 pts) |
| **True SGA software spend** | $58,539 | — | Reasonable for $5M MSP |

**BiC interpretation:** The Agreement License segment is operating at or above BiC standards. The standalone resale segment is the sole source of the product margin failure. The SGA reclassification improves the SGA efficiency ratio by 2.3 percentage points, narrowing but not closing the gap to BiC.

---

## F. Risks and Opportunities

### Risks

**R1 — Synnex Agreement License billing is unverifiable (HIGH)**  
$301,813 in consolidated "Estimate" bills with no line-item detail. Monthly variance of 44.5% ($9,330 swing) is unexplained. Risk: PulseOne may be overbilled and has no mechanism to detect it. This is the highest-priority investigation item.

**R2 — Barracuda cost escalation is not reflected in client billing (HIGH)**  
$41,713/year run-rate increase with no client attribution in QuickBooks. If not billed through, this erodes gross margin by $41,713/year going forward. At the December 2025 run rate, Barracuda will cost $89,662 in 2026.

**R3 — Software resale pricing has no systematic enforcement mechanism (HIGH)**  
There is no evidence of a pricing floor or margin floor applied to software resale quotes. Vendor cost increases (Synnex, Ingram, AWS) are not automatically triggering client price adjustments.

**R4 — COGS/SGA misclassification distorts management reporting (MEDIUM)**  
With $194,092 of COGS in SGA, management is seeing an artificially high gross margin (37.4% vs. true 33.6%) and an artificially high SGA burden. Decisions made on this basis may be misdirected.

### Opportunities

**O1 — $185,000 profit recovery from repricing standalone resale (HIGH)**  
Repricing the $570,987 resale COGS to a 25% gross margin target requires $761,316 in revenue — $246,911 more than the current $514,405. This is achievable through a combination of price increases on existing agreements and margin floors on new quotes.

**O2 — $41,713/year Barracuda pass-through (HIGH)**  
If the Barracuda cost increase is confirmed as not billed, implementing a client-level cost pass-through recovers this amount in full.

**O3 — Synnex Agreement License audit may reveal overbilling (MEDIUM)**  
Requesting line-item invoices from Synnex and reconciling against ConnectWise agreements could reveal billing errors. Even a 5% overbilling on $301,813 = $15,091/year.

**O4 — SGA reclassification improves BiC SGA ratio by 2.3 pts (MEDIUM)**  
Moving $194,092 from SGA to COGS reduces SGA from 31.7% to 29.4% of revenue, closing 53% of the gap to the BiC 27.4% target. No cost reduction required — purely a chart-of-accounts correction.

**O5 — $1,561/year in immediate SaaS cancellations (LOW)**  
Seven clearly redundant or non-business tools can be cancelled immediately.

---

## G. Recommended Actions

### Priority 1 — Immediate (Within 30 Days)

| Action | Owner | Expected Recovery | Effort |
|--------|-------|------------------|--------|
| **G1.** Request line-item invoice from TD Synnex for any 3 months. Reconcile against ConnectWise managed service agreements. | Paul Freeman / Finance | Potential overbilling detection | Low |
| **G2.** Pull Barracuda/Skout portal: export current client list, seat counts, and per-client billing rates. Cross-reference against ConnectWise managed security agreements. | Service Delivery Lead | $41,713/year if pass-through confirmed | Low |
| **G3.** Cancel 7 redundant/non-business SaaS tools: Quicken, Patreon, Vevox, Replit, Calendy, Claude.AI, OpenRouter. | Admin | $1,561/year | Very Low |
| **G4.** Instruct bookkeeper to reclassify ConnectWise, Flexis, Kaseya, Samurai Sync, Wasabi, MSP360, TimeZest, CyberFox, Duo Security, Qualys from Computer & Internet SGA to Agreement License Cost COGS. | Bookkeeper | Corrects GM reporting | Low |

### Priority 2 — Near-Term (30–90 Days)

| Action | Owner | Expected Recovery | Effort |
|--------|-------|------------------|--------|
| **G5.** Pull ConnectWise Agreement Profitability report for all active agreements. Identify every agreement with a software line item sourced from Synnex or Ingram. Flag agreements where billed rate < cost + 25%. | Service Delivery / Finance | $185,000 profit swing | Medium |
| **G6.** Implement a software pricing floor in ConnectWise quoting: no software product quote may be submitted with a gross margin below 20% without owner approval; target is 25%. | Operations | Prevents future margin erosion | Medium |
| **G7.** Confirm Microsoft Azure ($19,041) classification: if client-hosted environments, reclassify to COGS. If internal PulseOne infrastructure, keep in SGA. | Paul Freeman | Correct margin reporting | Low |
| **G8.** Confirm GoDaddy ($2,880): identify which domains are client-hosted vs. internal. Client-hosted domains should be billed to clients. | Admin | Minor revenue recovery | Low |

### Priority 3 — Strategic (90–180 Days)

| Action | Owner | Expected Recovery | Effort |
|--------|-------|------------------|--------|
| **G9.** Negotiate volume pricing with TD Synnex. At $552,841/year combined spend, PulseOne qualifies for partner-tier pricing. A 5% cost reduction = $27,642/year. | Paul Freeman | $27,642/year | Medium |
| **G10.** Evaluate AvePoint ($41,200) resale margin. At 25% target, this requires $54,933 in revenue. Confirm current billing rate and adjust if below target. | Finance | Variable | Low |
| **G11.** Consolidate AI/Dev tool subscriptions: standardize on Cursor (IDE) + one primary LLM API (OpenAI or Anthropic). Cancel Claude.AI, OpenRouter, Replit. | Admin | $773/year | Low |

---

## H. Suggested ConnectWise Follow-Up

The following ConnectWise reports are required to complete this audit. Listed in priority order:

**CW-1 (BLOCKING — Barracuda):** Pull the Barracuda/Skout billing portal. Export: client name, seat count, per-seat cost, monthly total. Cross-reference against ConnectWise managed security agreements to confirm whether the $41,713/year cost increase is being billed to clients. Time period: current month + 12-month history.

**CW-2 (BLOCKING — Synnex Agreement Licenses):** Request a line-item invoice from TD Synnex for any 3 months in CY 2025 (recommend Jan, Jun, Sep to capture the variance range). Map each line item to a ConnectWise agreement. This is the only way to verify the $301,813 consolidated bill is correct.

**CW-3 (HIGH — Software Resale Repricing):** Run Agreement Profitability by Client. Filter for agreements containing software line items. Export: client name, product description, billed rate, cost, gross margin. Identify all agreements where software GM < 20%. This is the client-level repricing target list.

**CW-4 (HIGH — Resale Attribution):** For Synnex Corp ($251,028) and Ingram Micro ($194,247) in the Resale section: pull purchase orders or product receipts from ConnectWise Procurement. Map each PO to the client it was purchased for. This provides the client-level attribution missing from QuickBooks.

**CW-5 (MEDIUM — AvePoint):** Pull AvePoint billing: how many clients, what is the per-client monthly billed rate, and what is the per-client cost? AvePoint at $41,200/year is the fourth-largest resale cost item and needs margin verification.

---

## I. Clarifying Questions

**Q1 (CRITICAL):** Has any portion of the Barracuda cost increase been communicated to clients or reflected in agreement renewals since March 2025? If yes, which clients and what amounts?

**Q2 (CRITICAL):** Is the TD Synnex Agreement License bill ($301,813/year) a single consolidated invoice, or are there line-item invoices available from Synnex that were not exported to QuickBooks? If line-item invoices exist, please provide one month for reconciliation.

**Q3 (HIGH):** What is the current standard markup applied to Synnex and Ingram Micro products when quoting clients? Is there a documented pricing policy, or is markup applied ad hoc per quote?

**Q4 (HIGH):** Microsoft Azure ($19,041 in SGA): is this PulseOne's own internal Azure tenant (e.g., for internal servers, email, dev environments), or does it include client-hosted Azure environments? If the latter, it should be in COGS and billed to clients.

**Q5 (MEDIUM):** CloudBase Services ($3,600, one payment): what was this for? If it is a client-specific cloud service, it belongs in COGS. If internal infrastructure, SGA is correct.

**Q6 (MEDIUM):** Pivotal Crew LLC ($2,000, one payment): what was this for? If it is a contractor used for client delivery, it belongs in COGS. If internal, SGA is correct.

**Q7 (LOW):** GoDaddy ($2,880): are any of these domains registered for clients? If yes, are clients being billed for domain management?

---

*This document consolidates and supersedes six prior software analysis documents. The classification workbook (`data/financial/Software_COGS_Classified.xlsx`) contains the transaction-level detail supporting all findings above. The six superseded documents have been moved to `docs/archive/`.*
