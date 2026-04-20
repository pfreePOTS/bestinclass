# Prompt Evolution — PulseOne Best in Class Audit

*Initialized: 2026-04-20*

This file tracks lessons learned from AI analysis sessions to improve future prompts and avoid repeating mistakes.

---

## Session 1 — April 20, 2026: Client Profitability Analysis

**Task:** Analyze client and customer profitability from uploaded financial documents.

**What worked well:**
- Loading the BIC framework reference first before analysis ensured benchmarks were correctly applied throughout.
- Separating ConnectWise-invoiced revenue from total P&L revenue early avoided a significant analytical error.
- Treating the Bunzl family as a consolidated economic relationship (not four separate clients) produced a more accurate concentration risk picture.

**Lessons learned:**
- Always check for revenue reconciliation gaps before beginning client-level analysis.
- The payroll file has a large unnamed bucket (~$3M) that needs clarification before labor cost analysis can be completed.
- The software resale COGS line (-9.4% GM) should always be flagged as an open item until resolved — do not include it in margin calculations without a caveat.
- When the P&L contains analyst notes (e.g., "Is this true? If so, we are losing money here"), always surface those notes in the analysis — they represent internal management awareness of issues.

**Prompt improvements for future sessions:**
- When writing prompts for financial analysis, always include: "Check for and flag any analyst notes embedded in the spreadsheet cells."
- When analyzing client concentration, always check for related-entity groupings (e.g., Bunzl family) before reporting top-client percentages.
