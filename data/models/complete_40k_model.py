"""
PulseOne Service Delivery Department - Complete $40K/Month Savings Model
Uses verified data from: Payroll Summary 2026, Upwork 2026, Payoneer 2026, BILL.com 2025
"""

print("="*90)
print("PULSEONE SERVICE DELIVERY - COMPLETE DEPARTMENT ROSTER & $40K REDUCTION MODEL")
print("="*90)
print()

# ============================================================================
# SECTION 1: COMPLETE CURRENT ROSTER (verified from payroll/Upwork/Payoneer data)
# ============================================================================

print("SECTION 1: COMPLETE CURRENT ROSTER")
print("-"*90)

roster = [
    # (Name, Platform, Role, Tier, Monthly Cost, Hourly?, Notes)
    ("Stephen Calkins",    "W-2",      "Service Manager / Escalation (L4)",  "Mgmt",  13867, False, "80 hrs/period"),
    ("James Froio",        "W-2",      "Sr. Tech / Projects / Admin (L3/4)", "Mgmt",  10637, False, "80 hrs/period"),
    ("Laura Walsh",        "W-2",      "Service Delivery Manager",           "Mgmt",  10204, False, "80 hrs/period"),
    ("Kaitlin Harris",     "W-2",      "Technician / Projects (L2)",         "Tech",   7515, False, "80 hrs/period"),
    ("Eric Anzalone",      "W-2",      "Technician / Client Services",       "Tech",   7302, False, "80 hrs/period"),
    ("Nicole Goodwin",     "W-2",      "Technician (PT) (L1/2)",             "Tech",   5152, False, "60 hrs/period"),
    ("Hagen McDonell",     "W-2",      "Technician (L1/2)",                  "Tech",   4709, False, "80 hrs/period"),
    ("Julia Morte",        "W-2",      "Technician (variable) (L1)",         "Tech",   3271, False, "~70 hrs/period"),
    ("Alexandria Calkins", "W-2",      "Dispatch (PT)",                      "Ops",    2103, False, "~45 hrs/period"),
    ("Vincent Williams",   "Upwork",   "Escalations + ITMS Projects (L3)",   "Tech",   9330, True,  "$60/hr"),
    ("Matthew Barnett",    "Upwork",   "Help Desk + Projects (L2/L3)",       "Tech",   7650, True,  "Fixed price contracts"),
    ("Omar Avalos",        "Upwork",   "Help Desk + Onsites (L1/2)",         "Tech",   4080, True,  "$25/hr, 420 hrs YTD"),
    ("Charlesdoone Castro","Upwork",   "Help Desk (Amiri contract) (L1)",    "Tech",   2784, True,  "Amiri gone since 2025"),
    ("Brendan Roe",        "Upwork",   "Help Desk (L1)",                     "Tech",   1908, True,  "$18/hr"),
    ("Dare Olusanjo",      "Payoneer", "Help Desk (offshore) (L1)",          "Tech",   2080, True,  "Biweekly $1,040"),
    ("George Oracion",     "Payoneer", "Help Desk + On-Call (offshore) (L1)","Tech",   1700, True,  "Biweekly $850"),
    ("Roe Tech LLC",       "BILL.com", "Projects + HD (Bunzl focus) (L2)",   "Tech",   8300, True,  "Jeremy + Brendan Roe"),
    ("My IT Services",     "BILL.com", "Projects / Onsites (L2)",            "Tech",   7280, True,  "AJ + Blaine Mulligan"),
]

print(f"{'#':<3} {'Name':<22} {'Platform':<10} {'Tier':<5} {'Cost/Mo':<10} {'Hourly?':<7} {'Role'}")
print("-"*90)
total = 0
mgmt_total = 0
tech_total = 0
ops_total = 0
for i, (name, platform, role, tier, cost, hourly, notes) in enumerate(roster, 1):
    h = "Yes" if hourly else "No"
    print(f"{i:<3} {name:<22} {platform:<10} {tier:<5} ${cost:>7,}  {h:<7} {role}")
    total += cost
    if tier == "Mgmt": mgmt_total += cost
    elif tier == "Tech": tech_total += cost
    elif tier == "Ops": ops_total += cost

print("-"*90)
print(f"    {'TOTAL':<22} {'18 people':<10} {'':5} ${total:>7,}")
print(f"    {'  Management':<22} {'3 people':<10} {'':5} ${mgmt_total:>7,}  ({mgmt_total/total*100:.0f}%)")
print(f"    {'  Technicians':<22} {'14 people':<10} {'':5} ${tech_total:>7,}  ({tech_total/total*100:.0f}%)")
print(f"    {'  Operations':<22} {'1 person':<10} {'':5} ${ops_total:>7,}  ({ops_total/total*100:.0f}%)")
print()

# ============================================================================
# SECTION 2: REVENUE BASELINE
# ============================================================================
print("SECTION 2: REVENUE BASELINE (June 2026)")
print("-"*90)
# From agreement invoicing analysis: $154,659 in June (after ARC, Conejo, etc. already gone)
revenue = 154659
print(f"  Monthly Agreement Revenue:        ${revenue:>10,}")
print(f"  Current Dept Cost:                ${total:>10,}")
print(f"  Current Gross Profit:             ${revenue - total:>10,}")
print(f"  Current Gross Margin:             {(revenue-total)/revenue*100:>9.1f}%")
print(f"  BiC Target Margin:                     50-55%")
print(f"  GAP:                              {50 - (revenue-total)/revenue*100:>9.1f}pp")
print()

