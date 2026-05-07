# PulseOne BiC Gap Attribution Analysis
**Date:** April 23, 2026  
**Status:** DEFINITIVE — Confidence-Graded Analysis  
**Prepared by:** Manus (PulseOne BiC Audit)

## A. Objective
This document answers the core question: **"We know the overall EBITDA gap is ~11.2 points ($578K), but how much of that gap is definitively proven vs. estimated, and where exactly does it live?"**

While previous reclassification work (moving labor to COGS, separating RepScheduler/POC entities) correctly established the *overall* operating baseline, the segment-level attribution of the resulting gap remains partially estimated. This document separates hard facts from derived estimates and defines exactly what data is needed to close the remaining unknowns.

---

## B. The Overall Baseline (High Confidence)
After all owner-confirmed corrections (removing $80.6K in separate entity costs and removing the $423K partner compensation add-back because it is paid at FMV), the overall operating baseline is locked.

| Metric | PulseOne Actual (CY 2025) | BiC Target (at $5.17M Rev) | Gap to BiC |
|---|---|---|---|
| **Total Revenue** | $5,168,754 | N/A | — |
| **Blended Gross Margin** | 38.5% ($1,992,117)* | 44.0% ($2,274,252) | **-$282,135** (5.5 pts) |
| **Total SG&A** | 31.6% ($1,634,707) | 27.4% ($1,416,239) | **+$218,468** (4.2 pts) |
| **Normalized EBITDA** | 6.3% ($326,275) | 17.5% ($904,532) | **-$578,257** (11.2 pts) |

*\*Note: Blended GM reflects the v3.1 COGS validation fix, which corrected a $60K overstatement in Upwork COGS.*

**Conclusion:** The 11.2-point EBITDA gap is driven by a combination of low gross margin (missing 5.5 points) and high SG&A overhead (overspending by 4.2 points).

---

## C. Gap Attribution: What We Know vs. What We Estimate

We can currently attribute 82% of the $578K profit gap to three specific areas. However, our confidence in *why* those gaps exist varies by segment.

### 1. Consulting / Projects Margin Gap: ~$303,159
* **PulseOne Actual:** 24.2% GM (estimated fully-loaded) on $1.17M revenue
* **BiC Target:** 50.0% GM
* **Confidence Grade: LOW (Estimated)**

**The Reality:** The 24.2% margin is a P&L allocation estimate, not a direct measurement. We know from QuickBase that true projects operate at a 47.1% *Cash Margin* (revenue minus out-of-pocket subcontractor invoices). The gap between 47.1% and 24.2% is the "invisible subsidy" of W-2 labor and Upwork escalations (like Vincent Williams) being consumed by projects but not tracked against them. 

**To lock this down:** We must pull ConnectWise time entries to see exactly how many W-2 hours were spent on discrete project boards. If W-2 labor was heavily utilized, the 24.2% estimate is correct (or even too high). If W-2 labor was rarely used, the project margin is actually much healthier, and the missing profit is hiding in the Help Desk.

### 2. Sales & Marketing Overspend: ~$79,731
* **PulseOne Actual:** 6.9% of revenue ($358,844)
* **BiC Target:** 5.4% of revenue ($279,112)
* **Confidence Grade: HIGH (Proven)**

**The Reality:** After removing the RepScheduler developer costs, the true S&M spend is $358K. The issue is not just the $80K overspend against the BiC target; it is the ROI failure of the spend. This investment produced a 16.2% decline in Managed Services revenue in CY 2025. This gap is definitive and structural.

### 3. SaaS Tool Sprawl: ~$91,000
* **PulseOne Actual:** 49 vendors in Computer & Internet Expenses
* **BiC Target:** N/A (General G&A efficiency)
* **Confidence Grade: HIGH (Proven)**

**The Reality:** Vendor-by-vendor analysis identified ~$91K in redundant or overlapping licenses (e.g., dual RMMs, overlapping security tools) that can be rationalized without impacting service delivery.

### 4. The Unidentified Remainder: ~$104,365
* **Confidence Grade: UNKNOWN (The Black Box)**

**The Reality:** After accounting for the project margin collapse, the S&M overspend, and the SaaS tool sprawl, there is still ~$104K (2.0 points) of missing profit. This is likely scattered across professional fees, travel, unbilled time, and general administrative inefficiencies.

---

## D. Segment Margin Confidence Map

To definitively prove where the remaining margin leakage lives, we need to move the "Low/Medium" confidence segments to "High" confidence.

| Segment | Revenue | Estimated GM% | Confidence | What's Missing to Prove It |
|---|---|---|---|---|
| **Managed Services** | $2.69M | 56.0% | **MEDIUM** | CW agreement-level profitability. We derived this 56% by subtracting the other segments from the total, but we haven't proven it from the bottom up. |
| **Comprehensive Services (ARC)** | $1.24M | 48.0% | **MED-HIGH** | W-2 management overhead allocation. QuickBase tracks the subcontractor invoices perfectly, but did PulseOne W-2s spend unlogged time managing the ARC relationship? |
| **Consulting / Projects** | $1.17M | 24.2% | **LOW** | CW time entries. We need to quantify the W-2 "invisible subsidy" to prove this margin is actually failing. |
| **Software Resale** | $180K* | 68.1% | **HIGH** | Nothing. CW transaction data proves this is highly profitable (68.1%), and the QB -9.4% figure is just a mapping artifact. |

*\*Note: $180K represents the standalone software line in QB; the majority of software revenue is blended into the Managed Services line.*

---

## E. The Path to 100% Certainty

To definitively lock down the 8-12% profit gap and move from reclassification to operational execution, we need the following specific data pulls from ConnectWise:

1. **W-2 Time by Board Type (The Project Subsidy):** How many hours did the core W-2 delivery team (Froio, Calkins, Walsh, Harris, McDonell, Alvarez) log to Project boards vs. Help Desk boards in 2025?
2. **Vincent Williams Allocation:** How many of his 1,706 Upwork hours were logged to Projects vs. Help Desk?
3. **Agreement Profitability:** A ConnectWise report showing the gross margin of the top 20 Managed Services agreements to prove the 56.0% derived margin is real.
