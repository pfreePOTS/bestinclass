#!/usr/bin/env python3
"""
PulseOne Departmental Expense Sheet & P&L — v7.1 (CORRECTED)
=============================================================
FIXES APPLIED:
1. W-2 amounts = ADP GROSS PAY ONLY (stripped employer liability)
   Source: ADP Payroll Detail, check dates 1/10/2025 - 12/26/2025
2. "Other OpEx" REMOVED — was a fake derived category with no real source
3. Payroll Tax/Benefits ($310,876) = separate real QB line, allocated to W-2 segments
4. Upwork = file actual ($299,924)
5. No double-counting of Payoneer (listed once per person, in their department)

Total model will NOT tie to QB $4,950,980 because QB includes expense lines
we haven't individually identified (rent, insurance, prof fees, etc.).
The DIFFERENCE between our model and QB = those unidentified operating expenses.
This is transparent — not hidden in a fake bucket.
"""

# ============================================================
# ALL PEOPLE
# ============================================================
people = [
    # --- W-2 Dept 100: Services Tech Service (ADP GROSS only) ---
    {"name": "Stephen Calkins", "method": "W-2", "total": 148_960,
     "alloc": {"MS": 0.60, "Projects": 0.15, "G&A": 0.20, "Sales": 0.05}},
    {"name": "James Froio", "method": "W-2", "total": 112_788,
     "alloc": {"MS": 0.25, "Projects": 0.30, "G&A": 0.45}},
    {"name": "Laura Walsh", "method": "W-2", "total": 108_186,
     "alloc": {"Projects": 0.35, "Sales": 0.30, "G&A": 0.35}},
    {"name": "Kaitlin Harris", "method": "W-2", "total": 79_760,
     "alloc": {"Projects": 0.90, "MS": 0.10}},
    {"name": "Eric Anzalone", "method": "W-2", "total": 76_718,
     "alloc": {"Sales": 1.00}},
    {"name": "Hagen McDonell", "method": "W-2", "total": 51_611,
     "alloc": {"MS": 0.80, "Projects": 0.20}},
    {"name": "Nicole Goodwin (Dept 100)", "method": "W-2", "total": 38_150,
     "alloc": {"MS": 1.00}},
    {"name": "Joel Alvarez", "method": "W-2", "total": 25_850,
     "alloc": {"MS": 1.00}},
    {"name": "Julia Morte", "method": "W-2", "total": 20_322,
     "alloc": {"MS": 1.00}},
    {"name": "Alexandria Calkins", "method": "W-2", "total": 17_258,
     "alloc": {"MS": 1.00}},
    {"name": "Breanna Copeland", "method": "W-2", "total": 11_444,
     "alloc": {"MS": 1.00}},
    {"name": "Debby Brooke", "method": "W-2", "total": 7_928,
     "alloc": {"MS": 1.00}},
    # --- W-2 Dept 200: Marketing (ADP GROSS only) ---
    {"name": "Chad Wiggins", "method": "W-2", "total": 95_000,
     "alloc": {"Sales": 1.00}},
    {"name": "Kyle Carey", "method": "W-2", "total": 51_800,
     "alloc": {"Sales": 0.50, "Marketing": 0.50}},
    {"name": "Marcello Moreira (W-2)", "method": "W-2", "total": 33_280,
     "alloc": {"Sales": 1.00}},
    {"name": "Heather Kohler", "method": "W-2", "total": 13_200,
     "alloc": {"Sales": 1.00}},
    {"name": "Dana Rankin", "method": "W-2", "total": 9_200,
     "alloc": {"Marketing": 1.00}},
    {"name": "Andrea Carcamo", "method": "W-2", "total": 7_492,
     "alloc": {"Marketing": 1.00}},
    {"name": "Anneliese Rivera", "method": "W-2", "total": 4_100,
     "alloc": {"Marketing": 0.50, "Non-Op": 0.50}},
    # --- W-2 Dept 300: Operations (ADP GROSS only) ---
    {"name": "Aimee Brock", "method": "W-2", "total": 23_300,
     "alloc": {"G&A": 1.00}},
    {"name": "Emily Wolf", "method": "W-2", "total": 18_400,
     "alloc": {"G&A": 1.00}},
    {"name": "Emily Acker", "method": "W-2", "total": 9_690,
     "alloc": {"G&A": 1.00}},
    {"name": "Jamie Davin", "method": "W-2", "total": 9_911,
     "alloc": {"G&A": 1.00}},
    {"name": "Juliet Simpson", "method": "W-2", "total": 9_262,
     "alloc": {"G&A": 1.00}},
    {"name": "Ashley Holmes", "method": "W-2", "total": 725,
     "alloc": {"G&A": 1.00}},
    # --- W-2 Dept 900: POC (ADP GROSS only) ---
    {"name": "Tracy Freeman", "method": "W-2", "total": 12_889,
     "alloc": {"Non-Op": 1.00}},
    {"name": "Nicole Goodwin (Dept 900/POC)", "method": "W-2", "total": 12_950,
     "alloc": {"Non-Op": 1.00}},
    # --- Partners (guaranteed payments) ---
    {"name": "Charlie Batsford", "method": "Partner", "total": 141_000,
     "alloc": {"G&A": 1.00}},
    {"name": "Paul Freeman", "method": "Partner", "total": 141_000,
     "alloc": {"Sales": 0.30, "Marketing": 0.70}},
    {"name": "Rod", "method": "Partner", "total": 141_000,
     "alloc": {"G&A": 1.00}},
    # --- Upwork (CY2025 file confirmed) ---
    {"name": "Vincent Williams", "method": "Upwork", "total": 104_740,
     "alloc": {"MS": 0.20, "Projects": 0.80}},
    {"name": "Matt Barnett", "method": "Upwork", "total": 83_390,
     "alloc": {"MS": 0.75, "Projects": 0.25}},
    {"name": "Omar Avalos", "method": "Upwork", "total": 49_442,
     "alloc": {"MS": 1.00}},
    {"name": "Charlesdoone Castro", "method": "Upwork", "total": 38_228,
     "alloc": {"MS": 1.00}},
    {"name": "Brendan Roe", "method": "Upwork", "total": 6_476,
     "alloc": {"Projects": 1.00}},
    {"name": "Basim Mashni (Upwork)", "method": "Upwork", "total": 5_906,
     "alloc": {"Comprehensive": 1.00}},
    {"name": "William McMillan", "method": "Upwork", "total": 4_444,
     "alloc": {"Projects": 1.00}},
    {"name": "Kirill Hovansky", "method": "Upwork", "total": 3_660,
     "alloc": {"Marketing": 1.00}},
    {"name": "Sabah Razaq", "method": "Upwork", "total": 2_438,
     "alloc": {"Marketing": 1.00}},
    {"name": "Yana Kosenko", "method": "Upwork", "total": 700,
     "alloc": {"Marketing": 1.00}},
    {"name": "Dustin Hagemeier", "method": "Upwork", "total": 500,
     "alloc": {"MS": 1.00}},
    # --- BILL / CS-Cost contractors ---
    {"name": "Blue Pisces - Ruben (ARC)", "method": "BILL", "total": 193_246,
     "alloc": {"Comprehensive": 1.00}},
    {"name": "David Fredrik (Falkenberg)", "method": "BILL", "total": 171_003,
     "alloc": {"Comprehensive": 1.00}},
    {"name": "Mash Tech (Basim BILL)", "method": "BILL", "total": 148_918,
     "alloc": {"Comprehensive": 1.00}},
    {"name": "Infinite Ideas (BJ Sinder)", "method": "BILL", "total": 132_390,
     "alloc": {"Comprehensive": 1.00}},
    {"name": "Blue Pisces - Damien+Julia", "method": "BILL", "total": 229_843,
     "alloc": {"Comprehensive": 1.00}},
    {"name": "Roe Tech (Jeremy Roe)", "method": "BILL", "total": 100_097,
     "alloc": {"Projects": 0.90, "Comprehensive": 0.10}},
    {"name": "Other Project Subs", "method": "BILL", "total": 13_187,
     "alloc": {"Projects": 1.00}},
    {"name": "MS Subs (misc)", "method": "BILL", "total": 6_677,
     "alloc": {"MS": 1.00}},
    {"name": "Marcy Dorman-Chandler", "method": "BILL", "total": 9_600,
     "alloc": {"Marketing": 1.00}},
    # --- Payoneer (international contractors) ---
    {"name": "Marcello Moreira (Payoneer)", "method": "Payoneer", "total": 42_645,
     "alloc": {"Sales": 1.00}},
    {"name": "George Oracion", "method": "Payoneer", "total": 43_020,
     "alloc": {"MS": 1.00}},
    {"name": "Dare Olusanjo", "method": "Payoneer", "total": 50_175,
     "alloc": {"MS": 1.00}},
    {"name": "Daniyal Arif", "method": "Payoneer", "total": 52_997,
     "alloc": {"Marketing": 0.50, "Non-Op": 0.50}},
    {"name": "Peal Miah", "method": "Payoneer", "total": 5_850,
     "alloc": {"Comprehensive": 1.00}},
    # --- Other ---
    # NOTE (May 4, 2026): Badar = "Batter" (same person). Actual total ~$41,885
    # from QB Salary Detail (Payoneer payments). Primarily service delivery, NOT
    # 100% RepScheduler. Pending owner confirmation of segment split (MS vs Projects).
    # Once confirmed, update total from 30,300 to ~41,885 and change alloc from
    # Non-Op to the correct service delivery segment(s).
    {"name": "Badar", "method": "Payoneer", "total": 30_300,
     "alloc": {"Non-Op": 1.00}},  # TODO: Reallocate per owner direction
]

