# PulseOne Definitive P&L Evaluation (CY 2025)

**Status:** Final (Revised April 30, 2026)
**Author:** Manus AI (Strategic Audit Assistant)
**Objective:** Provide a fully reconciled, evidence-based P&L analysis identifying the root causes of the 2025 margin gap against Service Leadership Best in Class (BiC) benchmarks.

---

## 1. Executive Summary

PulseOne’s 2025 normalized EBITDA of **6.3% ($326,303)** represents a **$578,257 profit gap** compared to a Best in Class peer (17.5% target). 

The gap is heavily concentrated in the **True Projects** segment, which operated at a **-27.5% net margin loss** when fully burdened with internal Cost of Delivery (COD) and untracked engineering time. The core Managed Services and Comprehensive Services (staff augmentation) segments are healthy and profitable, but their margins are being dragged down by the structural unprofitability of the project business.

### The Corrected 2025 P&L (Normalized)

| Metric | PulseOne Actual | BiC Target | Gap to BiC |
|---|---|---|---|
| **Revenue** | $5,168,754 | — | — |
| **Gross Margin** | **37.5% ($1.94M)** | 44.0%+ ($2.27M) | **-6.5 pts ($338K)** |
| **SG&A** | **31.2% ($1.61M)** | 27.4% ($1.42M) | **+3.8 pts ($197K)** |
| **Normalized EBITDA** | **6.3% ($326K)** | 17.5% ($905K) | **-11.2 pts ($578K)** |

*(Note: Normalization excludes $80,612 in non-operating expenses for RepScheduler and PulseOne Communications).*

---

## 2. Segment Profitability Breakdown

The most critical finding of the audit is the stark contrast in profitability between the three primary service lines. 

*Note: The Cost of Delivery (COD) overhead—representing project management, coordination, and pre-sales engineering (Kaitlin Harris, Laura Walsh, Steve Calkins, James Froio)—has been allocated 90% to True Projects and 10% to Comprehensive Services based on operational reality.*

| Segment | Revenue | Direct COGS | COD Allocation | Gross Profit | Margin % | BiC Target |
|---|---|---|---|---|---|---|
| **Managed Services** | $2,696,561 | $1,146,881 | — | $1,549,680 | **57.5%** | 48-52% |
| **Comprehensive Services** | $1,514,526 | $854,412 | $23,064 | $637,050 | **42.1%** | 40.0% |
| **True Projects** | $434,818 | $323,756* | $207,573 | -$96,511 | **-22.2%** | 40.0% |
| **Product Resale** | $522,849 | $570,987 | — | -$48,138** | **-9.2%** | 24-26% |

*\* True Projects direct COGS includes $205,419 in subcontractor invoices plus $118,337 in untracked internal engineering time (Vincent Williams, Matthew Barnett, Hagen McDonell).*
*\*\* The Product Resale loss is primarily a revenue attribution artifact in QuickBooks, where software revenue is bundled into MS agreements but the COGS remains in the Product line. ConnectWise data shows actual software margin is healthy (e.g., Barracuda at 35.4%).*

### Key Finding: The Project Subsidy
The **True Projects** segment is structurally unprofitable. For every $1.00 of project revenue billed in 2025, PulseOne spent **$1.22** to deliver it. The profitable Comprehensive Services and Managed Services businesses are heavily subsidizing the project delivery infrastructure.

---

## 3. The "Invisible Subsidy" (Project Margin Collapse)

Services Management previously viewed projects as highly profitable (47.1% cash margin) because QuickBase only tracked external subcontractor invoices. The audit revealed a **$348,973 "invisible subsidy"** of internal W-2 and contractor labor consumed by projects but never tracked against them.

This subsidy breaks down into three tiers:

### Tier 1: Planned Internal Delivery ($71,227)
PulseOne delivered 27 projects (e.g., Barracuda QuickStarts, network refreshes) totaling $71,227 in revenue using 100% internal resources. The strategy was legitimate—using internal capacity to capture 100% gross margin on paper to fund those roles. However, the COGS were never recorded in QuickBase.

