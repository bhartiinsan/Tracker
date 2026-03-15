#5. WAP to print calculate the factorial of number entered through keyboard

# num= int(input(" Enter the number "))

# for i in range (1,num-1):
#     print (i)


# WAP to calculate factorial of a number entered through keyboard

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial of", num, "is", fact)


#-------------------------------------------------

num = int(input("Enter a number: "))

fact = 1
if num>=0:
    for i in range( num,0,-1):
        fact = fact * i
    print("Factorial of", num, "is", fact)
else:
    print(" factorial is not possible")






#------------------------------------------------------------------------

# num = int(input("Enter a non-negative integer for recursive factorial: "))



# def factorial_recursive(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1  # Base case: Factorial of 0 or 1 is 1
#     else:
#         return n * factorial_recursive(n - 1)  # Recursive step

# # Get input from the user
# # num = int(input("Enter a non-negative integer for recursive factorial: "))

# # Calculate and print the factorial
# print(f"The factorial of {num} (recursive) is: {factorial_recursive(num)}")
    