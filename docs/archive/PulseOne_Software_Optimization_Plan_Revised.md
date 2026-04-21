# PulseOne: Software Cost Optimization & Pricing Correction Plan (Revised)

**Audit Date:** April 17, 2026  
**Prepared By:** Strategic Audit & Analysis — Service Leadership BIC Framework  
**Scope:** Standalone Software Resale Pricing, SaaS Rationalization, and COGS/SGA Misallocation  
**Revenue Context:** CY 2025 Total Revenue ~$5.17M

---

## A. Objective

This plan addresses three distinct but related profit leakage and accounting accuracy areas identified in PulseOne's CY 2025 financial audit:

1. **Standalone Software Resale Pricing Failure** — A $48,321 gross loss on $514,405 in software resale revenue, representing a -9.4% gross margin against the Service Leadership Best-in-Class (BIC) target of 24–27%.
2. **SG&A Tool Sprawl** — Redundant and overlapping internal SaaS tools driving up SG&A costs.
3. **Bidirectional Misallocation (COGS vs. SGA)** — Client delivery tools incorrectly booked as internal SG&A overhead, and internal business management tools incorrectly booked as COGS. Correcting these allocations is required to calculate accurate gross margin and SG&A efficiency metrics.

## B. Evidence Reviewed

| Source | Period | Key Data Points |
|--------|--------|-----------------|
| `2025 PulseOne Software COGS and Expense.xlsx` | CY 2025 | 1,104 transaction rows across 3 cost categories |
| `2025 Profit and Loss POTS_analysis.xlsx` | CY 2025 | Full P&L with segment-level gross margin |
| `Service Leadership Best in Class (BIC) Framework Reference.md` | Current | Product GM benchmark: 24.3%–26.3% |

**Three cost categories identified in the transaction file:**
- **Agreement Licenses COGS** — Software bundled into managed service agreements (booked at $366,527).
- **Standalone Software Resale COGS** — Software sold separately to clients (booked at $562,726).
- **Computer & Internet SGA** — Internal SaaS tools charged to SG&A (booked at $263,953; $52,008 captured in detailed transactions).

---

## C. Bidirectional Misallocation Analysis

A detailed review of vendor-level transactions reveals significant misallocation between Cost of Goods Sold (COGS) and Selling, General & Administrative (SG&A) expenses.

In the Service Leadership framework:
- **COGS** includes all tools used to deliver services to clients (RMM, backup, security stack, documentation, ticketing).
- **SG&A** includes tools used to run the business internally (accounting, CRM, internal HR, internal dev).

### Direction 1: SGA Items That Should Be COGS

These are client delivery tools currently buried in internal overhead. Moving these to COGS will decrease SG&A but increase COGS.

| Vendor | Current Booked Amount | Recommended Allocation | Reason |
|--------|----------------------|------------------------|--------|
| **Wasabi Technologies** | $7,353 | Move to COGS | Cloud object storage used for client backup delivery. |
| **Duo Security** | $2,068 | Move to COGS | MFA platform protecting client environments. |
| **Qualys** | $1,024 | Move to COGS | Vulnerability scanning platform for client security. |
| **TimeZest** | $3,609 | Split (lean COGS) | ConnectWise-integrated scheduling tool for technician dispatch. |
| **CyberFox** | $2,189 | Move to COGS (likely) | Cybersecurity tool; confirm if client-facing. |

**Impact:** At least **$10,445** (Wasabi, Duo, Qualys) of current SGA should be reclassified to COGS.

### Direction 2: COGS Items That Should Be SGA

These are internal business management tools currently suppressing gross margin. Moving these to SGA will improve reported gross margin.

| Vendor | Current Booked Amount | Recommended Allocation | Reason |
|--------|----------------------|------------------------|--------|
| **ConnectWise, Inc.** | $89,800 | Split (~65% COGS / 35% SGA) | PSA/RMM platform. Industry standard splits the cost between service delivery (COGS) and business management/sales (SGA). |
| **Atlassian** | $2,962 | Move to SGA | Internal dev/documentation tool (Jira/Confluence). |
| **GoDaddy.com** | $2,880 | Move to SGA (likely) | If these are PulseOne's own domains/hosting, they are SGA. |

**Impact:** Reallocating 35% of ConnectWise to SGA removes **$31,430** from COGS.

### High-Dollar Items Requiring Investigation

Several large expenditures require ConnectWise cross-referencing to determine their true nature:

- **Flexis ($64,009 in COGS):** If this is outsourced/subcontractor labor, it belongs in *Service COGS*, not *Software COGS*. If it is an internal tool, it belongs in SGA.
- **AWS ($73,982 in COGS) & Azure ($19,041 in COGS):** Billed as consolidated monthly charges. If this is PulseOne's own infrastructure (hosting the RMM, internal servers), it belongs in SGA or a separate infrastructure line. If these are client-specific cloud environments, they are COGS.
- **Samurai Sync ($9,450 in SGA):** Unclear business purpose; must be classified based on whether it serves clients or internal ops.

### Net Margin Impact of Reclassifications

Assuming only the high-confidence reclassifications are made:
- COGS increases by **+$10,445** (SGA → COGS)
- COGS decreases by **-$31,430** (COGS → SGA)
- **Net Result:** Software COGS decreases by **$20,985**.
- **Conclusion:** PulseOne's true gross margin is slightly *better* than currently reported, because internal business tools (like the CRM/billing portion of ConnectWise) are currently dragging down the COGS line.

---

## D. The Software Resale Problem

Even with reclassifications, the Standalone Software Resale segment is structurally inverted: PulseOne is paying more to vendors than it is collecting from clients (-9.4% GM). The root cause is stale agreement pricing — vendor costs have increased, but client-facing prices have not.

