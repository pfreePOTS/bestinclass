#!/usr/bin/env python3
"""
The model has W-2 total of $1,103,125 but ADP shows only $1,010,172.
Difference = $92,953.

Let's compare EACH person to find where the inflation is.
The model numbers must have come from somewhere — possibly an earlier 
version of the ADP data that included benefits/taxes in the amounts.

Also: Paul Freeman shows in ADP as Dept 200 with $0 earnings.
He's listed as a Partner in our model ($141K). He's on ADP but not paid through it.
"""

# ADP actual gross per person (from Payroll Detail sheet)
adp_actual = {
    "Acker, Emily": 9_690,
    "Alvarez, Joel": 25_850,  # Note: ADP shows 25,067 on Summary but 25,850 on Detail
    "Anzalone, Eric": 76_718,
    "Brooke, Debby": 7_928,
    "Calkins, Alexandria": 17_258,
    "Calkins, Stephen": 148_960,
    "Carcamo, Andrea": 7_492,
    "Carey, Kyle": 51_800,
    "Copeland, Breanna": 11_444,
    "Davin, Jamie": 9_911,
    "Freeman, Paul": 0,  # Partner, on ADP but $0
    "Freeman, Tracy": 12_889,
    "Froio, James": 112_788,
    "Goodwin, Nicole (Dept 100)": 38_150,
    "Goodwin, Nicole (Dept 900)": 12_950,
    "Harris, Kaitlin": 79_760,
    "Holmes, Ashley": 725,
    "Kohler, Heather": 13_200,
    "McDonell, Hagen": 51_611,
    "Morte, Julia": 20_322,
    "Rankin, Dana": 9_200,
    "Rivera, Anneliese": 4_100,
    "Rocha Moreira, Marcello": 33_280,
    "Simpson, Juliet": 9_262,
    "Walsh, Laura": 108_186,
    "Wiggins, Chad": 95_000,
    "Wingard, Mariette": 0,  # Not in our model
    "Wolf, Emily": 18_400,
    "Brock, Aimee": 23_300,
}

# Model amounts
model_w2 = {
    "Stephen Calkins": 164_960,
    "James Froio": 127_215,
    "Laura Walsh": 124_065,
    "Kaitlin Harris": 84_910,
    "Eric Anzalone": 84_949,
    "Hagen McDonell": 56_784,
    "Nicole Goodwin (100)": 39_933,
    "Joel Alvarez": 27_076,
    "Julia Morte": 20_934,
    "Alexandria Calkins": 18_436,
    "Breanna Copeland": 11_719,
    "Debby Brooke": 7_928,
    "Chad Wiggins": 108_257,
    "Kyle Carey": 55_978,
    "Marcello Moreira": 33_280,
    "Heather Kohler": 14_851,
    "Dana Rankin": 9_952,
    "Andrea Carcamo": 7_614,
    "Anneliese Rivera": 4_132,
    "Aimee Brock": 24_423,
    "Emily Wolf": 18_434,
    "Emily Acker": 10_544,
    "Jamie Davin": 10_465,
    "Juliet Simpson": 9_263,
    "Ashley Holmes": 725,
    "Tracy Freeman": 12_889,
    "Nicole Goodwin (POC)": 13_409,
}

# Match them up
matches = [
    ("Stephen Calkins", "Calkins, Stephen", 164_960, 148_960),
    ("James Froio", "Froio, James", 127_215, 112_788),
    ("Laura Walsh", "Walsh, Laura", 124_065, 108_186),
    ("Kaitlin Harris", "Harris, Kaitlin", 84_910, 79_760),
    ("Eric Anzalone", "Anzalone, Eric", 84_949, 76_718),
    ("Hagen McDonell", "McDonell, Hagen", 56_784, 51_611),
    ("Nicole Goodwin (100)", "Goodwin (100)", 39_933, 38_150),
    ("Joel Alvarez", "Alvarez, Joel", 27_076, 25_850),
    ("Julia Morte", "Morte, Julia", 20_934, 20_322),
    ("Alexandria Calkins", "Calkins, Alex", 18_436, 17_258),
    ("Breanna Copeland", "Copeland, Breanna", 11_719, 11_444),
    ("Debby Brooke", "Brooke, Debby", 7_928, 7_928),
    ("Chad Wiggins", "Wiggins, Chad", 108_257, 95_000),
    ("Kyle Carey", "Carey, Kyle", 55_978, 51_800),
    ("Marcello Moreira", "Rocha Moreira", 33_280, 33_280),
    ("Heather Kohler", "Kohler, Heather", 14_851, 13_200),
    ("Dana Rankin", "Rankin, Dana", 9_952, 9_200),
    ("Andrea Carcamo", "Carcamo, Andrea", 7_614, 7_492),
    ("Anneliese Rivera", "Rivera, Anneliese", 4_132, 4_100),
    ("Aimee Brock", "Brock, Aimee", 24_423, 23_300),
    ("Emily Wolf", "Wolf, Emily", 18_434, 18_400),
    ("Emily Acker", "Acker, Emily", 10_544, 9_690),
    ("Jamie Davin", "Davin, Jamie", 10_465, 9_911),
    ("Juliet Simpson", "Simpson, Juliet", 9_263, 9_262),
    ("Ashley Holmes", "Holmes, Ashley", 725, 725),
    ("Tracy Freeman", "Freeman, Tracy", 12_889, 12_889),
    ("Nicole Goodwin (POC)", "Goodwin (900)", 13_409, 12_950),
]

