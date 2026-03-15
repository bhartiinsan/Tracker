# a =3
# a*= 2
# print(a)
# print (int(a)+5)

#---------------------------------------------------------------------------------------------------------------------------

# a ="3"
# a*= 2
# print(a)
# print (int(a)+5)

#=-----------------------------------------------------------------------------------------------------------------------------
# s= "pizza"
# s= s.replace("z", "s")
# print(s)

# Here's what's happening step by step:

# s = "pizza" — the string "pizza" is assigned to the variable s.
# s = s.replace("z", "s") — the .replace() method finds every occurrence of "z" in s and swaps it for "s". Since "pizza" has two z's, both get replaced.
# print(s) — prints the result.

#-------------------------------------------------------------------------------------------------------------------------

# cities=["Toronto", "New York", "Delhi "]
# print(max(cities))

# Here's the core idea: Python doesn't "know" that Toronto is a bigger city — it just looks at the first character of each string and compares their ASCII values (the universal numeric codes assigned to every character).

# 'T' → 84
# 'N' → 78
# 'D' → 68

#---------------------------------------------------------------------------------------------------------------------------

# food= " ice cream"
# food = food.replace("cream", "")
# print(food)

# Here's what happens step by step:

# food = " ice cream" — the string " ice cream" is assigned (note the leading space at the start).
# food = food.replace("cream", "") — replaces "cream" with "" (nothing), effectively deleting it.
# print(food) — prints the result.

#------------------------------------------------------------------------------------------------------------------------------

# food = "tacos"
# print(food[1:4])  # aco , prints 1 to 4 index


#=-----------------------------------------------------------------------------------------------------------------------------

# s= "Puerto Rico"
# print(s[2:7]) #erto


#------------------------------------------------------------------------------------------------------------------------------

# for i in range(5,1,-1):     #5432 in column and 1 will be excluded
#     print(i)


#------------------------------------------------------------------------------------------------------------------------------

# total = 1
# for i in range (1,4):
#     total=total*i
# print(total)


# Output: 6
# Key things to notice:

# range(1, 4) gives 1, 2, 3 — the 4 is excluded (range stops before the end value)
# total starts at 1 and gets multiplied by each i in turn
# The loop is secretly computing 3 factorial → 1 × 2 × 3 = 6

# If you changed total = 1 to total = 0, the answer would be 0 forever — because anything multiplied by 0 stays 0!

#-------------------------------------------------------------------------------------------------------------------

# nums= [1,2,3]
# nums.append([4, 5])
# print(len(nums))


# Output: 4 — not 5, which surprises most beginners!
# Here's the key distinction:
# .append(x) — drops x in as a single item, no matter what x is. Pass it a list, and that whole list becomes one element sitting inside your list. Think of it as dropping a bag inside another bag.
# .extend(x) — opens x up and adds each item individually. It's like emptying the bag and putting each item in separately.
# Quick cheat sheet:
# pythonnums = [1, 2, 3]

# nums.append([4, 5])   # → [1, 2, 3, [4, 5]]   len = 4
# nums.extend([4, 5])   # → [1, 2, 3, 4, 5]      len = 5
# nums.append(4)        # → [1, 2, 3, 4]          len = 4  (same result as extend here)


#----------------------------------------------------------------------------------------------------------------------

# for i in range(2,6,2):
#     print(i)               #2,4

#-------------------------------------------------------------------------------------------------------------------

# i=0
# while i<5:
#     i+=1
#     if i==3:
#         continue
#     print(i)        #1,2,3,4,5