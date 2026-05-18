class account:
    ifsc='abc123'              #class data

    def __init__(self,a,b):
        self.bal=b             #instance data
        self.acn=a             #instance data

a1=account(101,1000)
a2=account(102,2000)

print(a1.acn,a1.bal,a1.ifsc)
print(a2.acn,a2.bal,a2.ifsc)

account.ifsc='pqr321'

print(a1.ifsc)
print(a2.ifsc)