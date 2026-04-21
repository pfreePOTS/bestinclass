# PulseOne Product Sales Analysis: Best in Class Review

**Date:** April 20, 2026
**Author:** Manus (Strategic Audit Assistant)
**Framework:** Service Leadership Best in Class (BIC)

---

## A. Objective
Conduct a comprehensive analysis of PulseOne's 2025 product sales data and financial statements, evaluating revenue composition, margin quality, and customer concentration against the Service Leadership Best in Class (BIC) framework. The goal is to identify structural inefficiencies, revenue quality issues, and actionable opportunities to improve EBITDA profitability.

## B. Evidence Reviewed
This analysis is grounded in the following project documents:
*   `product sales by vendor 2025.xlsx` (ConnectWise product sales export, 9,300+ line items)
*   `2025 Profit and Loss POTS_analysis.xlsx` (Full-year P&L)
*   `ClientStatement2025.xlsx` (AR and invoice data)
*   `Service Leadership Best in Class (BIC) Framework Reference.md`

*Note: The raw product sales export contained a $5.18M subtotal row incorrectly attributed to the "Unknown" customer and "WIFI - ExtremeCloud" vendor category. This artifact was successfully isolated and removed to reveal the true $5.18M in total 2025 revenue.*

## C. Current Understanding
PulseOne generated **$5,168,754** in total revenue in 2025, operating primarily under an Infrastructure-Managed Services Predominant Business Model (PBM). The company's overall Gross Margin sits at 58.9%, with Net Ordinary Income at $217,774 (4.2% of revenue). While the top-line gross margin appears healthy, the underlying composition reveals significant deviations from Service Leadership BIC benchmarks, particularly regarding product margins, customer concentration, and the mix of recurring versus non-recurring revenue.

## D. Findings

### 1. Revenue Composition and Quality
Analysis of the ConnectWise product sales data reveals that PulseOne's revenue is heavily skewed toward services, but with a significant reliance on non-recurring project work.

| Revenue Segment | 2025 Revenue | % of Total |
| :--- | :--- | :--- |
| **Managed Services (Recurring)** | $1,773,423 | 34.2% |
| **Project / Professional Services** | $1,177,894 | 22.7% |
| **Technology Consulting (T&M)** | $600,443 | 11.6% |
| **Software Licensing** | $555,030 | 10.7% |
| **Hardware** | $441,434 | 8.5% |
| **Backup / Security SaaS** | $427,852 | 8.3% |
| **Cloud Services (Recurring)** | $21,198 | 0.4% |
| **Other** | $188,468 | 3.6% |

When classified by revenue type, **73.8% ($3.82M)** is recurring or subscription-based, while **26.2% ($1.35M)** is derived from transactional hardware and one-time project/consulting work.

### 2. The Software Margin Crisis
The most alarming finding emerges when cross-referencing the P&L with the product sales data. The P&L reports 2025 Software Sales Revenue of $514,405 against Software Purchases (COGS) of $562,725. 

**This indicates a negative gross margin of -9.4% (-$48,320) on software sales.** 

In contrast, Hardware sales generated a healthy 51.3% gross margin ($278,518 revenue vs. $135,697 COGS). The software margin inversion suggests a severe pricing discipline issue, unbilled vendor cost increases, or a systemic miscategorization where software COGS are absorbing costs that belong to other revenue lines (such as bundled managed services).

### 3. Extreme Customer Concentration
PulseOne exhibits dangerous levels of customer concentration, far exceeding healthy MSP benchmarks. Out of 381 unique customers billed in 2025, the top 10 account for nearly 60% of total revenue.

| Customer | 2025 Revenue | % of Total | Primary Revenue Driver |
| :--- | :--- | :--- | :--- |
| **ARC Institute** | $1,237,145 | 23.9% | Project Services Agreement ($1.09M) |
| **Bunzl (incl. MCR & MX)** | $909,978 | 17.5% | Managed Services & Consulting |
| **CoolPak** | $256,231 | 4.9% | Mixed Services |
| **ACT A Change in Trajector** | $178,959 | 3.5% | Mixed Services |
| **Cordova Safety** | $158,885 | 3.1% | Mixed Services |

