
# #ITERATE DIC VALUES AND KEYS
# D={101:"SONU", 102:'MONU', 103:"SANJU"}

# for i in D:
#     print(i)

# for i in D.keys():
#     print(i)

# #===================================
# #values

# for i in D.values():
#     print(i)


# #===================================
# for i,k in D.items():
#     print(i,k)

# #IT GIVES TUPLE


#====================================

# #THE LAST VALUE IS SHOWN
# D={101:"SONU",101:1000,101:"DA", 102:'MONU', 103:"SANJU"}
# print(D)

# D={101:["SONU",20000,"DA"], 102:("MONU",25000,"DS")}
# print(D)
# print(D[101])
# print(D[102])

# D[101][1]= 22000
# print(D[101])


#================================================================

emps={101:{"ename":"sonu","esal":20000,"edept":"DA"},
      102:{"ename":"monu","esal":25000,"edept":"DS"},
       103:{"ename":"sanju","esal":22000,"edept":"AI"},
        }


#================================================================


print(emps[102])
print(emps[103]["edept"])
print(emps[103].get("edept"))


# print(list(emps[103].items()))


print(list[2])
d=emps[103]
i=d.items()
li=list(i)
print(li[2])

#==========================================================

#OUTPUT
# EID, ENAME, ESTATE, ESAL



print(d)
for i in d:
    print ()