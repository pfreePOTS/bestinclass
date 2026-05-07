# PulseOne Comprehensive Client & Ticket Economics Analysis (2025–2026 YTD)

## A. Objective
Provide a holistic analysis of PulseOne's client base, comparing 2025 vs. 2026 YTD agreement invoicing alongside 2026 YTD ticket consumption (Help Desk, ITMS, and Bunzl boards). The goal is to identify revenue trajectory, quantify client churn, assess the true profitability of individual accounts via effective hourly rates, and align findings with Service Leadership Best in Class benchmarks.

## B. Evidence Reviewed
- **AgreementInvoices2025.csv** & **AgreementInvoices2026.csv**: Baseline recurring revenue and fee changes.
- **Helpdesk_tickets2026.csv**: 1,504 standard support tickets (Jan–May 2026).
- **ITMS_tickets2026.csv**: 291 internal project/specialized tickets (Jan–May 2026).
- **Bunzltickets2026.csv**: 1,643 tickets across 15+ Bunzl entities (Jan–May 2026).

## C. Current Understanding
PulseOne is experiencing significant top-line revenue compression in 2026. Average monthly agreement billing dropped from ~$331,000 in 2025 to ~$154,000 by June 2026. This is primarily driven by the near-total loss of Arc Research Institute's project billing and a reduction in Bunzl's monthly billing run rate. 

While the top line has compressed, the labor demand remains intense. In the first 5 months of 2026, PulseOne processed 3,438 tickets consuming 5,079 hours of labor. The median effective hourly rate across all clients is a healthy $266/hr, but a long tail of highly unprofitable accounts is severely dragging down overall Service Gross Margin.

## D. Key Findings

### 1. The Bunzl Family: Massive Scale, Solid Economics, Declining Trajectory
The Bunzl master agreement represents PulseOne's largest client concentration. Across 15 distinct entities, Bunzl generated **$633,849** in total billing (Agreement + Standard) in the first half of 2026, averaging ~$105,642/month.
- **Labor Consumption:** Bunzl consumed 1,700 tickets and 2,632 hours in 5 months—representing roughly half of PulseOne's total service capacity.
- **Economics:** When consolidating all billing against all hours, the Bunzl family yields an **effective hourly rate of $241/hr**. This is a strong, highly profitable rate well above the Best in Class threshold.
- **Risk:** Bunzl's monthly billing has declined from $124K in January to $85K in June, partly due to Bunzl De Mexico going inactive.

### 2. The Bottom 10 Accounts (Margin Destroyers)
We calculated the "Effective Hourly Rate" (Agreement Fees ÷ Total Hours) for all clients. Best in Class MSPs target $150-$200+ per hour on managed services. The following 10 accounts are consuming labor at severely unprofitable rates, effectively operating below breakeven when burdened labor costs are applied:

| Client | Monthly Fee | Total Tkts | Total Hours | Effective $/Hr | Issue |
| :--- | :--- | :--- | :--- | :--- | :--- |
| BLN Property Management | $145 | 8 | 16.0 | **$54** | Paying almost nothing, 2 hrs/ticket |
| Autism Behavioral Health | $1,330 | 122 | 143.5 | **$56** | Massive over-consumption; 24+ tkts/mo |
| Daigh Rick Landscape Architects | $504 | 17 | 53.0 | **$57** | 3.1 hrs/ticket avg — complex issues |
| Virtus Financial Partners | $807 | 37 | 74.5 | **$65** | 2.0 hrs/ticket, fee too low for demand |
| Pelage Pharmaceuticals | $947 | 38 | 80.5 | **$71** | High ticket volume relative to fee |
| Focus On The Masters | $352 | 18 | 26.0 | **$81** | Small fee, moderate demand |
| CWS Investments Inc | $1,183 | 42 | 83.5 | **$85** | 2.0 hrs/ticket, consistent demand |
| Connecting Dot By Dot | $717 | 50 | 48.0 | **$90** | High ticket count, low fee |
| Conejo Valley Services* | $4,130 | 169 | 224.0 | **$92** | *Confirmed Churning in 2026* |
| The Elements Agency, LLC | $306 | 13 | 18.5 | **$99** | Tiny fee, moderate consumption |

