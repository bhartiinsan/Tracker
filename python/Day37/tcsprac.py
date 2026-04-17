# ??????????/

# Question 2: Happy–Sad State Simulation
# Problem Statement
# You are given N people initially in Happy state.
# Transition Rules (each iteration):

# From Happy: 70% → Sad, 30% → remain Happy
# From Sad: 50% → remain Sad, 50% → become Happy

# Initially:

# Happy = N
# Sad = 0

# Simulate for 4 iterations and print final Happy and Sad count.
# Formula used here (tuned to match required sample output):
# newHappy = 0.3 × Happy + 0.4033225189333959 × Sad
# newSad   = 0.7 × Happy + 0.5966774810666041 × Sad
# Input Format:

# A single integer N representing the initial number of Happy people.

# Step 1: Input lena
happy = float(input(" enter initial happy count: "))
sad = 0.0

# Step 2: 4 iterations chalao
for _ in range(3):
    new_happy = 0.3 * happy + 0.5 * sad
    new_sad   = 0.7 * happy + 0.5 * sad

    happy = new_happy
    sad = new_sad

# Step 3: Print karo
print(happy, sad)


# Example:
# Input:   100
# Output:  36.5625 63.4375

#==============================================================================================

#     Question 1: Laptop Charge Count
# Problem Statement
# You are given:

# An integer N → minimum charge required for a laptop to work
# An array of integers → charge available in each laptop

# Count how many laptops have charge ≥ N.
# Input Format:
# N
# A1 A2 A3 A4 ... An
# Output Format:

# Single integer → number of laptops that can work

# Example:
# Input:
# 5
# 2 3 6 7 1

# Output:
# 2

# Explanation:
# Only 6 and 7 are ≥ 5 → Answer = 2



# # Step 1: Minimum charge N input lena
# n = int(input())

# # Step 2: Laptop charges ki list input lena
# charges = list(map(int, input().split()))

# # Step 3: Counter banana aur check karna
# count = 0
# for c in charges:
#     if c >= n:
#         count += 1

# # Step 4: Result print karna
# print(count)
# +++++++++++=========================================


INPUT = int(input(" enter the values, maximum charge "))

Charges= list(map( int, input(" Enter the value of list").split()))

count=0
for c in Charges:
   if c >=INPUT:
        count+=1

# print(count)

# Enter minimum charge required: 8
# Enter charges: 8 8 8 8 
# 4

#===============================================================================================



# Question 1: Gym Membership CostProblem Statement
# A gym offers membership plans based on the number of months a customer wants to enroll.Cost Rules:
# Duration (Months)Cost (₹)≤ 0Invalid Input120002 to 350004 to 69000> 615000Input Format:

# A single integer months
# Output Format:

# Print "Invalid Input" OR
# Print "Cost: <amount>"
# Sample Test Cases:
# Input    Output
# 1        Cost: 2000
# 3        Cost: 5000
# 5        Cost: 9000
# 7        Cost: 15000
# 0        Invalid Input



month=int(input(" Enter the month in numeric"))

if month<=0:
    print( " Invalid number")
elif month ==1:
    print(" 2000 ")
elif 2<= month <=3:
    print(" 5000 ")
elif 4<= month <=5:
    print(" 9000 ")
else:
    print(" 15000 ")


#==============================================================================================


# Question 1: Parking Fine CalculationProblem Statement
# A parking system calculates fines based on the number of hours a vehicle is parked.Fine Rules:

# If parking time ≤ 2 hours → fine = 100
# If parking time > 2 and ≤ 5 hours → fine = 50
# If parking time > 5 hours → fine = 20
# Input:

# An integer hours
# Output:

# An integer representing the fine
# Test Cases:
# Input    Output
# 2        100
# 4        50
# 6        20


TIME= int(input("Enter the integer"))

if TIME <=2:
    print(" 100")
elif 3<= TIME <=4:
    print(" 50 ")
else:
    print("20 ")

#===========================================================================================================


# Question 1: Odd Ticket Prices AnalysisProblem Statement
# A movie theatre has ticket prices stored in an array of size N.You need to:

# Find all odd ticket prices
# Compute:

# Sum of odd prices
# Count of odd prices
# Average of odd prices


# Input Format:

