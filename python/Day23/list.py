LI= [12000,10000,15000,20000,11000,12000]

#SORTED()
desc_LI= sorted(LI,reverse=True)
print(desc_LI)



#=========================================================
# it is heterogeneous
# li=[20,10,'hi']
# print(li)
# print(len(li))
# print(sum(li))
# print(min(li))
# print(max(li))
# print(sorted(li))

# HETEROGENEOUS WITH COMPARABLE ITEMS
li=[10,20,10.5]
print(sum(li))
print(min(li))
print(max(li))
print(sorted(li))

# STRING CAN'T BE SUM
# ARRAY IS IN JAVA , C, C++
# HOMOGENEOUS WITH SAME DATATYPE

li=[10,20,30]
li=[2.1, 4.5, 6.7]
li=['sonu','monu']

# python is not type safe langauge

# list concatenation (merge)
a=[10,20]
b=[11,22,33,44]
c=a+b
print(c)
d=a*3+b
print(d)

print(c*3)
print(c*1000)

print([10000]*100)