**The top two clients (ARC Institute and the Bunzl/MCR family) alone account for 41.4% of total company revenue.** Furthermore, ARC Institute's $1.23M in revenue is almost entirely driven by a "Project Services Agreement" billed at roughly $70k-$95k per month, suggesting a staff augmentation or massive ongoing project rather than a standardized managed service contract.

## E. Service Leadership Best in Class Alignment

Based on the evidence, PulseOne's alignment with Service Leadership BIC benchmarks [1] is currently weak to moderate:

*   **Adjusted EBITDA:** At 4.2% Net Ordinary Income (plus 8.2% Partner Compensation), PulseOne is operating near the median (8.3% to 10.3%) but falls far short of the BIC standard of 18.3% to 19.0%+ [1].
*   **Product Gross Margin:** BIC firms achieve 24.3% to 26.3% product margins [1]. PulseOne's blended product margin is artificially depressed to 11.9% due to the negative software margins, though hardware performs exceptionally well at 51.3%.
*   **Operational Maturity Level (OML):** The negative software margins, high reliance on non-recurring consulting (11.6% of revenue), and extreme customer concentration indicate an OML of 2 (Emerging) or early 3 (Scaling), rather than a BIC OML of 4 or 5 [1].

## F. Risks and Opportunities

### Risks
1.  **The ARC Institute Dependency:** If the ARC Institute project concludes or the client churns, PulseOne will instantly lose 24% of its top-line revenue, likely triggering a severe cash flow crisis.
2.  **Margin Leakage in Software:** Losing nine cents on every dollar of software sold is mathematically unsustainable. This either represents a massive pricing failure (absorbing Microsoft NCE price hikes without passing them on) or a critical accounting error.
3.  **Sales Engine Weakness:** With 321 customers billing under $10,000 annually (totaling just 10.3% of revenue), the sales engine is managing hundreds of micro-accounts that likely consume disproportionate administrative overhead without contributing meaningfully to EBITDA.

### Opportunities
1.  **Hardware Margin Capitalization:** The 51.3% hardware margin is exceptional. Standardizing the hardware stack (Reference Architecture) and driving hardware refreshes into the "long tail" of the 321 micro-customers could yield immediate, highly profitable revenue.
2.  **Software Pricing Correction:** Correcting the software margin inversion to a median 15% margin would immediately add over $125,000 straight to the bottom line EBITDA.

## G. Recommended Actions

1.  **Immediate Software Margin Audit:** Conduct a line-by-line audit of the top 5 software vendors (Microsoft NCE, Adobe, AvePoint, Barracuda) to determine why COGS exceeds revenue. Implement immediate price increases for any software sold below cost.
2.  **ARC Institute Transition Plan:** Evaluate the ARC Institute engagement. If it is staff augmentation, begin transitioning the relationship into a standardized, recurring Managed Services agreement with a defined Reference Architecture to improve gross margin and reduce key-person risk.
3.  **Micro-Customer Rationalization:** Review the 321 customers generating less than $10k annually. Implement a minimum monthly recurring revenue (MRR) floor. Customers who refuse to upgrade to a standard managed services tier should be transitioned out to reduce SG&A burden.

## H. Suggested ConnectWise Follow-Up

To sharpen these recommendations, please retrieve the following from the ConnectWise AI interface:

1.  **Agreement Profitability for ARC Institute:** What is the actual gross margin and labor burden on the ARC Institute "Project Services Agreement"?
2.  **Product Catalog Margins:** Run a gross margin report specifically for the "Software" and "NCE" product categories for 2025. Which specific SKUs are being sold at a loss?
3.  **Service Board Utilization:** What percentage of total technician hours were billed to the Bunzl/MCR family versus the bottom 300 customers?

## I. Clarifying Questions

1.  Does the P&L "Purchases - Software for Resale" account include internal IT software costs (e.g., PulseOne's own ConnectWise or RMM licensing) that are artificially depressing the resale gross margin?
2.  Is the ARC Institute engagement a true fixed-fee project, or is it essentially a time-and-materials staff augmentation contract billed monthly?

---
**References:**
[1] Service Leadership Best in Class (BIC) Framework Reference.md
