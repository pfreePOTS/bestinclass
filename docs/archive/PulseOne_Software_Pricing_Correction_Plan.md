# PulseOne: Software Cost Optimization & Pricing Correction Plan
**Audit Date:** April 17, 2026  
**Prepared By:** Strategic Audit & Analysis — Service Leadership BIC Framework  
**Scope:** Standalone Software Resale Pricing + SaaS/SG&A Tool Rationalization  
**Revenue Context:** CY 2025 Total Revenue ~$5.17M

---

## A. Objective

This plan addresses two distinct but related profit leakage areas identified in PulseOne's CY 2025 financial audit:

1. **Standalone Software Resale Pricing Failure** — A $48,321 gross loss on $514,405 in software resale revenue, representing a -9.4% gross margin against the Service Leadership Best-in-Class (BIC) target of 24–27%. Correcting this pricing represents a **$185,000–$284,000 profit swing** depending on the margin target achieved.

2. **SG&A Tool Sprawl** — The "Computer & Internet Expenses" SG&A line contains 45+ discrete SaaS vendors with significant redundancy, particularly in scheduling tools and AI/development environments. Estimated recoverable savings: **$30,000–$50,000 annually**.

---

## B. Evidence Reviewed

| Source | Period | Key Data Points |
|--------|--------|-----------------|
| 2025 PulseOne Software COGS and Expense.xlsx | CY 2025 | 1,104 transaction rows across 3 cost categories |
| 2025 Profit and Loss POTS_analysis.xlsx | CY 2025 | Full P&L with segment-level gross margin |
| Service Leadership BIC Framework Reference | Current | Product GM benchmark: 24.3%–26.3% |

**Three cost categories identified in the file:**
- **Agreement Licenses COGS** — Software bundled into managed service agreements (healthy, 52% GM)
- **Standalone Software Resale COGS** — Software sold separately to clients (critical failure, -9.4% GM)
- **Computer & Internet SGA** — Internal SaaS tools charged to SG&A

---

## C. Current Understanding: The Software Resale Problem

### Why This Loss Exists

The standalone software resale segment is structurally inverted: PulseOne is paying **more to vendors than it is collecting from clients**. The root cause is almost certainly **stale agreement pricing** — client contracts were written at a specific cost basis, vendor prices have increased (particularly Microsoft/365 licensing through Synnex, and hardware/software through Ingram Micro), but the client-facing prices were never updated.

This is an extremely common MSP failure pattern. Distributors like Synnex and Ingram Micro raise prices annually, often mid-contract, while MSP agreements lock in client pricing for 12–36 months. Without a systematic price-pass-through or annual repricing process, the margin erodes to zero and then inverts.

### The Three Vendor Concentration Points

| Vendor | COGS (CY 2025) | % of Resale COGS | Revenue Needed @25% GM | Revenue Gap |
|--------|---------------|-----------------|------------------------|-------------|
| **Synnex Corp** | $251,028 | 53.0% | $334,704 | +$105,232 |
| **Ingram Micro** | $194,247 | 42.1% | $258,996 | +$81,429 |
| **Amazon Web Services** | $63,273 | 13.3% | $84,364 | +$26,524 |
| Other Vendors | $54,178 | 11.4% | $72,237 | +$22,712 |
| **TOTAL** | **$562,726** | **100%** | **$750,301** | **+$235,896** |

> **Note on AWS:** The $63,273 in AWS costs appears in the Agreement Licenses COGS section of the file (monthly charges with no client attribution), suggesting this is infrastructure cost for PulseOne's own managed services delivery platform — not client-specific resale. The $63,273 figure cited in your brief likely refers to a different classification. The analysis below treats Synnex and Ingram as the primary resale correction targets.

---

## D. Findings

### Finding 1: Ingram Micro — Single Client Concentration Risk

The Ingram Micro resale spend is **heavily concentrated in one client: ARC**, which accounts for $114,496 of the $194,247 total Ingram spend — **57.3% of all Ingram purchases**. This is both a pricing risk and a client concentration risk.

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

**Critical observation:** ARC alone represents a $38,165 pricing correction opportunity (from current estimated revenue of ~$104,656 to target of $152,661). This single client relationship, if repriced to 25% margin, recovers more than the entire current annual loss.

### Finding 2: Synnex Corp — Broad Client Distribution, Systematic Underpricing

