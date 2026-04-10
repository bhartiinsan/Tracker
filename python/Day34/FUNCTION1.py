# decimal places 14-16 places
# # first default arg then non-def
# def ac(r,pi=3.14):
#     a=pi*r**2
#     print(a)

# ac(r=4.5)
# ac(pi=22/7, r=4.5)

# FUNCTION { FINAL VALUE}


# def bill_details(a,b=10):
#     b= a*b/100
#     c=b
#     bill=a-c
#     print(bill)

# bill_details(2000,5)

#==========================================================

#KEYWORD ARGUMENT
# WHICH IS PARAMETER N AME . SO TO BETTER READABILITY
# YOU CAN'T PASS KEYWORD ARGUMENT IN REPEAT
def price(cp,sp):
    if sp>cp:
        print(f"profit {sp-cp}")
    elif cp>sp:
        print(f"loss {cp-sp}")
    else:
        print(" YOU HAVE A LOSS")

price(cp=100, sp=120)
price(sp=100, cp=120)

# FIRST POSITION ARG THAN KEYWORD ARG
price(500, sp=120)  

#=========================================================



