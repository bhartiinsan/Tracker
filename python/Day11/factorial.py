# for printing a factorial

num=(int(input("Enter the number =  ")))
fact=1
if num<0:
    print("factorial does not exist for negative numbers")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("the factorial of",num,"is",fact)

'''



num = int(input("Enter the number = "))

def factorial(n):
    if n <= 0:
        print("factorial undefined")
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result  # ← Now properly indented inside the function

print("the factorial of", num, "is", factorial(num))


























'''




num=(int(input("Enter the number =  ")))
def factorial(n):
    if n<=0:
        print(" factorial undefined")
        return 1
    for i in range(1, n+ 1):
        return *= i
    return result


num=(int(input("Enter the number =  ")))

def factorial(n):
    return 1 if n<=1 else n* factorial(n-1)