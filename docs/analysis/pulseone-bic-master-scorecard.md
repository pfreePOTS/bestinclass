# PulseOne Best in Class (BiC) Master Scorecard

**Version:** 4.0  
**Last Updated:** April 22, 2026  
**Author:** Manus AI  
**Source Data:** CY 2025 Definitive Resource Allocation Reference, Corrected P&L (`pulseone-definitive-pl-analysis.md`), Technician Efficiency Audit, Consolidated Software Resale Audit, CS-Cost Detail Report

**Related Documents:**
- [Resource Allocation Reference](pulseone-resource-allocation-reference.md) — Definitive CY 2025 labor inventory
- [Technician Scheduling & Utilization Audit](PulseOne_Technician_Scheduling_and_Utilization_Audit.md) — Scheduling patterns and utilization analysis
- [Profit Waterfall 2025](audit-profit-waterfall-2025.md) — $578K gap decomposition
- [Marketing Investment Data](audit-marketing-investment-data.md) — S&M spend breakdown

## Executive Summary

This scorecard provides the authoritative, single-source-of-truth mapping of PulseOne's financial and operational performance against the Service Leadership Best in Class (BiC) benchmarks for the Infrastructure-Managed Services Predominant Business Model (PBM) [1].

**Version 4.0 incorporates critical owner-confirmed structural corrections:** (a) **EBITDA Normalization:** Partner compensation is confirmed at Fair Market Value, removing the prior $423K add-back and resetting normalized EBITDA to 6.3%; (b) **Entity Separation:** $80.6K in RepScheduler and PulseOne Communications costs have been removed from the operating baseline; (c) **Segment Restructuring:** The $1.2M ARC staff augmentation contract has been isolated into a new "Comprehensive Services" segment; (d) **Direct Delivery Margins:** Segment margins now reflect exact transaction-level subcontractor tracing from the CS-Cost account, and exclude standalone product resale.

---

## 1. Core Profitability Metrics

| Metric | PulseOne Actual (CY 2025) | BiC Target | Variance | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Normalized EBITDA %** | 6.3% | 18.3% - 19.0%+ | -12.0 pts | **CRITICAL** | Corrected: No partner comp add-back (paid at FMV) |
| **Blended Gross Margin %** | 37.6% | 44.0%+ | -6.4 pts | BELOW | Corrected baseline (excludes RS/POC costs) |
| **Total SG&A % of Revenue** | 31.6% | 27.4% | +4.2 pts | BELOW | Corrected baseline (excludes RS/POC costs) |
| **Sales & Marketing % of Revenue** | 6.9% | 5.4% | +1.5 pts | BELOW | $358K spend after removing RS developer costs |

> **Interpretation (v3.0):** The 6.3% normalized EBITDA is the true operating reality of PulseOne. Previous versions artificially inflated this to 12.9% by adding back $423K in partner compensation, which is incorrect under BiC methodology because the partners (CEO, CMO, CFO) are paid at or below Fair Market Value. The true profit gap to BiC is $578K, driven primarily by project margin collapse, S&M overspend, and SaaS tool sprawl.

---

## 2. Segment Gross Margins

| Segment | PulseOne Actual (CY 2025) | BiC Target | Variance | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Managed Services GM %** | 73.1% | 48.7% - 52.4% | +20.7 pts | **EXCEEDS BiC** | Direct delivery margin (labor+tools only); core MSP is highly efficient |
| **Comprehensive Services GM %** | 46.1% | N/A | N/A | **HEALTHY** | ARC staff augmentation ($1.23M rev); exact cost traced from QB detail |
| **Project / Consulting GM %** | 44.0% traceable (24% fully-loaded est.) | 48%–52% | -4.0 to -28.0 pts | **CRITICAL** | $1.17M rev; $343K in sub costs confirmed; gap to 24% is invisible W-2 subsidy |
| **Software GM % (CW transaction view)** | 68.1% | 24.3% - 26.3% | +43.5 pts | **ALIGNED** | True margin per CW; QB -9.4% is a mapping artifact |
| **Microsoft M365 GM %** | ~43.4% | 24.3% - 26.3% | +17.1 pts | **ALIGNED** | $495K CW revenue vs $302K Synnex cost + $22K rebates |
| **Adobe Creative Cloud GM %** | 4.3% | 24.3% - 26.3% | -20.0 pts | **CRITICAL** | Near-zero margin; one-off product sale to ARC |

