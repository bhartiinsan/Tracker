
'''
2. Electricity Bill (Subsidy Based)
rules:
 If units ≤ 200 → Bill = ₹0 (free)
 If units &gt; 200:
o First 200 units are charged at ₹2 per unit
o Remaining units are charged at ₹4 per unit

Task:
Write a program using if-else that:
 Takes electricity units as input
 Calculates and prints the total bill amount
'''

# LOGIC IS UNITS IS 

units = int(input(" Give me the units you used "))

if units<=200: 
    bill = units*0
    print(" YOU ARE HAVING NO DUES ON BILL", bill)

else: 
    FIRST = 200* 2
    REMAINING = units -200 
    SECOND = REMAINING*4
    bill = FIRST+ SECOND
    print(" YOU HAVE DUES PENDING ON ELECTRICITY BILL ", bill)