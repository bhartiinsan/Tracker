
#DIC DATATYPE

D={'A':str, 1: int, 1.5:'float', (): tuple}
#LIST CAN'T USE DIC KEY, SET
print(D)

print(D)

#dict is mutable
d={101:'sonu',102:'monu',200:'virat',201:'rohit'}
print(d)

#add item to last id key does not exist
d[103]='sonu'
print(d)

#update value of item if key exists
d[102]='sanju'
print(d)

#delete item of given key
del d[101]
print(d)

#delete item of given key and also returns it's value
value=d.pop(102)
print(d,value)

#delete last item and returns it's key & value
key,value=d.popitem() #last item
print(d,key,value)

#delete all items
d.clear()
print(d)