Unlike Ingram, the Synnex spend is distributed across a very large number of clients — the data shows 100+ distinct client names. This indicates Synnex is the distributor for Microsoft 365, security, and other recurring software licenses that flow through managed service agreements. The top clients by Synnex COGS are:

| Client | COGS | Target Rev @25% |
|--------|------|-----------------|
| Donald Gaddis | $6,955 | $9,274 |
| Nahanni Butte | $4,649 | $6,199 |
| ChampionPayer | $3,199 | $4,265 |
| Pronoia | $3,180 | $4,240 |
| CustomBrokerage | $3,014 | $4,019 |
| Abundant Life | $2,972 | $3,963 |
| DougNewbornLaw | $2,603 | $3,471 |
| Invapharm | $2,554 | $3,405 |
| FirmoConstruction | $2,427 | $3,236 |
| 28 Gorilla | $2,382 | $3,176 |

The broad distribution means the Synnex correction requires a **systematic repricing process** applied across all agreements, not a single client negotiation.

### Finding 3: AWS — Infrastructure vs. Resale Classification Ambiguity

The AWS charges ($63,273/year, ~$5,988–$7,139/month) appear in the Agreement Licenses section with no client attribution — they are charged to a single card (XXXX4011) as monthly consolidated bills. This pattern is consistent with AWS being PulseOne's own cloud infrastructure for service delivery, not client-specific resale.

**Action required:** Confirm whether AWS costs are (a) infrastructure for PulseOne's own operations, (b) client-specific cloud hosting being resold, or (c) a mix. If (b) or (c), client-level attribution must be established in ConnectWise before repricing can occur.

### Finding 4: AvePoint — Hidden Resale Item

AvePoint ($15,508 in resale COGS, $25,692 in agreement licenses COGS) appears in both categories. The resale portion likely represents AvePoint licenses sold to clients outside of managed agreements. These should be reviewed for margin and potentially migrated into agreement bundles.

---

## E. Service Leadership BIC Alignment

| Metric | PulseOne Current | BIC Target | Gap | Status |
|--------|-----------------|------------|-----|--------|
| Agreement License Gross Margin | 52% | 48.7%–52.4% | None | **AT BIC** |
| Standalone Software Resale GM | -9.4% | 24.3%–26.3% | 33.7–35.7 pts | **CRITICAL FAILURE** |
| Blended Product GM | ~12% (est.) | 24.3%–26.3% | ~12–14 pts | **BELOW MEDIAN** |
| SG&A as % of Revenue | ~5.1% (Computer/Internet only) | Controlled | Sprawl risk | **WATCH** |

The agreement license segment is performing at or above BIC levels — this is a genuine strength. The standalone resale segment is the sole source of product margin failure and is dragging the blended product margin well below even bottom-quartile BIC performance.

---

## F. Software Pricing Correction Plan

### Step 1: Build the Client-Level Pricing Audit Workbook

The first action is to create a definitive view of what each client is currently being charged versus what PulseOne is paying. This requires pulling data from ConnectWise.

**From ConnectWise, extract:**
- All active agreements with a software/license line item
- For each agreement: client name, product description, vendor (Synnex/Ingram/AWS), monthly cost billed to client, and agreement renewal date
- Cross-reference against the QuickBooks transaction data (which shows what was paid to the vendor)

**Output:** A spreadsheet with columns:
`Client | Vendor | Product | Monthly COGS | Monthly Client Charge | Current GM% | Target Price @25% | Price Delta | Agreement Renewal Date | Priority`

### Step 2: Prioritize by Correction Value

Rank the client list by the dollar value of the pricing gap. Based on the data:

**Tier 1 — Immediate Action (>$5,000 annual COGS per client):**
- ARC (Ingram: $114,496 COGS) — highest priority single correction
- Calpine, TPF, DaighRick, ACT (Ingram: $8,000–$8,500 each)
- Donald Gaddis (Synnex: $6,955)
- Outside Analytics, FireSprinkler (Ingram: $6,400–$6,600)

**Tier 2 — Systematic Repricing ($1,000–$5,000 annual COGS per client):**
- All remaining Synnex clients (100+ accounts)
- Remaining Ingram clients

**Tier 3 — Review and Migrate:**
- AvePoint resale items
- AppRiver, ScalePad, Mosyle, Paddle.net (small amounts, confirm pricing)

### Step 3: Apply the Pricing Correction Formula

For each product line, the corrected client price is calculated as:

```
Corrected Monthly Price = Monthly Vendor Cost ÷ (1 - Target Margin)

At 25% target:  Price = Cost ÷ 0.75
At 27% target:  Price = Cost ÷ 0.73
```

**Example — ARC (Ingram Micro):**
- Current annual COGS: $114,496
- Monthly COGS: ~$9,541
- Current estimated monthly billing (at -9.4% blended): ~$8,720
- Corrected monthly billing @25% GM: $12,722
- Annual revenue increase: $47,904 from this client alone

### Step 4: Implement Price Pass-Through Language in All Agreements

The structural fix — beyond repricing existing clients — is to add **cost pass-through language** to every software resale agreement. This language should state:

> "Software license and subscription costs are subject to annual adjustment to reflect changes in vendor pricing. PulseOne will provide 30 days' written notice of any pricing adjustment. Client pricing will be adjusted to maintain a minimum gross margin of [X]% on all software products."

This prevents the recurrence of the current problem without requiring annual renegotiations.

### Step 5: Establish Monthly Margin Monitoring

Once repriced, monitor the standalone software resale margin monthly in ConnectWise (Agreement Profitability report). Flag any agreement where the software margin drops below 20% for immediate review.

---

## G. Pricing Correction Financial Model

### Scenario Analysis

| Scenario | Target GM | Required Revenue | Revenue Increase | Annual Profit Swing |
|----------|-----------|-----------------|-----------------|---------------------|
| **Minimum Fix** (BIC floor) | 24% | $740,429 | +$226,024 | +$274,345 |
| **BIC Target** | 25% | $750,301 | +$235,896 | +$284,217 |
| **BIC Best** | 27% | $770,858 | +$256,453 | +$304,774 |
| **Current State** | -9.4% | $514,405 | — | -$48,321 |

> The $185,000 figure referenced in your brief represents a conservative estimate. The full correction to 25% GM represents a **$284,217 swing** from the current -$48,321 loss to a +$140,576 profit on this segment alone.

### Implementation Timeline

| Phase | Action | Timeline | Expected Impact |
|-------|--------|----------|-----------------|
| **Week 1–2** | Pull ConnectWise agreement data; build pricing audit workbook | Immediate | Baseline established |
| **Week 3** | Reprice ARC (Ingram) — single largest correction | Week 3 | ~$47,904/year recovered |
| **Week 4–6** | Reprice all Tier 1 clients (>$5K COGS) | 30 days | ~$120,000–$140,000/year |
| **Month 2–3** | Systematic repricing of all Tier 2 clients | 60–90 days | Remaining $95,000–$115,000 |
| **Month 3** | Add cost pass-through language to new agreements | Ongoing | Prevents future recurrence |
| **Month 4** | Monthly margin monitoring dashboard live in ConnectWise | Month 4 | Ongoing protection |

---

## H. SaaS Rationalization Plan

### Current State: 45 Vendors, $52,008 in Tracked SGA Tools

> **Important note on the $263,953 figure:** The transaction-level data in the COGS/Expense file captures $52,008 in Computer & Internet SGA. The remaining ~$211,945 difference from the P&L figure of $263,953 likely includes items booked through other payment methods, allocated overhead, or categories not captured in this specific export. The rationalization plan below addresses the 45 vendors visible in the data.

### Tool Inventory by Category

| Category | Annual Spend | Vendors | Rationalization Action |
|----------|-------------|---------|----------------------|
| **Infrastructure** | $15,050 | Samurai Sync ($9,450), CloudBase ($3,600), Pivotal Crew ($2,000) | **Review** — confirm business purpose and necessity |
| **Tax/Finance** | $6,878 | Avalara ($6,807), Quicken ($72) | **Keep** — Avalara is compliance-critical |
| **Storage/Backup** | $7,473 | Wasabi ($7,353), Carbonite ($96), Google Storage ($24) | **Consolidate** — Wasabi is primary; cancel Carbonite |
| **Security/Compliance** | $5,303 | CyberFox ($2,189), Duo ($2,068), Qualys ($1,024), HIBP ($22) | **Review** — confirm no overlap with client-billed security tools |
| **AI/Dev Tools** | $5,630 | 12 vendors (see below) | **Major consolidation opportunity** |
| **Design/Creative** | $4,046 | Adobe ($3,739), Figma ($97), Frame.io ($210) | **Keep Adobe; evaluate Figma/Frame.io usage** |
| **Scheduling/Calendar** | $4,254 | TimeZest ($3,609), Calendly ($514), Vevox ($131) | **ELIMINATE REDUNDANCY — keep one** |
| **Automation** | $564 | Zapier ($360), Cognito ($204) | **Keep if actively used** |
| **Project/Collab** | $1,248 | Monday.com ($288), Eversign ($960) | **Keep if actively used** |
| **Learning/Content** | $368 | LearnDash ($199), Patreon ($71), DiviBooster ($39), WP Rocket ($59) | **Cancel or justify** |
| **Other** | $903 | Google ($352), Iron Software ($249), Reincubate ($100), etc. | **Audit individually** |

