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

---

## Session 1 Correction — April 20, 2026: Bunzl Corporate Structure

**Friction event:** The initial analysis incorrectly framed the Bunzl family as a single economic relationship with "critical" concentration risk equivalent to Arc Research. The user corrected this.

**Correct understanding:**
- Bunzl Group is the corporate parent, but PulseOne has separate service relationships with each subsidiary
- Each subsidiary has its own IT environment, agreement, and decision-making authority
- Loss risk is distributed — not monolithic like Arc
- The correct risk severity is "Moderate" (corporate dependency) not "Critical" (single-client concentration)
- The Bunzl pipeline (10 HubSpot subsidiaries not yet in ConnectWise) is the most important growth opportunity

**Lesson for future prompts:**
- When analyzing client families or related entities, always ask: "Does the parent control the buying decision, or does each subsidiary operate independently?"
- If subsidiaries operate independently, report concentration at the subsidiary level, and flag the parent as a "strategic dependency" rather than a "concentration risk"
- Always check HubSpot or CRM data for expansion pipeline context before finalizing a concentration risk assessment

---

## Session 2 — April 20, 2026: Documentation Governance & Naming

**Task:** Run project-docs-manager health check and fix naming, orphans, and consolidation gaps.

**What worked well:**
- Running lifecycle_scanner and organize.sh scan before making changes gave a clear, auditable picture of the repo state.
- Using git mv for renames preserved git history.
- Batch sed replacement of internal references caught 95%+ of cross-links in one pass.

**Lessons learned:**
- Always standardize filenames to lowercase kebab-case from the start of a project. Retrofitting 40+ files is expensive.
- When renaming files, archive docs should be renamed too — downstream tasks that read the manifest need consistent paths.
- The docs-manifest.json must be the single source of truth for all file paths. Any rename must update the manifest atomically.
- Reference files that are not tracked in the manifest will be flagged as orphans by the lifecycle scanner. Add them proactively.

**Prompt improvements for future sessions:**
- When writing prompts for new Manus tasks that commit to the repo, always specify: "Use lowercase kebab-case for all new filenames."
- When writing consolidation prompts, always include: "Move the legacy documents to docs/archive/ and update .docs-manifest.json."
