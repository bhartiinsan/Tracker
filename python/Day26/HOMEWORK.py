# 1. Sum all items in a list
li = [10, 12, 5, 7, 20, 5]
total = 0
for i in li:
    total += i
print("Sum:", total)


# 2. Largest number from a list
li = [10, 12, 5, 7, 20, 5]
largest = li[0]
for i in li:
    if i > largest:
        largest = i
print("Largest:", largest)


# 3. Count strings with length >= 2 and first == last character
li = ['abc', 'xyz', 'aba', '1221', 'a']
count = 0
for i in li:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
print("Count:", count)


# 4. Get unique values from a list
li = [10, 12, 5, 7, 20, 5, 10, 12]
li2 = []
for i in li:
    if i not in li2:
        li2.append(i)
print("Unique:", li2)


# 5. Check if list is empty or not
a = []
if len(a) == 0:
    print("Empty list")
else:
    print("Not empty")


# 6. Remove 0th, 4th and 5th elements
li = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
li2 = []
remove = [0, 4, 5]
for i in range(len(li)):
    if i not in remove:
        li2.append(li[i])
print("After removing:", li2)


# 7. Remove even numbers from list
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li2 = []
for i in li:
    if i % 2 != 0:
        li2.append(i)
print("Odd numbers:", li2)


# 8. Convert list of characters into a string
li = ['P', 'y', 't', 'h', 'o', 'n']
s = ""
for i in li:
    s += i
print("String:", s)


# 9. Second largest number in a list
li = [10, 20, 5, 8, 15]
largest = li[0]
for i in li:
    if i > largest:
        largest = i

second = li[0]
for i in li:
    if i > second and i != largest:
        second = i
print("Second Largest:", second)


# 10. Average of min and max values
li = [1, 4, 2, 7, 19, 17]
smallest = li[0]
largest = li[0]
for i in li:
    if i < smallest:
        smallest = i
    if i > largest:
        largest = i
avg = (smallest + largest) / 2
print("Average of min & max:", avg)


# **Output:**
# ```
# Sum: 59
# Largest: 20
# Count: 2
# Unique: [10, 12, 5, 7, 20]
# Empty list
# After removing: ['Green', 'White', 'Black']
# Odd numbers: [1, 3, 5, 7, 9]
# String: Python
# Second Largest: 15
# Average of min & max: 10.0