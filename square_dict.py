# Python script to generate a dictionary with numbers (x, x*x)

# Method 1: Using a for loop
print("Method 1 - Using a for loop:")
n = 5
square_dict = {}
for x in range(1, n + 1):
    square_dict[x] = x * x
print(f"Dictionary (n={n}):", square_dict)
print()

# Method 2: Using dictionary comprehension (most efficient)
print("Method 2 - Using dictionary comprehension:")
n = 6
square_dict = {x: x*x for x in range(1, n + 1)}
print(f"Dictionary (n={n}):", square_dict)
print()

# Method 3: Using a function
print("Method 3 - Using a function:")
def generate_square_dict(n):
    """Generate a dictionary with numbers (x, x*x) from 1 to n"""
    return {x: x*x for x in range(1, n + 1)}

n = 8
result = generate_square_dict(n)
print(f"Dictionary (n={n}):", result)
print()

# Method 4: Using map and dict()
print("Method 4 - Using map and dict():")
n = 5
square_dict = dict(map(lambda x: (x, x*x), range(1, n + 1)))
print(f"Dictionary (n={n}):", square_dict)
print()

# Method 5: Different values of n
print("Method 5 - Generating dictionaries for different values of n:")
for n in [3, 5, 10]:
    square_dict = {x: x*x for x in range(1, n + 1)}
    print(f"n={n}: {square_dict}")
print()

# Method 6: Display formatted output
print("Method 6 - Formatted output:")
n = 5
square_dict = {x: x*x for x in range(1, n + 1)}
print(f"\nDictionary for n = {n}:")
for key, value in square_dict.items():
    print(f"  {key} -> {key}*{key} = {value}")
