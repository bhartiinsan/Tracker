# Python script to add an item to a dictionary

# Sample dictionary
sample_dict = {0: 10, 1: 20}
print("Original dictionary:", sample_dict)

# Add a new item to the dictionary
sample_dict[2] = 30
print("After adding item:", sample_dict)

# Alternative methods to add items to a dictionary:
print("\n--- Alternative Methods ---")

# Method 1: Using update() method
dict1 = {0: 10, 1: 20}
dict1.update({2: 30})
print("Using update():", dict1)

# Method 2: Using the merge operator (Python 3.9+)
dict2 = {0: 10, 1: 20}
dict2 = dict2 | {2: 30}
print("Using merge operator (|):", dict2)

# Method 3: Using setdefault() method
dict3 = {0: 10, 1: 20}
dict3.setdefault(2, 30)
print("Using setdefault():", dict3)
