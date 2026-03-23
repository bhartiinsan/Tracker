# Scalar datatypes- one value at atime(strng ,int, float, complex, st5r, bool)
# Container datatypes- 0-N values at a time(multiple value)(list, tuple, set, dictinoery, frozenset)
#THESE ARE DYNAMIC  DEPENDS ON RAM 
#DYNAMIC IN SIZE
#OOPS 

#LIST DATATYPE
# []- 
#[V1,V2,V3]

# PREFIX[INDEX]
#PREFIX[:]-  SUBSCRIPT

# LI= []
# print(type(LI))
# print(LI)
# IT STORES DUPLICATE VALUES
#ORDER PRESERVe
# value, elements, items, objects
# container and scalar ka hissa hota hai
LI= [12000,10000,15000,20000,11000,12000]
# print(LI)
# print(LI[-1])
# print(LI[:-1])
# print(len(LI))


# it is iterable
# for values in LI:
#     print(values) 

# for values in str


#SUM FUNCTION
# res=sum(LI)
# print(res)

# #MIN FUNCTION
# res=min(LI)
# print(res)

# #MAX FUNCTION
# res=max(LI)
# print(res)
# # print(max(LI))

# res=(LI)
# print(res)



#------------------------------------------------------------------

# #SUM FUNCTION
# res=sum(LI)
# print(res)

# avg= print(f"(values/res)")

print(sorted(LI))

# AVERAGE
# avg=sum(LI)/len(LI)
# print(avg)
# print(round,(avg,2))
# print(f"{avg:.2f}")

#SORTED()
asc_LI= sorted(LI,reverse=True)
print(asc_LI)