# ============================================================
# Non-labor costs (verified from actual data)
# ============================================================
nonlabor_items = {
    "MS": [
        ("Service Delivery Tools (C&I split)", 197_693),
        ("Skout/Barracuda SOC (Agmt Lic Cost)", 72_960),
        ("EFolder/Axcient Backup (SW Resale)", 10_719),
    ],
    "Projects": [
        ("Installation Services (QB line)", 3_170),
    ],
    "Products-HW": [
        ("Hardware COGS (QB HW for Resale)", 135_697),
    ],
    "Products-SW": [
        ("Software Licensing COGS", 713_110),
    ],
    "Products-Cloud": [
        ("Hosting/Cloud COGS", 131_775),
    ],
    "Products-Other": [
        ("Merchant Fees", 10_468),
    ],
    "G&A": [
        ("Internal Tools (C&I split)", 58_539),
        ("C&I Unclassified", 7_721),
        ("ScalePad + Atlassian (from SW Resale)", 8_950),
    ],
    "Non-Op": [
        ("RepScheduler Platform Costs", 39_560),
    ],
}

# ============================================================
# AGGREGATE
# ============================================================
segments = ["MS", "Comprehensive", "Projects", "Sales", "Marketing", "G&A", "Non-Op"]
seg_labor = {s: [] for s in segments}
seg_labor_total = {s: 0 for s in segments}

