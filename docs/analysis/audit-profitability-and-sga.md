# PulseOne Strategic Audit: Profitability & SG&A Efficiency

## A. Objective

The objective of this audit is to quantify and locate the primary sources of profit leakage across PulseOne's operational model. By consolidating previous granular departmental analyses, this document maps the $738,444 gap between PulseOne's current EBITDA and the Service Leadership Best in Class (BiC) target, focusing specifically on structural margin failures and SG&A overhead inefficiencies.

## B. Evidence Reviewed

The findings in this audit are derived from the following sources:
*   PulseOne Definitive P&L Analysis (v3.0)
*   Service Leadership Best in Class (BiC) Framework Reference [1]
*   PulseOne Expenses Tracking MASTER 2023.xlsx
*   Upwork - Reports - Time by freelancer 2025.csv

## C. Current Understanding

PulseOne's definitive P&L (v3.0) shows a normalized EBITDA of 12.9%, which represents a significant improvement over the unadjusted 4.2% net income, but still falls short of the 18.5% BiC target [1]. While the Managed Services gross margin is performing at the BiC target (52.0%), the blended gross margin is dragged down to 33.6% (after COGS/SG&A reclassification) primarily due to structural failures in the Consulting/Projects division. Furthermore, SG&A overhead is consuming a disproportionate share of the remaining gross profit dollars.

## D. Findings

The analysis reveals four distinct areas of profit leakage that collectively account for the EBITDA gap.

### Leakage Area 1: Consulting Margin Deficit
The Consulting/Projects division generated $1.80M in revenue but cost $1.36M to deliver, resulting in a 24.2% gross margin. This is roughly half of the BiC target of 48-52% [1]. The primary driver of this margin collapse is subcontractor cost: PulseOne spent $1.04M on subcontractors, meaning 58 cents of every consulting dollar went directly to external labor before accounting for internal W-2 project management or overhead. If this division operated at the BiC 50% target, it would generate an additional ~$465,000 in gross profit.

### Leakage Area 2: The Contractor Cost Gap
There is a massive discrepancy in how contractor costs are being tracked versus reported. The Expense Tracker shows $1,798,225 in delivery contractors, but the P&L only shows $1,044,424 in the "Consulting Services - Cost" line. This $753,801 gap means either $750K of contractor costs are being incorrectly coded to "Salary Expense" or another SG&A line item in QuickBooks, or the Expense Tracker contains $750K in projected costs not actually incurred. Until this is reconciled, the true cost of service delivery remains obscured.

### Leakage Area 3: Sales & Marketing Inefficiency
PulseOne spent $536,000 on Sales & Marketing (10.4% of revenue), which is nearly double the BiC target of 5.4% [1]. The marketing investment alone was $469,823 (9.1% of revenue). Despite this heavy investment, Managed Services revenue declined 16.2% year-over-year. The marketing spend is currently destroying $257,000 in potential profit without generating the required recurring revenue growth to justify the expense.

### Leakage Area 4: G&A Tool Sprawl
General & Administrative (G&A) overhead is tracking at 18.9% of revenue ($974,810), well above the BiC target of ~12.5% [1]. A significant portion of this excess is driven by tool sprawl. The "Computer and Internet Expenses" line item totals $263,953 across 49 different vendors. An initial review indicates at least ~$91,000 in redundant SaaS tools (e.g., overlapping scheduling tools, multiple AI/Dev environments) that are not contributing to service delivery or revenue generation.

## E. Service Leadership BiC Alignment

| Metric | PulseOne Current | BiC Target | Status |
| :--- | :--- | :--- | :--- |
| Normalized EBITDA | 12.9% | 18.5% | **BELOW** |
| Consulting Gross Margin | 24.2% | 48.0% - 52.0% | **BELOW** |
| Sales & Marketing Spend | 10.4% | 5.4% | **BELOW** |
| G&A Overhead Spend | 18.9% | ~12.5% | **BELOW** |
| Total SG&A Spend | 29.4% (post-reclass) | 27.4% | **BELOW** |

## F. Risks and Opportunities

The primary risk is **unsustainable subcontractor dependency**. The Consulting division's reliance on external contractors at a 58% cost-of-goods-sold ratio makes it mathematically impossible to achieve Best in Class profitability, regardless of how efficiently the Help Desk operates.

The strategic opportunity lies in **rebalancing the operating model**. PulseOne must choose between two paths:
*   **Path A (Grow into the overhead):** Fix the S&M engine to actually produce Managed Services growth, adding $2M+ in new recurring revenue to absorb the current $1.64M SG&A burden.
*   **Path B (Shrink the overhead):** If rapid MS growth is not achievable, the SG&A burden must be aggressively cut (starting with the $470K marketing spend and $91K tool sprawl) to align with the current $5.17M revenue reality.

## G. Recommended Actions

1.  **Implement Project Margin Gates:** Require partner-level approval for any fixed-fee project proposal or T&M rate card that does not model out to a minimum 50% gross margin based on estimated hours and contractor costs.
2.  **Reconcile the Contractor Gap:** Conduct a line-by-line audit comparing the $1.79M Expense Tracker against the $1.04M P&L contractor line to determine where the missing $753K is being coded in QuickBooks.
3.  **Audit G&A Tool Sprawl:** Execute a SaaS rationalization project targeting the 49 vendors in the $263K "Computer and Internet Expenses" line, with a goal of cutting $91K in redundant licenses.
4.  **Rebalance Sales & Marketing:** Shift $200K+ of capacity from Marketing (which is currently failing to produce MS growth) into quota-carrying Sales roles focused exclusively on acquiring new Managed Services agreements.

## H. Suggested ConnectWise Follow-Up

To refine this analysis, the following specific data pulls are required from the ConnectWise AI interface:

1.  **Project Profitability by Subcontractor:** A report detailing the ratio of subcontractor cost to billed revenue for all projects involving Basim Mashni, David Fredrick, or Blue Pisces over the last 6 months.
2.  **Agreement vs. Project Hours:** A report showing the percentage of total logged technician hours applied to Managed Services agreements versus Consulting projects over the last 6 months.

## I. Clarifying Questions

1.  Why is the Expense Tracker showing $753K more in contractor costs than the P&L? Is this a coding error, or are these projected costs?
2.  What specific marketing initiatives consumed the $469K spend, and why did they fail to prevent a 16.2% decline in Managed Services revenue?
3.  Are subcontractor rates marked up consistently, or are they passed through at cost to remain competitive on project bids?

## References

[1] Service Leadership, Inc., "The Financial Value To Large MSPs of Implementing a Reference Architecture," 2016. https://www-cdn.webroot.com/6615/0473/1278/SL_MSP_Report_2017.pdf
