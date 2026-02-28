#4. WAP to find the greatest of three numbers entered through keyboard 


A= int(input(" Enter A"))
B= int(input("Enter B"))
C= int(input(" Enter C"))

if A<0 :
    print(" A IS A NEGATIVE INTEGER")
if B<0:
    print(" B IS A NEGATIVE INTEGER")
if C<0:
    print(" C IS A NEGATIVE INTEGER")
elif A==B==C :
    print(" ALL ARE SAME")
elif A==B:
    print(" A AND B ARE SAME")
elif B==C:
    print(" B AND C ARE SAME")
elif C==A:
    print(" C AND A ARE SAME")
elif A>B and A>C:
    print(" A is greatest")
elif B>C and B>A:
    print(" B IS GREATEST")
elif C>A and C>B:
    print(" C IS GREATEST")