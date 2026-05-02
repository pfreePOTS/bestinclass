#!/usr/bin/env python3
"""
FULL RECONCILIATION: Where does the $200K variance come from?

FACTS ESTABLISHED:
1. ADP file covers 1/10/2025 - 12/26/2025 (full CY2025) ✓
2. ADP Total Gross = $1,010,172 (employee gross pay, NOT including employer taxes)
3. ADP Employer Liability = $84,343 (FICA, FUTA, SUI only)
4. Upwork file total = $299,924 (CY2025, trusted)
5. QB Salary Expense = $1,441,010
6. QB Payroll Tax = $296,256
7. QB Payroll Expense = $14,620
8. Model W-2 total = $1,103,125 (HIGHER than ADP by $92,953)
9. Model Payroll Tax = $310,876 (QB Payroll Tax + QB Payroll Exp)

KEY QUESTIONS:
A. Why is model W-2 ($1,103,125) higher than ADP gross ($1,010,172)?
   - Model has $92,953 more than ADP
   - Model numbers must have come from a DIFFERENT source than this ADP file
   
B. What does QB Payroll Tax ($296,256) actually include?
   - ADP Employer Liability = only $84,343 (FICA/FUTA/SUI)
   - QB is $212K higher — must include health insurance, 401k match, workers comp
   - These are REAL costs in QB, separate from gross pay
   - We should NOT add $310,876 on top of ADP gross — it's already in QB total expenses

C. Where are Payoneer payments in QB?
   - QB Salary ($1,441,010) = ADP ($1,010,172) + Upwork ($299,924) + ??? ($130,914)
   - The $131K gap could be Payoneer people coded to "Salary" in QB
   - Payoneer total = $194,687 + Badar $30,300 = $224,987
   - If $131K is in Salary, remaining $94K is in other QB lines
"""

print("=" * 120)
print("  VARIANCE ROOT CAUSE ANALYSIS")
print("=" * 120)

# What QB says (ground truth for TOTAL expenses)
qb_total_expenses = 4_950_980
qb_net_income = 217_774
qb_total_revenue = 5_168_754

# QB expense lines we know
qb_salary = 1_441_010
qb_payroll_tax = 296_256
qb_payroll_exp = 14_620
qb_partner_comp = 423_000
qb_cs_cost = 1_044_424
qb_computer_internet = 263_953
qb_named_total = qb_salary + qb_payroll_tax + qb_payroll_exp + qb_partner_comp + qb_cs_cost + qb_computer_internet
qb_other = qb_total_expenses - qb_named_total

print(f"\n  QB EXPENSE BREAKDOWN:")
print(f"  {'Salary Expense':<40} ${qb_salary:>10,}")
print(f"  {'Payroll Tax Expense':<40} ${qb_payroll_tax:>10,}")
print(f"  {'Payroll Expense':<40} ${qb_payroll_exp:>10,}")
print(f"  {'Partner Comp (Guar Payments)':<40} ${qb_partner_comp:>10,}")
print(f"  {'CS-Cost (Consulting Svcs Cost)':<40} ${qb_cs_cost:>10,}")
print(f"  {'Computer & Internet':<40} ${qb_computer_internet:>10,}")
print(f"  {'-'*55}")
print(f"  {'Named Lines Subtotal':<40} ${qb_named_total:>10,}")
print(f"  {'All Other QB Lines':<40} ${qb_other:>10,}")
print(f"  {'='*55}")
print(f"  {'QB TOTAL EXPENSES':<40} ${qb_total_expenses:>10,}")

# What our model currently has
print(f"\n\n  OUR MODEL (CURRENT — WRONG):")
model_w2 = 1_103_125
model_ptax = 310_876
model_partners = 423_000
model_upwork = 304_424  # slightly off from file
model_bill = 1_004_961
model_payoneer = 194_687
model_badar = 30_300
model_nonlabor = 1_779_491  # includes the $389K "Other OpEx"
model_total = model_w2 + model_ptax + model_partners + model_upwork + model_bill + model_payoneer + model_badar + model_nonlabor

