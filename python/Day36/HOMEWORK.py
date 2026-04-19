"""Python Logic & Function Solutions.

This file contains small reusable functions for the assignment questions.
"""

import math


# Core Mathematical Functions


# 1. Even or Odd Determination
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"


# 2. Reverse a Number
def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)

    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10

    return sign * rev


# 3. Prime Number Validation
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False

    return True


# 4. Factorial Calculation
def calculate_factorial(n):
    if n < 0:
        return "Factorial is not possible for negative values"

    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact


# Series and Number Properties


# 5. Fibonacci Series
def print_fibonacci(terms):
    a, b = 0, 1

    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a + b

    print()  # For newline


# 6 & 9. Armstrong Number Check
def is_armstrong(n):
    if n < 0:
        return False

    temp = n
    total_sum = 0

    while temp > 0:
        digit = temp % 10
        total_sum += digit ** 3
        temp //= 10

    return n == total_sum


# 7. Palindrome Check
def is_palindrome(n):
    return n == reverse_number(n)


# Conditional and Utility Functions


# 8. Positive or Negative Check
def sign_check(n):
    if n > 0:
        return "Positive"
    if n < 0:
        return "Negative"
    return "Zero"


# 10. Find Greatest of Two Numbers
def find_greatest(a, b):
    return a if a > b else b


# 11. Sum of Digits
def sum_of_digits(n):
    n = abs(n)
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


# 12. Power Calculation (a^b)
def calculate_power(a, b):
    return a ** b


# Summary Table of Requirements
# Question No. | Functionality | Primary Logic Used
# 1            | Even/Odd      | Modulo operator (%)
# 3            | Prime Check   | Square root optimization
# 4            | Factorial     | Iterative product loop
# 5            | Fibonacci     | Parallel assignment (a, b = b, a + b)
# 11           | Sum of Digits | Floor division (//) and modulo (%)

# The logic for these functions is based on foundational programming concepts provided in the training documents.
