# PulseOne: Software Cost Allocation & Overpayment Analysis

**Audit Date:** April 17, 2026  
**Scope:** Software COGS vs. SGA allocation accuracy; TD Synnex and Barracuda overpayment risk  
**Revenue Context:** CY 2025 Total Revenue ~$5.17M

---

## A. Objective

This analysis has two purposes: (1) establish the correct allocation of every software cost between COGS and SGA so that gross margin is accurately stated, and (2) identify specific overpayment signals in the TD Synnex and Barracuda vendor relationships that warrant immediate investigation.

---

## B. Corrected Software Cost Allocation

### Confirmed Classifications (Owner-Provided)

The following classifications were confirmed directly:

| Vendor | Amount | Confirmed Bucket | Basis |
|--------|--------|-----------------|-------|
| Flexis | $64,009 | COGS — Agreement Licenses | Owner-confirmed |
| Amazon Web Services | $73,982 | COGS — Agreement Licenses | Owner-confirmed (client-specific) |
| Samurai Sync | $9,450 | COGS — Agreement Licenses | Owner-confirmed (move from SGA) |

### Confirmed Reclassifications: SGA → COGS

These are client delivery tools currently booked as internal overhead. Moving them to COGS correctly burdens the cost of service delivery.

| Vendor | Amount | Reason |
|--------|--------|--------|
| **Samurai Sync** | $9,450 | Owner-confirmed delivery tool |
| **Wasabi Technologies** | $7,353 | Cloud object storage for client backup delivery |
| **Duo Security** | $2,068 | MFA platform protecting client environments |
| **Qualys** | $1,024 | Vulnerability scanning for client security delivery |
| **Subtotal** | **$19,895** | |

### Items Requiring Confirmation: COGS → SGA

These are small-dollar items currently in COGS that may be internal tools. Individually minor, but correct allocation matters for margin accuracy.

| Vendor | Amount | Question |
|--------|--------|---------|
| Atlassian | $2,962 | Is this Jira/Confluence for internal dev ops, or client-facing? |
| GoDaddy.com | $2,880 | Are these PulseOne's own domains/hosting, or client-managed domains? |
| Microsoft (Agreement COGS) | $2,644 | Are these internal Microsoft licenses, or client-specific items? |
| **Subtotal** | **$8,486** | |

### Corrected Software COGS Summary

| Cost Category | As Currently Booked | After Confirmed Reclassifications | Net Change |
|---------------|--------------------|------------------------------------|------------|
| Agreement Licenses COGS | $681,071 | $700,966 | +$19,895 |
| Standalone Software Resale COGS | $473,779 | $473,779 | — |
| Computer & Internet SGA (partial) | $51,807 | $31,912 | -$19,895 |

> **Note:** The SGA figures above reflect only the $52,008 portion of the $263,953 total Computer & Internet SGA line that is captured in the detailed transaction export. The remaining ~$212,000 requires a separate export to complete the full allocation review.

---

## C. TD Synnex — Overpayment Analysis

### Combined Synnex Exposure

TD Synnex is PulseOne's single largest vendor relationship. It appears in **two separate cost buckets**, making the total exposure easy to understate:

| Bucket | Annual Spend |
|--------|-------------|
| Agreement Licenses COGS | $301,813 |
| Standalone Software Resale COGS | $251,028 |
| **Combined Total** | **$552,841** |

This represents **10.7% of PulseOne's total annual revenue** flowing through a single distributor. That concentration alone warrants active management.

### Monthly Spend Trend — Agreement Licenses

| Month | Amount | Month-over-Month Change |
|-------|--------|------------------------|
| Jan 2025 | $21,552 | (baseline) |
| Feb 2025 | $24,879 | +$3,327 (+15.4%) |
| Mar 2025 | $25,840 | +$962 (+3.9%) |
| Apr 2025 | $28,644 | +$2,803 (+10.8%) |
| May 2025 | $25,373 | -$3,271 (-11.4%) |
| Jun 2025 | $27,493 | +$2,120 (+8.4%) |
| Jul 2025 | $24,775 | -$2,718 (-9.9%) |
| Aug 2025 | $20,947 | -$3,828 (-15.5%) |
| Sep 2025 | $26,188 | +$5,241 (+25.0%) |
| Oct 2025 | $30,277 | +$4,089 (+15.6%) |
| Nov 2025 | $22,321 | -$7,956 (-26.3%) |
| Dec 2025 | $23,524 | +$1,203 (+5.4%) |
| **Annual Total** | **$301,813** | |
| Monthly Average | $25,151 | |
| Monthly Min/Max | $20,947 / $30,277 | **44.5% swing** |