### Priority 1: Scheduling Tool Redundancy — Immediate $4,123 Savings

PulseOne is paying for **three scheduling tools simultaneously**:

| Tool | Annual Cost | Primary Use |
|------|-------------|-------------|
| **TimeZest** | $3,609 | ConnectWise-native scheduling (MSP-specific) |
| **Calendly** | $514 | Generic meeting scheduling |
| **Vevox** | $131 | Meeting/polling tool |

**Recommendation:** Keep TimeZest exclusively. It is the only tool purpose-built for MSP dispatch and ConnectWise integration. Cancel Calendly and Vevox. **Annual savings: $645** (Calendly + Vevox).

> Note: If TimeZest is not being used for its ConnectWise integration, reconsider — but the answer is to use it properly, not to keep Calendly alongside it.

### Priority 2: AI/Development Tool Sprawl — $3,000–$4,000 Rationalization Opportunity

The AI/Dev stack has 12 separate vendors totaling $5,630/year. Many of these are overlapping or experimental:

| Vendor | Annual Cost | Category | Action |
|--------|-------------|----------|--------|
| Cursor | $1,184 | AI code editor | **Keep** — primary dev tool |
| OpenAI | $1,076 | LLM API | **Keep** — if actively used in production |
| Railway | $823 | Cloud deployment | **Keep if active** — evaluate vs. existing infrastructure |
| Replit | $526 | Cloud IDE | **Evaluate** — likely redundant with Cursor |
| Anthropic | $425 | LLM API | **Consolidate** — likely redundant with OpenAI |
| Manus AI | $389 | AI assistant | **Evaluate** — confirm active use |
| AI MAD FZCO | $360 | Unknown | **Investigate** — unclear business purpose |
| RapidAPI | $261 | API marketplace | **Keep if active** |
| Scrapfly | $230 | Web scraping | **Evaluate** — confirm active use |
| Claude.AI | $220 | LLM (Anthropic) | **Redundant with Anthropic API** — cancel |
| OpenRouter | $27 | LLM routing | **Likely redundant** — cancel |
| PromptSMRT | $109 | Prompt tool | **Evaluate** |

**Consolidation logic:** If Cursor is the primary development environment, Replit is redundant. Claude.AI (the consumer product) is redundant if Anthropic API is already in use. OpenRouter is redundant if direct API access exists. Estimated savings from AI consolidation: **$1,000–$1,500/year**.

### Priority 3: Storage Consolidation — $120 Immediate Savings

Wasabi Technologies ($7,353/year) is clearly the primary storage platform. Carbonite ($96/year) and Google Storage ($24/year) are likely legacy or personal-use holdovers. Cancel both. **Annual savings: $120**.

### Priority 4: Infrastructure Spend Review — $15,050 Requires Justification

The three infrastructure vendors represent the largest single SGA category:

| Vendor | Annual Cost | Notes |
|--------|-------------|-------|
| **Samurai Sync** | $9,450 | $1,350/month — unclear business purpose from data |
| **CloudBase Services** | $3,600 | Single invoice dated 4.7.23 — may be a one-time or legacy item |
| **Pivotal Crew LLC** | $2,000 | Single payment in February |

**Action required:** Confirm the business purpose of each. If Samurai Sync is a recurring $1,350/month subscription, it must be justified against specific business outcomes. If CloudBase is a legacy item from 2023 that was incorrectly booked to 2025, it should be reclassified.

### SaaS Rationalization Decision Framework

For every tool under $5,000/year, apply this three-question test:

1. **Is it actively used?** (Check login logs, usage reports, or ask the team)
2. **Does it duplicate functionality of another tool we already pay for?**
3. **Is it client-billable or internal-only?**

If the answer to question 1 is "no," cancel immediately.  
If the answer to question 2 is "yes," cancel the lower-value tool.  
If the answer to question 3 is "internal-only," apply a stricter justification standard.

