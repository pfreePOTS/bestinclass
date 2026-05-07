# Interaction Rules — PulseOne Best in Class Audit

*Last updated: 2026-05-01*
*Project: pfreePOTS/bestinclass*

## Project Context

This repository is the central knowledge base for the PulseOne Best in Class (BIC) audit project. It contains financial documents, operational data exports, analysis reports, and framework reference materials used to benchmark PulseOne against Service Leadership Best in Class standards.

## How Manus Should Work in This Project

1. **Always treat Service Leadership BIC as the controlling benchmark.** Do not substitute generic MSP advice for Service Leadership-specific standards. If BIC data is unavailable, explicitly state that.

2. **Ground all conclusions in uploaded evidence.** Separate documented facts from interpretations and inferred risks. Never invent benchmarks.

3. **Maintain a persistent working model of PulseOne.** When new documents are added, update the model rather than restarting analysis.

4. **Document structure:**
   - `data/financial/` — Source financial files (Excel, CSV) — READ ONLY
   - `data/clients/` — Client-level data exports
   - `data/payroll/` — Payroll and contractor data
   - `docs/analysis/` — Analysis reports and audit findings (latest versions only)
   - `docs/reference/` — BIC framework and benchmark reference materials
   - `docs/archive/` — Superseded documents
   - `docs/meta/` — AI interaction rules and persistent memory
   - `scripts/` — Canonical build scripts and audit tools
   - `scripts/audit/` — Data validation and reconciliation scripts

5. **ConnectWise is an active follow-up channel.** When data is missing, specify exactly what to pull from ConnectWise AI and why.

6. **All financial figures are in USD.** Fiscal year is calendar year (Jan–Dec).

7. **Canonical revenue figure for 2025: $5,168,754** (from the 2025 P&L). The ConnectWise product sales export shows $5,185,747 — a ~$17k difference due to timing. Use P&L as the authoritative source for financial benchmarking.

8. **Product Resale is a separate P&L stream.** Standalone product sales (M365, hardware, Adobe) have their own revenue and COGS lines and must not be treated as Managed Services COGS. MS COGS should only include service delivery labor and service delivery tools.

9. **CS-Cost Line Contains Multi-Segment Costs.** The QuickBooks "Consulting Services-Cost" line ($1.04M) is not a single bucket. It contains ARC contractors, Bunzl project contractors, MS contractors, and misclassified SGA. Always trace it at the vendor/client level before allocating it to a segment.

10. **Do NOT trust QB expense line allocations.** QB total expenses ($4,950,980) are reliable as a control total, but the individual line items (Salary, Payroll Tax, CS-Cost, etc.) are misclassified. We are rebuilding the P&L from source data (ADP, Upwork, Payoneer, BILL), not from QB line allocations.

11. **W-2 amounts must use ADP gross pay only.** The ADP file contains both "Total Earnings" (gross pay, Col 67) and "Total Employer Liability" (FICA/FUTA/SUI, Col 104). The model must use gross pay only. Employer liability is already included in the separate Payroll Tax/Benefits line ($310,876). Using gross+ER creates a double-count of ~$93K.

12. **Never create derived "remainder" categories.** Do not compute a QB remainder and label it as a real expense category (e.g., "Other OpEx"). If expenses are unidentified, label them transparently as "G&A Operating Expenses (unitemized)" and place them in G&A.

13. **Payoneer contractors are already in QB Salary.** Payoneer payments (Daniyal, George, Dare, Marcello, Peal, Badar) are coded into QB expense lines. List each person once in their department — do not also include them in a separate bucket.

14. **The canonical P&L model is `scripts/build_pl_v7_corrected.py`.** This is the latest corrected version. It ties to QB total expenses within $1 (rounding). All prior versions (v1–v7.0) are superseded.

15. **The canonical P&L document is `docs/analysis/PulseOne_Definitive_PL_Evaluation_2025.md`.** This is the master deliverable. Updated May 1, 2026 with v7.1 corrections.

16. **Bunzl is a consolidated master agreement.** All Bunzl entities (MCR Safety, Cool Pak, Cordova Safety, Kishigo, Majestic Glove, Tingley Rubber, SAS Safety, Revco Industries, Steiner Industries, Liberty Safety, Monte Package, Tillman, Intergro, Bunzl De Mexico) are covered under a single master agreement billed at ~$100K/month across multiple billing entities. When analyzing Bunzl economics, always consolidate all entities together.

17. **Three ticket boards exist in ConnectWise.** Help Desk (standard agreement-covered support), ITMS (Internal Projects Team — should generally be billable), and Bunzl (dedicated Bunzl support board). All three must be included when calculating client ticket economics.

18. **The canonical client ticket economics analysis is `docs/analysis/PulseOne_Comprehensive_Client_Analysis.md`.** Updated May 6, 2026. Covers 2025–2026 YTD invoicing comparison, ticket economics across all boards, and bottom 10 accounts by effective hourly rate.

19. **Confirmed 2026 churn:** Conejo Valley Services (~$4,130/mo) and The Sea Ranch Lodge (~$2,600/mo) are confirmed leaving. Arc Research Institute appears fully inactive since March 2026 (was ~$94K/mo in 2025). ACT dropped from $14.7K/mo to $218/mo (effectively churned).

- When creating iterative analysis documents during a session, actively archive superseded versions to `docs/archive/` to maintain a clean `docs/analysis/` folder containing only the authoritative current state.