> **Software Margin Resolution (v4.0):** The previously reported -9.4% software resale margin was a QuickBooks revenue mapping artifact, not a true pricing failure. ConnectWise Cost/Sell data shows 6,704 software/subscription line items generating $2,978,392 in revenue against $949,040 in cost (68.1% GM). Furthermore, the prior claim of a 16.4% M365 margin was based on flawed QB cost mapping; the actual M365 margin is a healthy ~43.4%. The primary structural product issue is the $99K Adobe purchase for ARC at 4.3% margin. Management should track software margin at the ConnectWise agreement level, not the QB P&L level, and treat standalone product sales as entirely separate from Managed Services.

---

## 3. Operational Efficiency & Utilization

| Metric | PulseOne Actual | BiC Target | Variance | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Service Multiple of Labor (Help Desk)** | 5.41x | 2.80x+ | +2.61x | **EXCEEDS BiC** | $2.73M revenue / $505K cost; nearly 2x the BiC target |
| **Managed Services GM %** | 73.1% | 48.7% - 52.4% | +20.7 pts | **EXCEEDS BiC** | Direct delivery margin (labor+tools only); core delivery engine is highly efficient |
| **Technician Billable %** | 23.0% | 65% - 75% | -42.0 pts | **DATA TRAP** | Deceptive in fixed-fee MSP model; Service Multiple is the correct measure |
| **Total Service Delivery Labor % of Revenue** | 35.6% | 25% - 30% | +5.6 to +10.6 pts | ABOVE | $1.838M total; excess likely in Consulting/Projects division |
| **S. Calkins Ticket Share** | 24% of all tickets | N/A | N/A | **KEY-PERSON RISK** | 3,238 of 13,412 non-system tickets handled by one technician |

> **Utilization Assessment (v2.0):** The Technician Efficiency Audit confirms that the 23% billable recovery rate is a "data trap" typical of mature MSPs operating on flat-fee agreements. The correct efficiency measure is the Service Multiple of Labor, where PulseOne's Help Desk team dramatically exceeds the BiC target. However, total service delivery labor at 35.6% of revenue exceeds the BiC 25-30% range by $285K-$544K, indicating that the excess cost is hiding in the Consulting/Projects division, not in the Help Desk.

---

## 4. Client Concentration & Revenue Quality

| Metric | PulseOne Actual | BiC Target | Variance | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Top Client % of Revenue (Arc Research)** | 23.9% ($1.237M) | < 10% - 15% | +8.9 to +13.9 pts | **CRITICAL RISK** | 91.3% agreement revenue; dedicated Upwork resource |
| **Top 2 Clients % of Revenue (Arc + Bunzl)** | 41.8% ($2.16M) | < 25% - 30% | +11.8 to +16.8 pts | **MODERATE RISK** | Bunzl is a portfolio of 6 independent entities |
| **Bunzl Ticket Share** | 46.9% (6,293 tickets) | N/A | N/A | **ANOMALY** | 46.9% of tickets but only 17.9% of revenue |
| **Bunzl Uncaptured Growth** | 10 entities in HubSpot | N/A | N/A | **OPPORTUNITY** | 10 Bunzl subsidiaries not yet under contract |
| **Revenue Growth (YoY CAGR)** | ~5.7% | 16.3%+ | -10.6 pts | BELOW | Based on 2022-2025 CAGR |
| **Revenue Composition — Recurring** | 73.8% | > 70% | N/A | **ALIGNED** | Strong recurring base |
| **Client Retention Rate** | *Unknown* | > 76% | *Unknown* | TBD | Requires ConnectWise historical data |

