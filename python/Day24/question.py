# create a list of 3 values from the user input
# li=[]

# for i in range(0,3):
# #      k= int(input("enter value="))
# #      li.append(k)
# # print(li)

#     # print(f" {you.append} ',{ li.append[]}")

# #==============================================================================

# #LIST SEARCHING
# li=[10,20,30,40,50]
# # FOR SEARCHING YOU CAN USE MEMBERSHIP OPERATOR
# print(20 in li)
# print(200 in li)


# #===============================================================================

# #REMOVE A LIST VALUE
# li.remove(20)
# print(li)

# li.remove(10)
#=============================================================================


# li=[10,20,30,40,50]

# values=[20,25,30,35]
# for v in values:
#     if v in li:
#         li.remove(v)
#         print(f"{v} removed from list")
# print(li)


#==============================================================================

li=[5,8,10,20,10,30,40,10,50,10,22,10]
print(li)
li.remove(10)
print(li)

#===============================================================================

# remove of occurence of 10 values in list
# you don't haved to use [append, insert, remove]
# don't manipulate it



# WRONG APPROACH
# li=[5,8,10,20,10,30,40,10,50,10,22,10]
# count=10
# for values in count:
#     if values==10:
#         print(f" {li.remove(10)}")
#     count+=1
# print(li)

#==================================================================================

li=[5,8,10,20,10,30,40,10,50,10,22,10,10,10]
print(li)
while 10 in li:
    li.remove(10)
print(li)


#====================================================================================