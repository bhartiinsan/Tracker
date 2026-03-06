'''
4. Write a program that has following menu:
Enter code w for withdraw.
Enter code d for deposit.
Enter code c for checking balance.

Note: 1 take initial amount as input from user.

Note:2 You can withdraw an amount only if balance is greater
than or equal to withdrawing amount

'''


balance = float(input("Enter initial amount: "))

print("Enter code w for withdraw")
print("Enter code d for deposit")
print("Enter code c for checking balance")

code = input("Enter your choice: ").lower()

if code == 'w':
    amount = float(input("Enter amount to withdraw: "))
    
    if balance >= amount:
        balance = balance - amount
        print("Withdrawal successful")
        print("Current balance ₹", balance)
    else:
        print("Insufficient balance")

elif code == 'd':
    amount = float(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Deposit successful")
    print("Current balance ₹", balance)

elif code == 'c':
    print("Your current balance ₹", balance)

else:
    print("Invalid code entered")


