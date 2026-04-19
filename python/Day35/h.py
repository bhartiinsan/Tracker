# 1. Write a Python script to sort (ascending and descending) a dictionary by
# key.

data = {'orange': 2, 'apple': 5, 'grape': 1, 'banana': 8}

# Ascending (A-Z)
data_asc = dict(sorted(data.items()))

# Descending (Z-A)
data_desc = dict(sorted(data.items(), reverse=True))

print(f"Asc:  {data_asc}")
print(f"Desc: {data_desc}")
#=================================================================================



# 1. Sort dictionary by key
data = {'orange': 2, 'apple': 5, 'grape': 1, 'banana': 8}
print(dict(sorted(data.items())))
print(dict(sorted(data.items(), reverse=True)))

#=================================================================================



# 2. Write a Python script to add an item to a dictionary
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# Sample dictionary
sample_dict = {0: 10, 1: 20}
print("Original dictionary:", sample_dict)

# Add an item to the dictionary
sample_dict[2] = 30

print("Updated dictionary:", sample_dict)


# 2. Add item in dictionary
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
    
return sample_dict

#=================================================================================

# # Add single item
# my_dict[key] = value

# # Add multiple items
# my_dict.update({key1: value1, key2: value2})

# # Add with default value
# my_dict.setdefault(key, default_value)


#=============================================================================


# 3. Write a Python script to concatenate following dictionaries to create a new
# one.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# 3. Concatenate dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
print({**dic1, **dic2, **dic3})

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Method 1: Using merge operator (simplest)
result = dic1 | dic2 | dic3
print(result)

# Method 2: Using dictionary unpacking
result = {**dic1, **dic2, **dic3}
print(result)

# Method 3: Using update()
result = dic1.copy()
result.update(dic2)
result.update(dic3)
print(result)

# Method 4: Using a loop
result = {}
for d in [dic1, dic2, dic3]:
    result.update(d)
print(result)

# Method 5: Using dictionary comprehension
result = {k: v for d in [dic1, dic2, dic3]
                    for k, v in d.items()}                  

#=============================================================================

# 4. Write a Python script to check if a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30}
key = 2
if key in d:
    print("present")
else:
    print("not present")



sample_dict = {1: 10, 2: 20, 3: 30, 4: 40}

# Method 1: Using 'in' operator (RECOMMENDED - most common)
if 2 in sample_dict:
    print("Key exists")
else:
    print("Key does not exist")

# Method 2: Using 'not in' operator
if 5 not in sample_dict:
    print("Key does not exist")

# Method 3: Using get() method
if sample_dict.get(2) is not None:
    print(f"Key exists with value: {sample_dict.get(2)}")

# Method 4: Using keys() method
if 1 in sample_dict.keys():
    print("Key exists")

# Method 5: Using try-except
try:
    value = sample_dict[4]
    print(f"Key exists with value: {value}")
except KeyError:
    print("Key does not exist")

#=================================================================================

# 5. Write a Python program to iterate over dictionaries using for loops.


d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v)



#=============================================================================
sample_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# 1. Iterate over keys only
for key in sample_dict:
    print(key)

# 2. Iterate over values only
for value in sample_dict.values():
    print(value)

# 3. Iterate over key-value pairs (MOST COMMON)
for key, value in sample_dict.items():
    print(f"{key}: {value}")

# 4. Iterate with index
for index, (key, value) in enumerate(sample_dict.items()):
    print(f"{index}: {key} = {value}")

# 5. Reverse iteration
for key in reversed(sample_dict):
    print(f"{key}: {sample_dict[key]}")


# 6. Using keys() and access values
for key in sample_dict.keys():      
    print(f"{key} -> {sample_dict[key]}")

#=============================================================================

# 6. Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

n = 5
# Dictionary comprehension: (x, x*x)
squares = {x: x*x for x in range(1, n + 1)}

print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


n = 5

# Method 1: Using a for loop
square_dict = {}
for x in range(1, n + 1):
    square_dict[x] = x * x
