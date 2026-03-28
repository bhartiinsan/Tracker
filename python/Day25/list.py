# li=[5,8,10,20,10,30,40,10,50,10,22,10,10,10]
# frq= li.count(10)

# for i in range(frq):
#     li.remove(10)
# print(li)

#===========================================================
# remove value by index

li=[5,8,10,20,10,30,40,10,50,10,22,10,10,10]
print(li)

del li[1] #8 got remove
print(li)

#============================================================
# IT WILL SHOW THE DELETE VALUE
del li[:3] #0,1,2
print(li)

value=li.pop(0)
print(li,value)


value=li.pop(-1)  # IT IS THE BY DEFAULT VALUE

#=======================================================================

#DEL        AND                      POP DIFF

# KEYWORD                            METHOD
#DOES NOT SUPPORT DEFAULT VALUE         -1
# DOES NOT RETURN DEFAULT VALUE        YES
# SLICING                               NO


#=======================================================================

# REMOVE ALL  VALUES

li.clear()
print(li)




