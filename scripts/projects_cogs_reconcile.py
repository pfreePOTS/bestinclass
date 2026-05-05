#!/usr/bin/env python3
"""
Reconcile the two different views of Projects COGS:
1. P&L Model (build_pl_v7_corrected.py): $452,365
2. Four Questions Analysis: $714,499 ($365,526 OOP + $348,973 labor)

These should be measuring the same thing but aren't. Why?
"""

print("=" * 80)
print("  PROJECTS COGS RECONCILIATION: MODEL vs FOUR QUESTIONS")
print("=" * 80)

# Model COGS breakdown (from build_pl_v7_corrected.py output):
model_cogs = {
    "Kaitlin Harris (90%)": 79_760 * 0.90,       # $71,784
    "Laura Walsh (35%)": 108_186 * 0.35,          # $37,865
    "James Froio (30%)": 112_788 * 0.30,          # $33,836
    "Stephen Calkins (15%)": 148_960 * 0.15,      # $22,344
    "Hagen McDonell (20%)": 51_611 * 0.20,        # $10,322
    "Vincent Williams (80%)": 104_740 * 0.80,     # $83,792
    "Matt Barnett (25%)": 83_390 * 0.25,          # $20,848
    "Brendan Roe (Upwork)": 6_476,                # $6,476
    "William McMillan (Upwork)": 4_444,           # $4,444
    "Roe Tech (BILL 90%)": 100_097 * 0.90,        # $90,087
    "Other Project Subs (BILL)": 13_187,          # $13,187
}

# Payroll tax allocated to Projects W-2
w2_in_projects = (79_760*0.90 + 108_186*0.35 + 112_788*0.30 + 148_960*0.15 + 51_611*0.20)
total_w2 = 1_010_174
ptax_total = 310_876
ptax_projects = round(ptax_total * w2_in_projects / total_w2)

# Non-labor
nonlabor = 3_170  # Installation Services

print(f"\n  MODEL COGS (from build_pl_v7_corrected.py):")
print(f"  {'-'*60}")
print(f"  W-2 Labor (allocated):")
for name, amt in model_cogs.items():
    if "Harris" in name or "Walsh" in name or "Froio" in name or "Calkins" in name or "McDonell" in name:
        print(f"    {name:<35} ${round(amt):>10,}")

w2_subtotal = sum(round(v) for k, v in model_cogs.items() 
                  if any(x in k for x in ["Harris", "Walsh", "Froio", "Calkins", "McDonell"]))
print(f"    {'W-2 Subtotal':<35} ${w2_subtotal:>10,}")

print(f"\n  Upwork/Contractors:")
for name, amt in model_cogs.items():
    if "Vincent" in name or "Matt" in name or "Brendan" in name or "William" in name:
        print(f"    {name:<35} ${round(amt):>10,}")

upwork_subtotal = sum(round(v) for k, v in model_cogs.items()
                      if any(x in k for x in ["Vincent", "Matt", "Brendan", "William"]))
print(f"    {'Upwork Subtotal':<35} ${upwork_subtotal:>10,}")

print(f"\n  BILL Contractors:")
for name, amt in model_cogs.items():
    if "Roe" in name or "Other" in name:
        print(f"    {name:<35} ${round(amt):>10,}")

bill_subtotal = sum(round(v) for k, v in model_cogs.items()
                    if any(x in k for x in ["Roe", "Other"]))
print(f"    {'BILL Subtotal':<35} ${bill_subtotal:>10,}")

print(f"\n  Payroll Tax/Benefits (W-2 portion): ${ptax_projects:>10,}")
print(f"  Installation Services:              ${nonlabor:>10,}")

total_model = w2_subtotal + upwork_subtotal + bill_subtotal + ptax_projects + nonlabor
print(f"\n  {'TOTAL MODEL COGS':<35} ${total_model:>10,}")

