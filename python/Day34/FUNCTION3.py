#DOCUMENTATION OF THIS FUNCTION, HOW TO USE IT


# help(sorted)

# Help on built-in function sorted in module builtins:                                                           

# sorted(iterable, /, *, key=None, reverse=False)
#     Return a new list containing all items from the iterable in ascending order.

#     A custom key function can be supplied to customize the sort order, and the
#     reverse flag can be set to request the result in descending order.

# sorted(li)

#=================================================================================

# def show():
#     x=10
#     return x
# res=show()
# print(res) --10

# WHOLE PROCESS OF CALLING THE LOCAL VARIABLE
# IT RETURNS X VALUE ---> SHOW()

#==================================================================================
# def arithmetic (a,b):  # a and b are parameters
#     c=a+b
#     d=a*b

#     return c #--> the function c stops here only and returns c
#     return d #--> the function d will not run because we can call one at a time

# res= arithmetic(10,2)
# print(res)

#===============================================================================
 
# def arith(a,b):
#     c=a+b
#     d=a*b

#     return c,d  # RETURN AS A TUPLE
# r=arith(10,23)
# print(r)

# (33, 230) ----> it will take parameters for both in TUPLE FORMAT

#===============================================================================

# def show():  # it will give none , there is no parameter
#     x=10

# res=show()  # calling empty function
# print(res)

#================================================================================

# def sho(a,b):
#     return a+b   # it is directly telling to perform this function

# r=sho(2,4)   #6
# print(r)

# print(sho(10,20)) #30

#=================================================================================

def fun():
    print("hi")

x= fun()
print(x)   # none --> no parameter is given and define

#====================================================================================