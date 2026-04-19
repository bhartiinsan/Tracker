# Simple Python program to remove duplicates from dictionary

# Sample dictionary
sample_dict = {1: 'a', 2: 'b', 3: 'a', 4: 'c', 5: 'b', 6: 'd'}

print("Original dictionary:", sample_dict)
print()

# Simple Method - Keep first occurrence
result = {}
seen = set()

for key, value in sample_dict.items():
    if value not in seen:
        result[key] = value
        seen.add(value)

print("After removing duplicates:", result)