### The Three Vendor Concentration Points

| Vendor | COGS (CY 2025) | % of Resale COGS | Target Revenue @25% GM | Revenue Gap |
|--------|---------------|-----------------|------------------------|-------------|
| **Synnex Corp** | $251,028 | 53.0% | $334,704 | +$105,232 |
| **Ingram Micro** | $194,247 | 42.1% | $258,996 | +$81,429 |
| **Amazon Web Services** | $63,273 | 13.3% | $84,364 | +$26,524 |
| Other Vendors | $54,178 | 11.4% | $72,237 | +$22,712 |
| **TOTAL** | **$562,726** | **100%** | **$750,301** | **+$235,896** |

### Finding 1: Ingram Micro — Single Client Concentration Risk

The Ingram Micro resale spend is heavily concentrated in one client: **ARC**, which accounts for $114,496 of the $194,247 total Ingram spend (57.3%). 

ARC alone represents a **$38,165 pricing correction opportunity** (from current estimated revenue of ~$104,656 to a target of $152,661). This single client relationship, if repriced to 25% margin, recovers nearly the entire current annual loss.

### Finding 2: Synnex Corp — Broad Client Distribution

Unlike Ingram, the Synnex spend is distributed across 100+ distinct clients. This indicates Synnex is the distributor for Microsoft 365, security, and other recurring software licenses. The broad distribution means the Synnex correction requires a systematic repricing process applied across all agreements, not a single client negotiation.

---

## E. Service Leadership BIC Alignment

| Metric | PulseOne Current (Reported) | BIC Target | Status |
|--------|----------------------------|------------|--------|
| Agreement License GM | 52% | 48.7%–52.4% | **AT BIC** |
| Standalone Resale GM | -9.4% | 24.3%–26.3% | **CRITICAL FAILURE** |
| Blended Product GM | ~12% (est.) | 24.3%–26.3% | **BELOW MEDIAN** |

The agreement license segment is performing at or above BIC levels — this is a genuine strength. The standalone resale segment is the sole source of product margin failure.

---

## F. Software Pricing Correction Plan

### Step 1: Build the Client-Level Pricing Audit Workbook

**From ConnectWise, extract:**
- All active agreements with a software/license line item.
- For each agreement: client name, product description, vendor (Synnex/Ingram/AWS), monthly cost billed to client, and agreement renewal date.
- Cross-reference against the QuickBooks transaction data.

### Step 2: Prioritize by Correction Value

**Tier 1 — Immediate Action (>$5,000 annual COGS per client):**
- ARC (Ingram: $114,496 COGS) — highest priority single correction.
- Calpine, TPF, DaighRick, ACT (Ingram: $8,000–$8,500 each).
- Donald Gaddis (Synnex: $6,955).
- Outside Analytics, FireSprinkler (Ingram: $6,400–$6,600).

**Tier 2 — Systematic Repricing ($1,000–$5,000 annual COGS per client):**
- All remaining Synnex clients (100+ accounts).
- Remaining Ingram clients.

### Step 3: Apply the Pricing Correction Formula

`Corrected Monthly Price = Monthly Vendor Cost ÷ (1 - Target Margin)`

At 25% target: `Price = Cost ÷ 0.75`

### Step 4: Implement Price Pass-Through Language in All Agreements

Add cost pass-through language to every software resale agreement to prevent recurrence:

> "Software license and subscription costs are subject to annual adjustment to reflect changes in vendor pricing. PulseOne will provide 30 days' written notice of any pricing adjustment. Client pricing will be adjusted to maintain a minimum gross margin of [X]% on all software products."

---

## G. SaaS Rationalization Plan

The transaction data captures $52,008 of the $263,953 Computer & Internet SGA line across 45 vendors. The rationalization plan below addresses the visible vendors.

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

---

## H. Suggested ConnectWise Follow-Up

The following ConnectWise data extracts are required to execute this plan:

| Priority | Report to Pull | Why It Matters | Time Period |
|----------|---------------|----------------|-------------|
| **P1 — Critical** | Agreement Profitability by Client | Identify which agreements have software line items and what margin they are generating | CY 2025 full year |
| **P1 — Critical** | Product/Software Line Items by Agreement | Match client billing to vendor COGS for Synnex and Ingram products | CY 2025 full year |
| **P2 — High** | Agreement Renewal Dates | Prioritize repricing by upcoming renewal — easiest to reprice at renewal | Next 12 months |
| **P2 — High** | AWS Cost Allocation by Client | Determine if AWS costs are client-specific or infrastructure | CY 2025 full year |

## I. Clarifying Questions

1. **ARC client relationship:** ARC represents $114,496 in Ingram Micro COGS — 57% of all Ingram spend. Is ARC a managed services client, a project client, or a software resale-only relationship?
2. **Flexis classification:** What is the $64,009 Flexis spend in COGS? Is this subcontractor labor (Service COGS) or a software platform?
3. **AWS/Azure classification:** Are the $73,982 in AWS charges and $19,041 in Azure charges PulseOne's own infrastructure costs, or are they client-specific cloud environments being resold?
4. **Synnex billing model:** Is Synnex billing PulseOne for Microsoft 365 licenses that are then passed through to clients at a fixed price, or is each Synnex transaction a discrete product purchase?
5. **Samurai Sync:** What is Samurai Sync ($9,450/year in SGA)? Its business purpose is not clear from the transaction data.
6. **Full SGA detail:** The transaction data captures $52,008 of the $263,953 Computer & Internet SGA line. What accounts for the remaining ~$212,000?

---

*This document is a working audit deliverable. All figures are derived from CY 2025 transaction-level data in the uploaded QuickBooks export. Pricing correction targets are based on Service Leadership BIC product gross margin benchmarks of 24.3%–26.3%.*