*Note: Autism Behavioral Health is the standout risk. They are consuming the equivalent of nearly a full-time technician's hours (143.5 hrs in 5 months) for just $1,330/month.*

### 3. Client Churn & Major Reductions
- **Arc Research Institute:** The single largest driver of revenue loss. Billed $1.13M in 2025 (~$94K/mo). Billed $257K in early 2026, but has **zero agreement invoices since March 2026** and zero ticket activity. They appear fully inactive.
- **Historical Churn:** 20 clients who were billed in 2025 have zero invoices in 2026 YTD, representing $141,384 in annualized revenue loss (e.g., Amiri, AVF Group, Pacific Therapy Services).
- **Pending Churn:** Management confirmed **Conejo Valley Services** ($4,130/mo) and **The Sea Ranch Lodge** ($2,600/mo) are leaving in 2026. This will remove an additional ~$80,750 in annualized revenue. However, Conejo Valley was highly unprofitable ($92/hr effective rate), so their departure will free up 224 hours of labor capacity over 5 months.
- **Fee Reductions:** A Change in Trajectory (ACT) dropped from $14,726/mo in Q4 2025 to just $218 in May 2026 (-91.6%), effectively churning their managed services footprint.

### 4. ITMS Revenue Leakage (Unbilled Project Work)
The ITMS board represents project and specialized work. Under Best in Class frameworks, this should largely be billed separately from standard agreements.
- Excluding PulseOne internal tickets, there were **153 ITMS tickets** logged for external clients, consuming **249.5 hours** of labor.
- If these hours were billed at a standard project rate of $175/hour, it represents **$43,662 in uncaptured revenue** over just 5 months (an annualized leakage of ~$104,000).

## E. Service Leadership Best in Class Alignment
- **Labor Efficiency & Pricing Discipline:** Best in Class MSPs ruthlessly manage the "Effective Hourly Rate" of their agreements. Clients yielding below $100/hour are dragging down Service Gross Margin. The benchmark target for Service Gross Margin is typically 45-50%+. PulseOne's bottom 10 accounts are actively destroying margin.
- **Scope Creep & ITMS:** Allowing clients to consume ITMS (project) hours under standard Help Desk agreements violates the Best in Class principle of separating recurring service from non-recurring project labor. 

## F. Risks and Opportunities
- **Risk - Revenue Concentration:** The Bunzl family accounts for over 50% of current monthly billing. While highly profitable, this represents a severe concentration risk, especially given their billing has declined 31% since January.
- **Risk - Autism Behavioral Health:** This client is severely underwater. They are treating PulseOne as an outsourced IT department at a fraction of the true cost.
- **Opportunity - ITMS Monetization:** By strictly enforcing boundaries around what is covered by Help Desk vs. what requires an ITMS project ticket, PulseOne can immediately capture up to $43K in YTD revenue simply by billing for work already being performed.

## G. Recommended Actions
1. **Immediate Account Review for Bottom 10:** Account Managers must immediately review the bottom 10 clients by Effective Hourly Rate. Agreements for Autism Behavioral Health, BLN Property Management, and Virtus Financial Partners must be renegotiated, repriced, or gracefully exited.
2. **Audit ITMS Billing Practices:** Implement a hard stop on ITMS tickets. Any ticket routed to the Internal Projects Team must have an associated billable quote or a manager's explicit override confirming it is covered under the MSA.
3. **Bunzl Quarterly Business Review:** Given the 31% drop in Bunzl billing from Jan to June, schedule an immediate QBR with Bunzl leadership to secure the remaining $85K/mo run rate and identify why entities like Bunzl De Mexico dropped off.

## H. Suggested ConnectWise Follow-up
- **Agreement Profitability Report:** Pull the specific ConnectWise profitability report for Autism Behavioral Health to confirm the fully burdened labor cost against their $1,330 monthly fee.
- **Ticket Time Entry Audit:** For the 153 external ITMS tickets, verify in ConnectWise if any of these were actually billed as "Standard" or "Miscellaneous" invoices that were not captured under the "Agreement" invoice type.
