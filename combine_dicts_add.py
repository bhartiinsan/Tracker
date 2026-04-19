# Simple Python program to combine two dictionaries adding values for common keys

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

print("Dictionary 1:", d1)
print("Dictionary 2:", d2)
print()

# Method 1: Using a loop (SIMPLE)
print("Method 1 - Using a loop:")
result = d1.copy()  # Copy d1 to result

for key, value in d2.items():
    if key in result:
        result[key] += value  # Add if key exists
    else:
        result[key] = value   # Add if key doesn't exist

print("Result:", result)
print()

# Method 2: Using dictionary comprehension
print("Method 2 - Using dictionary comprehension:")
all_keys = set(d1.keys()) | set(d2.keys())  # Get all unique keys
result = {key: d1.get(key, 0) + d2.get(key, 0) for key in all_keys}
print("Result:", result)
print()

# Method 3: Using Counter (from collections)
print("Method 3 - Using Counter:")
from collections import Counter
result = dict(Counter(d1) + Counter(d2))
print("Result:", result)
print()

# Method 4: Using update() and loop
print("Method 4 - Using update() and loop:")
result = d1.copy()
for key, value in d2.items():
    result[key] = result.get(key, 0) + value
print("Result:", result)
