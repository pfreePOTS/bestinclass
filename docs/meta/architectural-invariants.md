# Architectural Invariants — PulseOne Best in Class Audit

*Initialized: 2026-04-20*

These are the hard rules that must not be broken when analyzing PulseOne data or producing recommendations.

---

## Invariant 1: BIC Benchmarks Are the Controlling Standard

Service Leadership BIC benchmarks are the controlling benchmark source. Do not substitute or blend in other frameworks without explicitly labeling them as non-BIC comparisons.

Key BIC thresholds to always reference:
- Adjusted EBITDA: 18.3–19.0%+
- Blended Gross Margin: 44.0%+
- Managed Services GM: 48.7–52.4%
- Revenue Growth: 16.3%+ YoY
- Client Retention: >76%
- Service Multiple of Labor: 2.8x+
- SG&A % of Revenue: ~27.4%

---

## Invariant 2: Do Not Conflate Revenue Sources

PulseOne has multiple legal entities and revenue streams. Always distinguish between:
- ConnectWise-invoiced revenue (ClientStatement = $3.33M in 2025)
- Total P&L revenue ($5.17M in 2025)
- The $1.84M gap is unreconciled as of April 2026

---

## Invariant 3: Bunzl Is a Family of Accounts

Never treat "Bunzl" as a single client. The Bunzl family includes:
- Bunzl (parent): $494,570
- MCR Safety-Bunzl: $334,807
- Bunzl De Mexico: $78,413
- Majestic Glove-Bunzl: $15,692
- Total Bunzl family: $923,482 (27.7% of revenue)

---

## Invariant 4: Partner Compensation Must Be Normalized for EBITDA (UPDATED — April 22, 2026)

The $423,000 partner compensation line in the P&L is an operating expense. The three partners serve as CEO (Charlie Batsford), CMO (Paul Freeman), and CFO (Rod). At $141K average each, their compensation is at or below Fair Market Value (FMV) for a $5.2M MSP. Therefore:
- **No add-back is applied** when calculating normalized EBITDA
- Normalized EBITDA = Net Operating Income + D&A only
- The correct normalized EBITDA for 2025 is **6.3%**, not the previously reported 12.9%

---

#### Invariant 5: Software Resale Margin Is a Mapping Issue, Not a Pricing Failure (UPDATED — April 22, 2026)

The -9.4% gross margin on software resale in QuickBooks is a revenue mapping artifact. ConnectWise Cost/Sell reports show 68.1% software margin at the transaction level. Software revenue is being blended into Managed Services revenue lines on the P&L while costs correctly hit software COGS accounts. The real structural product issue is the Adobe Creative Cloud purchase for ARC at 4.3% GM. (Note: Prior claims of a 16.4% M365 margin were based on flawed QB cost mapping; the actual M365 margin is a healthy ~43.4%).

---

## Invariant 6: Data Files Are Source of Truth

Raw data files in data/ are the source of truth. Analysis documents in docs/analysis/ are derived. If there is a conflict, the raw data takes precedence.

---

## Invariant 7: Bunzl Is a Corporate Parent with Independent Subsidiaries (CORRECTED — April 20, 2026)

**Do not treat the Bunzl family as a single economic relationship.** Bunzl Group is the corporate parent, but PulseOne supports each subsidiary independently. Each subsidiary has its own IT environment, support agreement, and operational decision-making authority.

**Correct framing:**
- Loss risk is distributed across subsidiaries — losing one does not mean losing all
- Bunzl Distribution USA ($494,570 = 14.9% of CW revenue) is the largest single subsidiary and the correct unit of concentration measurement
- The Bunzl family total ($923,482 = 27.7%) should be reported as "Bunzl Group (distributed across N subsidiaries)" — not as a single client

**Residual corporate risk (still real):**
- A corporate-level IT strategy change by Bunzl Group could affect multiple subsidiaries simultaneously
- This risk should be tracked as a "strategic dependency" rather than a "client concentration" risk

**Expansion pipeline (as of April 2026):**
Active in ConnectWise: Bunzl Distribution USA, MCR Safety-Bunzl, Bunzl De Mexico, Majestic Glove-Bunzl, Cool Pak-Bunzl, Tillman-Bunzl, Cordova Safety-Bunzl, Tingley Rubber-Bunzl

In HubSpot but not yet in ConnectWise (warm pipeline):
- Bunzl Agriculture Group (Oxnard, CA | 500 employees)
- Liberty Safety - Bunzl (Liberty, SC | 50 employees)
- Intergro - Bunzl (Clearwater, FL | 30 employees)
- SAS Safety Corp. - Bunzl (Long Beach, CA | 60 employees)
- Kishigo - Bunzl (Fountain Valley, CA | 125 employees)
- Steiner Industries - Bunzl (Chicago, IL | 5 employees)
- Revco Industries - Bunzl (Santa Fe Springs, CA | 45 employees)
- Monte Package Company - Bunzl (Riverside, MI | 45 employees)
- McCue - Bunzl (Danvers, MA)
- MCR Safety - Bunzl (Collierville, TN | 235 employees) — already in CW

This pipeline makes Bunzl PulseOne's largest near-term growth opportunity.

---

## Invariant 8: Distinguish Cash Margin from Fully-Loaded Margin

When analyzing project profitability, always explicitly state whether a margin is a **Cash Margin** (revenue minus out-of-pocket subcontractor invoices) or a **Fully-Loaded Gross Margin** (which includes allocated W-2 labor and burden). The QuickBase project tracker only measures Cash Margin. Fully-Loaded Margin requires ConnectWise time entry data.

---

## Invariant 9: Staff Augmentation is Not Project Delivery

