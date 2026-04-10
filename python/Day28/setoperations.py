#SET OPERATIONS
#INTERSECTION

S1= {10,20,30}
S3={30,40,50}

S3=S1.intersection(S3)
print(S3) #{30}

#WE CAN ALSO USE BITWISE OPERATOR
S3= S1 and S3
print(S3)

#======================================================================================================

# UNION 
# MERGE (NO DUPLICACY ALLOWED)

S4=S1.union(S3)
print(S4)

# WE CAN ALSO USE BITWISE OR
S4=S1|S3
print(S4)

#======================================================================================================

#DIFFREENCE

S5=S1.difference(S3)
print(S5)

S6=S3.difference(S1)
print(S6)

# ++/////???


#====================================================================================================

#SYMMETRIC DIFF
# SAME ELEMENT REMOVE

S7=S1.symmetric_difference(S3)
print(S7)

# Bitwise XOR
S7=S1^S3
print(S7)