for p in people:
    for dept, pct in p["alloc"].items():
        amt = round(p["total"] * pct)
        seg_labor[dept].append({"name": p["name"], "method": p["method"], "pct": pct, "amount": amt})
        seg_labor_total[dept] += amt

# Payroll tax/benefits: allocated proportionally to W-2 gross by segment
ptax_total = 310_876
total_w2 = sum(p["total"] for p in people if p["method"] == "W-2")
w2_by_seg = {s: 0 for s in segments}
for p in people:
    if p["method"] == "W-2":
        for dept, pct in p["alloc"].items():
            w2_by_seg[dept] += p["total"] * pct
ptax_by_seg = {s: round(ptax_total * w2_by_seg[s] / total_w2) if total_w2 > 0 else 0 for s in segments}

# ============================================================
# OUTPUT
# ============================================================
def print_dept(name, seg_key):
    entries = sorted(seg_labor[seg_key], key=lambda x: -x["amount"])
    print(f"\n{'='*90}")
    print(f"  {name}")
    print(f"{'='*90}")
    print(f"  {'Name':<38} {'Method':<10} {'Alloc':>6} {'Amount':>12}")
    print(f"  {'-'*70}")
    for e in entries:
        pstr = f"{e['pct']*100:.0f}%" if e['pct'] < 1.0 else "100%"
        print(f"  {e['name']:<38} {e['method']:<10} {pstr:>6} ${e['amount']:>10,}")
    print(f"  {'-'*70}")
    print(f"  {'Labor Subtotal':<38} {'':10} {'':>6} ${seg_labor_total[seg_key]:>10,}")
    print(f"  {'Payroll Tax/Benefits (W-2 only)':<38} {'':10} {'':>6} ${ptax_by_seg[seg_key]:>10,}")
    labor_plus_tax = seg_labor_total[seg_key] + ptax_by_seg[seg_key]
    print(f"  {'Total Labor + Benefits':<38} {'':10} {'':>6} ${labor_plus_tax:>10,}")
    return labor_plus_tax