print(square_dict)

# Method 2: Using dictionary comprehension (RECOMMENDED)
square_dict = {x: x*x for x in range(1, n + 1)}
print(square_dict)

# Method 3: As a function
def generate_square_dict(n):
    return {x: x*x for x in range(1, n + 1)}

result = generate_square_dict(5)
print(result)


#=============================================================================

# 7. Write a Python program to remove item using key from a dictionary.


d = {'a': 1, 'b': 2, 'c': 3}
# Method 1: Using pop() (RECOMMENDED - most common)
d.pop('b', none)
print(d)
# Method 2: Using del
del d['c']
print(d)
# Method 3: Using popitem() - removes last item
d.popitem()
print(d)

sample_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
#==================================================================================

# Method 1: Using del statement
del sample_dict[2]
print(sample_dict)

# Method 2: Using pop() - returns the value
removed_value = sample_dict.pop(3)
print(removed_value)

# Method 3: Using pop() with default value (safe)
result = sample_dict.pop(10, "Not found")

# Method 4: Remove last item
sample_dict.popitem()

# Method 5: Remove all items
sample_dict.clear()


# #=====================================================================================
# 8. Write a Python program to map two lists into a dictionary.

# Combine multiple lists into nested values
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

result = dict(zip(names, zip(ages, cities)))
# {Alice': (25, 'NYC'), 'Bob': (30, 'LA'), 'Charlie': (35, 'Chicago')}


# 8. Map two lists into dictionary
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
print(dict(zip(keys, vals)))


#=====================================================================================


# 9. Write a Python program to remove duplicates(based on values) from
# Dictionary.


sample_dict = {1: 'a', 2: 'b', 3: 'a', 4: 'c', 5: 'b', 6: 'd'}

# Method 1: Keep first occurrence (RECOMMENDED)
result_dict = {}
seen = set()
for key, value in sample_dict.items():
    if value not in seen:
        result_dict[key] = value
        seen.add(value)
print(result_dict)

# Method 2: Keep last occurrence
value_to_key = {}
for key, value in sample_dict.items():
    value_to_key[value] = key
result_dict = {v: k for k, v in value_to_key.items()}
print(result_dict)


sample_dict = {1: 'a', 2: 'b', 3: 'a', 4: 'c', 5: 'b', 6: 'd'}

result = {}
seen = set()

for key, value in sample_dict.items():
    if value not in seen:
        result[key] = value
        seen.add(value)

print(result)
#===============================================================


keys = ['id', 'name', 'rank']
vals = [101, 'Rahul', 1]

result = {}
for i in range(len(keys)):
    result[keys[i]] = vals[i]

print(result)
# Output: {'id': 101, 'name': 'Rahul', 'rank': 1}
#==============================================================================

# 10. Write a Python program to check a dictionary is empty or not.

# 10. Check empty dictionary
d = {}
if d == {}:
    print("empty")
#==============================================================================

d = {}
if not d:
    print("Empty")
else:
    print("Not empty")

#==============================================================================
my_dict = {}

# Method 1: Using len()
if len(my_dict) == 0:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")

# Method 2: Using if (SIMPLEST)
if my_dict:
    print("Dictionary is not empty")
else:
    print("Dictionary is empty")

# Method 3: Check if not empty
if not my_dict:
    print("Dictionary is empty")


#==============================================================================


# 11. Write a Python program to combine two dictionary adding values for
# common keys.
# d1 = {&#39;a&#39;: 100, &#39;b&#39;: 200, &#39;c&#39;:300}
# d2 = {&#39;a&#39;: 300, &#39;b&#39;: 200, &#39;d&#39;:400}
# Sample output: {&#39;a&#39;: 400, &#39;b&#39;: 400, &#39;d&#39;: 400, &#39;c&#39;: 300}


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = d1.copy()
for k, v in d2.items():
    result[k] = result.get(k, 0) + v
print(result)



d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Method 1: Using loop (SIMPLEST)
result = d1.copy()
for key, value in d2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)

