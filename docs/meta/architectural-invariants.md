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
