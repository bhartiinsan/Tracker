
#4. WAP to find the greatest of three numbers entered through keyboard 


A= int(input(" Enter A:  "))
B= int(input("Enter B:  "))
C= int(input(" Enter C:  "))

if A<0 :
    print(" A IS A NEGATIVE INTEGER")
elif A==B==C :
    print(" ALL ARE SAME")
elif A==B:
    print(" A AND B ARE SAME")
elif B==C:
    print(" B AND C ARE SAME")
elif C==A:
    print(" C AND A ARE SAME")
if A>B and A>C:
    print(" A is greatest")
elif B>C and B>A:
    print(" B IS GREATEST")
else:
    print(" C IS GREATEST")

# if elif are used to check multiple conditions. If the first condition is true, the rest of the conditions are not checked. 
# If the first condition is false, the next condition is checked, and so on. 
# This allows for more efficient code, as it avoids unnecessary checks once a true condition is found. 
    