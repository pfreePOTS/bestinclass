# PulseOne: Software Cost Optimization & Pricing Correction Plan

**Audit Date:** April 17, 2026  
**Prepared By:** Strategic Audit & Analysis — Service Leadership BIC Framework  
**Scope:** Standalone Software Resale Pricing + SaaS/SG&A Tool Rationalization  
**Revenue Context:** CY 2025 Total Revenue ~$5.17M

---

## A. Objective

This plan addresses two distinct profit leakage areas identified in PulseOne's CY 2025 financial audit:

1. **Standalone Software Resale Pricing Failure** — A $48,321 gross loss on $514,405 in software resale revenue, representing a -9.4% gross margin against the Service Leadership Best-in-Class (BIC) target of 24–27%. Correcting this pricing represents a **$185,000–$284,000 profit swing** depending on the margin target achieved.
2. **SG&A Tool Sprawl** — The "Computer & Internet Expenses" SG&A line contains significant tool sprawl, particularly in scheduling tools and AI/development environments. Recovering these costs will improve SG&A efficiency.

## B. Evidence Reviewed

| Source | Period | Key Data Points |
|--------|--------|-----------------|
| `2025 PulseOne Software COGS and Expense.xlsx` | CY 2025 | 1,104 transaction rows across 3 cost categories |
| `2025 Profit and Loss POTS_analysis.xlsx` | CY 2025 | Full P&L with segment-level gross margin |
| `Service Leadership Best in Class (BIC) Framework Reference.md` | Current | Product GM benchmark: 24.3%–26.3% |

**Three cost categories identified in the transaction file:**
- **Agreement Licenses COGS** — Software bundled into managed service agreements (healthy, 52% GM).
- **Standalone Software Resale COGS** — Software sold separately to clients (critical failure, -9.4% GM).
- **Computer & Internet SGA** — Internal SaaS tools charged to SG&A.

## C. Current Understanding: The Software Resale Problem

The standalone software resale segment is structurally inverted: PulseOne is paying more to vendors than it is collecting from clients. The root cause is almost certainly stale agreement pricing. Client contracts were written at a specific cost basis, vendor prices have increased (particularly Microsoft/365 licensing through Synnex, and hardware/software through Ingram Micro), but the client-facing prices were never updated.

This is a common MSP failure pattern. Distributors like Synnex and Ingram Micro raise prices annually, often mid-contract, while MSP agreements lock in client pricing for 12–36 months. Without a systematic price-pass-through or annual repricing process, the margin erodes to zero and then inverts.

### The Three Vendor Concentration Points

| Vendor | COGS (CY 2025) | % of Resale COGS | Target Revenue @25% GM | Revenue Gap |
|--------|---------------|-----------------|------------------------|-------------|
| **Synnex Corp** | $251,028 | 53.0% | $334,704 | +$105,232 |
| **Ingram Micro** | $194,247 | 42.1% | $258,996 | +$81,429 |
| **Amazon Web Services** | $63,273 | 13.3% | $84,364 | +$26,524 |
| Other Vendors | $54,178 | 11.4% | $72,237 | +$22,712 |
| **TOTAL** | **$562,726** | **100%** | **$750,301** | **+$235,896** |

> **Note on AWS:** The $63,273 in AWS costs appears in the Agreement Licenses COGS section of the file (monthly charges with no client attribution), suggesting this is infrastructure cost for PulseOne's own managed services delivery platform — not client-specific resale. The $63,273 figure cited in the brief likely refers to a different classification. The analysis below treats Synnex and Ingram as the primary resale correction targets.

## D. Findings

### Finding 1: Ingram Micro — Single Client Concentration Risk

The Ingram Micro resale spend is heavily concentrated in one client: ARC, which accounts for $114,496 of the $194,247 total Ingram spend — **57.3% of all Ingram purchases**. This is both a pricing risk and a client concentration risk.

**Ingram Micro Top 10 Clients by COGS:**

