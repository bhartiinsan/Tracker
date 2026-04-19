# Simple Python program to check if a dictionary is empty

# Empty dictionary
empty_dict = {}

# Non-empty dictionary
non_empty_dict = {1: 'a', 2: 'b', 3: 'c'}

print("Dictionary 1:", empty_dict)
print("Dictionary 2:", non_empty_dict)
print()

# Method 1: Using len()
print("Method 1 - Using len():")
if len(empty_dict) == 0:
    print("Dictionary 1 is empty")
else:
    print("Dictionary 1 is not empty")

if len(non_empty_dict) == 0:
    print("Dictionary 2 is empty")
else:
    print("Dictionary 2 is not empty")
print()

# Method 2: Using if statement (simple)
print("Method 2 - Using if statement (SIMPLEST):")
if empty_dict:
    print("Dictionary 1 is not empty")
else:
    print("Dictionary 1 is empty")

if non_empty_dict:
    print("Dictionary 2 is not empty")
else:
    print("Dictionary 2 is empty")
print()

# Method 3: Using bool()
print("Method 3 - Using bool():")
print(f"Is empty_dict empty? {not bool(empty_dict)}")
print(f"Is non_empty_dict empty? {not bool(non_empty_dict)}")
