# WE CAN MAKE TUPLE BY USING TUPLE FUNCTION
t=tuple()
print(t) # empty tuple

t= tuple(range(1,11))
print(t)   # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#=======================================================================================
# We also create tuple function by putting string function in it
t=tuple(" python ")
print(t)

#========================================================================================

li= [10,20,30]
t=tuple(li)
print(t) #(10, 20, 30)

li[-1]=40

print(li) #[10, 20, 40] it will change
print(t)  #(10, 20, 30) no change

#++++++++=====================================================================================

t=((1,2,3),[1,2,3])
print(t)

print(t[1])  #[1, 2, 3]

t[1].append(4)
print(t)  #((1, 2, 3), [1, 2, 3, 4])

# WE CAN CHANGE IN LIST THAT IS IN THE TUPLE
# BUT WE CAN'T REPLACE THE WHOLE LIST, CAUSE IT CONSIDER AS A CHANGE IN TUPLE

print(t[1][1]) #2

#==============================================================================================

# DIFFERENCE BETWEEN THE LIST AND TUPLE

# LIST
#1. MUTUABLE
# MEMORY USAGE HIGH
# SLOW ITERATION
# CAUSE IT DOESN'T STORE IT'S VALUES DIRECTLY INTO MEMORY BUT IT ALLOCATE MEMORY ADDRESS TO OTHER TO POINT OUT

#TUPLE
#1. IMMUTABLE
# MEMORY USAGE LOW
# FAST ITERATION
#IT STORES VALUES DIRECTLY INTO THE MEMORY BLOCK


#====================================================================================================

# EXAMPLE
t=(10,20,30,40)
li=[10,20,30,40]

import sys
print(sys.getsizeof(li)) #88
print(sys.getsizeof(t))  #72