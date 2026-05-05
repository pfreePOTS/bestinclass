#!/usr/bin/env python3
"""
Itemize the $286,697 G&A Operating Expenses from QB P&L detail.

Logic:
- QB Total Expenses = $2,827,968 (operating expense section only, excl COGS)
- QB Total COGS = $2,123,012
- QB Grand Total = $4,950,980

Our model accounts for these QB expense lines:
- Salary Expense: $1,441,010 (W-2 + Payoneer coded into salary)
- Payroll Taxes: $296,256 (part of our $310,876 payroll tax/benefits)
- Payroll Expenses: $14,620 (remainder of our $310,876 payroll tax/benefits)
- Partner Compensation: $423,000
- Computer & Internet: $263,953 (split into COGS tools + G&A tools in our model)
- RepScheduler Expenses: $39,560 (Non-Op)

That accounts for: $1,441,010 + $296,256 + $14,620 + $423,000 + $263,953 + $39,560 = $2,478,399
QB Total Expense section = $2,827,968
Difference = $2,827,968 - $2,478,399 = $349,569

Wait — but our model's G&A unitemized = $286,697. Let me reconcile differently.

Our model:
- Total Identified = $4,664,283
- QB Total = $4,950,980
- Gap = $286,697

The gap represents ALL QB expense lines NOT individually sourced in our model.
From the QB data, the expense lines NOT in our model are:
"""

# QB Expense lines from the P&L file
qb_expense_lines = {
    "Advertising and Promotion": 51_969.60,
    "Automobile Expense": 1_075.45,
    "Bank Service Charges": 8_351.78,
    "Business Gifts": 25.00,
    "Business Licenses and Permits": 1_751.45,
    "Charitable Contributions": 112.62,
    "Computer and Internet Expenses": 263_953.24,
    "Consulting Fees": -738.14,
    "Dues and Subscriptions": 674.08,
    "Insurance Expense": 129_248.05,
    "Interest Expense": 11_410.41,
    "Janitorial Expense": 1_947.00,
    "Meals and Entertainment": 1_541.61,
    "Office Supplies": 10_619.50,
    "Partner Compensation": 423_000.00,
    "Payroll Expenses": 14_620.01,
    "Payroll Taxes": 296_256.31,
    "Professional Fees": 14_685.83,
    "Reconciliation Discrepancies": 9.43,
    "Rent Expense": 39_640.45,
    "Repairs and Maintenance": 205.00,
    "RepScheduler Expenses": 39_560.33,
    "Salary Expense": 1_441_009.99,
    "Sales Tax": 717.68,
    "Shipping": 5_770.56,
    "Tax - California": 17_810.53,
    "Telephone Expense": 20_198.72,
    "Training and Development": 23_516.64,
    "Travel Expense": 531.30,
    "Utilities": 8_493.06,
}

# Lines already accounted for in our model
already_modeled = {
    "Salary Expense": 1_441_009.99,       # W-2 + Payoneer in salary
    "Payroll Taxes": 296_256.31,          # Part of $310,876 payroll tax/benefits
    "Payroll Expenses": 14_620.01,        # Part of $310,876 payroll tax/benefits
    "Partner Compensation": 423_000.00,   # Partners
    "Computer and Internet Expenses": 263_953.24,  # Split into COGS tools + G&A tools
    "RepScheduler Expenses": 39_560.33,   # Non-Op
}

# QB COGS lines (already in our model as product/service COGS)
qb_cogs_lines = {
    "Agreement License Cost": 366_527.17,
    "Consulting Services - Cost": 1_044_423.75,
    "Installation Services - Cost": 3_170.00,
    "Merchant Account Fees": 10_467.80,
    "Purchases - Hardware for Resale": 135_697.45,
    "Purchases - Software for Resale": 562_725.72,
}

# Calculate unitemized G&A
unitemized_lines = {}
for name, amt in qb_expense_lines.items():
    if name not in already_modeled:
        unitemized_lines[name] = amt

