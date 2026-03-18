

# for i in range(3):
#     print(i) #0,1,2
#     i=10



# #------------------------------------------------------




# cars = ["Porshe", "BMW", "Audi"]

# trending=[]
# for c in cars:
#     if c=="BMW" or "Porshe":
#         trending.append(c)
# print(trending)

#================================================================



# nums=[10,20,30]
# for i, v in enumerate(nums):
#     nums[i]= v+i
#     print(nums)



#==========================================================

# def foo(x):
#     return x**2
# print(foo(foo(2))) #16


#===========================================================

packages= ["box1", "box2", "box3"]
next_delivery= packages.pop(0)
packages.append("box4")

print(next_delivery)