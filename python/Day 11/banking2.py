bal=int(input("enter available balance"))
amt= int(input("enter amount to withdraw"))
if bal>=amt:
    bal-= amt
    print("Balance Amount", bal)
else:
    print("insufficienyt bal")
print("thank you")