total_unitemized = sum(unitemized_lines.values())

# Also verify the QB total
qb_total_expenses = sum(qb_expense_lines.values()) + sum(qb_cogs_lines.values())

print("=" * 80)
print("  RECONCILIATION: QB TOTAL EXPENSES")
print("=" * 80)
print(f"\n  QB COGS Section Total:          ${sum(qb_cogs_lines.values()):>12,.2f}")
print(f"  QB Expense Section Total:       ${sum(qb_expense_lines.values()):>12,.2f}")
print(f"  QB Grand Total:                 ${qb_total_expenses:>12,.2f}")
print(f"  Expected (from model):          $4,950,980.00")
print(f"  Variance:                       ${qb_total_expenses - 4_950_980:>12,.2f}")

print(f"\n\n{'='*80}")
print("  G&A OPERATING EXPENSES — FULLY ITEMIZED")
print("=" * 80)
print(f"\n  These are the QB expense lines NOT individually modeled in build_pl_v7_corrected.py.")
print(f"  They represent the $286,697 'G&A Operating Expenses (unitemized)' line.\n")
print(f"  {'Expense Line':<40} {'Amount':>12} {'% of Rev':>10}")
print(f"  {'-'*65}")

for name, amt in sorted(unitemized_lines.items(), key=lambda x: -abs(x[1])):
    pct = amt / 5_168_754 * 100
    print(f"  {name:<40} ${amt:>10,.2f} {pct:>9.2f}%")

print(f"  {'-'*65}")
print(f"  {'TOTAL UNITEMIZED G&A':<40} ${total_unitemized:>10,.2f} {total_unitemized/5_168_754*100:>9.2f}%")
print(f"\n  Model G&A unitemized target:     ${286_697:>10,.2f}")
print(f"  Variance:                        ${total_unitemized - 286_697:>10,.2f}")

# Categorize for BiC analysis
print(f"\n\n{'='*80}")
print("  G&A CATEGORIZATION FOR BIC ANALYSIS")
print("=" * 80)

categories = {
    "Facilities": ["Rent Expense", "Janitorial Expense", "Utilities", "Repairs and Maintenance"],
    "Insurance & Taxes": ["Insurance Expense", "Tax - California", "Interest Expense", "Sales Tax"],
    "Marketing/Advertising": ["Advertising and Promotion"],
    "Professional Development": ["Training and Development"],
    "Professional Services": ["Professional Fees", "Consulting Fees"],
    "Office & Admin": ["Office Supplies", "Telephone Expense", "Shipping", "Bank Service Charges",
                       "Automobile Expense", "Business Licenses and Permits", "Business Gifts",
                       "Charitable Contributions", "Meals and Entertainment", "Travel Expense",
                       "Dues and Subscriptions", "Reconciliation Discrepancies"],
}

for cat, lines in categories.items():
    cat_total = sum(unitemized_lines.get(l, 0) for l in lines)
    print(f"\n  {cat}: ${cat_total:,.2f} ({cat_total/5_168_754*100:.2f}% of revenue)")
    for l in lines:
        if l in unitemized_lines:
            print(f"    {l:<38} ${unitemized_lines[l]:>10,.2f}")

# Note about Advertising
print(f"\n\n{'='*80}")
print("  IMPORTANT NOTE: ADVERTISING & PROMOTION ($51,970)")
print("=" * 80)
print("""
  The $51,970 in Advertising and Promotion is currently sitting in the
  $286,697 G&A bucket. However, this should arguably be classified as
  Marketing SG&A, not G&A. If reclassified:
  
  - Marketing would increase from $199,976 (3.9%) to $251,946 (4.9%)
  - G&A unitemized would decrease from $286,697 to $234,727
  
  This is a classification decision, not a model error. The total SG&A
  remains the same either way.
""")
