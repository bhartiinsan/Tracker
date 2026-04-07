# CREATE A DICT WITH 3 ITEMS, WHERE KEY IS ROLL(INT) AND VALUE IS NAME (STRING)

# TAKE KEYS AND VALUES FROM USER

#PSEUDO CODE

# d={}
# for i in range(3):
#     key=int(input(" ENTER THE KEY"))
#     value=input(" ENTER THE VALUE")
#     d[key] =value
# print(d)


#=========================================================================

# DICT FUNCTIN TO CREATE DIC
d=dict()
print(d)

# list/iterable of tuples, len is 2

d=dict([(1,"sonu"),(2,"monu"),(3,"sanju")])
print(d)

d2={3:"virat",4:"rohit"}
print(d2)

#COMBINING 3RD DIC USING COMBINING D,D2
d3=d|d2
print(d3)

#SANJU UPDATED VALUE AYEGI(UPDATED VALUE AYEGI)
#============================================================
d3=d2|d
print(d3)

#VRAT

#=====================================
#PEHLI WALI DIC UPDATE HOTI H
d.update(d2)
print(d)