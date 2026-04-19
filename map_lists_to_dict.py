# Python program to map two lists into a dictionary

# Sample lists
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

print("List 1 (Keys):", list1)
print("List 2 (Values):", list2)
print()

# Method 1: Using zip() and dict() - MOST COMMON
print("Method 1 - Using zip() and dict():")
result_dict = dict(zip(list1, list2))
print("Result:", result_dict)
print()

# Method 2: Using dictionary comprehension
print("Method 2 - Using dictionary comprehension:")
result_dict = {k: v for k, v in zip(list1, list2)}
print("Result:", result_dict)
print()

# Method 3: Using a for loop with index
print("Method 3 - Using a for loop with index:")
result_dict = {}
for i in range(len(list1)):
    result_dict[list1[i]] = list2[i]
print("Result:", result_dict)
print()

# Method 4: Using enumerate() in a loop
print("Method 4 - Using enumerate():")
result_dict = {}
for index, key in enumerate(list1):
    result_dict[key] = list2[index]
print("Result:", result_dict)
print()

# Method 5: Handling lists of different lengths
print("Method 5 - Handling lists of different lengths:")
keys = ['name', 'age', 'city', 'country', 'job']
values = ['John', 25, 'New York']  # Shorter list
print(f"Keys: {keys}")
print(f"Values: {values}")

# Using zip() - ignores extra keys
result_dict = dict(zip(keys, values))
print("Using zip():", result_dict)
print()

# Method 6: Using map() with lambda
print("Method 6 - Using map() with lambda:")
list_keys = [1, 2, 3, 4]
list_values = [10, 20, 30, 40]
result_dict = dict(map(lambda k, v: (k, v), list_keys, list_values))
print("Result:", result_dict)
print()

# Method 7: Create dictionary from lists with default values
print("Method 7 - Create dictionary from list (list items as keys):")
items = ['apple', 'banana', 'cherry']
# All keys with same default value
result_dict = {item: 0 for item in items}
print("Result:", result_dict)
print()

# Method 8: More complex example with nested structure
print("Method 8 - More complex example:")
names = ['Alice', 'Bob', 'Charlie', 'Diana']
ages = [25, 30, 35, 28]
cities = ['NYC', 'LA', 'Chicago', 'Boston']

# Create dictionary with tuples as values
result_dict = dict(zip(names, zip(ages, cities)))
print("Result:", result_dict)
for name, (age, city) in result_dict.items():
    print(f"  {name}: age={age}, city={city}")
print()

# Method 9: Function to map lists to dictionary
print("Method 9 - Using a function:")
def map_lists_to_dict(keys, values):
    """Map two lists into a dictionary"""
    return dict(zip(keys, values))

keys = ['one', 'two', 'three', 'four']
values = [1, 2, 3, 4]
result = map_lists_to_dict(keys, values)
print("Result:", result)
print()

# Method 10: Handling duplicates
print("Method 10 - Handling duplicate keys (last value wins):")
keys = ['a', 'b', 'c', 'a', 'b']
values = [1, 2, 3, 4, 5]
result_dict = dict(zip(keys, values))
print(f"Keys: {keys}")
print(f"Values: {values}")
print("Result (duplicates ignored, last value wins):", result_dict)
