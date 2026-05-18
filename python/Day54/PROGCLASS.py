# independent function
def deposit():
    print("Deposit is a function") # bina class k function (karne wala nahi hai) function kehlata hai 

# dependent function
class account:
    def deposit():
        print("Deposit is a method") # class ke andar ka function method kehlata hai(karne wala hai) method kehlata hai

# min max sum len etc are functions
# upper lower append pop etc are methods

# method of str
 # upper lower replace etc are method of str class

# method of list
# append pop remove etc are method of list class

deposit() # function call
account.deposit() # method call