ms_lt = print_dept("MANAGED SERVICES (COGS)", "MS")
ms_nl = sum(a for _, a in nonlabor_items["MS"])
print(f"\n  Non-Labor:")
for item, amt in nonlabor_items["MS"]:
    print(f"    {item:<50} ${amt:>10,}")
print(f"  {'Non-Labor Subtotal':<38} {'':10} {'':>6} ${ms_nl:>10,}")
ms_total = ms_lt + ms_nl
print(f"\n  {'>>> MS TOTAL COGS':<38} {'':10} {'':>6} ${ms_total:>10,}")

comp_lt = print_dept("COMPREHENSIVE SERVICES (COGS)", "Comprehensive")
comp_total = comp_lt
print(f"\n  {'>>> COMP TOTAL COGS':<38} {'':10} {'':>6} ${comp_total:>10,}")

proj_lt = print_dept("TRUE PROJECTS (COGS)", "Projects")
proj_nl = sum(a for _, a in nonlabor_items["Projects"])
print(f"\n  Non-Labor:")
for item, amt in nonlabor_items["Projects"]:
    print(f"    {item:<50} ${amt:>10,}")
proj_total = proj_lt + proj_nl
print(f"\n  {'>>> PROJECTS TOTAL COGS':<38} {'':10} {'':>6} ${proj_total:>10,}")

print(f"\n{'='*90}")
print(f"  PRODUCTS & LICENSING (COGS)")
print(f"{'='*90}")
prod_hw = sum(a for _, a in nonlabor_items["Products-HW"])
prod_sw = sum(a for _, a in nonlabor_items["Products-SW"])
prod_cl = sum(a for _, a in nonlabor_items["Products-Cloud"])
prod_ot = sum(a for _, a in nonlabor_items["Products-Other"])
print(f"  {'Hardware COGS':<50} ${prod_hw:>10,}")
print(f"  {'Software Licensing COGS':<50} ${prod_sw:>10,}")
print(f"  {'Hosting/Cloud COGS':<50} ${prod_cl:>10,}")
print(f"  {'Merchant Fees':<50} ${prod_ot:>10,}")
prod_total = prod_hw + prod_sw + prod_cl + prod_ot
print(f"  {'-'*66}")
print(f"  {'>>> PRODUCTS TOTAL COGS':<50} ${prod_total:>10,}")

sales_lt = print_dept("SALES (SG&A)", "Sales")
sales_total = sales_lt
print(f"\n  {'>>> SALES TOTAL':<38} {'':10} {'':>6} ${sales_total:>10,}")

mktg_lt = print_dept("MARKETING (SG&A)", "Marketing")
mktg_total = mktg_lt
print(f"\n  {'>>> MARKETING TOTAL':<38} {'':10} {'':>6} ${mktg_total:>10,}")

ga_lt = print_dept("G&A (SG&A)", "G&A")
ga_nl = sum(a for _, a in nonlabor_items["G&A"])
print(f"\n  Non-Labor:")
for item, amt in nonlabor_items["G&A"]:
    print(f"    {item:<50} ${amt:>10,}")
print(f"  {'Non-Labor Subtotal':<38} {'':10} {'':>6} ${ga_nl:>10,}")
ga_total = ga_lt + ga_nl
print(f"\n  {'>>> G&A TOTAL':<38} {'':10} {'':>6} ${ga_total:>10,}")

nonop_lt = print_dept("NON-OPERATING", "Non-Op")
nonop_nl = sum(a for _, a in nonlabor_items["Non-Op"])
print(f"\n  Non-Labor:")
for item, amt in nonlabor_items["Non-Op"]:
    print(f"    {item:<50} ${amt:>10,}")
