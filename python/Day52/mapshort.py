li=[1,2,3,4,5,6,7,8,9,10]

res= list(map(lambda x: x**2,li))
print(res)

res= list(map(lambda x: x**3,li))
print(res)

# IF WE DO WITHOUT LIST THEN IT WILL RETURN MAP OBJECT WHICH IS AN ITERABLE
res= map(lambda x: x**2,li)
print(res)  # <map object at 0x0000021B8C8F3A30>


##==========================================================================
# ALSO WE CAN CONVERT INTO TUPLE OR SET OR DICTIONARY
res= tuple(map(lambda x: x**2,li))
print(res)


res= set(map(lambda x: x**2,li))
print(res)
# set me duplicate values ko store nhi krta hai isliye 1 aur 9 ek hi baar print honge


res= dict(map(lambda x: (x,x**2),li))  # dictionary me
# hum key value pair ko tuple ke form me pass karte hain
print(res)


#======================================================
# ONE THING TO REM
res=map(lambda x: x**2,li)
print(list(res))  # map object ko list me convert karne ke baad hi hum uske elements ko access kar sakte hain
print(tuple(res))  # EMPTY TUPLE BECAUSE MAP OBJECT KO HUM NE PEHLE LIST ME CONVERT KAR LIYA HAI ISLIYE AB MAP OBJECT EMPTY HO CHUKA HAI



#==========================================================================
# MAP FUNCTION ME HUM EK SE JYADA ITERABLES BHI PASS KAR SAKTE HAIN
li1=[1,2,3,4,5]
li2=[6,7,8,9,10]
res= list(map(lambda x,y: x+y,li1,li2))  # map function me jitne bhi iterables pass karte hain unke corresponding elements ko function me pass karte hain
print(res)


# FLOW DIAGRAM OF MAP FUNCTION

# MAP== ADDRESS OF FUNCTION
# MAP== ADDRESS OF ITERABLE