# Four Questions COGS breakdown:
print(f"\n\n  FOUR QUESTIONS COGS:")
print(f"  {'-'*60}")
print(f"  QuickBase OOP (subcontractor invoices): $365,526")
print(f"  W-2 Invisible Subsidy:                  $244,333")
print(f"  Upwork Invisible Subsidy:               $104,640")
print(f"  TOTAL:                                  $714,499")

# Now reconcile
print(f"\n\n  RECONCILIATION:")
print(f"  {'-'*60}")
print(f"  The two approaches measure OVERLAPPING but DIFFERENT cost pools:")
print(f"")
print(f"  Model approach: Allocates each person's ANNUAL cost by percentage")
print(f"    - W-2 labor: ${w2_subtotal:,} (annual salary * project %)")
print(f"    - Upwork: ${upwork_subtotal:,} (annual Upwork * project %)")
print(f"    - BILL: ${bill_subtotal:,} (annual BILL * project %)")
print(f"    - Payroll tax: ${ptax_projects:,}")
print(f"    - Non-labor: ${nonlabor:,}")
print(f"    - TOTAL: ${total_model:,}")
print(f"")
print(f"  Four Questions approach: Uses QuickBase project-level data")
print(f"    - OOP COGS from QuickBase: $365,526 (actual invoices per project)")
print(f"    - THEN adds estimated internal labor ON TOP")
print(f"    - W-2 subsidy: $244,333")
print(f"    - Upwork subsidy: $104,640")
print(f"    - TOTAL: $714,499")
print(f"")
print(f"  KEY DIFFERENCE: The QuickBase OOP ($365,526) includes:")
print(f"    - Roe Tech: ~$90K (also in our model as BILL)")
print(f"    - Other Project Subs: ~$13K (also in our model as BILL)")
print(f"    - PLUS additional subcontractor costs that may be in")
print(f"      'Consulting Services-Cost' but allocated to Comprehensive")
print(f"      in our model (e.g., Blue Pisces Bunzl project work)")
print(f"")
print(f"  The $262K gap ($714K - $452K) is explained by:")
print(f"    1. QuickBase OOP includes costs our model puts in Comprehensive")
print(f"       (Blue Pisces Bunzl = $229K, but that's staffing not projects)")
print(f"    2. The Four Questions doc uses $690K revenue (QuickBase)")
print(f"       while our model uses $432K revenue (QB P&L)")
print(f"    3. The QuickBase 'true projects' definition may include")
print(f"       Bunzl work that our model classifies as Comprehensive")
print(f"")
print(f"  BOTTOM LINE:")
print(f"  Both approaches agree: Projects are unprofitable when fully loaded.")
print(f"  - Model: -4.6% GM on $432K revenue")
print(f"  - Four Questions: -3.4% GM on $691K revenue")
print(f"  The difference is scope (what counts as 'project' revenue/cost),")
print(f"  not a fundamental disagreement about profitability.")

# Revenue investigation
print(f"\n\n{'='*80}")
print(f"  REVENUE DISCREPANCY: $432K vs $691K")
print(f"{'='*80}")
print(f"""
  The $258K revenue gap between QB P&L ($432K) and QuickBase ($691K) is
  the MOST IMPORTANT unresolved issue for the Projects segment.
  
  If the model is UNDERSTATING project revenue by $258K, then:
  - The segment may actually be at ~34.5% GM (using model COGS of $452K)
  - OR the model is also understating COGS (missing some contractor costs)
  
  Most likely explanation:
  The QB P&L revenue line 'Consulting Income' ($1,804,393) is split:
  - Comprehensive: $1,384,375 (ARC + Bunzl staffing)
  - Projects: $420,018 (remainder)
  
  But QuickBase shows $690,839 in 'true project' revenue because:
  - Some Bunzl project revenue is coded to 'IT Managed Services' in QB
  - Some project-related hardware/software is in Sales-HW/Sales-SW
  - The Consulting Income split may be wrong
  
  THIS NEEDS CONNECTWISE VALIDATION:
  Pull CW invoices tagged to project boards for CY2025 to determine
  the true project revenue figure.
""")