Do not blend Staff Augmentation (e.g., the ARC Research managed contractor pool) with discrete Project Delivery. They have different cost structures, different billing models, and different Best in Class benchmark expectations. Staff Augmentation should be evaluated on markup percentage, while Projects should be evaluated on fully-loaded gross margin.

---

## Invariant 10: Separate Entity Cost Isolation — RepScheduler & PulseOne Communications (NEW — April 22, 2026)

**Invariant:** Costs incurred by PulseOne on behalf of separate ventures (RepScheduler and PulseOne Communications) must be removed from the PulseOne operating baseline before calculating margins or BiC gaps.

**Affected personnel:**
- **Badar** (~100% RepScheduler) — $30,300/year
- **Daniyal Arif** (~50% RepScheduler) — $22,059/year RS portion
- **Tracy Freeman** (100% POC) — $14,111/year
- **Nicole Goodwin** (25-50% POC) — $14,142-$27,605/year POC portion

**Total removal: ~$80K-$94K/year**

**Enforcement:** Any P&L analysis must explicitly deduct these costs and note the adjustment.

---

## Invariant 11: Comprehensive Services (Staff Augmentation) Is a Separate Segment (UPDATED — April 22, 2026)

**Invariant:** Staff augmentation revenue and costs (e.g., the ARC engagement) must be separated from Managed Services and reported as "Comprehensive Services."

**Reasoning:** ARC paid a flat monthly fee for a dedicated team. This is fundamentally different from per-device/per-user managed services. Blending them distorts both the MS margin (makes it look lower) and the true size of the recurring MSP base (makes it look larger).

**Correct segment structure (Direct Delivery Margin v4.0):**
- Managed Services: $2,696,716 (73.1% GM) — core MSP
- Comprehensive Services: $1,237,145 (46.1% GM) — ARC staff aug
- Consulting/Project: $1,175,036 (44.0% traceable GM, ~24% fully-loaded) — discrete projects
- Software Resale: Standalone P&L stream, not MS COGS

---

## Invariant 12: Product Resale Is a Separate P&L Stream (NEW — April 22, 2026)

**Invariant:** Standalone product sales (M365, hardware, Adobe) have their own revenue and COGS lines and must not be treated as Managed Services COGS.

**Reasoning:** Dumping product COGS into Managed Services artificially depresses the MS margin (e.g., from 73.1% down to 36.6%). MS COGS should only include service delivery labor and service delivery tools (ConnectWise, Kaseya, etc.).

---

## Invariant 13: CS-Cost Line Contains Multi-Segment Costs (NEW — April 22, 2026)

**Invariant:** The QuickBooks "Consulting Services-Cost" line ($1.04M) is not a single bucket. It contains ARC contractors, Bunzl project contractors, MS contractors, and misclassified SGA (Marcello).

**Reasoning:** Any P&L model must trace the CS-Cost line at the vendor/client level. Assuming it all belongs to one segment or relying on estimates rather than transaction-level detail will result in massive margin errors (e.g., the $200K+ underestimation of project costs in early models).

---

## Invariant 14: ADP Gross Pay vs. Employer Liability (NEW — May 1, 2026)

**Invariant:** W-2 labor costs in the P&L model must use ADP "Total Earnings" (gross pay, Col 67) only. ADP "Total Employer Liability" (Col 104) must NOT be added to per-person amounts.

**Reasoning:** The ADP file contains both gross pay and employer-side taxes (FICA, FUTA, SUI) as separate columns. The QB "Payroll Tax" line ($296,256) + "Payroll Expense" line ($14,620) = $310,876 already covers all employer burden (FICA, health insurance, 401k match, workers comp, state taxes). If per-person amounts include ADP employer liability AND the model adds $310,876 as a separate line, the result is a ~$93K double-count.

**Confirmed by audit:** Person-by-person comparison showed model amounts = ADP Gross + ADP ER Liability (e.g., Stephen Calkins: $148,960 gross + $16,000 ER = $164,960 model). The corrected model uses $148,960.

---

## Invariant 15: No Derived Remainder Categories (NEW — May 1, 2026)

**Invariant:** Never compute a QB remainder (QB Total minus named lines) and present it as a real expense category.

**Reasoning:** The "Other OpEx ($389,129)" category in prior model versions was a mathematical remainder with no source document. It created confusion and contributed to a $200K variance. If expenses are unidentified, they must be labeled transparently (e.g., "G&A Operating Expenses — unitemized, $286,697") and placed in G&A. The amount should be derived as: QB Total Expenses minus all individually sourced expense lines.

---

## Invariant 16: Canonical Model Version Control (NEW — May 1, 2026)

**Invariant:** The canonical P&L build script is `scripts/build_pl_v7_corrected.py`. All prior versions (build_departmental_pl.py through build_pl_v7.py) are superseded and should not be used.

**Key properties of the canonical model:**
- W-2 amounts = ADP gross pay only ($1,010,174 total, 27 people)
- Payroll Tax/Benefits = $310,876 (separate line, allocated proportionally to W-2 segments)
- Upwork = $299,924 (11 freelancers, CY2025 file)
- BILL/CS-Cost = $1,004,961 (9 contractors)
- Payoneer = $194,687 (5 contractors)
- Partners = $423,000 (3 partners at $141K each)
- G&A Operating Expenses = $286,697 (unitemized QB remainder, in G&A)
- Total expenses = $4,950,981 (ties to QB $4,950,980 within $1)
- Net Income = $217,774 (ties to QB exactly)

**Revenue segments (v7.1):**
- Managed Services: $1,799,686 (34.8%) — 48.4% GM
- Comprehensive Services: $1,384,375 (26.8%) — 35.2% GM
- True Projects: $432,343 (8.4%) — -4.6% GM (loss)
- Products: $1,552,350 (30.0%) — 36.2% blended GM