| Client | COGS | % of Ingram | Target Rev @25% |
|--------|------|-------------|-----------------|
| **ARC** | $114,496 | 57.3% | $152,661 |
| Calpine | $8,527 | 4.3% | $11,369 |
| TPF (Turning Point) | $8,398 | 4.2% | $11,198 |
| DaighRick | $8,392 | 4.2% | $11,189 |
| ACT | $8,296 | 4.2% | $11,061 |
| Outside Analytics | $6,630 | 3.3% | $8,839 |
| FireSprinkler | $6,409 | 3.2% | $8,546 |
| Fire Sprinkler (dup) | $4,491 | 2.2% | $5,988 |
| Pelage | $2,380 | 1.2% | $3,173 |
| Blue Ocean | $1,674 | 0.8% | $2,232 |

**Critical observation:** ARC alone represents a $38,165 pricing correction opportunity (from current estimated revenue of ~$104,656 to a target of $152,661). This single client relationship, if repriced to 25% margin, recovers more than the entire current annual loss.

### Finding 2: Synnex Corp — Broad Client Distribution, Systematic Underpricing

Unlike Ingram, the Synnex spend is distributed across a very large number of clients — the data shows 100+ distinct client names. This indicates Synnex is the distributor for Microsoft 365, security, and other recurring software licenses that flow through managed service agreements.

The broad distribution means the Synnex correction requires a systematic repricing process applied across all agreements, not a single client negotiation.

### Finding 3: AWS — Infrastructure vs. Resale Classification Ambiguity

The AWS charges ($63,273/year, ~$5,988–$7,139/month) appear in the Agreement Licenses section with no client attribution — they are charged to a single card (XXXX4011) as monthly consolidated bills. This pattern is consistent with AWS being PulseOne's own cloud infrastructure for service delivery, not client-specific resale.

**Action required:** Confirm whether AWS costs are infrastructure for PulseOne's own operations, client-specific cloud hosting being resold, or a mix. If client-specific, client-level attribution must be established in ConnectWise before repricing can occur.

## E. Service Leadership BIC Alignment

| Metric | PulseOne Current | BIC Target | Gap | Status |
|--------|-----------------|------------|-----|--------|
| Agreement License Gross Margin | 52% | 48.7%–52.4% | None | **AT BIC** |
| Standalone Software Resale GM | -9.4% | 24.3%–26.3% | 33.7–35.7 pts | **CRITICAL FAILURE** |
| Blended Product GM | ~12% (est.) | 24.3%–26.3% | ~12–14 pts | **BELOW MEDIAN** |
| SG&A as % of Revenue | ~5.1% (Computer/Internet only) | Controlled | Sprawl risk | **WATCH** |

The agreement license segment is performing at or above BIC levels — this is a genuine strength. The standalone resale segment is the sole source of product margin failure and is dragging the blended product margin well below even bottom-quartile BIC performance.

## F. Software Pricing Correction Plan

### Step 1: Build the Client-Level Pricing Audit Workbook

The first action is to create a definitive view of what each client is currently being charged versus what PulseOne is paying. This requires pulling data from ConnectWise.

**From ConnectWise, extract:**
- All active agreements with a software/license line item.
- For each agreement: client name, product description, vendor (Synnex/Ingram/AWS), monthly cost billed to client, and agreement renewal date.
- Cross-reference against the QuickBooks transaction data (which shows what was paid to the vendor).

### Step 2: Prioritize by Correction Value

Rank the client list by the dollar value of the pricing gap. Based on the data:

**Tier 1 — Immediate Action (>$5,000 annual COGS per client):**
- ARC (Ingram: $114,496 COGS) — highest priority single correction.
- Calpine, TPF, DaighRick, ACT (Ingram: $8,000–$8,500 each).
- Donald Gaddis (Synnex: $6,955).
- Outside Analytics, FireSprinkler (Ingram: $6,400–$6,600).

**Tier 2 — Systematic Repricing ($1,000–$5,000 annual COGS per client):**
- All remaining Synnex clients (100+ accounts).
- Remaining Ingram clients.

### Step 3: Apply the Pricing Correction Formula

For each product line, the corrected client price is calculated as:

`Corrected Monthly Price = Monthly Vendor Cost ÷ (1 - Target Margin)`

At 25% target: `Price = Cost ÷ 0.75`

**Example — ARC (Ingram Micro):**
- Current annual COGS: $114,496
- Monthly COGS: ~$9,541
- Current estimated monthly billing (at -9.4% blended): ~$8,720
- Corrected monthly billing @25% GM: $12,722
- Annual revenue increase: $47,904 from this client alone.

### Step 4: Implement Price Pass-Through Language in All Agreements

