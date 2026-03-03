'''

3.Income Tax Calculation
Tax slabs:
 Income ≤ ₹12,00,000 → No tax

 Income &gt; ₹12,00,000
o Upto ₹4,00,000 → No tax
o ₹4,00,001 to ₹8,00,000 → 5% tax
o ₹8,00,001 to ₹12,00,000 → 10% tax
o ₹12,00,001 to ₹15,00,000 → 15% tax
o ₹15,00,001 to ₹18,00,000 → 20% tax
o Above ₹18,00,000 → 30% tax

Task:
Write a program using if-else that:
 Takes annual income as input
 Calculates and prints the tax amount


Income = int(input(" Give me the ANNUAL INCOME:   "))
if Income <= 1200000:
    print(" There is no tax slabs for you")
elif Income >1200000:
     
     TAX = FIRST + REMAINING
     if REMAINING >= 800000:
          REMAINING
          print(" YOU HAVE TO PAY", TAX)
     elif REMAINING >= 1200000:
          REMAINING = FIRST * (10/100)
          print(" YOU HAVE TO PAY", TAX)
     elif REMAINING >= 15000000:
          REMAINING = FIRST * (15/100)
          print(" YOU HAVE TO PAY", TAX)
     elif REMAINING >= 18000000:
          REMAINING = FIRST * (20/100)
          print(" YOU HAVE TO PAY", TAX)
     else:
          REMAINING = FIRST * (30/100)
          print(" YOU HAVE TO PAY", TAX)
          


'''





Income = int(input("Give me the ANNUAL INCOME: "))

tax = 0

if Income <= 1200000:
    print("There is no tax for you")

else:
    if Income > 1800000:
        tax = tax + (Income - 1800000) * 30 / 100
        Income = 1800000

    if Income > 1500000:
        tax = tax + (Income - 1500000) * 20 / 100
        Income = 1500000

    if Income > 1200000:
        tax = tax + (Income - 1200000) * 15 / 100
        Income = 1200000

    if Income > 800000:
        tax = tax + (Income - 800000) * 10 / 100
        Income = 800000

    if Income > 400000:
        tax = tax + (Income - 400000) * 5 / 100
        Income = 400000

    print("YOU HAVE TO PAY TAX ₹", tax)