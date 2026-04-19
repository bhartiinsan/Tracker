# Python program to remove item using key from a dictionary

# Sample dictionary
sample_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

print("Original dictionary:", sample_dict)
print()

# Method 1: Using del statement
print("Method 1 - Using del statement:")
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print("Before deletion:", dict1)
del dict1[3]
print("After deleting key 3:", dict1)
print()

# Method 2: Using pop() method (returns the value)
print("Method 2 - Using pop() method:")
dict2 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print("Before deletion:", dict2)
removed_value = dict2.pop(2)
print(f"Removed key 2 with value: {removed_value}")
print("After deletion:", dict2)
print()

# Method 3: Using pop() with default value
print("Method 3 - Using pop() with default value (handles missing keys):")
dict3 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print("Before deletion:", dict3)
# Try to remove key that exists
result = dict3.pop(4, "Key not found")
print(f"Removed key 4: {result}")
# Try to remove key that doesn't exist
result = dict3.pop(10, "Key not found")
print(f"Try to remove key 10: {result}")
print("After operations:", dict3)
print()

# Method 4: Using popitem() - removes last item
print("Method 4 - Using popitem() - removes last item:")
dict4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print("Before deletion:", dict4)
removed_pair = dict4.popitem()
print(f"Removed item: {removed_pair}")
print("After deletion:", dict4)
print()

# Method 5: Removing multiple keys using pop()
print("Method 5 - Removing multiple keys:")
dict5 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print("Before deletion:", dict5)
keys_to_remove = [1, 3, 5]
for key in keys_to_remove:
    dict5.pop(key, None)  # None is default if key doesn't exist
print("After removing keys 1, 3, 5:", dict5)
print()

# Method 6: Using clear() to remove all items
print("Method 6 - Using clear() to remove all items:")
dict6 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print("Before clear:", dict6)
dict6.clear()
print("After clear:", dict6)
print()

# Method 7: Error handling when removing keys
print("Method 7 - Error handling:")
dict7 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print("Dictionary:", dict7)

# Using try-except with del
try:
    del dict7[10]
except KeyError:
    print("Error: Key 10 does not exist")

# Using pop() with default (no error)
result = dict7.pop(10, "Not found")
print(f"Trying to pop key 10: {result}")
print()

# Method 8: Conditional removal
print("Method 8 - Conditional removal (remove if exists):")
dict8 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print("Before:", dict8)
key_to_remove = 3
if key_to_remove in dict8:
    del dict8[key_to_remove]
    print(f"Key {key_to_remove} removed")
else:
    print(f"Key {key_to_remove} does not exist")
print("After:", dict8)
