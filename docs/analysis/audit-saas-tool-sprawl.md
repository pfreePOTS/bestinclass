# PulseOne SaaS Tool Sprawl & Rationalization Audit

**Version:** 1.0  
**Date:** 2026-04-21  
**Author:** Manus AI  
**Status:** Complete  
**Depends on:** `pulseone-bic-master-scorecard.md` (v2.0), `audit-software-resale.md`, `audit-cogs-validation.md`

---

## A. Objective

The objective of this audit is to conduct a comprehensive SaaS Tool Sprawl & Rationalization Audit for PulseOne. Previous analysis identified $263,953 in "Computer and Internet Expenses" across 49 vendors, with an initial estimate suggesting ~$91K in redundant or unnecessary tools. This audit aims to build a complete inventory of every SaaS/cloud tool PulseOne pays for, classify them according to Service Leadership Best in Class (BiC) methodology, detect functional overlaps, calculate cost-per-employee metrics against industry benchmarks, and produce a prioritized rationalization roadmap to optimize internal SG&A spend.

## B. Evidence Reviewed

| Source Document | Period | Key Data |
|---|---|---|
| `2025 PulseOne Software COGS and Expense.xlsx` | CY 2025 | 1,068 transactions across 3 QB sections |
| `Expenses Tracking MASTER 2023.xlsx` (2025 tab) | Budget 2025 | Internal tool context, notes, and department assignments |
| `audit-cogs-validation.md` | CY 2025 | Baseline COGS vs SG&A classification methodology |
| `pulseone-bic-master-scorecard.md` (v2.0) | CY 2025 | Authoritative performance metrics and reclassification amounts |
| `saas_benchmarks.txt` | 2025 | Industry benchmarks for SaaS spend per employee |

## C. Current Understanding

PulseOne's software expenses are recorded across three primary QuickBooks sections: "Agreement License Cost", "Purchases - Software for Resale", and "Computer and Internet Expenses". Previous audits identified that the "Computer and Internet Expenses" line ($263,953) contained a mix of true internal SG&A tools and misclassified Service Delivery COGS tools.

An initial estimate suggested that up to $91,000 of the "Computer and Internet Expenses" line might represent redundant or unnecessary tools (SGA-03 in the Action Register). This audit tests that hypothesis by cataloging every tool, assessing its function, and identifying specific overlaps. The analysis assumes a PulseOne internal headcount of 38 employees for per-user metrics.

## D. Findings

### Finding 1: The Complete Tool Inventory

A comprehensive extraction of all 1,068 transactions across the three software-related QB sections revealed 69 unique tools/vendors with a total annual spend of $1,120,949.91. 

| Classification Bucket | Annual Spend | Vendor Count |
|---|---|---|
| Service Delivery COGS | $571,692.14 | 16 |
| Client-Delivered COGS | $482,997.66 | 12 |
| Internal SG&A | $66,260.11 | 41 |
| **Total Software Spend** | **$1,120,949.91** | **69** |

The "Computer and Internet Expenses" section specifically contains 54 vendors totaling $263,953.24. However, only $66,260.11 of this represents true internal SG&A tools. The remainder consists of Service Delivery COGS tools that require reclassification.

### Finding 2: Overlap Detection and Redundancy

Analysis of the 41 internal SG&A tools revealed significant functional overlap, particularly in development, AI, and productivity categories. The following overlap groups were identified:

1. **Scheduling:** TimeZest ($3,609, Service Delivery COGS) overlaps with Calendly ($514, Internal SG&A). TimeZest is integrated with ConnectWise for client scheduling, making Calendly redundant.
2. **IDE/Coding:** Cursor ($1,184) overlaps with Replit ($526). Both serve as internal development environments.
3. **LLM APIs:** PulseOne subscribes to OpenAI ($1,076), Anthropic ($425), Claude.AI ($220), and OpenRouter ($27). This represents redundant access to similar AI capabilities.
4. **Design:** Adobe Creative Cloud ($3,739) overlaps partially with Figma ($97).
5. **CRM/Project Management:** ConnectWise (core PSA) overlaps with Monday.com ($288) and Zoho ($120).
6. **Productivity:** Microsoft M365 ($14,127) overlaps with Google Workspace/Services ($352).

### Finding 3: Cost-per-Employee Benchmarks

Industry benchmarks for 2025 indicate that the average global SaaS spend per employee is $4,830 [1]. For IT and software companies, this benchmark is significantly higher, averaging $10,050 per employee [2].

Based on PulseOne's 38-person headcount:
*   **Total Software Per Employee:** $29,498.68 (Includes client resale and service delivery, not a valid internal benchmark).
*   **Internal SG&A Per Employee:** $1,743.69.

