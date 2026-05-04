# UNPACKING OF ITERABLE
# STORING VALUES INTO SEPARATE VARIABLES WITHOUT USING INDEXING OR ITERATION

#BASIC SYNTAX
li=[10,20,30,40]  # PACKINF STORED IN A CONTAINER
a,b,c,d=li  # UNPACKING OF ITERABLE

# WITH STAR EXPRESSION
li=[10,20,30,40,50,60]
a,*b=li
print(li)
print(a)  # 10
print(b)  # [20, 30, 40, 50, 60]

# SO HERE FIRST VALUE IS ASSIGNED TO A AND REST OF THE VALUES ARE UNPACKED TO B IN THE FORM OF A LIST

#===========================================================================================

s={10,20,30,40,50,60}
a,n,*b=s
print(s)
print(a)  # 10
print(b)  # [20, 30, 40, 50, 60
print(n)  # 30

#=============================================================================================


k={10,20,30,40,50,60}
a,*b,c=k
print(k)
print(a)  # 10
print(b)  # [20, 30, 40, 50]
print(c)  # 60

#=============================================================================================

# WHY PERFORMED LIST BECAUSE SET IS UNORDERED AND UNINDEXED SO IT CAN'T ASSIGN THE VALUES TO VARIABLES IN THE ORDER OF THE SET

# [10,20,30,40,50,60]  # THIS IS THE ORDER OF THE VALUES IN THE SET
# SETS DON'T HOLD DUPLICATE VALUES
# TUPLE ARE IMMUTABLE. SO? HOW YOU PERFORM FUNCTIONS ON IT
# USE?
# PARALLEL ITERATION
# FUNCTION PROGRAMMING

# PARALLEL ITERATION
# {ZIP K SATH LOOP}

roll= [1,2,3]
marks= [90,80,70]
names= ["bharti", "sneha", "priya"]

for tuple in zip(roll, marks, names):
    print(tuple[0],tuple[1],tuple[2])

# NOW WE WILL UNPACK BY GIVING NAME VALUE TO THE VARIABLES
for r,m,n in zip(roll, marks, names):
    print(r,m,n, sep="-\t-", end="\n\n") 


# print("Roll","Name","Marks", sep="---\t---", end="\n\n")
# for r,m,n in zip(roll, marks, names):
#     print(r,m,n, sep="---\t---", end="\n\n")
