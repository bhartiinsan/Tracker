
#6. Write a program that has following menu:
#Enter 1 to find the area of rectangle.
#Enter 2 to find the area of circle.
#Values for length and width of a rectangle and value of a radius of
#circle will be entered through keyboard.    




output= int(input("PRESS 1 to print rectangle   \n PRESS 2  for circle area   "))
if output is 1:
        L= int(input(" Enter the lenght"))    # output==1
        B =int(input("Enter the breadth"))
        area= (L*B)
        print("Area of rectangle is",area)
elif output is 2:
        R= int(input("Enter the radiuus"))
        P= 3.14*R*R
        print("Area of circle is", P)
else:
        print(" print a valid number")