print(f"  {'W-2 (from ???)':<40} ${model_w2:>10,}")
print(f"  {'Payroll Tax (from QB lines)':<40} ${model_ptax:>10,}")
print(f"  {'Partners':<40} ${model_partners:>10,}")
print(f"  {'Upwork':<40} ${model_upwork:>10,}")
print(f"  {'BILL (CS-Cost subs)':<40} ${model_bill:>10,}")
print(f"  {'Payoneer':<40} ${model_payoneer:>10,}")
print(f"  {'Badar':<40} ${model_badar:>10,}")
print(f"  {'Non-Labor (incl $389K Other OpEx)':<40} ${model_nonlabor:>10,}")
print(f"  {'-'*55}")
print(f"  {'MODEL TOTAL':<40} ${model_total:>10,}")
print(f"  {'QB TOTAL':<40} ${qb_total_expenses:>10,}")
print(f"  {'VARIANCE (model - QB)':<40} ${model_total - qb_total_expenses:>10,}")

# Now let's trace the CORRECT approach
print(f"\n\n  {'='*120}")
print(f"  CORRECT APPROACH: Build from QB lines, not from ADP+extras")
print(f"  {'='*120}")

print(f"""
  The CORRECT way to build the P&L is:
  
  QB tells us TOTAL expenses = $4,950,980. That's the constraint.
  
  We DON'T need to independently sum ADP + Upwork + Payoneer + taxes.
  QB already has all of that in its lines. Our job is to ALLOCATE those
  QB lines to departments, not to re-derive the totals.
  
  QB Salary ($1,441,010) ALREADY INCLUDES:
    - ADP gross pay ($1,010,172)
    - Upwork payments ($299,924)  
    - Some portion of Payoneer ($130,914 to balance)
    Total: $1,441,010 ✓
  
  QB Payroll Tax ($296,256) + Payroll Exp ($14,620) = $310,876
    This ALREADY INCLUDES all employer costs:
    - FICA employer match
    - FUTA
    - State unemployment
    - Health insurance premiums (employer portion)
    - 401k match
    - Workers comp
    We should NOT add this on top of ADP gross — it's a SEPARATE QB line.
  
  QB CS-Cost ($1,044,424) ALREADY INCLUDES:
    - All BILL contractor payments ($1,004,961 in our model)
    - Difference of $39,463 = other items in CS-Cost
  
  So the CORRECT model is:
""")

# Correct model
print(f"  CORRECT MODEL:")
print(f"  {'QB Salary (ADP+Upwork+Payoneer)':<45} ${qb_salary:>10,}")
print(f"  {'QB Payroll Tax + Payroll Exp':<45} ${qb_payroll_tax + qb_payroll_exp:>10,}")
print(f"  {'QB Partner Comp':<45} ${qb_partner_comp:>10,}")
print(f"  {'QB CS-Cost':<45} ${qb_cs_cost:>10,}")
print(f"  {'QB Computer & Internet':<45} ${qb_computer_internet:>10,}")
print(f"  {'QB All Other Lines':<45} ${qb_other:>10,}")
print(f"  {'-'*60}")
correct_total = qb_salary + qb_payroll_tax + qb_payroll_exp + qb_partner_comp + qb_cs_cost + qb_computer_internet + qb_other
print(f"  {'TOTAL (= QB Total)':<45} ${correct_total:>10,}")

# Now identify the DOUBLE COUNTS in our current model
print(f"\n\n  {'='*120}")
print(f"  DOUBLE-COUNT IDENTIFICATION")
print(f"  {'='*120}")

