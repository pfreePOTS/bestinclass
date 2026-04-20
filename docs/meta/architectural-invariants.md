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

## Invariant 4: Partner Compensation Must Be Normalized for EBITDA

The $423,000 partner compensation line in the P&L is an operating expense. For adjusted EBITDA calculations, this must be normalized to market-rate compensation before comparing to BIC EBITDA benchmarks.

---

## Invariant 5: Software Resale Is an Open Investigation Item

The -9.4% gross margin on software resale is flagged but not yet explained. Do not treat software resale as profitable until the root cause is determined.

---

## Invariant 6: Data Files Are Source of Truth

Raw data files in data/ are the source of truth. Analysis documents in docs/analysis/ are derived. If there is a conflict, the raw data takes precedence.