nonop_total = nonop_lt + nonop_nl
print(f"\n  {'>>> NON-OP TOTAL':<38} {'':10} {'':>6} ${nonop_total:>10,}")

# ============================================================
# P&L SUMMARY
# ============================================================
rev = {
    "MS": 1_799_686,
    "Comprehensive": 1_384_375,
    "Projects": 432_343,
    "Products-HW": 283_715,
    "Products-SW": 999_880,
    "Products-Cloud": 268_755,
}
total_rev = 5_168_754

cogs_detail = {
    "MS": ms_total,
    "Comprehensive": comp_total,
    "Projects": proj_total,
    "Products-HW": prod_hw,
    "Products-SW": prod_sw + prod_ot,
    "Products-Cloud": prod_cl,
}
total_cogs = sum(cogs_detail.values())
total_gp = total_rev - total_cogs

total_sga = sales_total + mktg_total + ga_total
op_income = total_gp - total_sga
net_income = op_income - nonop_total

print(f"\n\n{'='*120}")
print(f"  PULSEONE DEPARTMENTAL P&L — CY 2025 (v7.1 CORRECTED)")
print(f"{'='*120}")

print(f"\n  {'':40} {'Amount':>12} {'% Rev':>8} {'BiC Target':>12}")
print(f"  {'-'*78}")
print(f"  {'REVENUE':40}")
print(f"    {'Managed Services':38} ${rev['MS']:>10,} {rev['MS']/total_rev*100:>7.1f}%")
print(f"    {'Comprehensive Services':38} ${rev['Comprehensive']:>10,} {rev['Comprehensive']/total_rev*100:>7.1f}%")
print(f"    {'True Projects':38} ${rev['Projects']:>10,} {rev['Projects']/total_rev*100:>7.1f}%")
print(f"    {'Products - Hardware':38} ${rev['Products-HW']:>10,} {rev['Products-HW']/total_rev*100:>7.1f}%")
print(f"    {'Products - Software Licensing':38} ${rev['Products-SW']:>10,} {rev['Products-SW']/total_rev*100:>7.1f}%")
print(f"    {'Products - Hosting/Cloud':38} ${rev['Products-Cloud']:>10,} {rev['Products-Cloud']/total_rev*100:>7.1f}%")
print(f"  {'TOTAL REVENUE':40} ${total_rev:>10,} {'100.0%':>8}")

print(f"\n  {'COST OF GOODS SOLD':40}")
for seg_name, seg_key in [("MS COGS", "MS"), ("Comprehensive COGS", "Comprehensive"),
                           ("Projects COGS", "Projects"), ("Products-HW COGS", "Products-HW"),
                           ("Products-SW COGS", "Products-SW"), ("Products-Cloud COGS", "Products-Cloud")]:
    print(f"    {seg_name:<38} ${cogs_detail[seg_key]:>10,} {cogs_detail[seg_key]/total_rev*100:>7.1f}%")
print(f"  {'TOTAL COGS':40} ${total_cogs:>10,} {total_cogs/total_rev*100:>7.1f}%")

print(f"\n  {'GROSS PROFIT':40} ${total_gp:>10,} {total_gp/total_rev*100:>7.1f}% {'~50%':>12}")
print(f"  {'-'*78}")
gp_items = [
    ("MS GP", rev["MS"], cogs_detail["MS"], "48-52%"),
    ("Comprehensive GP", rev["Comprehensive"], cogs_detail["Comprehensive"], "~40%"),
    ("Projects GP", rev["Projects"], cogs_detail["Projects"], "~40%"),
    ("Products-HW GP", rev["Products-HW"], cogs_detail["Products-HW"], "24-26%"),
    ("Products-SW GP", rev["Products-SW"], cogs_detail["Products-SW"], "24-26%"),
    ("Products-Cloud GP", rev["Products-Cloud"], cogs_detail["Products-Cloud"], "24-26%"),
]
for name, r, c, bic in gp_items:
    gp_val = r - c
    gm = gp_val / r * 100 if r > 0 else 0
    print(f"    {name:<38} ${gp_val:>10,} {gm:>7.1f}% {bic:>12}")

