# 1. Write a Python program to create a set.

# Create a set
s = set()
s.add("apple")
s.add("banana")
s.add("cherry")
print(s)

# #===============================================================

s = {"apple", "banana", "cherry"}
print(s)

#================================================================



# 2. Write a Python program to iteration over sets.

s = {"apple", "banana", "cherry"}
for i in s:
    print(i)


#==================================================================


# 3. Write a Python program to add member(s) in a set.

s=set()
for i in range(5):
    values=input(" Enter the input :  ")
    s.add(values)
    
print(s)




#====================================================================

# 4. Write a Python program to remove item(s) from set


s = {"apple", "banana", "cherry"}
s.remove("apple")
print(s)







#======================================================================

# # 5. Write a Python program to remove an item from a set if it is present in the set.

s = {"apple", "banana", "cherry", 23, 10}
value=input(" enter the value: ")
value = int(value) if value.isdigit() else value

print(s)
if value in s:
     s.remove(value) 
     print(f"Item removed successfuly {s}")
else:
    print( f" Item is not found in the set {s}")


#==========================================================================






# s = {"apple", "banana", "cherry", 23, 10}

# value = input("Enter the value: ")

# # else we can put all strings to skip this additional step
# if value.isdigit():
#     value = int(value)

# print(s)

# if value in s:
#     s.remove(value)
#     print(f"Item removed successfully {s}")
# else:
#     print(f"Item is not found in the set {s}")


#=====================================================================================================

# 6. Write a Python program to create an intersection of sets.
#INTERSECTION= COMMON VALUES ARE GET ASIDE

s1={10,20,40,50,100}
s2={50,30,22,34,10}

inter= s1.intersection(s2)
print(inter)

# {50, 10}

#=======================================================================================================

# 7. Write a Python program to create a union of sets. 
# IT PRODUCES UNIQUE VALUES FROM THE SET

s1={10,20,40,50,100}
s2={50,30,22,34,10}

uni=s1.union(s2)
print(uni)

# {34, 100, 40, 10, 50, 20, 22, 30}

#========================================================================================

# 8. Write a Python program to create set difference. 
# IT SHOWS VALUE OF #S1 REMOVE DUPLICATE ELEMENTS FROM S2 (matching)

s1={10,20,40,50,100}
s2={50,30,22,34,10}

diff=s1.difference(s2)
print(diff)

# {40, 100, 20}
#========================================================================================
# IT SHOWS VALUE OF #S2 REMOVE DUPLICATE ELEMENTS FROM S1 (matching)

# s1={10,20,40,50,100}
# s2={50,30,22,34,10}

# diff=s2.difference(s1)
# print(diff)

# {34, 22, 30}

#=========================================================================================

# 9. Write a Python program to create a symmetric difference.

# IT REMOVE SAME ELEMENTS FROM THE SET

s1={10,20,40,50,100}
s2={50,30,22,34,10}

symdiff=s1.symmetric_difference(s2)
print(symdiff)

# {34, 100, 20, 22, 40, 30}

#==========================================================================================
# 10. Write a Python program to clear a set.

s1={10,20,40,50,100}
s1.clear()
print(s1)

#===========================================================================================

# 11. Write a Python program to use of frozenset.


s = {1, 2, 3, 4}

f = frozenset(s)
value=int(input(" ENTER THE VALUE"))

print("Frozenset:", f)

if value in f:
    print(f"{value}    is present in frozenset")




#============================================================================




# 12. Write a Python program to find maximum and the minimum value in a set.

s = {10, 5, 30, 2, 50}

maximum = max(s)
minimum = min(s)

print("Maximum value:", maximum)
print("Minimum value:", minimum)


# 13. Write a Python program to find the length of a set

s1={10,20,40,50,100}
length=len(s1)
print(length)

