# BANKING SYSTEM
bal=5000
print("Available Balance = 5000")

amt = int(input("Enter amount to withdraw=  "))
if bal>=amt:
    bal-= amt
    print("Balance Amount", bal)
else:
    print("insufficienyt bal")
print("thank you")