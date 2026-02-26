



num=(int(input("Enter the number =  ")))
def factorial (n):
    if n<=0:
        print(" factorial undefined")
        return 1
    result=1
    for i in range(1, n+ 1):
        result*=i
    return result
print("the factorial of",num,"is",factorial(num))



#FACTORIAL USING RECURSION

num = int(input("Enter number: "))

if num < 0:
    print("Factorial undefined")

else:
    result = 1

    for i in range(1, num + 1):
        result *= i

    print("Factorial:", result)


#PALLENDROME

num = int(input("Enter number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if num == rev:
    print("Palindrome") 
else:
    print("Not a palindrome")












'''
def factorial(n):
    return 1 if n<=1 else n* factorial(n-1)

'''

