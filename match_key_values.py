# Python program to match key values in two dictionaries

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

print("Dictionary x:", x)
print("Dictionary y:", y)
print()

# ============ METHOD 1: Simple Loop (EASIEST) ============
print("METHOD 1 - Simple Loop:")
for key in x:
    if key in y and x[key] == y[key]:
        print(f"{key}: {x[key]} is present in both x and y")
print()

# ============ METHOD 2: Using for loop with items() ============
print("METHOD 2 - Using items():")
for key, value in x.items():
    if key in y:
        if y[key] == value:
            print(f"{key}: {value} is present in both x and y")
print()

# ============ METHOD 3: Using set intersection ============
print("METHOD 3 - Using set intersection:")
common_keys = set(x.keys()) & set(y.keys())
for key in common_keys:
    if x[key] == y[key]:
        print(f"{key}: {x[key]} is present in both x and y")
print()

# ============ METHOD 4: Get all matches in a list ============
print("METHOD 4 - Store matches in a list:")
matches = []
for key in x:
    if key in y and x[key] == y[key]:
        matches.append(f"{key}: {x[key]}")

print("Matching key-values:")
for match in matches:
    print(match, "is present in both x and y")
print()

# ============ METHOD 5: Using get() method ============
print("METHOD 5 - Using get() method:")
for key, value in x.items():
    if y.get(key) == value:
        print(f"{key}: {value} is present in both x and y")
print()

# ============ BONUS: Compare different things ============
print("="*60)
print("BONUS: Other comparisons")
print("="*60)
print()

# Find keys in both
print("1. Keys present in both:")
for key in x:
    if key in y:
        print(f"  {key}")
print()

# Find matching key-values
print("2. Key-values that match:")
for key in x:
    if key in y and x[key] == y[key]:
        print(f"  {key}: {x[key]}")
print()

# Find key-values that don't match
print("3. Key-values that DON'T match:")
for key in x:
    if key in y and x[key] != y[key]:
        print(f"  {key}: x={x[key]}, y={y[key]}")
print()

# Find keys only in x
print("4. Keys only in x:")
for key in x:
    if key not in y:
        print(f"  {key}: {x[key]}")
print()

# Find keys only in y
print("5. Keys only in y:")
for key in y:
    if key not in x:
        print(f"  {key}: {y[key]}")