# ============================================================================
# SECTION 3: ALL AVAILABLE REDUCTION LEVERS
# ============================================================================
print("SECTION 3: ALL AVAILABLE REDUCTION LEVERS")
print("="*90)
print()

# --- LEVER A: Client Shedding (revenue impact) ---
print("LEVER A: SHED BOTTOM 8 CLIENTS")
print("-"*90)
shed_revenue_loss = 6185
print(f"  Revenue lost:                     -${shed_revenue_loss:>7,}/mo")
print(f"  Tickets eliminated:               ~64/month")
print(f"  Hours freed:                      ~94 hrs/month")
print(f"  Justifies reducing:               ~0.6 FTE of tech capacity")
print()

# --- LEVER B: Immediate Eliminations (zero risk) ---
print("LEVER B: IMMEDIATE ELIMINATIONS (zero operational risk)")
print("-"*90)
elim = [
    ("Charlesdoone Castro", 2784, "Amiri contract - client gone since 2025"),
    ("Breanna Copeland",    0,    "Already appears gone from 2026 payroll"),
]
elim_total = 0
for name, cost, reason in elim:
    if cost > 0:
        print(f"  {name:<25} ${cost:>6,}/mo  Reason: {reason}")
        elim_total += cost
print(f"  SUBTOTAL:                         ${elim_total:>7,}/mo")
print()

# --- LEVER C: Coverage Reduction (9-5 PT) ---
print("LEVER C: COVERAGE HOUR REDUCTION (9-5 Pacific only)")
print("-"*90)
print("  Current: 9am-5pm all US timezones (6am-8pm PT = 14 hrs)")
print("  Proposed: 9am-5pm PT only (8 hrs)")
print()
coverage = [
    ("Dare Olusanjo",  2080, "Eliminate - early shift no longer needed"),
    ("George Oracion",  850, "Reduce 50% - on-call only (nights/weekends)"),
]
coverage_total = 0
for name, savings, action in coverage:
    print(f"  {name:<25} ${savings:>6,}/mo  {action}")
    coverage_total += savings
print(f"  SUBTOTAL:                         ${coverage_total:>7,}/mo")
print()

# --- LEVER D: Contractor Hour Reductions ---
print("LEVER D: CONTRACTOR HOUR REDUCTIONS (all hourly - dial down immediately)")
print("-"*90)
contractor_reductions = [
    ("Roe Tech (Jeremy+Brendan)", 8300, 0.50, "Bunzl projects declining significantly"),
    ("My IT Services (AJ+Blaine)", 7280, 0.50, "Fewer projects/onsites with client losses"),
    ("Vincent Williams",   9330, 0.20, "Protect L3 escalation path - modest cut"),
    ("Matthew Barnett",    7650, 0.25, "Protect L2/L3 - reduce HD allocation"),
    ("Omar Avalos",        4080, 0.30, "Fewer tickets after client shedding"),
    ("Brendan Roe",        1908, 0.50, "Reduce HD hours - covered by others"),
]
contractor_total = 0
print(f"  {'Name':<28} {'Current':<10} {'Cut %':<7} {'Savings':<10} {'Reason'}")
print(f"  {'-'*85}")
for name, current, cut_pct, reason in contractor_reductions:
    savings = int(current * cut_pct)
    contractor_total += savings
    print(f"  {name:<28} ${current:>6,}   {cut_pct*100:>4.0f}%  ${savings:>6,}   {reason}")
print(f"  {'-'*85}")
print(f"  {'SUBTOTAL':<28} {'':10} {'':7} ${contractor_total:>6,}")
print()

# --- LEVER E: W-2 Furloughs (user-specified rates) ---
print("LEVER E: W-2 FURLOUGHS (user-specified reduction rates)")
print("-"*90)
furloughs = [
    ("Stephen Calkins",  13867, 0.15, "4-day weeks / reduced schedule"),
    ("Laura Walsh",      10204, 0.10, "Absorbs dispatch, reduced schedule"),
    ("James Froio",      10637, 0.10, "Reduced admin time"),
    ("Eric Anzalone",     7302, 0.10, "Reduced schedule"),
    ("Kaitlin Harris",    7515, 0.20, "Projects declining - significant reduction"),
    ("Hagen McDonell",    4709, 0.20, "Reduced schedule"),
    ("Nicole Goodwin",    5152, 0.25, "Already PT - further reduction"),
    ("Julia Morte",       3271, 0.20, "Variable hours - reduce floor"),
    ("Alexandria Calkins",2103, 1.00, "Eliminate - Walsh absorbs dispatch"),
]
furlough_total = 0
print(f"  {'Name':<22} {'Current':<10} {'Cut %':<7} {'Savings':<10} {'Action'}")
print(f"  {'-'*80}")
for name, current, cut_pct, action in furloughs:
    savings = int(current * cut_pct)
    furlough_total += savings
    if cut_pct == 1.0:
        print(f"  {name:<22} ${current:>6,}   100%   ${savings:>6,}   ELIMINATE: {action}")
    else:
        new_cost = current - savings
        print(f"  {name:<22} ${current:>6,}   {cut_pct*100:>4.0f}%  ${savings:>6,}   {action} (new: ${new_cost:,})")
