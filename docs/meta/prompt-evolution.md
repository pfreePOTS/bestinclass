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

---

## Session 3 — April 20, 2026: Project Profitability & Data Tracing

**Task:** Deep dive into the Consulting/Projects margin to reconcile a 47.1% QuickBase cash margin against a 24.2% P&L fully-loaded margin.

**What worked well:**
- Stepping back to write a "What we actually know" script that pulled only from raw source files (QuickBase, Upwork) rather than derived analysis documents.
- Clearly defining the difference between "Cash Margin" (revenue minus out-of-pocket invoices) and "Fully-Loaded Gross Margin" (which requires W-2 labor allocation).
- Isolating ARC Research as "Staff Augmentation" rather than discrete project delivery, which clarified the underlying structural issue.

**Lessons learned:**
- **Never trust a derived number without a clear source trail.** The 24.2% margin on $1,175,036 revenue cited in earlier documents could not be traced to a single primary source. It was an artifact of P&L allocation logic, not a direct measurement.
- The P&L is a blunt instrument. When QuickBooks lumps W-2 payroll into a single line, any segment margin derived from it is an *estimate based on allocation*, not a fact.
- "Invisible Subsidies" are a major risk in MSP accounting. When Help Desk W-2 staff work on projects but don't log project-specific costs, the project margin looks artificially high and the Help Desk margin looks artificially low.

**Prompt improvements for future sessions:**
- When writing prompts for profitability analysis, always include: "Distinguish between Cash Margin (revenue minus direct out-of-pocket expenses) and Fully-Loaded Gross Margin (including allocated W-2 labor and burden)."
- When a derived metric (like a blended margin) is questioned, always include: "Trace the figure back to its raw source data (e.g., QuickBase, ADP, ConnectWise) before defending it."
- When analyzing project profitability, always ask: "Are internal W-2 resources used on these projects? If so, how is their cost tracked and allocated?"

## Session 4 — April 22, 2026: Subcontractor and Product Tracing

**Task:** Rebuild the segment P&Ls with exact owner allocations and trace the remaining $373K COGS gap.

**What worked well:**
- Creating a script to trace the entire QuickBooks "Consulting Services-Cost" line item by vendor and client memo, rather than relying on prior estimates.
- Finding that the CS-Cost line was a multi-segment dumping ground containing $650K ARC, $343K Projects, and $46K misclassified SGA (Marcello).
- Proving that the project margin was 44.0% traceable, not 64.2% as the un-traced model suggested.
- Proving that M365 is a healthy standalone product line (~43% GM), not a 16.4% margin drag on Managed Services.

**Lessons learned:**
- **Never treat a QuickBooks COGS line as a single segment.** The CS-Cost line contained costs for ARC, Projects, and Marketing. Any model that doesn't trace it at the vendor level will be massively wrong.
- **Product Resale is a separate P&L stream.** Dumping product COGS into Managed Services artificially depresses the MS margin (e.g., from 73.1% down to 36.6%).
- **Data integrity is fragile.** The fact that Adobe was an ARC purchase was known in an early document, but overwritten in a later document with "Bunzl." Always trace back to the source data when an anomaly appears.

**Prompt improvements for future sessions:**
- When analyzing P&L segments, always include: "Trace the Consulting Services-Cost line at the vendor/client level before allocating it to a segment."
- When analyzing Managed Services margin, always include: "Ensure standalone product sales (M365, hardware, Adobe) are separated from MS service delivery costs."

---

## Session 5 — May 7, 2026: Sales Rep Performance Audit & IT Assessment Conversion

**Task:** Audit sales rep performance using 2025 and 2026 won opportunity exports. Analyze sales mix, IT Assessment conversion rates, and managed services production by rep.

**What worked well:**
- Starting with raw CSV exploration before building classification logic ensured correct column mapping.
- Iterative reclassification based on user feedback (separating Software from MS, Comprehensive from MS, IT Assessments from Projects, Hardware from ITMS/Install) produced a much more accurate picture than the raw ConnectWise categories.
- Cross-referencing IT Assessment clients against all subsequent deal types revealed the broken conversion engine — assessments lead to hardware/projects, not MS agreements.
- The user's domain knowledge corrections (Santa Barbara Sky refunded, Bunzl = Cool Pak location, Arc Research gone April 1) were critical to accuracy.

**Lessons learned:**
- **ConnectWise "Install Type" and "Opportunity Type" fields are unreliable for classification.** A deal marked "ITMS/Install" could be a laptop purchase, a Windows 11 refresh, or actual managed services delivery. Always classify by opportunity name content first, then fall back to Install Type.
- **Software vendors (AvePoint, Barracuda, Microsoft) must be identified by name in the opportunity, not by Install Type.** These appear under multiple Install Types (Agreement, Procurement, Renewal) but are all fundamentally software resale.
- **"Managed Services / Install" is a misleading category.** It contains both true MS delivery work AND hardware purchases delivered to MS clients. Must filter by opportunity name keywords (laptop, shipping, dock, monitor = hardware; firewall install, Windows refresh, onboarding = MS delivery).
- **IT Assessments are projects, not agreements.** Even though they are a sales pipeline step toward MS, they should be categorized as a project sub-type for revenue classification purposes.
- **Comprehensive Services (Arc Research) must be separated from standard Managed Services.** It distorts the MS production picture if combined — one $178K client makes a rep look productive when their true MS sales are $5.8K.
- **Always ask about refunds and client status.** Won opportunity reports show deals as closed, but some may have been subsequently refunded or the client may have churned. User confirmation is essential.

**Prompt improvements for future sessions:**
- When analyzing ConnectWise won opportunity data, always include: "Classify deals by opportunity name content first (vendor keywords, service keywords), then by Install Type as a fallback. Never trust Install Type alone."
- When calculating managed services production, always include: "Exclude hardware purchases (laptops, shipping, docks, monitors) that happen to be delivered through the ITMS channel. Only count true service delivery and agreement revenue."
- When reporting IT Assessment conversion, always include: "A 'conversion' means the client signed a recurring Managed Services Agreement, not just that they bought hardware or a one-time project from us after the assessment."
- When analyzing sales rep productivity, always include: "Separate software renewal processing (AvePoint, Barracuda, Microsoft) from consultative selling (IT Assessments, Projects, MS Agreements). These are fundamentally different activities with different value to the business."
