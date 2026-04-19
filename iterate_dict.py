# Python program to iterate over dictionaries using for loops

# Sample dictionary
sample_dict = {'name': 'John', 'age': 25, 'city': 'New York', 'profession': 'Engineer'}

print("Sample dictionary:", sample_dict)
print()

# Method 1: Iterate over keys
print("Method 1 - Iterate over keys:")
for key in sample_dict:
    print(f"Key: {key}")
print()

# Method 2: Iterate over keys explicitly using keys()
print("Method 2 - Iterate over keys using keys():")
for key in sample_dict.keys():
    print(f"Key: {key}")
print()

# Method 3: Iterate over values
print("Method 3 - Iterate over values:")
for value in sample_dict.values():
    print(f"Value: {value}")
print()

# Method 4: Iterate over key-value pairs using items()
print("Method 4 - Iterate over key-value pairs using items():")
for key, value in sample_dict.items():
    print(f"{key}: {value}")
print()

# Method 5: Iterate with index using enumerate()
print("Method 5 - Iterate with index using enumerate():")
for index, (key, value) in enumerate(sample_dict.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")
print()

# Method 6: Iterate using keys() and access values
print("Method 6 - Iterate using keys() and access values:")
for key in sample_dict.keys():
    print(f"{key} -> {sample_dict[key]}")
print()

# Example with numeric dictionary
print("=" * 50)
print("Example with numeric dictionary:")
numeric_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print("Dictionary:", numeric_dict)
print()

print("Iterating with key-value pairs:")
for key, value in numeric_dict.items():
    print(f"Key: {key}, Value: {value}, Sum: {key + value}")
print()

# Reverse iteration
print("Reverse iteration (using reversed):")
for key in reversed(numeric_dict):
    print(f"Key: {key}, Value: {numeric_dict[key]}")
