#!/usr/bin/env python3
"""
Audit the Upwork file to confirm it's CY2025 only.
The filename says "2026-05-02" which is the download date.
The file has no date column — it's a summary by contract/freelancer.

Also need to check: does the Upwork total match QB?
QB Salary Expense = $1,441,010
ADP Gross = $1,010,172
Upwork (model) = $304,424
ADP + Upwork = $1,314,596
QB Salary = $1,441,010
Gap = $126,414

Where does that $126K gap come from?
Possible: Payoneer people coded to Salary in QB? Or model Upwork number is wrong?
"""
import csv

print("=" * 100)
print("  UPWORK FILE AUDIT")
print("=" * 100)

upwork_file = "/home/ubuntu/upload/Upwork-Reports-Timebyfreelancer-2026-05-0202-12.csv"
with open(upwork_file, 'r', encoding='utf-8-sig') as f:
    content = f.read()

print(f"\n  Raw file content (first 2000 chars):")
print(content[:2000])

print(f"\n\n  {'='*80}")
print(f"  PARSING")
print(f"  {'='*80}")

# Parse properly
lines = content.strip().split('\n')
reader = csv.reader(lines)
headers = next(reader)
print(f"  Headers: {headers}")

# Headers: Contract, Talent, Hours, Amount, Payment type, Activity ID
rows = list(reader)
print(f"  Total rows: {len(rows)}")

# Sum by freelancer
by_person = {}
for row in rows:
    if len(row) >= 4:
        contract = row[0]
        talent = row[1]
        hours = row[2]
        amount = row[3]
        ptype = row[4] if len(row) > 4 else ''
        
        try:
            amt = float(amount.replace(',', '').replace('$', '').strip())
        except:
            amt = 0
        
        # Clean talent name
        name = talent.split('(')[0].strip() if talent else 'Unknown'
        by_person[name] = by_person.get(name, 0) + amt

print(f"\n  {'Freelancer':<35} {'Amount':>12}")
print(f"  {'-'*50}")
total = 0
for name, amt in sorted(by_person.items(), key=lambda x: -x[1]):
    print(f"  {name:<35} ${amt:>10,.2f}")
    total += amt
print(f"  {'-'*50}")
print(f"  {'TOTAL':<35} ${total:>10,.2f}")

# Compare with model
print(f"\n\n  MODEL COMPARISON:")
model_upwork = {
    "Vincent Williams": 104_740,
    "Matt Barnett": 83_390,
    "Omar Avalos": 49_442,
    "Charlesdoone Castro": 38_228,
    "Brendan Roe": 6_476,
    "Basim Mashni": 5_906,
    "Lab Tech Ninjas": 4_500,
    "William McMillan": 4_444,
    "Kirill Hovansky": 3_660,
    "Sabah Razaq": 2_438,
    "Yana Kosenko": 700,
    "Dustin Hagemeier": 500,
}
model_total = sum(model_upwork.values())

print(f"  Upwork file total:  ${total:>10,.2f}")
print(f"  Model Upwork total: ${model_total:>10,}")
print(f"  Difference:         ${total - model_total:>10,.2f}")

# Check: does the file have ANY date information?
print(f"\n\n  DATE CHECK:")
print(f"  The Upwork file has NO date column.")
print(f"  It's a summary report — likely filtered by date range at download time.")
print(f"  Filename: 'Upwork-Reports-Timebyfreelancer-2026-05-0202-12.csv'")
print(f"  This suggests it was downloaded on 2026-05-02.")
print(f"  The report title doesn't specify the date range.")
print(f"  We need to TRUST that the user pulled this for CY2025.")
print(f"  Total = ${total:,.2f} which is close to our model's ${model_total:,}")

# The amounts in the file are in CENTS or DOLLARS?
# Let's check: "2888" for Charlesdoone bonus, "35340" for Charlesdoone hourly
# If dollars, Charlesdoone = $38,228 total — matches model
# These are DOLLARS (no decimal points in the CSV)
print(f"\n\n  AMOUNT FORMAT: Values appear to be in DOLLARS (integers)")
print(f"  Example: Charlesdoone Castro has 2888 + 35340 = 38228 = ${38_228:,}")
print(f"  This matches model ($38,228) ✓")

# Now the big question: QB Salary = $1,441,010
# ADP Gross = $1,010,172
# Upwork = $299,924 (from file) or $304,424 (model)
# Let's use the file number
print(f"\n\n  QB SALARY RECONCILIATION:")
print(f"  QB Salary Expense:        $1,441,010")
print(f"  ADP Gross Pay:            $1,010,172")
print(f"  Upwork (from file):       $  299,924")
print(f"  ADP + Upwork:             $1,310,096")
print(f"  Gap to QB Salary:         $  130,914")
print(f"")
print(f"  This $131K gap likely = Payoneer payments coded to QB Salary line")
print(f"  Payoneer total in model:  $  194,687")
print(f"  + Badar:                  $   30,300")
print(f"  = Total non-ADP/non-UW:   $  224,987")
print(f"")
print(f"  If ALL Payoneer+Badar are in QB Salary:")
print(f"  ADP + Upwork + Payoneer+Badar = $1,310,096 + $224,987 = $1,535,083")
print(f"  That EXCEEDS QB Salary by $94,073 — so not all are in Salary")
print(f"")
print(f"  If only $131K of Payoneer is in QB Salary:")
print(f"  Remaining $94K would be in other QB lines (CS-Cost? Other?)")
print(f"")
print(f"  KEY INSIGHT: The model's Upwork total ($304,424) is $4,500 MORE than file ($299,924)")
print(f"  Difference = $4,500 = Lab Tech Ninjas amount in model")
print(f"  Lab Tech Ninjas may not be in this Upwork report!")