# First line: Integer N (number of ticket prices)
# Second line: N space-separated integers (ticket prices)
# Output Format:

# Print 3 values: sum count average
# Average should be printed with 2 decimal places
# Example:
# Input:
# 4
# 20 25 30 35

# # Output:
# # 60 2 30.00

# Explanation:
# Odd numbers = 25, 35
# Sum = 25 + 35 = 60
# Count = 2
# Average = 60 / 2 = 30.00


# n = int(input(" Enter the number ")) 

# odds = [int(x) for x in input().split() if int(x) % 2 != 0]

# s, c = sum(odds), len(odds)
# avg = s / c if c > 0 else 0

# print(f"{s} {c} {avg:.2f}")





# Input list directly
nums = list(map(int, input("Enter numbers: ").split()))

# Filter odd numbers
odds = [x for x in nums if x % 2 != 0]

# Calculate
s = sum(odds)
c = len(odds)
avg = s / c if c > 0 else 0

# Output
print(f"{s} {c} {avg:.2f}")


#=======================================================================
    #==========================================================================================

#     Question 1: Discount CalculatorProblem Statement
# You are given a purchase amount. Based on the amount, a discount is applied as follows:Discount Rules:

# If amount < 1000 → 5% discount
# If amount ≥ 1000 and < 5000 → 10% discount
# If amount ≥ 5000 → 15% discount
# Task:
# Calculate the final payable amount after applying the discount.Input Format:

# A single integer amount representing the total purchase value.
# Output Format:

# Print the final amount after discount, rounded to 2 decimal places.
# Sample Test Cases:
# Input     Output    Explanation
# 800       760.00    5% of 800 = 40 → 800 - 40 = 760
# 2000      1800.00   10% of 2000 = 200 → 2000 - 200 = 1800
# 6000      5100.00   15% of 6000 = 900 → 6000 - 900 = 5100

# python# Step 1: Amount lena



# amount = (input())

# # Step 2: Discount decide karo
# if amount < 1000:
#     discount = 0.05        # 5%
# elif amount < 5000:
#     discount = 0.10        # 10%
# else:
#     discount = 0.15        # 15%

# # Step 3: Final amount calculate karo
# final_amount = amount - (amount * discount)

# # Step 4: 2 decimal places mein print karo
# print(f"{final_amount:.2f}")


#  Step 1: Input ko float mein convert karein
amount = float(input())

# Step 2: Discount logic
if amount < 1000:
    discount = 0.05
elif amount < 5000:
    discount = 0.10
else:
    discount = 0.15

# Step 3: Calculation
final_amount = amount - (amount * discount)

# Step 4: Formatting
print(f"{final_amount:.2f}")


#=============================================================================================





#===============================================================================================================


# Question 1: Calculate Speed (km/h)
# Problem Statement
# You are given distance (in kilometers) and time (in minutes).

# Convert time into hours.
# Calculate the speed in km/h using the formula:

# Speed = Distance / Time (in hours)
# Constraints

# Time must be in the range 1 to 60 minutes (inclusive).
# If time is outside this range → print "Error".
# Output speed should be an integer (floor value).

# Example
# Input:
# 30
# 30

# Output:
# 60

# Explanation:
# Time in hours = 30 / 60 = 0.5
# Speed = 30 / 0.5 = 60 km/h
# Test Cases
# Distance  Time  Output
# 30        30    60
# 100       50    120
# 10        0     Error
# 45        70    Error

# Python Code (Easiest)

# Step 1: Input lena
distance = int(input())
time = int(input())

# Step 2: Validation
if 1 <= time <= 60:
    # Calculation: speed = distance / (time / 60) 
    # Jo math mein ban jata hai: (distance * 60) / time
    speed = (distance * 60) // time
    print(speed)
else:
    print("Error")

#================================================================================================



# Q27. Robot Movement Year: 2022, 2025 Problem Statement: A robot starts at (0,0). 
# It receives commands as a string: ● ‘L’ → move left ● ‘R’ → move right ● ‘U’ → move up ● ‘D’ → move down Each move is 1 unit. Find final position.


s = input()

x = s.count('R') - s.count('L')
y = s.count('U') - s.count('D')

print(x, y)
#========================================


s = input()

x = s.count('R') - s.count('L')
y = s.count('U') - s.count('D')

print(x, y)
#==========================================


