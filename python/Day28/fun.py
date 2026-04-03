# SET FUN
s= set()
print(s)

s=set("bharat")
print(s)
#{'r', 'h', 'a', 't', 'b'}

s=set(range(1,11))
print(s)

#================================================================================================

#SET FROM LIST
s=set([10,20,30,40])
print(s)
#{40, 10, 20, 30}


#SET FROM TUPLE
s=set((90,20,30,440))
print(s)
#{440, 90, 20, 30}

#================================================================================================================

# QUESTION TAKE INPUT FROM THE USER AND MAKE SET

# DECLARE EMPTY SET
# s=set()

# for i in range(3):
#     v=int(input(" Enter the input"))
#     s.add(v)
# print(s)

#==================================================================================================================


#NOW WE ARE EXPLORING DICTINORARY COMPREHENSION
s= {int(input(" Enter the input"))for i in range(3)}
print(s)

# USING TERNARY OPERATION