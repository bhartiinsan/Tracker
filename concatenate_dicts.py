# Python script to concatenate dictionaries

# Given dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

print("Original dictionaries:")
print("dic1 =", dic1)
print("dic2 =", dic2)
print("dic3 =", dic3)
print()

# Method 1: Using update() method
result1 = dic1.copy()
result1.update(dic2)
result1.update(dic3)
print("Method 1 - Using update():")
print("Result:", result1)
print()

# Method 2: Using merge operator (Python 3.9+)
result2 = dic1 | dic2 | dic3
print("Method 2 - Using merge operator (|):")
print("Result:", result2)
print()

# Method 3: Using dictionary unpacking
result3 = {**dic1, **dic2, **dic3}
print("Method 3 - Using dictionary unpacking:")
print("Result:", result3)
print()


# Method 5: Using a loop
result5 = {}
for d in [dic1, dic2, dic3]:
    result5.update(d)
print("Method 5 - Using a loop:")
print("Result:", result5)
