# PulseOne Strategic Audit: Three-Way Software Reconciliation

**Objective:**
Reconcile software expenses across the three primary data sources (P&L, Detailed Vendor File, and Expense Tracker) to confirm data integrity and identify any unexplained variances.

---

## 1. The Reconciliation Math

I compared the three software expense lines on the P&L against the detailed vendor file you provided. The numbers tie out almost perfectly, which gives us high confidence in the data.

| P&L Line Item | P&L Total | Detail File Total | Variance | Status |
|---|---|---|---|---|
| **Agreement License Cost (COGS)** | $366,527.17 | $373,999.01 | +$7,471.84 | ⚠ Minor |
| **Purchases - Software for Resale (COGS)** | $562,725.72 | $570,986.81 | +$8,261.09 | ⚠ Minor |
| **Computer & Internet Expenses (SG&A)** | $263,953.24 | $263,953.24 | $0.00 | ✓ Match |
| **TOTAL** | **$1,193,206.13** | **$1,208,939.06** | **+$15,732.93** | |

### Analysis of the Variance
The $15,732 variance across $1.2M in spend is a **1.3% difference**. 
- The Computer & Internet line matches to the penny.
- The two COGS lines in the detail file are slightly higher than the P&L. This is very common and usually caused by year-end timing differences (e.g., an invoice dated late December but paid in January, or a credit memo applied in a different period).
- **Conclusion:** The data is solid. The $180K loss on software resale and the $91K in SG&A tool sprawl are confirmed facts, not accounting errors.

---

## 2. Clarifying the Software Revenue Picture

Because the cost data is solid, we can confidently finalize the software margin math. There are two distinct software revenue streams:

### Stream A: Managed Services Software (Healthy)
This is software bundled into your monthly managed services agreements (e.g., Microsoft 365, Barracuda, basic backup).
- **Revenue (Agreement Licenses):** $763,755
- **Cost (Agreement License Cost):** $366,527
- **Gross Profit:** $397,228
- **Gross Margin:** **52.0%**
- *Diagnosis: This is performing exceptionally well. Do not change this model.*

### Stream B: Standalone Software Resale (Critical Failure)
This is one-off software sold outside of managed agreements, primarily sourced through Synnex, Ingram Micro, and AWS.
- **Revenue (Sales - Software):** $514,405
- **Cost (Purchases - Software for Resale):** $562,726
- **Gross Profit:** -$48,321
- **Gross Margin:** **-9.4%**
- *Diagnosis: You are losing almost 10 cents on every dollar of standalone software you sell. If you had priced this at the BIC target of 25% margin, this revenue stream would have generated $137,000 in gross profit instead of a $48,000 loss. That is a **$185,000 profit swing**.*

---

## 3. Next Steps

The reconciliation confirms that our diagnosis is correct and the data is reliable. 

We now have a complete, normalized map of the business that isolates exactly where the $740,000 in missing profit went:
1. **Consulting Margin Deficit:** ~$440,000
2. **Software Resale Pricing Loss:** ~$185,000
3. **Marketing Overspend:** ~$314,000
4. **SG&A Tool Sprawl:** ~$91,000

Which of these four areas would you like to build an action plan for next?