print(f"""
  PROBLEM 1: Payoneer people ($194,687 + Badar $30,300 = $224,987)
  ----------------------------------------------------------------
  These people are ALREADY inside QB Salary ($1,441,010).
  QB Salary = ADP ($1,010,172) + Upwork ($299,924) + Payoneer/Other ($130,914)
  
  Wait — that only accounts for $131K of the $225K Payoneer+Badar.
  The remaining $94K must be in OTHER QB lines (maybe CS-Cost or Other).
  
  Regardless: by listing Payoneer people AS SEPARATE LINE ITEMS and ALSO
  having the "Other OpEx" remainder that was computed from QB totals,
  we're double-counting the Payoneer amounts.
  
  PROBLEM 2: "Other OpEx" ($389,129) 
  -----------------------------------
  This was computed as:
    QB Total ($4,950,980) - Salary ($1,441,010) - Payroll Tax ($296,256) 
    - Payroll Exp ($14,620) - Partner Comp ($423,000) - C&I ($263,953) = $2,512,141
  
  Wait, that doesn't equal $389K. Let me recalculate...
  Actually it was: QB Total Expenses ($2,827,968??) — that number is wrong.
  
  Let me trace where $389,129 came from:
""")

# The $389K was computed in an earlier session. Let me reverse-engineer it.
# From the context: QB Total Expenses ($2,827,968) - Salary ($1,441,010) - Payroll Tax ($296,256) 
# - Payroll Exp ($14,620) - Partner Comp ($423,000) - Computer & Internet ($263,953) = $389,129
# But QB Total Expenses is $4,950,980, not $2,827,968.
# $2,827,968 must be QB Total Expenses MINUS CS-Cost ($1,044,424) MINUS something else

# Let's check: 1,441,010 + 296,256 + 14,620 + 423,000 + 263,953 + 389,129 = ?
check = 1_441_010 + 296_256 + 14_620 + 423_000 + 263_953 + 389_129
print(f"  Sum of named lines + Other OpEx = ${check:,}")
print(f"  This equals $2,827,968")
print(f"  QB Total Expenses = $4,950,980")
print(f"  Difference = ${4_950_980 - check:,} = CS-Cost ($1,044,424) + Products COGS + other")
print(f"  So $2,827,968 was the 'operating expenses excluding CS-Cost and Products COGS'")

# The real issue: 
remaining_after_named = 4_950_980 - (1_441_010 + 296_256 + 14_620 + 423_000 + 1_044_424 + 263_953)
print(f"\n  QB Total - all named lines = ${remaining_after_named:,}")
print(f"  This ${remaining_after_named:,} = Products COGS + all other operating expenses")

# Products COGS in our model
products_cogs = 135_697 + 713_110 + 131_775 + 10_468  # HW + SW + Cloud + Merchant
print(f"  Products COGS in model = ${products_cogs:,}")
print(f"  Remaining after Products = ${remaining_after_named - products_cogs:,}")
print(f"  This should be the 'Other OpEx' = rent, insurance, prof fees, etc.")
true_other = remaining_after_named - products_cogs
print(f"  TRUE Other OpEx = ${true_other:,}")

# Now let's see what the model has vs what it should have
print(f"\n\n  {'='*120}")
print(f"  THE ACTUAL DOUBLE-COUNT")
print(f"  {'='*120}")

print(f"""
  Our model SEPARATELY lists:
    - ADP W-2 people:     ${model_w2:>10,}  (should be from ADP gross = $1,010,172)
    - Payroll Tax:        ${model_ptax:>10,}  (from QB lines, correct)
    - Upwork people:      ${model_upwork:>10,}  (from Upwork file, correct)
    - Payoneer people:    ${model_payoneer:>10,}  (ALREADY IN QB Salary!)
    - Badar:              ${model_badar:>10,}  (ALREADY IN QB Salary or other line!)
    - Other OpEx:         $   389,129  (remainder from QB — INCLUDES Payoneer!)
    
  The double-count is:
    Payoneer ($194,687) + Badar ($30,300) = $224,987
    MINUS the portion NOT in QB Salary gap ($224,987 - $130,914) = $94,073
    
  Actually, let me think about this differently.
  
  The "Other OpEx" ($389,129) was computed as a REMAINDER of QB lines.
  It represents QB expense lines we haven't individually named.
  
  If Payoneer payments are coded to QB "Salary" line:
    - They're INSIDE the $1,441,010 QB Salary
    - They're NOT inside the $389,129 Other OpEx remainder
    - Listing them separately = double-count vs QB Salary
    
  Our model uses $1,103,125 for W-2 (not $1,010,172 from ADP).
  Where did $1,103,125 come from?
""")

