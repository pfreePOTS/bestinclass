# PulseOne — Best in Class Audit Repository

This repository contains all financial, operational, and analytical documents supporting PulseOne's **Service Leadership Best in Class (BIC) audit and improvement program**.

## Purpose

The goal of this repository is to serve as the single source of truth for:

- Raw financial and operational data used in the BIC audit
- Analysis outputs and findings documents
- Service Leadership BIC framework reference materials
- Ongoing meta-harness rules and interaction guidelines for AI-assisted analysis

All analysis is benchmarked against **Service Leadership's Best in Class framework** for managed service providers and technology integration companies.

---

## Repository Structure

```
bestinclass/
├── data/
│   ├── financial/          # P&L, balance sheet, COGS, multi-year reports
│   ├── payroll/            # Payroll reports and Upwork contractor data
│   └── clients/            # Client statement and billing data
├── docs/
│   ├── analysis/           # Completed audit analyses and findings
│   ├── reference/          # Service Leadership BIC framework and benchmarks
│   ├── planning/           # Roadmaps and implementation plans
│   ├── design/             # Architecture and system design docs
│   ├── meta/               # AI interaction rules and architectural invariants
│   ├── diagnostics/        # AI tool failure logs and diagnostic reports
│   └── archive/            # Previous versions of documents
└── README.md
```

---

## Key Documents

| Document | Location | Description |
|----------|----------|-------------|
| Client & Customer Profitability Analysis | `docs/analysis/pulseone-client-profitability-analysis.md` | Full 2025 client profitability audit vs. BIC benchmarks |
| BIC Framework Reference | `docs/reference/service-leadership-bic-framework-reference.md` | Service Leadership benchmark definitions and thresholds |
| 2025 P&L Analysis | `data/financial/2025 Profit and Loss POTS_analysis.xlsx` | Monthly P&L with analyst notes |
| Client Statement 2025 | `data/clients/ClientStatement2025.xlsx` | All 2025 invoices by client (319 clients, 2,498 lines) |
| Multi-Year P&L (2022–2024) | `data/financial/Report_from_PulseOne_Group,_LLC 2022 2023 2024.xlsx` | Historical P&L for trend analysis |

---

## Current Audit Status

**Last updated:** April 20, 2026

| Audit Area | Status | Key Finding |
|-----------|--------|-------------|
| Client Concentration | Complete | Arc (37.2%) + Bunzl (27.7%) = 64.9% of revenue — critical risk |
| Revenue Quality | Complete | 50% recurring — below BIC target of 65–75% |
| Gross Margin | Complete | 58.9% blended GM — above BIC benchmark of 44% |
| Net Profitability | Complete | 4.2% net margin — well below BIC target of 18–19% |
| Software Resale Margin | Flagged | -9.4% GM on software resale — requires investigation |
| Client-Level Profitability | Pending | Requires ConnectWise hours-by-client data |
| Technician Utilization | Pending | Requires ConnectWise utilization report |

---

## AI Interaction Guidelines

This repository uses the **Meta-Harness** system for persistent AI memory. Before starting any analysis session, the AI assistant should read:

- `docs/meta/interaction-rules.md`
- `docs/meta/architectural-invariants.md`
- `docs/meta/prompt-evolution.md`

---

*Maintained by Paul Freeman / PulseOne. Analysis powered by Manus AI.*