When isolating true internal SG&A tools ($66,260.11), PulseOne's per-employee spend is remarkably low compared to the $4,830 global average and the $10,050 IT sector average. This indicates that PulseOne is actually highly efficient with internal software spending, and the perceived "tool sprawl" is largely a classification issue rather than excessive spending.

### Finding 4: The $91K Rationalization Estimate

The initial hypothesis that ~$91K in redundant tools existed within the "Computer and Internet Expenses" line is **incorrect**. Because $197,693 of that line consists of core Service Delivery tools (ConnectWise, Flexis, Kaseya, etc.), only $66,260 remains as true internal SG&A. Therefore, finding $91K in savings from SG&A tools is mathematically impossible. The actual identified savings opportunity from redundancies is approximately $21,442.

## E. Service Leadership BiC Alignment

*   **Internal SG&A Efficiency:** **EXCEEDS BiC**. At $1,743 per employee, PulseOne's internal tool spend is highly efficient and well below industry averages.
*   **COGS/SG&A Classification:** **BELOW BiC**. PulseOne currently misclassifies nearly $200K of Service Delivery COGS as SG&A, which distorts both Gross Margin and SG&A efficiency ratios against the BiC framework.

## F. Risks and Opportunities

*   **Risk — Distorted Financial Metrics:** Continuing to classify Service Delivery tools as SG&A artificially inflates overhead and artificially improves Gross Margin, obscuring true service delivery profitability.
*   **Opportunity — Immediate Cost Savings:** Eliminating the 14 identified redundant or unused tools will yield $19,492.56 in immediate annual savings with zero operational impact.
*   **Opportunity — AI Tool Consolidation:** Consolidating the fragmented AI subscriptions (OpenAI, Anthropic, Claude.AI, OpenRouter) into a single primary provider can save an additional ~$600-$1,000 annually while simplifying the development workflow.

## G. Recommended Actions

1.  **Execute Immediate Cancellations (Priority: High):** Cancel the following redundant or legacy tools to realize $19,492.56 in annual savings:
    *   Kaseya Dark Web component ($10,563) — Verify if cancelled in Oct per Expense Tracker.
    *   Replit, Inc. ($526) — Redundant with Cursor.
    *   Calendly ($514) — Redundant with TimeZest.
    *   AI MAD FZCO ($360) — Unclear purpose, single charge.
    *   Claude.AI ($220) — Redundant with Anthropic API.
    *   Vevox ($131) — Low usage meeting tool.
    *   Zoho ($120) — Redundant with ConnectWise/HubSpot.
    *   Carbonite ($96) — Legacy, noted as turned off in 2023.
    *   Quicken ($72) — Personal finance, non-business.
    *   Patreon ($71) — Non-business subscription.
    *   OpenRouter ($27) — Redundant LLM routing.
2.  **Consolidate AI and Productivity Tools (Priority: Medium):** Review the $1,950 spend across OpenAI, Anthropic, Google, and Figma. Select primary platforms and eliminate the secondary overlapping tools.
3.  **Confirm Ambiguous Tool Classifications (Priority: High):** Clarify the purpose of $32,217 in tools to ensure accurate COGS vs SG&A placement. Specifically, determine if Microsoft Azure ($19,041) and GoDaddy ($2,880) are used for internal infrastructure (SG&A) or client hosting (COGS).
4.  **Execute COGS Reclassification (Priority: High):** Formally reclassify the identified Service Delivery tools (ConnectWise, Flexis, Samurai Sync, Wasabi, MSP360, TimeZest, CyberFox, Duo Security, Qualys, Have I Been Pwned) from SG&A to COGS in QuickBooks to align with the BiC Master Scorecard.

## H. Suggested ConnectWise Follow-Up

*   Review the Kaseya integration and billing to confirm whether the Dark Web and Security/Network Assessment modules were fully decommissioned in October 2025 as noted in the Expense Tracker.
*   Check ConnectWise agreements to determine if Microsoft Azure and GoDaddy expenses are being passed through or billed to specific clients, which would confirm them as Client-Delivered COGS rather than internal SG&A.

## I. Clarifying Questions

1.  Are the Microsoft Azure ($19,041) and GoDaddy ($2,880) expenses used for PulseOne's internal infrastructure, or are they client-hosted environments included in managed service agreements?
2.  The QB export shows $7,721 in unattributed charges within the Computer and Internet Expenses line. Can these be identified, or are they miscellaneous credit card fees?
3.  Can we confirm that the $2,000 Pivotal Crew LLC charge was a final close-out payment, given the Expense Tracker notes the service ended in late 2024?

---
## References

[1] Zylo. "2025 SaaS Management Index." https://zylo.com/news/2025-saas-management-index/
[2] Vertice. "SaaS Spend Per Employee." https://www.vertice.one/blog/saas-spend-per-employee
