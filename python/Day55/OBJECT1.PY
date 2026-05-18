# class account:
#     def deposit():
#         print("Deposit is a method")

# a1= account()
# a2= account()

# a1.deposit() # method call using object a1
# a2.deposit() # method call using object a2

# so by default a1  and a2 chale jate h argument bankar toh error aajati hai
# by interpretation a1.deposit() is account.deposit(a1) and a2.deposit() is account.deposit(a2)
# so by default a1 and a2 chale jate h argument bankar toh error aajati hai
##==============================  
# 
# 
class account:
    def deposit(self,amt):
        print("Deposit is a method", amt)   

a1= account()
a2= account()

a1.deposit(1000) # method call using object a1
a2.deposit(2000) # method call using object a2