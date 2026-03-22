# 1.	Take three sides and check if they form a valid triangle.

# side1=int(input(" Enter the number 1:  "))
# side2= int(input("Enter the number 2:  "))
# side3= int(input("Enter the number 3:  "))

# CON1=side1+side2>side3
# CON2=side1+side3>side2
# CON3=side2+side3>side1

# if CON1 or CON2 or CON3 is True:
#      print(" IT IS VALID FOR A TRIANGLE ")

# else: print(" IT IS NOT VALID FOR TRIANGLE")

#---------------------------------------------------------------------------------------

# 2. If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene.

# Equilateral: All three sides are equal (A=B=C)
# Isosceles: Exactly two sides are equal (A=B OR B=C OR C=A)
# Scalene: No sides are equal (A!=B!=C)


# A =int(input(" Enter the SIDE 1:  "))
# B = int(input("Enter the SIDE 2:  "))
# C = int(input("Enter the SIDE 3:  "))

# if A==B==C:
#     print("IT IS A EQUILATERAL TRIANGLE")
# elif A==B or B==C or C==A:
#     print(" IT IS A ISOSCELES TRIANGLE ")
# else: print(" IT IS A SCALENE TRIANGLE")

#==================================================================================

# 3.	Take marks (0–100) and print the corresponding grade (A/B/C/D/F).

# A (90–100): Exceptional.
# B (80–89): Very Good.
# C (70–79): Good.
# D (60–69): Pass.
# F (Below 60): Fail
# DON'T ALLOW NEGATIVE MARKS ENTERING

marks=float(input(" Enter the marks "))
if marks<60:
    print("fail")
elif marks>=60 and marks<70:
    print(" YOU ARE HAVING GRADE D")
elif marks>=70 :
    print("YOU ARE HAVING GRADE C")
elif marks<90:
    print(" YOU ARE HAVING GRADE B")
elif marks<=100:
    print(" YOU ARE HAVING GRADE A")
else:
    print(" NEGATIVE NUMBER ARE NOT ALLOWED")


#==============================================================================================

# 4.	Check if one of two given numbers is a multiple of the other.


#  Is num1/num2 giving a 0 remainder?
#  Is num2/num1 giving a 0 remainder?

num1= int(input(" Enter the number "))
num2= int(input(" Enter the number "))

if num1%num2==0 and num2%num1==0:
    print(" THEY ARE MULTIPLE OF EACH OTHER")
else:
    print(" THEY ARE NOT MULTIPLES OF EACH OTHER")

#=================================================================================================

# 5.	Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night”.
