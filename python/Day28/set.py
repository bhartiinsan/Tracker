#SET 
# UNIQUE VALUES GET STORED
# UNORDERED STORED/MANAGED VALUE OF SET (BY DEFAULT)

#UNORDERED MUTUABLE COLLECTION OF UNIQUE VALUES
#{} - SYMBOL

s={10,20,10,3.5,-5,"hi"} # memory save cause no redundancy allowed
print(s)


print(len(s))

#MIN()
# print(min(s))  # it will not work in hetrogeneous datatypes

# #MAX()
# print(max(s))  # it will not work in hetrogeneous datatypes

# #SUM()
# print(sum(s))   # it will not work in hetrogeneous datatypes

# #SORTED()
# print(sorted(s))   # it will not work in hetrogeneous datatypes

#IN
print(23 in s)

#remove
print(s.remove(10))  # none -------why??
print(s)

#=======================================================================

# We can't do subscripting--- finding index, perform slicing
# ITERABLE
# for i in s:
    # print(i)

# print(s[0]) # it will not run

# LEN()
# # LEN FUN IS RUN ON ITERABLE DATATYPE
# s= {10,20,30}
# print(len(s))

# #MIN()
# print(min(s))

# #MAX()
# print(max(s))

# #SUM()
# print(sum(s))

# #SORTED()
# print(sorted(s))

# #IN
# print(23 in s)



#=====================================================================================
#RULES THAT ELEMENT CAN BE IN SET
# SUPPORTS IMMUTABLE VALUES
# WHO COME INTO THAT CATEGORY-- INT, FLOAT, STRING, BOOLEAN, TUPLE
# SO NO LIST CAN BE STORED CAUSE IT IS MUTABLE 

s= {10, 3.4, "bharti", False, ()}
print(s)

#======================================================================================

# MUTUABLE {RUN KRTE WAQT BADLNA}
s={10,20,30}
print(s)

#FOR ADDING ELEMENT (IT ADDS IN THE ARBITARY POSITION , CAUSE OF HASING)
s.add(60)
print(s)

#POP()   (KOI BHI RANDOM VALUE DELETE KARDEGA)
s.pop()
print(s)

#remove
s.remove(60)
print(s)

#Clear
s.clear()
print(s)