# Let's check: $1,103,125 - $1,010,172 = $92,953
# Is this the Payoneer amount that's in QB Salary?
diff_w2 = model_w2 - 1_010_172
print(f"  Model W-2 ({model_w2:,}) - ADP Gross ({1_010_172:,}) = ${diff_w2:,}")
print(f"  Payoneer+Badar = ${model_payoneer + model_badar:,}")
print(f"  QB Salary gap (after ADP+Upwork) = $130,914")
print(f"")
print(f"  HYPOTHESIS: The model's W-2 numbers were inflated by including")
print(f"  some non-ADP payments (Payoneer?) in the 'W-2' bucket.")
print(f"  Then Payoneer was ALSO listed separately = double count of ~$93K")

# Final variance decomposition
print(f"\n\n  {'='*120}")
print(f"  VARIANCE DECOMPOSITION: Model ($5,150,864) vs QB ($4,950,980) = $199,884")
print(f"  {'='*120}")

print(f"""
  The $200K variance has TWO components:

  1. MODEL W-2 IS INFLATED: ${model_w2:,} vs ADP actual ${1_010_172:,}
     Excess: ${model_w2 - 1_010_172:,}
     
  2. PAYONEER LISTED SEPARATELY when already in QB Salary:
     Payoneer + Badar: ${model_payoneer + model_badar:,}
     
  3. BUT: "Other OpEx" ($389,129) was derived AFTER subtracting QB Salary.
     So Payoneer is NOT in Other OpEx — it's in QB Salary.
     
  Net double-count:
    If we use ADP actual ($1,010,172) instead of model W-2 ($1,103,125):
      Savings: ${model_w2 - 1_010_172:,}
      
    If we recognize that Payoneer IS inside QB Salary and remove separate listing:
      But then QB Salary ($1,441,010) = ADP ($1,010,172) + Upwork ($299,924) + Payoneer ($130,914)
      That only accounts for $131K of Payoneer — not all $225K.
      
    The remaining $94K of Payoneer+Badar must be in CS-Cost or Other QB lines.
    Our CS-Cost model ($1,004,961) vs QB CS-Cost ($1,044,424) — gap of $39,463.
    So maybe $39K of Payoneer/Badar is in CS-Cost, and $55K in other lines.
    
  CORRECT FIX:
  =============
  Option A (cleanest): Use QB line totals directly, allocate to departments.
    - QB Salary ($1,441,010) = all people costs (ADP + Upwork + Payoneer + Badar)
    - Don't separately list Payoneer — they're INSIDE QB Salary
    - Don't use model W-2 numbers — use ADP actuals
    - Payroll Tax ($310,876) stays as-is — it's a separate QB line
    - Other OpEx = QB remainder after all named lines = ${true_other:,}
    
  Option B (bottom-up, what we've been trying):
    - Use ADP gross ($1,010,172) for W-2 people
    - Use Upwork file ($299,924) for Upwork people  
    - Use Payoneer actuals ($194,687) for Payoneer people
    - Use Badar ($30,300)
    - Total people costs = ${1_010_172 + 299_924 + 194_687 + 30_300:,}
    - Compare to QB Salary: ${qb_salary:,}
    - Difference: ${qb_salary - (1_010_172 + 299_924 + 194_687 + 30_300):,}
    - This negative means our bottom-up EXCEEDS QB Salary by $94K!
    - Those $94K must be in OTHER QB lines, not Salary.
    
  The REAL fix for the $200K variance:
    - Use ADP actual gross ($1,010,172) not inflated model ($1,103,125): saves $93K
    - Remove "Other OpEx" double-count of Payoneer:
      Current Other OpEx: $389,129
      This was computed as QB remainder AFTER subtracting Salary line.
      Payoneer is IN Salary, so it's NOT in Other OpEx.
      But our model lists Payoneer SEPARATELY ($225K) AND has Other OpEx ($389K).
      If the model's W-2 number ($1,103,125) already includes some Payoneer,
      then the double-count is: $1,103,125 - $1,010,172 = $93K (Payoneer in W-2)
      PLUS the separate Payoneer listing ($225K) that's already in QB Salary.
      
  Wait — let me just add it up the RIGHT way:
""")

