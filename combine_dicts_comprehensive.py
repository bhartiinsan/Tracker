# Python program to combine two dictionaries - Multiple Methods

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

print("="*60)
print("Dictionary 1:", d1)
print("Dictionary 2:", d2)
print("="*60)
print()

# ============ METHOD 1: Using Loop with Copy ============
print("METHOD 1 - Using Loop with Copy:")
result = d1.copy()
for key, value in d2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value
print("Result:", result)
print()

# ============ METHOD 2: Using get() Method ============
print("METHOD 2 - Using get() Method:")
result = d1.copy()
for key, value in d2.items():
    result[key] = result.get(key, 0) + value
print("Result:", result)
print()

# ============ METHOD 3: Using Dictionary Comprehension ============
print("METHOD 3 - Using Dictionary Comprehension:")
all_keys = set(d1.keys()) | set(d2.keys())
result = {key: d1.get(key, 0) + d2.get(key, 0) for key in all_keys}
print("Result:", result)
print()

# ============ METHOD 4: Using Counter from collections ============
print("METHOD 4 - Using Counter (collections module):")
from collections import Counter
c1 = Counter(d1)
c2 = Counter(d2)
result = dict(c1 + c2)
print("Result:", result)
print()

# ============ METHOD 5: Using defaultdict ============
print("METHOD 5 - Using defaultdict:")
from collections import defaultdict
result = defaultdict(int)
for d in [d1, d2]:
    for key, value in d.items():
        result[key] += value
result = dict(result)
print("Result:", result)
print()

# ============ METHOD 6: Using setdefault() ============
print("METHOD 6 - Using setdefault():")
result = d1.copy()
for key, value in d2.items():
    result.setdefault(key, 0)
    result[key] += value
print("Result:", result)
print()

# ============ METHOD 7: Using update() and get() ============
print("METHOD 7 - Using Custom Function:")
def combine_dicts(dict1, dict2):
    result = dict1.copy()
    for key in dict2:
        result[key] = result.get(key, 0) + dict2[key]
    return result

result = combine_dicts(d1, d2)
print("Result:", result)
print()

# ============ METHOD 8: Using dict() Constructor ============
print("METHOD 8 - Using dict() Constructor with unpacking:")
result = dict(d1)
result.update({k: result.get(k, 0) + v for k, v in d2.items()})
print("Result:", result)
print()

# ============ METHOD 9: Using reduce() from functools ============
print("METHOD 9 - Using reduce() from functools:")
from functools import reduce
def merge_add(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result

result = reduce(merge_add, [d1, d2])
print("Result:", result)
print()

# ============ METHOD 10: One-liner with comprehension ============
print("METHOD 10 - One-liner (Dictionary Comprehension):")
result = {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)}
print("Result:", result)
print()

# ============ DIFFERENT SCENARIOS ============
print("="*60)
print("DIFFERENT SCENARIOS")
print("="*60)
print()

# Scenario 1: Three dictionaries
print("Scenario 1 - Combine THREE dictionaries:")
d3 = {'a': 50, 'b': 100, 'e': 500}
all_dicts = [d1, d2, d3]
result = {}
for d in all_dicts:
    for key, value in d.items():
        result[key] = result.get(key, 0) + value
print("d1:", d1)
print("d2:", d2)
print("d3:", d3)
print("Combined:", result)
print()

# Scenario 2: Using Chain with Counter
print("Scenario 2 - Chain multiple dicts with Counter:")
from itertools import chain
combined_counter = Counter(dict(chain(d1.items(), d2.items())))
for k, v in chain(d1.items(), d2.items()):
    combined_counter[k] = v
# Recalculate
result = {}
for key in set(d1.keys()) | set(d2.keys()):
    result[key] = d1.get(key, 0) + d2.get(key, 0)
print("Result:", result)
print()

# Scenario 3: Subtract instead of add
print("Scenario 3 - Subtract values for common keys:")
result = d1.copy()
for key, value in d2.items():
    if key in result:
        result[key] -= value
    else:
        result[key] = -value
print("d1:", d1)
print("d2:", d2)
print("Result (d1 - d2):", result)
print()

# Scenario 4: Multiply values
print("Scenario 4 - Multiply values for common keys:")
result = d1.copy()
for key, value in d2.items():
    if key in result:
        result[key] *= value
    else:
        result[key] = value
print("d1:", d1)
print("d2:", d2)
print("Result (d1 * d2 for common keys):", result)
print()

# Scenario 5: Keep only common keys and add
print("Scenario 5 - Only combine COMMON keys:")
common_keys = set(d1.keys()) & set(d2.keys())
result = {key: d1[key] + d2[key] for key in common_keys}
print("d1:", d1)
print("d2:", d2)
print("Common keys only:", result)
print()

# Scenario 6: Nested dictionaries
print("Scenario 6 - Combine nested dictionaries:")
nd1 = {'person1': {'age': 25, 'salary': 50000}}
nd2 = {'person1': {'bonus': 5000}, 'person2': {'age': 30, 'salary': 60000}}
result = {}
for key in set(nd1.keys()) | set(nd2.keys()):
    if key in nd1 and key in nd2:
        inner_result = nd1[key].copy()
        for k, v in nd2[key].items():
            inner_result[k] = inner_result.get(k, 0) + v
        result[key] = inner_result
    elif key in nd1:
        result[key] = nd1[key]
    else:
        result[key] = nd2[key]
print("nd1:", nd1)
print("nd2:", nd2)
print("Combined:", result)
print()

# ============ PERFORMANCE COMPARISON ============
print("="*60)
print("PERFORMANCE & RECOMMENDATION")
print("="*60)
print("""
Best Methods:
1. METHOD 2 (get() + Loop) - Simple, readable, efficient
2. METHOD 3 (Dict Comprehension) - Pythonic, concise
3. METHOD 4 (Counter) - Best for multiple dicts

Choose based on:
- Simplicity: Method 2 or get() approach
- Performance: Counter or defaultdict
- Readability: Dict Comprehension (Method 3)
- Multiple dicts: Use Counter or loop
""")