### Overpayment Signals

**Signal 1: Consolidated "Estimate" billing with no product detail.** Every Synnex Agreement Licenses charge in the QuickBooks export is tagged with the memo "Estimate" — meaning PulseOne is receiving a single monthly bill with no line-item breakdown of which products, seat counts, or clients are driving the charge. This is the most important control failure. Without line-item detail, it is impossible to verify that the bill is correct.

**Signal 2: Unexplained monthly variance of 44.5%.** The Synnex Agreement Licenses charge swings from $20,947 to $30,277 within the same year — a $9,330 monthly range — with no visible correlation to new client additions or contract changes. This volatility is inconsistent with a stable, seat-count-driven license portfolio. It suggests one or more of the following: mid-year price increases absorbed silently, seat count drift (licenses being added without corresponding client billing), or billing errors.

**Signal 3: No client attribution on the Agreement Licenses portion.** The $301,813 Agreement Licenses spend from Synnex has zero client attribution in the data. The $251,028 Standalone Resale spend does have client-level detail. This asymmetry means the larger of the two Synnex buckets is entirely untracked at the client level.

**Signal 4: Combined Synnex spend ($552,841) vs. total software revenue ($514,405 + $763,755 = $1,278,160).** Synnex alone represents 43% of total software revenue. If the Agreement Licenses portion is being billed to clients at a 52% margin, the math works — but only if the client-level billing is being updated when Synnex raises prices. Given the monthly variance, there is a material risk that it is not.

### What to Do

1. **Request a line-item invoice from TD Synnex** for any month in 2025. The invoice should show: product SKU, description, seat count, unit price, and total. Compare this to what ConnectWise is billing each client for the same products.
2. **Pull the Synnex portal seat count report** (available in the TD Synnex StreamOne portal) and compare active seat counts to what is in each client's ConnectWise agreement.
3. **Reconcile the September spike (+$5,241, +25%)** — this is the largest single-month increase and should have a clear explanation (new client, new product, or price increase).

---

## D. Barracuda (Skout Cybersecurity) — Overpayment Analysis

### Monthly Spend Trend

| Month | Amount | Month-over-Month Change |
|-------|--------|------------------------|
| Jan 2025 | $3,996 | (baseline) |
| Feb 2025 | $4,237 | +$242 (+6.0%) |
| Mar 2025 | $4,957 | +$719 (+17.0%) |
| Apr 2025 | $5,644 | +$687 (+13.9%) |
| May 2025 | $5,889 | +$245 (+4.3%) |
| Jun 2025 | $6,340 | +$451 (+7.7%) |
| Jul 2025 | $6,696 | +$357 (+5.6%) |
| Aug 2025 | $6,509 | -$187 (-2.8%) |
| Sep 2025 | $6,990 | +$481 (+7.4%) |
| Oct 2025 | $6,862 | -$128 (-1.8%) |
| Nov 2025 | $7,368 | +$506 (+7.4%) |
| Dec 2025 | $7,472 | +$104 (+1.4%) |
| **Annual Total** | **$72,960** | |
| Jan → Dec Increase | +$3,476 | **+87.0%** |

### Annualized Run-Rate Comparison

| Scenario | Monthly Rate | Annualized Cost |
|----------|-------------|-----------------|
| January 2025 pace | $3,996 | $47,949 |
| December 2025 pace | $7,472 | $89,662 |
| **Difference** | **+$3,476/month** | **+$41,713/year** |

### Overpayment Signals

**Signal 1: 87% cost increase in 12 months with no visible client attribution.** The Barracuda spend nearly doubled over the course of 2025. The transaction data shows no client name or memo on any Barracuda charge — every transaction is a consolidated monthly bill. This means PulseOne cannot determine whether this cost growth is driven by new clients, price increases, or seat count drift.

**Signal 2: The cost growth pattern is inconsistent with organic client growth.** A legitimate 87% cost increase driven purely by new client additions would require adding roughly 87% more protected endpoints or seats during the year. If PulseOne's managed security client count did not grow by that magnitude, the cost increase is being absorbed as margin compression rather than passed through to clients.

