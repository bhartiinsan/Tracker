Weight = int(input("ENTER THE WEIGHT kg :"))

if Weight <= 40:
    print("Underweight")
elif Weight <= 60:
    print("Normal weight")
elif Weight <= 80:
    print("Overweight")
else:
    print("Obese")



# the logic is correct but the code is not efficient because we are checking the condition for each weight range separately.
# # We can optimize the code by using a single if-elif-else statement to check the weight range and print the corresponding message.

# so the optimised code is as follows:
'''''
Weight = int(input("ENTER THE WEIGHT kg :"))
if Weight < 0:
    print("Invalid weight")
elif Weight < 40:
    print("Underweight")
elif Weight < 60:
    print("Normal weight")
elif Weight < 80:
    print("Overweight")
elif Weight <= 100:
    print("Obese")

'''''

# In this code, we first check if the weight is negative, which is invalid. 
#Then we check the weight ranges in a single if-elif-else statement, which is more efficient and easier to read.

# it will take less time to execute because we are not checking the condition for each weight range separately.