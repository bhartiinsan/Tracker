# 1. Write a Python script to sort (ascending and descending) a dictionary by
# key.
 
# d = {103: 'sanju', 101: 'sonu', 104: 'virat', 102: 'monu'}

# asc_dict = dict(sorted(d.items()))
# print(asc_dict)

# dsc_dict= dict(sorted(d.items(), reverse =True))
# print(dsc_dict)

#======================================================================================

# 2. Write a Python script to add an item to a dictionary
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# d=  {0: 10, 1: 20}
# print(d)
# d[2]=30
# print(d)


#=======================================================================================


# 3. Write a Python script to concatenate following dictionaries to create a new
# one.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# Add= dic1|dic2|dic3
# print(Add)

#======================================================================================

# 4. Write a Python script to check if a given key already exists in a dictionary.


# d = {103: 'sanju', 101: 'sonu', 104: 'virat', 102: 'monu'}
# value= int(input(" enter the value"))

# if value in d:
#     print(" IT IS PRESENT")
# else:
#     print(" IT IS NOT PRESENT")

# #=======================================================================================

# 5. Write a Python program to iterate over dictionaries using for loops.

# d = {103: 'sanju', 101: 'sonu', 104: 'virat', 102: 'monu'}
# for key in d:
#     print(key , d[key])

#===========================================================================================

# 6. Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n=5
d={i:i*i for i in range(1,n+1)}
print(d)

# n = 5
# # Use i * i or i ** 2 for the square
# d = {i: i * i for i in range(1, n + 1)}

# print(d)
#=========================================================================================

# 7. Write a Python program to remove item using key from a dictionary.


# d = {103: 'sanju', 101: 'sonu', 104: 'virat', 102: 'monu'}
# user_input = int(input("Enter key to delete: "))


# if user_input in d:
#     del d[user_input]
#     print(f"Deleted successfully.{d}")
# else:
#     print(f"That key doesn't exist.{d}")


#=================================================================================================


# 8. Write a Python program to map two lists into a dictionary.

keys = ['name', 'age', 'job']
values = ['John', 25, 'Developer']

# Map the two lists into a dictionary
my_dict = dict(zip(keys, values))

print(my_dict)
# Output: {'name': 'John', 'age': 25, 'job': 'Developer'}

#====================================================================================================


# 9. Write a Python program to remove duplicates(based on values) from
# Dictionary.

d = {101: 'apple', 102: 'banana', 103: 'apple', 104: 'cherry', 105: 'banana'}

result = {}
seen_values = set()

for key, value in d.items():
    if value not in seen_values:
        result[key] = value
        seen_values.add(value)

print(result)
# Output: {101: 'apple', 102: 'banana', 104: 'cherry'}

#=========================================================================================
# 10. Write a Python program to check a dictionary is empty or not.

my_dict = {}

if my_dict == {}:
    print("It is empty")


#==========================================================================================


# 11. Write a Python program to combine two dictionary adding values for
# common keys.
# d1 = {&#39;a&#39;: 100, &#39;b&#39;: 200, &#39;c&#39;:300}
# d2 = {&#39;a&#39;: 300, &#39;b&#39;: 200, &#39;d&#39;:400}
# Sample output: {&#39;a&#39;: 400, &#39;b&#39;: 400, &#39;d&#39;: 400, &#39;c&#39;: 300}


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Start with a copy of d1
result = d1.copy()

# Loop through d2 and add values to result
for key, value in d2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)

#=================================================================================================

# 12. Write a Python program to print a dictionary in table format.


d = {103: 'sanju', 101: 'sonu', 104: 'virat', 102: 'monu'}

print("ID\tName")
print("-" * 15) # Adds a small underline for the header

for key, value in d.items():
    print(f"{key}\t{value}")




























#13





shop_data = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

# 1. Create a list of tuples like [(45.5, 'item1'), (35, 'item2')...]
items_list = []
for key, val in shop_data.items():
    items_list.append((val, key))

# 2. Sort the list (it sorts by the first element of the tuple by default)
# reverse=True puts the highest numbers at the top
sorted_list = sorted(items_list, reverse=True)

# 3. Print the top 3
for i in range(3):
    val, key = sorted_list[i]
    print(f"{key} {val}")


#===============================================================================================
#14


x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

# Loop through keys of the first dictionary
for key, value in x.items():
    # Check if the key exists in y AND the value matches
    if key in y and y[key] == value:
        print(f"{key}: {value} is present in both x and y")
