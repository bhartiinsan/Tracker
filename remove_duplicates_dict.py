# Python program to remove duplicates based on values from a dictionary

# Sample dictionary with duplicate values
sample_dict = {1: 'a', 2: 'b', 3: 'a', 4: 'c', 5: 'b', 6: 'd'}

print("Original dictionary:", sample_dict)
print()

# Method 1: Using a set to track seen values (keeps first occurrence)
print("Method 1 - Keep first occurrence using set:")
result_dict = {}
seen = set()
for key, value in sample_dict.items():
    if value not in seen:
        result_dict[key] = value
        seen.add(value)
print("Result:", result_dict)
print()

# Method 2: Using dictionary comprehension with enumerate
print("Method 2 - Keep first occurrence using dict comprehension:")
result_dict = {key: value for key, value in sample_dict.items()
               if value not in list(sample_dict.values())[:list(sample_dict.values()).index(value)]}
print("Result:", result_dict)
print()

# Method 3: Keep last occurrence (reverse iteration)
print("Method 3 - Keep last occurrence using reversed:")
result_dict = {}
for key, value in reversed(list(sample_dict.items())):
    if value not in result_dict.values():
        result_dict[key] = value
result_dict = dict(reversed(list(result_dict.items())))
print("Result:", result_dict)
print()

# Method 4: Using dict.fromkeys() approach
print("Method 4 - Using dict.fromkeys() with values:")
unique_values = list(dict.fromkeys(sample_dict.values()))
result_dict = {v: k for k, v in sample_dict.items()}
print("Result:", result_dict)
print()

# Method 5: Using a more efficient method with seen set
print("Method 5 - Efficient method (keep first occurrence):")
seen = set()
result_dict = {}
for key, value in sample_dict.items():
    if value not in seen:
        result_dict[key] = value
        seen.add(value)
print("Result:", result_dict)
print()

# Method 6: Using function with options
print("Method 6 - Using a function with option to keep first/last:")

def remove_duplicates_by_value(dictionary, keep='first'):
    """
    Remove duplicates from dictionary based on values
    keep='first' - keeps first occurrence
    keep='last' - keeps last occurrence
    """
    if keep == 'first':
        result = {}
        seen = set()
        for key, value in dictionary.items():
            if value not in seen:
                result[key] = value
                seen.add(value)
        return result
    elif keep == 'last':
        result = {}
        for key, value in dictionary.items():
            if value not in result.values() or key > list(result.keys())[-1]:
                result[key] = value
        # Cleaner approach for last
        seen = {}
        for key, value in dictionary.items():
            seen[value] = key
        return {v: k for k, v in seen.items()}

# Keep first
result1 = remove_duplicates_by_value(sample_dict, keep='first')
print(f"Keep first: {result1}")

# Keep last
result2 = remove_duplicates_by_value(sample_dict, keep='last')
print(f"Keep last: {result2}")
print()

# Method 7: Get unique values count
print("Method 7 - Show duplicate values:")
value_counts = {}
for value in sample_dict.values():
    value_counts[value] = value_counts.get(value, 0) + 1

print("Value counts:")
for value, count in value_counts.items():
    print(f"  '{value}': {count} occurrence(s)")

print("\nDuplicate values:", [v for v, c in value_counts.items() if c > 1])
print()

# Method 8: Using a dictionary to map values to keys
print("Method 8 - Create value-to-key mapping (last occurrence):")
value_to_key = {}
for key, value in sample_dict.items():
    value_to_key[value] = key  # Last occurrence overwrites
result_dict = {v: k for k, v in value_to_key.items()}
print("Result:", result_dict)
print()

# Method 9: Complex example with nested operations
print("Method 9 - Remove duplicates and sort:")
sample_dict2 = {'a': 100, 'b': 200, 'c': 100, 'd': 300, 'e': 200}
print("Original:", sample_dict2)

# Remove duplicates (keep first)
seen = set()
result_dict = {}
for key, value in sample_dict2.items():
    if value not in seen:
        result_dict[key] = value
        seen.add(value)

# Sort by value
result_dict = dict(sorted(result_dict.items(), key=lambda x: x[1]))
print("After removing duplicates and sorting:", result_dict)
print()

# Method 10: Comparison with set operations
print("Method 10 - Finding which values are duplicated:")
all_values = list(sample_dict.values())
unique_values = set(all_values)
duplicate_values = {v for v in unique_values if all_values.count(v) > 1}

print(f"All values: {all_values}")
print(f"Unique values: {unique_values}")
print(f"Duplicate values: {duplicate_values}")

# Remove items with duplicate values
result_dict = {k: v for k, v in sample_dict.items() if v not in duplicate_values}
print(f"Dict without any duplicate values: {result_dict}")