> **Concentration Risk (v2.1 Update):** The Technician Efficiency Audit originally flagged Bunzl as a severe concentration risk. However, owner clarification confirms that Bunzl is not a monolithic contract. It is a portfolio of 6 distinct subsidiary agreements (Cool Pak, Majestic Glove, Tillman, Cordova Safety, Tingley Rubber, Bunzl Distribution USA), each with its own IT environment and P&L. Therefore, losing the entire Bunzl revenue stream in a single event is unlikely unless driven by a corporate-level IT consolidation mandate. 
> 
> The ticket anomaly (46.9% of tickets vs 17.9% of revenue) must now be investigated at the *subsidiary* level to identify which specific entities are driving the excess load. Furthermore, HubSpot data reveals 10 additional Bunzl subsidiaries (e.g., MCR Safety, SAS Safety Corp) that are not currently under contract, representing a significant organic growth opportunity to leverage the existing corporate relationship.

---

## 5. COGS/SGA Classification Corrections

The consolidated Software Resale Audit identified $194,092 in service delivery tools currently misclassified as SGA in QuickBooks. The following reclassifications have been recommended:

| Vendor | Amount | Current Classification | Recommended | Confidence |
| :--- | :--- | :--- | :--- | :--- |
| ConnectWise, Inc. | $89,800 | SGA | COGS | Analysis |
| Flexis | $64,009 | SGA | COGS | **Owner Confirmed** |
| Kaseya | $10,563 | SGA | COGS | Analysis |
| Samurai Sync | $9,450 | SGA | COGS | **Owner Confirmed** |
| Wasabi Technologies | $7,353 | SGA | COGS | Analysis |
| MSP360 | $4,005 | SGA | COGS | Analysis |
| TimeZest | $3,609 | SGA | COGS | Analysis |
| CyberFox | $2,189 | SGA | COGS | Analysis |
| Duo Security | $2,068 | SGA | COGS | Analysis |
| Qualys | $1,024 | SGA | COGS | Analysis |
| Have I Been Pwned | $22 | SGA | COGS | Analysis |
| **Total** | **$194,092** | | | |

> **Pending confirmations:** Microsoft Azure ($19,041) and GoDaddy ($2,880) require owner input to determine if they are client-hosted (COGS) or internal (SGA).

---

## 6. Profit Leakage Summary (Consolidated)

| Leakage Area | Estimated Annual Impact | Source Audit | Confidence |
| :--- | :--- | :--- | :--- |
| Consulting/Project margin deficit | ~$303K | Profit Waterfall 2025, Project Profitability Audit | Medium — depends on W-2 labor allocation |
| Uncaptured billable revenue | $514K ($16K write-downs + $115K unbilled + $385K unlogged) | Utilization & Billing Audit | Medium |
| S&M overspend vs BiC | $257K | Marketing & Sales Investment Audit | High |
| G&A tool sprawl | $91K | SaaS Tool Sprawl Audit | High |
| **Total estimated leakage** | **~$1.16M–$1.23M** | | |

> **Note:** These leakage areas are not fully additive — some overlap exists between the consulting margin deficit and the uncaptured revenue estimates. The W-2 labor "invisible subsidy" (see Project Profitability Audit) is a primary contributor to the consulting margin deficit but cannot be precisely quantified without ConnectWise time-entry data.

---

## 7. Known Data Gaps & Open Items

| Gap | Impact | Blocking Action(s) | Priority |
| :--- | :--- | :--- | :--- |
| **W-2 Time Entries by Board** | Cannot finalize the exact size of the "invisible subsidy" on projects | Pull CY 2025 time entries for Calkins, Froio, Walsh | P1 |
| **Bunzl Agreement Profitability** | Cannot determine if 46.9% ticket share is profitable | ConnectWise agreement profitability pull | P1 |
| **Amiri Agreement Audit** | Cannot verify Castro's $38K Upwork cost is recovered | ConnectWise agreement profitability pull | P1 |
| **Barracuda Client Pass-Through** | Cannot confirm $41.7K cost increase is billed to clients | Barracuda portal + CW reconciliation | P1 |
| **Client Retention Rate** | Cannot assess BiC retention benchmark | ConnectWise historical agreement data | P2 |
| **Employee Turnover Rate** | Cannot assess BiC turnover benchmark | HR / Payroll historical data | P3 |

---

## References

[1] Service Leadership, Inc., "The Financial Value To Large MSPs of Implementing a Reference Architecture," 2016. https://www-cdn.webroot.com/6615/0473/1278/SL_MSP_Report_2017.pdf
