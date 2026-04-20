# PulseOne BIC Audit — Architectural Invariants
*Hard rules that govern all analysis work on this project*
*Last updated: 2026-04-20*

## Invariant 1: QB P&L Is the Cost Total Anchor

All P&L reclassification work must reconcile to the QB total costs. The sum of corrected COGS + corrected SG&A must equal the QB total costs (excluding Tracy Freeman's $12,888.75 which belongs to POC entity). Any difference greater than $1.00 must be explained. Current reconciliation: $0.30 rounding.

## Invariant 2: Net Income Does Not Change on Reclassification

Moving costs between COGS and SG&A is a presentation correction only. Net operating income must remain the same before and after reclassification ($230,663 corrected, vs. $217,775 QB as-reported — the difference is the Tracy Freeman exclusion only).

## Invariant 3: BIC Benchmarks Are Service Leadership Specific

"Best in Class" refers exclusively to Service Leadership benchmark methodology. Do not substitute generic MSP industry benchmarks. If Service Leadership data is unavailable for a specific metric, state that explicitly rather than using a proxy.

## Invariant 4: Upwork File Period Identification

- File with ~$92K total = YTD 2026 (Jan–Apr 2026)
- File with ~$300K total = Full CY 2025
- Do not use the YTD 2026 file for CY 2025 P&L calculations
- The $35,971 difference between Upwork CY 2025 actual ($299,924) and QB Computer/Internet ($263,953) is unresolved — treat conservatively (assume already in COGS) until bookkeeper confirms

## Invariant 5: Tracy Freeman Is Excluded

Tracy Freeman's costs ($12,888.75 gross) belong to the POC entity, not PulseOne Services. She must be excluded from all PulseOne P&L analysis. Her exclusion is the primary reason corrected net income ($230,663) differs slightly from QB net income ($217,775).

## Invariant 6: Partner Compensation Is Always Normalized Out for EBITDA

Paul Freeman, Charlie Batsford, and Rod (total $423,000) are in SG&A as Partner Compensation. For BIC EBITDA comparison, this is always added back. Normalized EBITDA = Net Income + $423,000 Partner Comp + ~$15,000 D&A.

## Invariant 7: Confirmed Classifications Are Final

The personnel classifications confirmed by Paul Freeman on April 17, 2026 are final. Do not re-open these without explicit instruction. See `docs/meta/interaction-rules.md` for the full confirmed list.