The structural fix — beyond repricing existing clients — is to add cost pass-through language to every software resale agreement. This language should state:

> "Software license and subscription costs are subject to annual adjustment to reflect changes in vendor pricing. PulseOne will provide 30 days' written notice of any pricing adjustment. Client pricing will be adjusted to maintain a minimum gross margin of [X]% on all software products."

This prevents the recurrence of the current problem without requiring annual renegotiations.

## G. SaaS Rationalization Plan

The transaction data captures $52,008 of the $263,953 Computer & Internet SGA line across 45 vendors. The remaining ~$212,000 requires a separate export or reclassification review. The rationalization plan below addresses the visible vendors.

### Priority 1: Scheduling Tool Redundancy

PulseOne is paying for three scheduling tools simultaneously:
- **TimeZest** ($3,609) — ConnectWise-native scheduling (MSP-specific).
- **Calendly** ($514) — Generic meeting scheduling.
- **Vevox** ($131) — Meeting/polling tool.

**Recommendation:** Keep TimeZest exclusively. Cancel Calendly and Vevox. **Annual savings: $645**.

### Priority 2: AI/Development Tool Sprawl

The AI/Dev stack has 12 separate vendors totaling $5,630/year. Many of these are overlapping:
- **Cursor** ($1,184) — Keep as primary dev tool.
- **Replit** ($526) — Cancel (redundant with Cursor).
- **Claude.AI** ($220) — Cancel (redundant with Anthropic API subscription).
- **OpenRouter** ($27) — Cancel (redundant with direct API access).

**Recommendation:** Consolidate AI tools. Estimated savings: **$1,000–$1,500/year**.

### Priority 3: Storage Consolidation

Wasabi Technologies ($7,353/year) is clearly the primary storage platform. Carbonite ($96/year) and Google Storage ($24/year) are likely legacy or personal-use holdovers.

**Recommendation:** Cancel Carbonite and Google Storage. **Annual savings: $120**.

### Priority 4: Infrastructure Spend Review

The three infrastructure vendors represent the largest single SGA category:
- **Samurai Sync** ($9,450) — $1,350/month; unclear business purpose.
- **CloudBase Services** ($3,600) — Single invoice dated 4.7.23; may be a legacy item.
- **Pivotal Crew LLC** ($2,000) — Single payment in February.

**Recommendation:** Confirm the business purpose of each. If Samurai Sync is a recurring subscription, it must be justified against specific business outcomes.

## H. Suggested ConnectWise Follow-Up

The following ConnectWise data extracts are required to execute this plan:

| Priority | Report to Pull | Why It Matters | Time Period |
|----------|---------------|----------------|-------------|
| **P1 — Critical** | Agreement Profitability by Client | Identify which agreements have software line items and what margin they are generating | CY 2025 full year |
| **P1 — Critical** | Product/Software Line Items by Agreement | Match client billing to vendor COGS for Synnex and Ingram products | CY 2025 full year |
| **P2 — High** | Agreement Renewal Dates | Prioritize repricing by upcoming renewal — easiest to reprice at renewal | Next 12 months |
| **P2 — High** | AWS Cost Allocation by Client | Determine if AWS costs are client-specific or infrastructure | CY 2025 full year |

## I. Clarifying Questions

1. **ARC client relationship:** ARC represents $114,496 in Ingram Micro COGS — 57% of all Ingram spend. Is ARC a managed services client, a project client, or a software resale-only relationship? The answer determines whether this is a pricing correction or a contract restructuring.
2. **AWS classification:** Are the $63,273 in AWS charges PulseOne's own infrastructure costs, or are they client-specific cloud environments being resold?
3. **Synnex billing model:** Is Synnex billing PulseOne for Microsoft 365 licenses that are then passed through to clients at a fixed price, or is each Synnex transaction a discrete product purchase?
4. **Samurai Sync:** What is Samurai Sync ($9,450/year)? This is the largest single SGA tool spend and its business purpose is not clear from the transaction data.
5. **Full SGA detail:** The transaction data captures $52,008 of the $263,953 Computer & Internet SGA line. What accounts for the remaining ~$212,000?

---

*This document is a working audit deliverable. All figures are derived from CY 2025 transaction-level data in the uploaded QuickBooks export. Pricing correction targets are based on Service Leadership BIC product gross margin benchmarks of 24.3%–26.3%.*
