# Interaction Rules — PulseOne Best in Class Audit

*Initialized: 2026-04-20*

These rules govern how Manus (and other AI assistants) should behave when working in this repository. They are the project-specific layer on top of the global universal-ai-identity rules.

---

## Project Context

This is the **PulseOne Best in Class Audit** repository. All analysis work is benchmarked against **Service Leadership's Best in Class (BIC) framework** for managed service providers. The user is **Paul Freeman**, co-owner of PulseOne.

---

## Rule 1: Always Load Context Before Analyzing

Before beginning any analysis session, read the following files into context:
- `docs/meta/interaction-rules.md` (this file)
- `docs/meta/architectural-invariants.md`
- `docs/reference/service-leadership-bic-framework-reference.md`

Do not begin analysis without the BIC framework reference in context.

---

## Rule 2: Use Service Leadership BIC Correctly

"Best in Class" in this project refers specifically to **Service Leadership's benchmark methodology**. Do not substitute generic MSP industry advice. Always cite the specific BIC threshold when making a benchmark comparison.

---

## Rule 3: Revenue Figure Reconciliation

There is a known gap between ConnectWise-invoiced revenue ($3.33M in the ClientStatement) and total P&L revenue ($5.17M). Always acknowledge this gap when discussing revenue figures. Do not treat either number as definitive without reconciliation.

---

## Rule 4: Client Concentration Is the Primary Risk

The single most important strategic risk for PulseOne is client concentration: Arc Research (37.2%) and Bunzl family (27.7%) = 64.9% of revenue. Always surface this risk when discussing growth, profitability, or strategic planning.

---

## Rule 5: ConnectWise Is the Missing Data Source

Client-level profitability cannot be completed without ConnectWise hours-by-client data. When analysis is blocked by missing operational data, always specify exactly what to pull from ConnectWise and why.

---

## Rule 6: Output Format

Use the standard 9-section audit format defined in the project instructions:
A. Objective | B. Evidence | C. Current Understanding | D. Findings | E. BIC Alignment | F. Risks & Opportunities | G. Recommended Actions | H. ConnectWise Follow-Up | I. Clarifying Questions

---

## Rule 7: Partner Compensation Normalization

The $423,000 partner compensation line is classified as an operating expense. When calculating adjusted EBITDA for BIC comparison, flag this line as requiring normalization. Do not compare raw net income to BIC EBITDA benchmarks without this adjustment.

---

## Rule 8: Software Resale Margin Is Flagged

The 2025 P&L shows a -9.4% gross margin on software resale ($514K revenue vs $563K cost). This is an open investigation item. Do not treat software resale as a profitable line until this is resolved.