print(f"\n  {'SG&A EXPENSES':40}")
print(f"    {'Sales':38} ${sales_total:>10,} {sales_total/total_rev*100:>7.1f}%")
print(f"    {'Marketing':38} ${mktg_total:>10,} {mktg_total/total_rev*100:>7.1f}%")
print(f"    {'G&A':38} ${ga_total:>10,} {ga_total/total_rev*100:>7.1f}%")
print(f"  {'TOTAL SG&A':40} ${total_sga:>10,} {total_sga/total_rev*100:>7.1f}% {'~30%':>12}")

print(f"\n  {'OPERATING INCOME':40} ${op_income:>10,} {op_income/total_rev*100:>7.1f}% {'12-18%':>12}")
print(f"  {'Non-Operating Expenses':40} $({nonop_total:>9,}) {nonop_total/total_rev*100:>7.1f}%")
print(f"  {'NET INCOME':40} ${net_income:>10,} {net_income/total_rev*100:>7.1f}%")

# ============================================================
# RECONCILIATION
# ============================================================
print(f"\n\n{'='*120}")
print(f"  RECONCILIATION TO QB")
print(f"{'='*120}")

total_identified_expenses = total_cogs + total_sga + nonop_total
qb_total_expenses = 4_950_980
unidentified = qb_total_expenses - total_identified_expenses

print(f"\n  {'Identified COGS':<40} ${total_cogs:>10,}")
print(f"  {'Identified SG&A':<40} ${total_sga:>10,}")
print(f"  {'Identified Non-Op':<40} ${nonop_total:>10,}")
print(f"  {'TOTAL IDENTIFIED':<40} ${total_identified_expenses:>10,}")
print(f"  {'QB Total Expenses':<40} ${qb_total_expenses:>10,}")
print(f"  {'UNIDENTIFIED GAP':<40} ${unidentified:>10,}")
print(f"")
print(f"  The ${unidentified:,} gap represents QB expense lines we haven't")
print(f"  individually sourced yet (rent, insurance, professional fees,")
print(f"  advertising, travel, office supplies, etc.).")
print(f"  These are real G&A costs that will be added when identified.")
print(f"")
print(f"  If allocated to G&A, adjusted totals would be:")
adj_ga = ga_total + unidentified
adj_sga = total_sga + unidentified
adj_op = total_gp - adj_sga
adj_net = adj_op - nonop_total
print(f"  {'G&A (adjusted)':<40} ${adj_ga:>10,} {adj_ga/total_rev*100:>7.1f}%")
print(f"  {'Total SG&A (adjusted)':<40} ${adj_sga:>10,} {adj_sga/total_rev*100:>7.1f}%")
print(f"  {'Operating Income (adjusted)':<40} ${adj_op:>10,} {adj_op/total_rev*100:>7.1f}%")
print(f"  {'Net Income (adjusted)':<40} ${adj_net:>10,} {adj_net/total_rev*100:>7.1f}%")
print(f"  {'QB Net Income':<40} ${217_774:>10,}")
print(f"  {'Remaining variance':<40} ${adj_net - 217_774:>10,}")

# ============================================================
# EXPENSE BY SOURCE SUMMARY
# ============================================================
print(f"\n\n{'='*120}")
print(f"  EXPENSE SUMMARY BY PAYMENT SOURCE")
print(f"{'='*120}")
by_method = {}
for p in people:
    m = p["method"]
    by_method[m] = by_method.get(m, 0) + p["total"]

print(f"\n  {'Source':<40} {'Amount':>12} {'People':>8}")
for method in ["W-2", "Partner", "Upwork", "BILL", "Payoneer", "Unknown"]:
    count = sum(1 for p in people if p["method"] == method)
    print(f"  {method:<40} ${by_method.get(method, 0):>10,} {count:>6}")
print(f"  {'Payroll Tax/Benefits':<40} ${ptax_total:>10,}")
all_nonlabor = sum(sum(a for _, a in items) for items in nonlabor_items.values())
print(f"  {'Non-Labor Items':<40} ${all_nonlabor:>10,}")
print(f"  {'-'*55}")
total_sourced = sum(by_method.values()) + ptax_total + all_nonlabor
print(f"  {'TOTAL SOURCED':<40} ${total_sourced:>10,}")
