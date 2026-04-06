#DICTINOERY
#MUTUABLE
#INDEX WHEREEVER WE WANT TO START
# KEY- PROGRAMMER PROVIDABLE
#VALUE -KEY (ITEM 1)
# D={}

D={101:"SONU", 102:'MONU', 103:"SANJU"}

# D={}  # EMPTY CURLY BRACES IS DICT
# print(type(D),D)

# UNORDERED 3.5 SE PEHLE
# NOW IT IS ORDERED
#THERE IS NO INDEXING 
# KEYS ARE IMMUTABLE= TUPLE,INT, KEY, FLOAT

print(D[102])
#.GET METHOD
print(D.get(103))
print(D.get(104,"key not found"))


#====================================================================================================================
#IT SEACHES ONLY KEY
print(101 in D)
# print("sanju" in D) # ERROR

# IT SEARCHES ON VALUES
print('SANJU' in D.values())

#MIN
print(min(D))

#MAX
print(max(D))

#SORTED
print(sorted(D))

#not run
#SUM
print(sum(D))
# print(sum(D.values()))

#LEN
print(len(D))
print(len(D.values()))


#=====================================================================================





