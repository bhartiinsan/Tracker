

balance = float(input("Enter initial amount: "))



while True:
    print("Enter code w for withdraw")
    print("Enter code d for deposit")
    print("Enter code c for checking balance")
    print(" Enter code n for stoping the loop ")

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

    else :
        break
print(" thankyou ")
        