### SaaS Rationalization Summary — Estimated Savings

| Category | Action | Estimated Annual Savings |
|----------|--------|--------------------------|
| Scheduling redundancy (Calendly + Vevox) | Cancel | $645 |
| AI/Dev consolidation (Claude.AI, OpenRouter, Replit, AI MAD FZCO) | Cancel/Consolidate | $1,133–$1,493 |
| Storage (Carbonite, Google Storage) | Cancel | $120 |
| Infrastructure review (Samurai Sync, CloudBase) | Justify or cancel | $0–$13,050 |
| Other low-use tools (LearnDash, Patreon, DiviBooster, Vevox, SessionBox) | Cancel | $469 |
| **Conservative total** | | **$2,367–$15,777** |
| **If Samurai Sync is unjustified** | | **Up to $15,777** |

> The $30,000–$50,000 savings estimate in your brief likely refers to the full $263,953 SGA line, which includes items not captured in this export. The rationalization framework above should be applied to the complete vendor list once the full SGA detail is available.

---

## I. Service Leadership BIC Alignment Summary

### Product Gross Margin

The BIC benchmark for product gross margin is **24.3%–26.3%**. PulseOne's current blended product margin is approximately **12%** (weighted average of +52% agreement licenses and -9.4% standalone resale). Correcting the standalone resale pricing to 25% GM would bring the blended product margin to approximately **40%**, which would exceed BIC standards.

### SG&A Efficiency

BIC firms maintain total SG&A at **27.4% of revenue**. The Computer & Internet SGA line alone represents approximately 5.1% of PulseOne's $5.17M revenue. While this is not excessive in isolation, tool sprawl creates operational friction, security surface area, and management overhead that compounds across the organization. The BIC principle here is not just cost reduction — it is **standardization and discipline** in the technology stack, which mirrors the Reference Architecture principle applied to client-facing services.

---

## J. Suggested ConnectWise Follow-Up

The following ConnectWise data extracts are required to execute this plan:

| Priority | Report to Pull | Why It Matters | Time Period |
|----------|---------------|----------------|-------------|
| **P1 — Critical** | Agreement Profitability by Client | Identify which agreements have software line items and what margin they are generating | CY 2025 full year |
| **P1 — Critical** | Product/Software Line Items by Agreement | Match client billing to vendor COGS for Synnex and Ingram products | CY 2025 full year |
| **P2 — High** | Agreement Renewal Dates | Prioritize repricing by upcoming renewal — easiest to reprice at renewal | Next 12 months |
| **P2 — High** | AWS Cost Allocation by Client | Determine if AWS costs are client-specific or infrastructure | CY 2025 full year |
| **P3 — Medium** | AvePoint License Allocation | Confirm which clients have AvePoint licenses and at what price | Current |

**Specific ConnectWise query to run:**  
In ConnectWise Manage → Finance → Agreement Profitability Report → Filter by "Product/Software" type → Export to Excel → Cross-reference vendor names against the QuickBooks COGS data.

---

## K. Clarifying Questions

1. **ARC client relationship:** ARC represents $114,496 in Ingram Micro COGS — 57% of all Ingram spend. Is ARC a managed services client, a project client, or a software resale-only relationship? The answer determines whether this is a pricing correction or a contract restructuring.

2. **AWS classification:** Are the $63,273 in AWS charges PulseOne's own infrastructure costs (e.g., hosting the RMM platform, backup infrastructure), or are they client-specific cloud environments being resold? This changes both the pricing strategy and the margin calculation.

3. **Synnex billing model:** Is Synnex billing PulseOne for Microsoft 365 licenses that are then passed through to clients at a fixed price, or is each Synnex transaction a discrete product purchase? If it is Microsoft 365, the correction is to update the per-seat pricing in all agreements. If it is discrete purchases, the correction requires a quote-level markup policy.

4. **Samurai Sync:** What is Samurai Sync ($9,450/year, $1,350/month)? This is the largest single SGA tool spend and its business purpose is not clear from the transaction data.

5. **Full SGA detail:** The transaction data captures $52,008 of the $263,953 Computer & Internet SGA line. What accounts for the remaining ~$212,000? Is this in a separate QuickBooks category, allocated from payroll, or captured in a different report?

---

*This document is a working audit deliverable. All figures are derived from CY 2025 transaction-level data in the uploaded QuickBooks export. Pricing correction targets are based on Service Leadership BIC product gross margin benchmarks of 24.3%–26.3%.*
