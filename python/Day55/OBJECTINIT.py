#OBJECT INITIALIZATION
    # special (magic) method-------> __init__(self) ----  constructor 

class account:
    def __init__(self):
        print("This is init method")

a1= account() # object banate hi init method call ho jata hai
a2= account() # object banate hi init method call ho jata hai

print("---------------------------------------" )

class account:
    def __init__(self,b,a):
        self.bal=b
        self.acn=a

a1= account(101,1000) # object banate hi init method call ho jata hai
a2= account(102,2000) # object banate hi init method call ho jata hai

print(a1.acn,a1.bal) # 1000
print(a2.acn,a2.bal) # 2000 

a1.bal= a1.bal+500 # balance update karna hai toh aise kar sakte hain

print(a1.acn,a1.bal) # 1500
print(a2.acn,a2.bal) # 2000 