print(f"  {'-'*80}")
print(f"  {'SUBTOTAL':<22} {'':10} {'':7} ${furlough_total:>6,}")
print()

# ============================================================================
# SECTION 4: TOTAL PLAN SUMMARY
# ============================================================================
print("="*90)
print("SECTION 4: TOTAL PLAN SUMMARY")
print("="*90)
print()

total_savings = elim_total + coverage_total + contractor_total + furlough_total
net_improvement = total_savings - shed_revenue_loss

print(f"  COST REDUCTIONS:")
print(f"    B. Immediate eliminations:        +${elim_total:>7,}/mo")
print(f"    C. Coverage hour reductions:      +${coverage_total:>7,}/mo")
print(f"    D. Contractor hour reductions:    +${contractor_total:>7,}/mo")
print(f"    E. W-2 furloughs & eliminations:  +${furlough_total:>7,}/mo")
print(f"    ─────────────────────────────────────────────")
print(f"    TOTAL COST SAVINGS:               +${total_savings:>7,}/mo")
print()
print(f"  REVENUE IMPACT:")
print(f"    A. Revenue lost (8 shed clients): -${shed_revenue_loss:>7,}/mo")
print()
print(f"  ═══════════════════════════════════════════════")
print(f"  NET MONTHLY P&L IMPROVEMENT:        +${net_improvement:>7,}/mo")
print(f"  NET ANNUAL P&L IMPROVEMENT:         +${net_improvement*12:>7,}/yr")
print(f"  ═══════════════════════════════════════════════")
print()

# Target check
target = 40000
if net_improvement >= target:
    print(f"  ✓ TARGET ACHIEVED: ${net_improvement:,}/mo vs ${target:,}/mo target (+${net_improvement-target:,} buffer)")
else:
    print(f"  ✗ SHORT OF TARGET: ${net_improvement:,}/mo vs ${target:,}/mo target (-${target-net_improvement:,} gap)")
print()

# ============================================================================
# SECTION 5: BEFORE vs AFTER
# ============================================================================
print("SECTION 5: BEFORE vs AFTER")
print("-"*90)

new_revenue = revenue - shed_revenue_loss
new_cost = total - total_savings
new_profit = new_revenue - new_cost
new_margin = new_profit / new_revenue * 100

print(f"  {'Metric':<30} {'BEFORE':<15} {'AFTER':<15} {'CHANGE'}")
print(f"  {'-'*75}")
print(f"  {'Monthly Revenue':<30} ${revenue:>10,}  ${new_revenue:>10,}  -${shed_revenue_loss:,}")
print(f"  {'Monthly Dept Cost':<30} ${total:>10,}  ${new_cost:>10,}  -${total_savings:,}")
print(f"  {'Monthly Gross Profit':<30} ${revenue-total:>10,}  ${new_profit:>10,}  +${net_improvement:,}")
print(f"  {'Gross Margin':<30} {(revenue-total)/revenue*100:>9.1f}%  {new_margin:>9.1f}%  +{new_margin-(revenue-total)/revenue*100:.1f}pp")
print(f"  {'Headcount':<30} {'18':<15} {'~12 reduced':<15}")
print(f"  {'BiC Target (50-55%)':<30} {'BELOW':<15} {'{'+'MET' if new_margin >= 50 else 'CLOSE'+'}':<15}")
print()

# ============================================================================
# SECTION 6: PEOPLE ACTIONS SUMMARY
# ============================================================================
print("SECTION 6: PEOPLE ACTIONS SUMMARY")
print("-"*90)
print()
print("  TERMINATED (4 people):")
print("    Charlesdoone Castro (Upwork)    $2,784/mo  Dead client contract")
print("    Dare Olusanjo (Payoneer)        $2,080/mo  Coverage hours eliminated")
print("    Alexandria Calkins (W-2 PT)     $2,103/mo  Dispatch absorbed by Walsh")
print("    [Breanna Copeland]              Already gone from 2026 payroll")
print()
print("  REDUCED HOURS - Contractors (6 entities):")
for name, current, cut_pct, reason in contractor_reductions:
    savings = int(current * cut_pct)
    new = current - savings
    print(f"    {name:<28} ${current:>6,} → ${new:>6,}  (-{cut_pct*100:.0f}%)")
print()
print("  REDUCED HOURS - W-2 (7 people):")
for name, current, cut_pct, action in furloughs:
    if cut_pct < 1.0:
        savings = int(current * cut_pct)
        new = current - savings
        print(f"    {name:<22} ${current:>6,} → ${new:>6,}  (-{cut_pct*100:.0f}%)")
print()
print("  UNCHANGED (1 person):")
print("    George Oracion (50% reduction already counted in coverage lever)")
