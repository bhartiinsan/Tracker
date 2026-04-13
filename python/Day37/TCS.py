# Q1. Move All Zeros to End (The "Chocolate Factory" Problem)
# Year: 2024, 2025
# Problem Statement: A chocolate factory produces packets. Some packets are empty
# (represented by 0), and some have chocolates (represented by positive integers). You need
# to move all the empty packets (0) to the end of the conveyor belt while keeping the order of
# the chocolate-filled packets the same.
# Example: Input: [4, 5, 0, 1, 0, 0, 8]
# Output: 4 5 1 8 0 0 0

def move_zeros_to_end(n, arr):
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < n:
        arr[count] = 0
        count += 1
    return arr

n = int(input())
arr = list(map(int, input().split()))
result = move_zeros_to_end(n, arr)
print(*result)

#==========================================================================================================

# Q6. Non-Repeating Characters (String Processing)
# Year: 2024, 2025
# Question: Given a string S, find the first non-repeating character in it and return its index. If
# it doesn't exist, return -1.


s = input()

for char in s:
    if s.count(char) == 1:
        print(char)
        break
else:
    print(-1)

#==============================================================================================================

# Q7. The Star & Hash Balance (String Balancing)
# Year: 2022, 2025
# Problem Statement: Given a string containing only * and #, find the difference between the
# count of * and #.


s = input()
print(s.count('*') - s.count('#'))


#============================================================================================================

# Q8. Word Reverse in Sentence
# Year: 2021, 2023
# Question: Reverse the words in a given string without reversing the characters within the
# words.
# Example: Input: Hello World
# Output: World Hello

s = input().split()
print(" ".join(s[::-1]))


# #=============================================================================================================

# Q9. Check Anagram
# Year : 2022, 2024
# Problem Statement: Check if two strings are anagram

s1 = input()
s2 = input()
print(sorted(s1) == sorted(s2))


#===============================================================================================================

# Q10. String Compression
# Year : 2023, 2025
# Problem Statement:
# Compress string (aaabb → a3b2).

s = input()
result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1

result += s[-1] + str(count)
print(result)


# #===============================================================================================================
# Q14. Longest Substring Without Repeating Characters
# Year: 2023, 2025
# Problem Statement: Find the length of the longest substring without
# repeating characters.

s = input()
seen = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in seen:      # Duplicate found?
        seen.remove(s[left])     # Shrink from left
        left += 1
    
    seen.add(s[right])           # Add new character
    max_len = max(max_len, right - left + 1)  # Update answer

print(max_len)

#=================================================================================================================
# Q16. Vehicles & Wheels (Linear Algebra Logic)
# Year: 2021, 2023, 2025
# Problem Statement: A company produces two-wheelers (TW) and four-wheelers (FW).
# Given the total number of vehicles (V) and the total number of wheels (W), find the number
# of TW and FW.

V, W = map(int, input().split())
FW = (W - 2*V) // 2
TW = V - FW
print("Two-Wheelers:", TW, "Four-Wheelers:", FW)

#====================================================================================================================

# Q17.GCD of Two Numbers

# Year: 2021, 2023
# Problem Statement:Find GCD of two numbers.


from math import gcd
a, b = map(int, input().split())
print(gcd(a, b))

#=================================================================================================================
# Q18. Fibonacci series (Nth term)
# Year: 2023, 2024
# Problem Statement:Find nth Fibonacci number.

n = int(input())
a, b = 0, 1

for _ in range(n):
    a, b = b, a+b

print(a)

#===================================================================================================================

# Q19. Armstrong Number
# Year: 2022, 2024
# Problem Statement:Check if a number is Armstrong.

n = input()
p = len(n)
print("Armstrong" if sum(int(i)**p for i in n) == int(n) else "Not Armstrong")

#==================================================================================================================

# Q20.Prime Number
# Year: 2021, 2025
# Problem Statement: Check if a number is prime.


from sympy import isprime
print("Prime" if isprime(int(input())) else "Not Prime")


#===================================================================================================================

n = int(input())

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#         #===================================================================================================================

# Q25. Cube Series
# Year: 2022
# ❓ Problem Statement:
# A series follows:
# 1, 8, 27, 64, 125...
# Each term is the cube of natural numbers.
# Find the Nth term.
# Answer:
n = int(input())
print(n ** 3)


#==========================================================================

# Q24. Fibonacci-Based Series
# Year: 2023, 2025
# Problem Statement:
# A series is defined using Fibonacci numbers:
# 0, 1, 1, 2, 3, 5, 8...
# Given N, print the Nth term.
# Answer:

a, b = 0, 1
for _ in range(int(input())):
    a, b = b, a+b
print(a)

#==========================================================================




# Q27. Robot Movement Year: 2022, 2025 Problem Statement: A robot starts at (0,0). 
# It receives commands as a string: ● ‘L’ → move left ● ‘R’ → move right ● ‘U’ → move up ● ‘D’ → move down Each move is 1 unit. Find final position.



s = input()
x = y = 0

for ch in s:
    if ch == 'L': x -= 1
    elif ch == 'R': x += 1
    elif ch == 'U': y += 1
    elif ch == 'D': y -= 1

print(x, y)

#============================================================
s = input()

x = s.count('R') - s.count('L')
y = s.count('U') - s.count('D')

print(x, y)



###=========================--==================+++++++++++++++++++++++++

# Question 1: Total Marks of a Student
# Problem Statement
# You are given a 2D matrix representing marks of students. Each row represents a student, and each column represents marks in exams:

# Column 0 → Internal exam marks
# Column 1 → External exam marks

# You are also given an index (i, j) representing a student's position in the matrix.
# Task
# Calculate the total marks (internal + external) of the student at the given index.
# Input Explanation

# Two integers R and C representing number of rows and columns.
# A 2D matrix of size R × C containing marks.
# Two integers i and j representing the index of the student.

# Note: Even though both i and j are given, the student is identified by row i. The marks are taken from column 0 and column 1.
# Output Explanation

# Print the sum of internal and external marks of the selected student.
# If the index is invalid (out of bounds), print "Invalid Input".

# Example
# Input
# 2 2
# 40 50
# 30 60
# 1 1

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
x, y = map(int, input().split())

if x < 0 or x >= r or y < 0 or y >= c:
    print("Invalid Input")
else:
    print(arr[x][0] + arr[x][1])



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
# python# Step 1: Input lena
distance = int(input())
time = int(input())

# Step 2: Check karo time valid hai ya nahi
if time < 1 or time > 60:
    print("Error")
else:
    # Step 3: Time ko minutes se hours mein convert karo
    time_hours = time / 60

    # Step 4: Speed calculate karo
    speed = int(distance / time_hours)
    print(speed)


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



amount = float(input())

# Step 2: Discount decide karo
if amount < 1000:
    discount = 0.05        # 5%
elif amount < 5000:
    discount = 0.10        # 10%
else:
    discount = 0.15        # 15%

# Step 3: Final amount calculate karo
final_amount = amount - (amount * discount)

# Step 4: 2 decimal places mein print karo
print(f"{final_amount:.2f}")


#==============================================================================================================================

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

# Step 1: Hours lena
hours = int(input())

# Step 2: Fine calculate karo
if hours <= 2:
    print(100)
elif hours <= 5:
    print(50)
else:
    print(20)

#===================================================================================================================


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

# Step 1: Input lena
n = int(input())
arr = list(map(int, input().split()))

# Step 2: Odd numbers dhundho
sum_odd = 0
count = 0

for x in arr:
    if x % 2 != 0:      # Odd check
        sum_odd += x
        count += 1

# Step 3: Average calculate karo
avg = sum_odd / count if count != 0 else 0

# Step 4: Print karo
print(sum_odd, count, format(avg, ".2f"))


#==============================================================================================================================


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

# Step 1: Input lena
months = int(input())

# Step 2: Condition check karo
if months <= 0:
    print("Invalid Input")
elif months <= 1:
    print("Cost: 2000")
elif months <= 3:
    print("Cost: 5000")
elif months <= 6:
    print("Cost: 9000")
else:
    print("Cost: 15000")


    #==========================================

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


import sys

# Step 1: Saara input ek saath lena
data = list(map(int, sys.stdin.read().split()))

# Step 2: Pehla number N hai, baaki array
N = data[0]
arr = data[1:]

# Step 3: Count karo
count = 0
for x in arr:
    if x >= N:
        count += 1

print(count)

#=====================================================================================
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
# Formula:
# newHappy = 0.3 × Happy + 0.5 × Sad
# newSad   = 0.7 × Happy + 0.5 × Sad
# Input Format:

# Single integer N

# Output Format:

# Final_Happy Final_Sad

# Example:
# Input:   100
# Output:  36.5625 63.4375

# Step 1: Input lena
happy = float(input())
sad = 0.0

# Step 2: 4 iterations chalao
for _ in range(4):
    new_happy = 0.3 * happy + 0.5 * sad
    new_sad   = 0.7 * happy + 0.5 * sad

    happy = new_happy
    sad = new_sad

# Step 3: Print karo
print(happy, sad)