# 12. Write a Python program to print a dictionary in table format.
data = {
    'Rahul': {'Age': 25, 'City': 'Delhi'},
    'Simran': {'Age': 22, 'City': 'Mumbai'},
    'Amit': {'Age': 28, 'City': 'Pune'}
}

# Header Print Karo
print(f"{'NAME':<10} | {'AGE':<5} | {'CITY':<10}")
print("-" * 30)

# Dictionary Items Print Karo
for name, info in data.items():
    print(f"{name:<10} | {info['Age']:<5} | {info['City']:<10}")

#==============================================================================
dict_data = {'a': 100, 'b': 200, 'c': 300}
print("Key".ljust(10) + "Value")
print("-" * 15)
for key, value in dict_data.items():
    print(str(key).ljust(10) + str(value))

#==============================================================================
print("+-------+-------+")
print("| Key   | Value |")
print("+-------+-------+")
for key, value in dict_data.items():
    print(f"| {str(key):5} | {str(value):5} |")
print("+-------+-------+")

#==============================================================================
print("Key\tValue")
print("-" * 20)
for key, value in dict_data.items():
    print(f"{key}\t{value}")


#==============================================================================
print(f"{'Key':<10} {'Value':<10}")
print("-" * 20) 
for key, value in dict_data.items():
    print(f"{str(key):<10} {str(value):<10}")

#==============================================================================



# 13. Write a Python program to get the top three items in a shop.
# Sample data: {&#39;item1&#39;: 45.50, &#39;item2&#39;:35, &#39;item3&#39;: 41.30, &#39;item4&#39;:55, &#39;item5&#39;: 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
data = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

# List of tuples: (price, name)
prices = []
for k, v in data.items():
    prices.append((v, k))

# Descending sort
prices.sort(reverse=True)

# Print top 3
for i in range(3):
    price, name = prices[i]
    print(f"{name} {price}")

    #==============================================================================

data = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

# 1. Sirf values ko nikalo aur sort karo (bade se chota)
prices = sorted(data.values(), reverse=True)

# 2. Top 3 values uthao
top_3_prices = prices[:3]

# 3. In values ke liye dictionary mein se keys (names) dhoondo
for p in top_3_prices:
    for name in data:
        if data[name] == p:
            print(f"{name} {p}")

#==============================================================================


# 14. Write a Python program to match key values in two dictionaries.
# Sample dictionary: {&#39;key1&#39;: 1, &#39;key2&#39;: 3, &#39;key3&#39;: 2}, {&#39;key1&#39;: 1, &#39;key2&#39;: 2}
# Expected output: key1: 1 is present in both x and y


x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

# Loop chalao pehli dictionary par
for k, v in x.items():
    # Check karo agar wahi key doosri dictionary mein hai 
    # AUR uski value bhi same hai
    if k in y and y[k] == v:
        print(f"{k}: {v} is present in both x and y")

# Alternative method using set intersection
common_keys = set(x.keys()) & set(y.keys())
for key in common_keys:
    if x[key] == y[key]:
        print(f"{key}: {x[key]} is present in both x and y")

#==============================================================================
# Alternative method using dictionary comprehension
matches = {k: v for k, v in x.items() if k in y and
                    y[k] == v}  
for k, v in matches.items():
    print(f"{k}: {v} is present in both x and y")




x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

for key in x:
    if key in y and x[key] == y[key]:
        print(f"{key}: {x[key]} is present in both x and y")

#==============================================================================

# Keys present in both
for key in x:
    if key in y:
        print(key)

# Key-values that DON'T match
for key in x:
    if key in y and x[key] != y[key]:
        print(f"{key}: x={x[key]}, y={y[key]}")

# Keys only in x
for key in x:
    if key not in y:
        print(f"{key}: {x[key]}")

# Keys only in y
for key in y:
    if key not in x:
        print(f"{key}: {y[key]}")

#==============================================================================
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for key in x:
    if key in y and x[key] == y[key]:
        print(f"{key}: {x[key]} is present in both")

