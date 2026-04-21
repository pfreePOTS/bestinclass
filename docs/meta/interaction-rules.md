# Interaction Rules — PulseOne Best in Class Audit

*Last updated: 2026-04-20*
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
   - `docs/analysis/` — Analysis reports and audit findings
   - `docs/reference/` — BIC framework and benchmark reference materials
   - `docs/archive/` — Superseded documents
   - `docs/meta/` — AI interaction rules and persistent memory

5. **ConnectWise is an active follow-up channel.** When data is missing, specify exactly what to pull from ConnectWise AI and why.

6. **All financial figures are in USD.** Fiscal year is calendar year (Jan–Dec).

7. **Canonical revenue figure for 2025: $5,168,754** (from the 2025 P&L). The ConnectWise product sales export shows $5,185,747 — a ~$17k difference due to timing. Use P&L as the authoritative source for financial benchmarking.
