
#DEFINE AND CALL

#logic fun
# def add():
#     a=2
#     b=3
#     print(a+b)

# def mul():
#     f=2
#     g=4
#     print(f*g)

# add()
# mul()
# #memory will produce when it is run (local variable)


#===============================================================

#declare global varibale
# a=2
# b=3
# def add():
#         print(a+b)

# def mul():
#         print(a*b)

# add()
# mul()

#================================================================

# priority goes to local when declare


# a=2
# b=3
# def add():
#         a=4
#         b=5
#         print(a+b)

# def mul():
#         print(a*b)

# add()
# mul()


#======================================
# DECLARATION GLOBAL VARIABLE IN LOCAL 
a=2
b=3
def add():
        global a,b
        a=4
        b=5
        print(a+b)

def mul():
        print(a*b)

print(a,b)
#add()  if we do this then we get 2, 3
mul()
print(a,b)

# else first it print 2,3 and after calling add fun where global variable is declared it become 4,5

#====================================================================================================


