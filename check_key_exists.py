# Python script to check if a key exists in a dictionary

# Sample dictionary
sample_dict = {1: 10, 2: 20, 3: 30, 4: 40}

print("Sample dictionary:", sample_dict)
print()

# Method 1: Using 'in' operator (most common)
print("Method 1 - Using 'in' operator:")
key_to_check = 2
if key_to_check in sample_dict:
    print(f"Key {key_to_check} exists in the dictionary")
else:
    print(f"Key {key_to_check} does not exist in the dictionary")

key_to_check = 5
if key_to_check in sample_dict:
    print(f"Key {key_to_check} exists in the dictionary")
else:
    print(f"Key {key_to_check} does not exist in the dictionary")
print()

# Method 2: Using 'not in' operator
print("Method 2 - Using 'not in' operator:")
key_to_check = 3
if key_to_check not in sample_dict:
    print(f"Key {key_to_check} does not exist in the dictionary")
else:
    print(f"Key {key_to_check} exists in the dictionary")
print()

# Method 3: Using get() method
print("Method 3 - Using get() method:")
key_to_check = 2
if sample_dict.get(key_to_check) is not None:
    print(f"Key {key_to_check} exists in the dictionary with value: {sample_dict.get(key_to_check)}")
else:
    print(f"Key {key_to_check} does not exist in the dictionary")

key_to_check = 5
if sample_dict.get(key_to_check) is not None:
    print(f"Key {key_to_check} exists in the dictionary with value: {sample_dict.get(key_to_check)}")
else:
    print(f"Key {key_to_check} does not exist in the dictionary")
print()

# Method 4: Using keys() method
print("Method 4 - Using keys() method:")
key_to_check = 1
if key_to_check in sample_dict.keys():
    print(f"Key {key_to_check} exists in the dictionary")
else:
    print(f"Key {key_to_check} does not exist in the dictionary")
print()

# Method 5: Using try-except (exception handling)
print("Method 5 - Using try-except:")
key_to_check = 4
try:
    value = sample_dict[key_to_check]
    print(f"Key {key_to_check} exists in the dictionary with value: {value}")
except KeyError:
    print(f"Key {key_to_check} does not exist in the dictionary")

key_to_check = 10
try:
    value = sample_dict[key_to_check]
    print(f"Key {key_to_check} exists in the dictionary with value: {value}")
except KeyError:
    print(f"Key {key_to_check} does not exist in the dictionary")