# THE CORRECT BOTTOM-UP BUILD
print(f"\n  CORRECT BOTTOM-UP BUILD:")
correct_adp = 1_010_172
correct_upwork = 299_924
correct_payoneer = 194_687
correct_badar = 30_300
correct_people = correct_adp + correct_upwork + correct_payoneer + correct_badar
print(f"  ADP Gross:          ${correct_adp:>10,}")
print(f"  Upwork:             ${correct_upwork:>10,}")
print(f"  Payoneer:           ${correct_payoneer:>10,}")
print(f"  Badar:              ${correct_badar:>10,}")
print(f"  = Total People:     ${correct_people:>10,}")
print(f"  QB Salary:          ${qb_salary:>10,}")
print(f"  Excess over QB:     ${correct_people - qb_salary:>10,}  (people costs in OTHER QB lines)")
print(f"")
print(f"  + Partners:         ${qb_partner_comp:>10,}")
print(f"  + Payroll Tax/Ben:  ${qb_payroll_tax + qb_payroll_exp:>10,}")
print(f"  + CS-Cost (BILL):   ${qb_cs_cost:>10,}")
print(f"  + Computer & Int:   ${qb_computer_internet:>10,}")
print(f"  + Products COGS:    ${products_cogs:>10,}")
print(f"  + True Other OpEx:  ${true_other:>10,}")
print(f"  {'-'*35}")
total_correct = correct_people + qb_partner_comp + (qb_payroll_tax + qb_payroll_exp) + qb_cs_cost + qb_computer_internet + products_cogs + true_other
print(f"  TOTAL:              ${total_correct:>10,}")
print(f"  QB Total:           ${qb_total_expenses:>10,}")
print(f"  Variance:           ${total_correct - qb_total_expenses:>10,}")

print(f"""

  *** THE VARIANCE IS ${total_correct - qb_total_expenses:,} ***
  
  This is because our bottom-up people costs ($1,535,083) EXCEED QB Salary ($1,441,010)
  by $94,073. Those extra costs are ALREADY counted in CS-Cost or Other QB lines.
  
  SOLUTION: We must choose ONE approach:
  
  APPROACH 1 (QB-constrained):
    - Total people in "Salary" bucket = $1,441,010 (QB number)
    - Allocate that $1,441,010 to departments using the PROPORTIONS from ADP/Upwork/Payoneer
    - Payroll Tax = $310,876 (QB number), allocated proportionally
    - CS-Cost = $1,044,424 (QB number), allocated per BILL data
    - Everything else from QB lines
    - GUARANTEED to tie to $4,950,980
    
  APPROACH 2 (Bottom-up, QB as check):
    - Use actual amounts per person from ADP/Upwork/Payoneer
    - Accept that some Payoneer people may be coded to CS-Cost in QB
    - Reduce CS-Cost by the Payoneer amounts that are in it
    - Reduce "Other OpEx" by any Payoneer amounts in it
    - Must still tie to $4,950,980 total
""")