### Tier 2: The Plan Shortfall ($47,110)
The internal resources designated to deliver those Tier 1 projects (Vincent Williams, Matthew Barnett, Hagen McDonell) cost **$118,337** in project-allocated time. The $71K in planned revenue was insufficient to cover their cost, resulting in a $47K shortfall.

### Tier 3: Unrecovered Cost of Delivery ($230,637)
The structural overhead required to deliver projects—Project Management (Kaitlin Harris), Service Coordination (Laura Walsh), and Engineering (James Froio, Steve Calkins)—cost $230,637 in project-allocated time. **This Cost of Delivery (COD) was never priced into project quotes.** 

BiC standards dictate that COD should represent ~10% of project revenue, and direct COGS ~50%, leaving a 40% gross margin. PulseOne's COD alone represented **53.0%** of true project revenue. The project volume ($435K) is simply too small to absorb the current delivery infrastructure without significantly higher pricing.

---

## 4. Software COGS & The Synnex Black Box

The audit reconciled the software resale business and identified a major visibility gap regarding Microsoft and Barracuda licensing.

### Barracuda Profitability
Initial concerns that Barracuda was losing money due to unpassed price increases were partially mitigated by TD Synnex purchase data. 
- **CW Revenue:** $323,737
- **Synnex Cost:** $209,123 (monthly recurring licenses)
- **Gross Margin:** **35.4%** (Healthy, exceeds BiC 24% target)

*Note: The $72,960 direct payment to Barracuda/Skout was reclassified as an internal Help Desk SOC tool, not a resale product.*

### The Microsoft Rebate Risk
Microsoft 365 margin appears healthy at 43.4% ($495K revenue vs $302K cost), but this relies on **$22K in backend rebates**. Without rebates, the operational margin drops to 39.0%.

### The Synnex Reconciliation Gap
TD Synnex purchase history shows **$4.55M** in gross Microsoft CSP orders for CY2025. QuickBooks only records **$301,813** in Agreement License Cost to Synnex. This indicates that the TD Synnex portal shows the gross retail value of licenses passing through PulseOne's tenant, while QuickBooks only records the net cost (or potentially just the margin/fee). **A line-item invoice from Synnex remains the most critical missing piece of financial evidence.**

---

## 5. SG&A Inefficiencies

SG&A ran at **31.2%** of revenue, compared to the BiC target of 27.4%. This represents $197,000 in excess overhead.

1. **Sales & Marketing ROI Failure (~$80K):** PulseOne spent $383K (7.4% of revenue) on S&M, slightly above the BiC 7.0% target. However, the mix was entirely wrong. The company employed three highly compensated "closers" (Chad, Marcello, Eric) who generated virtually zero self-sourced pipeline, relying entirely on the CEO's network.
2. **SaaS Tool Sprawl (~$91K):** The company maintained 68 distinct SaaS applications, including 5 overlapping project management tools (QuickBase, Asana, Monday, ConnectWise, MS Project) and 4 distinct documentation platforms.
3. **General Admin (~$26K):** Scattered inefficiencies in finance and admin overhead.

---

## 6. What Could Have Been Done Differently (Hindsight)

If management had perfect visibility in January 2025, the $578K profit gap could have been closed through three specific actions:

1. **Require Fully-Loaded Project Quoting:** If the $231K in Cost of Delivery had been accurately priced into the 58 true projects (requiring roughly 60% higher project pricing), or if internal resources were strictly capped, the project margin would have stabilized at 40%, recovering **$270K** in profit.
2. **Rebalance the Sales Team:** Replacing one unproductive closer with a dedicated SDR/BDR to generate pipeline would have saved **$80K** while actually increasing lead flow.
3. **Rationalize SaaS Tools:** Consolidating the 68 tools down to the core ConnectWise stack would have recovered **$91K** in pure EBITDA.

Combined, these three actions would have recovered **$441,000** (76% of the total gap), pushing PulseOne to a 14.8% EBITDA—within striking distance of Best in Class.