**Signal 3: The $41,713 annualized run-rate increase is a direct margin leak.** If the December run rate continues into 2026, PulseOne will pay $89,662 for Barracuda — $41,713 more than the January 2025 annualized rate. Unless managed security revenue grew proportionally, this entire increase is coming out of gross margin.

**Signal 4: No client-level attribution makes repricing impossible.** Unlike the Synnex Standalone Resale transactions (which have client names), the Barracuda charges have no client attribution in the QuickBooks data. This means PulseOne cannot currently identify which clients are on the Barracuda platform or what they are being charged.

### What to Do

1. **Pull the Barracuda/Skout portal** and export the current client list with seat counts and per-seat pricing. This is the ground truth for what PulseOne is being charged.
2. **Cross-reference against ConnectWise agreements** — identify every client with a managed security line item and confirm the monthly billing matches the current Barracuda cost per seat.
3. **Identify the inflection point.** The largest single-month increase was March (+$719, +17%). Determine what changed in March — new client onboarding, a price increase from Barracuda, or a product tier change.
4. **If the cost growth is from new clients:** Verify those clients are being billed in ConnectWise at a margin of at least 25%.
5. **If the cost growth is from a Barracuda price increase:** Issue a contract amendment to all affected clients with 30 days' notice, passing through the increase plus the target margin.

---

## E. Service Leadership BIC Alignment

The two overpayment situations identified above are directly relevant to the BIC framework in two ways:

**Product/Software Gross Margin (BIC Target: 24.3%–26.3%):** Both the Synnex variance and the Barracuda escalation are suppressing software gross margin. Every dollar of unattributed cost increase that is not passed through to clients reduces the margin on the affected service lines. Achieving BIC product margins requires that cost increases are systematically identified and passed through within 30–60 days.

**Reference Architecture Discipline:** BIC MSPs enforce a standardized technology stack and manage vendor relationships with discipline. The pattern here — consolidated invoices with no line-item detail, no client attribution, and no monthly reconciliation — is characteristic of OML 2–3 operational maturity. Implementing a monthly vendor reconciliation process (Synnex portal vs. ConnectWise agreements) is an OML 4 practice and a prerequisite for sustained BIC margin performance.

---

## F. Recommended Actions — Prioritized

| Priority | Action | Owner | Timeline | Expected Impact |
|----------|--------|-------|----------|-----------------|
| **P1** | Request line-item Synnex invoice; reconcile to ConnectWise | Finance/Ops | Week 1 | Identify billing errors and unattributed cost |
| **P1** | Pull Barracuda portal client/seat list; reconcile to ConnectWise | Finance/Ops | Week 1 | Identify seat count drift and margin leak |
| **P1** | Confirm Samurai Sync, Wasabi, Duo, Qualys as COGS in QuickBooks | Accounting | Week 1 | Correct gross margin reporting |
| **P2** | Identify September Synnex spike ($5,241) root cause | Finance | Week 2 | Confirm or dispute billing accuracy |
| **P2** | Identify Barracuda March inflection point root cause | Finance | Week 2 | Confirm or dispute cost growth |
| **P2** | Issue price amendments to all clients affected by Barracuda increase | Account Mgmt | Month 1 | Recover $41,713/year run-rate cost |
| **P3** | Confirm Atlassian, GoDaddy, Microsoft COGS items as internal or client | Accounting | Month 1 | Complete allocation accuracy |
| **P3** | Add cost pass-through language to all new software agreements | Legal/Sales | Month 2 | Prevent future margin erosion |

---

## G. Suggested ConnectWise Follow-Up

| Report | Purpose | Specifics |
|--------|---------|-----------|
| **Agreement Profitability — Managed Security** | Identify Barracuda-backed agreements and current billing per client | Filter by security/SOC service type; CY 2025 |
| **Agreement Profitability — Software/Licensing** | Identify Synnex-backed agreements and current billing per client | Filter by software/license type; CY 2025 |
| **Product Catalog — Active License Items** | Confirm per-seat pricing for Microsoft 365 and security products | Current snapshot |
| **Client List with Agreement Renewal Dates** | Prioritize repricing by upcoming renewal | Next 12 months |

---

*All figures derived from CY 2025 transaction-level data in the uploaded QuickBooks export. Benchmark references from Service Leadership Best-in-Class Framework Reference document.*
