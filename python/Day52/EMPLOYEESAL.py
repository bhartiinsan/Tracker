# ## employee salary increase by 5%

# sal=[12000, 15000, 11000, 20000]
# res= list(map(lambda x: x+x*5/100, sal)) 
# print(res)

##===================================================================

phy=[8,9,7,6,10]
chm=[7,7,7,8,9]
maths=[8,8,9,9,10]

res=map(lambda p,c,m: (p+c+m)/3, phy,chm,maths)  # map function me jitne bhi iterables pass karte hain unke corresponding elements ko function me pass karte hain
print(list(res))

