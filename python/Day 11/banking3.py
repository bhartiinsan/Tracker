# insufficient pin code if matches  # checking 
pin=int(input(" enter your pin amount"))
if pin==1234:
    print("Proceed your transaction, thankyou for verifying")

    bal=int(input("enter available balance"))
    amt= int(input("enter amount to withdraw"))
    if bal>= amt:
        bal-=amt
        print("Here is your remaining balance",bal)
    else:
        print("insufficient balance")
else: 
    print("invalid pin")
print("thankyou")