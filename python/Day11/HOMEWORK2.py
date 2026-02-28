#5. The marks obtain by a student in 5 different subjects are input through keyboard. The student gets the division as per the following
#rules:  Percentage above or equal to 60- first division
#Percentage between 50 and 59- second division
#Percentage between 40 and 49 – third division
#Percentage below 40- fails.



marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))
marks4 = int(input("Enter marks of subject 4: "))
marks5 = int(input("Enter marks of subject 5: "))


total = marks1 + marks2 + marks3 + marks4 + marks5

percentage = (total / 500) * 100

if percentage >= 60:
    print("First Division ")

elif percentage >= 50:
    print("Second Division ")

elif percentage >= 40:
    print("Third Division ")

else:
    print(" You have failed ")



#6. Write a program that has following menu:
#Enter 1 to find the area of rectangle.
#Enter 2 to find the area of circle.
#Values for length and width of a rectangle and value of a radius of
#circle will be entered through keyboard.    




output= int(input("PRESS 1 to print rectangle \n PRESS 2  for circle area"))
if output is 1:
        L= int(input(" Enter the lenght"))
        B =int(input("Enter the breadth"))
        area= (L*B)
        print("Area of rectangle is",area)
elif output is 2:
        R= int(input("Enter the radiuus"))
        P= 3.14*R*R
        print("Area of circle is", P)
else:
        print(" print a valid number")








#7. Write a program that has following menu:

# Enter 1 to find out whether the entered number is even or odd.
# Enter 2 to find out whether the entered number is positive or negative.


Num = float(input("Enter the number : "))

Output= int(input(" Press 1 to know whether the number is even or odd \n" 
" Press 2 to know whether the number is positive or negative"))
if Num<=0:
    print("The number is negative")
elif Num%2!=0:
    print("The number is Odd")
elif Num%2 ==0:
    print("The number is Even and positive ")
else:
    print(" Enter the valid number")








#8. WAP that implements the simple calculator that has following menu:
#Enter 1 to find the True division of 2 numbers.
#Enter 2 to find the square of a number.
#Enter 3 to find the cube of a number.

Output= int(input(" PRESS 1 FOR TRUE DIVISION \n PRESS 2 FOR SQUARE OF NUMBER \n PRESS 3 FOR CUBE OF A NUMBER"))
if Output is 1:
    num1= int(input(" ENTER THE FIRST NUMBER"))
    num2= int(input("ENTER THE SECOND NUMBER"))
    FLOOR= (num1/num2)
    print(" This is a true division of a number", FLOOR)
elif Output is 2:
    R = int(input("ENTER THE NUMBER"))
    area= R*R
    print(" This is square of a given number" , area)
elif Output is 3:
    C= int(input(" ENTER THE NUMBER"))
    cube= C*C*C
    print("This is a cube of given number", cube)