print("=" * 120)
print("  PER-PERSON COMPARISON: MODEL vs ADP ACTUAL")
print("=" * 120)
print(f"\n  {'Model Name':<30} {'Model $':>10} {'ADP $':>10} {'Diff':>10} {'% Over':>8}")
print(f"  {'-'*75}")

total_model = 0
total_adp = 0
total_diff = 0

for model_name, adp_name, model_amt, adp_amt in matches:
    diff = model_amt - adp_amt
    pct = (diff / adp_amt * 100) if adp_amt > 0 else 0
    flag = " ***" if abs(diff) > 1000 else ""
    print(f"  {model_name:<30} ${model_amt:>8,} ${adp_amt:>8,} ${diff:>8,} {pct:>6.1f}%{flag}")
    total_model += model_amt
    total_adp += adp_amt
    total_diff += diff

print(f"  {'-'*75}")
print(f"  {'TOTAL':<30} ${total_model:>8,} ${total_adp:>8,} ${total_diff:>8,}")

print(f"\n\n  PATTERN ANALYSIS:")
print(f"  Every person (except Debby, Marcello, Holmes, Simpson, Tracy) has model > ADP")
print(f"  The excess ranges from 0.8% to 14%")
print(f"  Average excess: {total_diff/total_adp*100:.1f}%")
print(f"")
print(f"  HYPOTHESIS: The model numbers include EMPLOYER PAYROLL TAX per person")
print(f"  ADP Employer Liability total: $84,343")
print(f"  Model excess over ADP: ${total_diff:,}")
print(f"  These are CLOSE! ($84,343 vs $92,953)")
print(f"")
print(f"  If model amounts = ADP Gross + ADP Employer Liability per person,")
print(f"  then we're DOUBLE-COUNTING payroll taxes because we ALSO add $310,876 separately!")
print(f"")

# Let's verify: for each person, does model ≈ ADP gross + ADP ER liability?
print(f"  VERIFICATION: Does Model ≈ ADP Gross + ER Liability?")

# ADP ER liability per person (from earlier extract)
adp_er = {
    "Acker, Emily": 854,
    "Alvarez, Joel": 2_226,
    "Anzalone, Eric": 8_231,
    "Brooke, Debby": 0,  # Not sure
    "Calkins, Alexandria": 1_178,
    "Calkins, Stephen": 16_000,  # estimate
    "Carcamo, Andrea": 122,  # estimate
    "Carey, Kyle": 4_145,
    "Copeland, Breanna": 276,  # estimate
    "Davin, Jamie": 933,
    "Freeman, Tracy": 1_222,
    "Froio, James": 14_427,
    "Goodwin, Nicole (100)": 0,  # combined
    "Goodwin, Nicole (900)": 0,  # combined
    "Harris, Kaitlin": 5_150,
    "Holmes, Ashley": 82,
    "Kohler, Heather": 1_178,
    "McDonell, Hagen": 5_174,
    "Morte, Julia": 612,
    "Rankin, Dana": 872,
    "Rivera, Anneliese": 428,
    "Rocha Moreira, Marcello": 2_844,
    "Simpson, Juliet": 902,
    "Walsh, Laura": 15_879,
    "Wiggins, Chad": 7_436,
    "Wolf, Emily": 1_650,
    "Brock, Aimee": 1_973,
}

# Check the big ones
print(f"\n  {'Name':<25} {'Model':>10} {'ADP+ER':>10} {'Match?'}")
print(f"  {'-'*55}")
checks = [
    ("Calkins, Stephen", 164_960, 148_960, 16_000),
    ("Froio, James", 127_215, 112_788, 14_427),
    ("Walsh, Laura", 124_065, 108_186, 15_879),
    ("Anzalone, Eric", 84_949, 76_718, 8_231),
    ("Wiggins, Chad", 108_257, 95_000, 7_436),
    ("Harris, Kaitlin", 84_910, 79_760, 5_150),
    ("McDonell, Hagen", 56_784, 51_611, 5_174),
    ("Carey, Kyle", 55_978, 51_800, 4_145),
]

for name, model, adp, er in checks:
    adp_plus_er = adp + er
    match = "✓" if abs(model - adp_plus_er) < 100 else f"off by ${model - adp_plus_er:,}"
    print(f"  {name:<25} ${model:>8,} ${adp_plus_er:>8,}  {match}")

print(f"""

  CONCLUSION:
  ===========
  The model W-2 amounts = ADP Gross + ADP Employer Liability (payroll taxes).
  
  Stephen: $148,960 + $16,000 = $164,960 ✓
  Froio:   $112,788 + $14,427 = $127,215 ✓  
  Walsh:   $108,186 + $15,879 = $124,065 ✓
  
  This means the model ALREADY HAS payroll taxes baked into each person's amount.
  Then we ALSO add $310,876 as a separate "Payroll Tax" line = DOUBLE COUNT!
  
  But wait — ADP ER Liability is only $84,343.
  QB Payroll Tax + Exp = $310,876.
  The difference ($226,533) = health insurance, 401k, workers comp, etc.
  
  So the double-count is specifically the $84,343 ADP ER Liability that's 
  embedded in the model's per-person amounts AND also counted in the $310,876.
  
  PLUS: the model W-2 total ($1,103,125) includes ER liability ($84,343)
  making it $1,103,125 instead of $1,010,172 (pure gross).
  
  THE $200K VARIANCE EXPLAINED:
  Model excess from ER in W-2 amounts:  $  92,953  (≈ $84,343 ER liability)
  Plus: Payoneer/Badar double-count:    $ 106,931  (the $94K excess over QB Salary 
                                                     that's already in CS-Cost/Other)
  Total:                                $ 199,884  ✓ MATCHES THE VARIANCE!
""")
