# list()
# li=list()
# print(li)

# # string and range are iterable in python
# li=list(range(1,101))
# print(li)

# li=list("python")
# print(li)


# creating list in one more method
# list comprehension-- concise way to create a list using expression

#li=[expression for]

# li=[i*i for i in range(1,5)] # for same number multiplication
# print(li)

# # without  comprehension

# li=[]
# for i in range(1,5):
#     li.append(i*i)
# print(i,li)

#====================================================================
# creating list taking input 4 times and appending into a list

# li=[input(" enter name= ") for i in range(4)]
# print(li)


#=====================================================================

#CAN USE TERNARY EXPRESSION
#li=[true_exp if condition else false_exp for]

# li=[21,10,20,33,44,8,7,5]
# print(li)
# li2=[f"{i}even" if i%2==0 else f"{i}odd" for i in li]
# print(li2)

#========================================================================
# # 1- for condition than if condition chalega
# li=[21,10,20,33,44,8,7,5]
# print(li)

# li2=[i for i in li if i%2==0]
# print(li2)

#=========================================================================

#li[expression for for for .............]

# li=[i*j for i in range(1,3) for j in range(1,3)]
# print(li)

# #without compare
# li=[]
# for i in range (1,3):
#         for j in range(1,3):
#             li.append(i*j)
# print(li)


# NESTED LIST

# li=[10,20,[30,40,50]]
# print(li)
# print(li[-1])
# print(li[-1][0])

#==================================================
# how this processing

# li=[10,20,[30,40,50]]
# for i in range (1,3):
#         for j in range(1,3):
#             li.append(i*j)
# print(li)

#=====================================================

# students=[[1,"sonu", 20],[2,"monu",18]]

# for i in range(2):
#     r=int(input(" Enter roll number "))
#     n=(input(" Enter name "))
#     a=int(input(" Enter age  "))

#     sl=[r,a,n]
#     students.append(sl)


# print("roll","name", "age",sep="\t")
# for s in students:
#       for i in s:
#             print(i,end="\t")
#             print()

#=====================================================


# SHALLOW COPY AND DEEP COPY
# REPLICATION OF THAT COPY

li=[10,20,[30,40]]
import copy
shallow_li=copy.copy(li)  # SHALLLOW COPY
deep_li=copy.deepcopy(li)       #DEEP COPY

print(li)
print(shallow_li)
print(deep_li)

li[-1][0]=31

print(li)
print(shallow_li)
print(deep_li)




