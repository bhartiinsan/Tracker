

#1. An Integer is Input through keyboard. Write a program to find whether it is odd or even number.

Num = int(input("Enter the number : ")) 
if Num<0:
    print (" This is a negative number")   
elif Num%2 ==0:
    print ("this is an even number")
else:
    print(" this is an odd number")








#2. If cost price and selling price of an item is input through keyboard. Write a program to check profit or loss.

# Profit = SELLING PRICE – COST PRICE
# Loss = COST PRICE – SELLING PRICE


SP = int(input("Enter the selling cost"))
CP = int(input("Enter the Cost Price of product"))

if SP>CP:
    print(" You are having profit")
elif CP>SP:
    print(" You are having Loss ")
else:
    print("no profit no loss")









    
#3. WAP to test a whether a number is divisible by 3 or 5 or both.


num = int(input(" Enter the number:"))

if num<0:                                             # nested loop
    print ("The non-negative number are not allowed")
    num= abs(num)  # abs value no negative sign

elif num%3 ==0 and num%5==0:
    print(" The number is divisible by 3 and 5")

elif num % 3 == 0:
    print("Number is divisible by 3")

elif num % 5 == 0:
    print("Number is divisible by 5")

else:
    print("Number is NOT divisible by 3 or 5")













#4. WAP to find the greatest of three numbers entered through keyboard 


A= int(input(" Enter A"))
B= int(input("Enter B"))
C= int(input(" Enter C"))

if A<0 or B<0 or C<0 :
    print(" Non - negative integers")
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









































#5. The marks obtain by a student in 5 different subjects are input through keyboard. The student gets the division as per the following
#rules:  Percentage above or equal to 60- first division
#Percentage between 50 and 59- second division
#Percentage between 40 and 49 – third division
#Percentage below 40- fails.
'''

Marks1= int(input(" Enter subject 1"))
Marks2 =int(input(" Enter subject 2"))
Marks3 =int(input(" Enter subject 3"))
Marks4 =int(input(" Enter subject 4"))
Marks5 = int(input(" Enter subject 5"))


sum=Marks1+Marks2+Marks3+Marks4+Marks5

percentage=(sum / 500) * 100

if percentage>=0 and percentage<=40:
    print("FAIL")
elif percentage>40 and percentage<50:
    print(" THIRD DIVISION")
elif percentage>50 and percentage<60:
    print(" SECOND DIVISION")
elif percentage>60 and percentage >= 100:
    print(" FIRST DIVISION")
else:
    (" thankyou")

'''''




