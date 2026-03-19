# 1.	Take a number and print whether it’s positive, negative, or zero.
# LOGIC IS IF NUMBER IS GREATER THAN 0 IT IS POSITIVE, LESS THAN 0 IT WILL BE NEGATIVE AND IF EQUALS TO ZERO IS ZERO
# num=int(input(" enter the integer"))
# if num<0:
#     print("this is a negative number")
# elif num>0:
#     print(" This is a positive number")
# else :
#     print(" This is a zero")


#---------------------------------------------------------------------------
# 2. Check if a number is even or odd.
# num=int(input(" enter the integer"))
# if num %2==0:
#     print("The number is even")

# else : print(" The number is odd ")

#----------------------------------------------------------------------------

# 3.	Check if a number is divisible by 5.

# num=int(input(" enter the integer"))
# if num% 5==0:
#     print(" It is divisible by 5")
# else: print(" Not divisible by 5 ")

#------------------------------------------------------------------------------


# 4.	Check if a number is divisible by both 3 and 5.

#LOGIC FIRSTLY CHECK NUMBER IS DIVISIBLE BY BOTH THEN INDIVIDUALLY BY BOTH AND THEN FOR NEGATIVE NUMBER- ENETER A VALID  NUMBER

# num= int(input(" Enter the integer "))
# if num%3==0 and num%5==0:
#     print(" This number is divisible by both 3 and 5")
# elif num% 3== 0:
#     print(" THIS NUMBER IS DIVISIBLE BY 3 ")
# elif num% 5== 0:
#     print(" This is divisible by 5")
# elif (num%3 and num%5) ==0:
#     print(" This number is divisible by both 3 and 5")
# else: print(" Enter a valid number")





#-----------------------------------------------------------------------------------------------------------

# 5.	Check if a given year is a leap year.
#IF USER GIVING 1J445T IS HAVING A VALUEERROR

# LOGIC: 4 AND 400 SE DIVISIBLE. 100 SE NAHI DIVISIBLE HO

# num= int(input(" Enter the integer "))

# if num%100==0 and num%400:
#     print(" This is not a leap year")
# elif num%4==0:
#       print(" This is a leap year")
# else: print(" Enter a valid year")

#--------------------------------------------------------------------------------------------------------------

# 6.	Take two numbers and print the larger one.
# here also we getting the value error

# num1=int(input(" Enter the number 1:  "))
# num2= int(input("Enter the number 2:  "))
# if num1==num2:
#     print(" BOTH ARE EQUAL ")
# elif num1>num2:
#     print(" THE NUM1 IS THE LARGESt")
# elif num1<num2:
#     print(" THE NUM2 IS LARGEST ")
# else: 
#    print(" ENTER A VALID NUMBER")

#--------------------------------------------------------------------------------------------------------------------

# 7.	Take three numbers and print the largest.
#LOGIC : FIRST WE CHECK THAT ALL THREE NUMBERS ARE EQUAL, SECOND WE  check alternatively 2 numbers are greater than second one
# third we check 2 number that they are similar, else print the valid number


num1=int(input(" Enter the number 1:  "))
num2= int(input("Enter the number 2:  "))
num3= int(input("Enter the number 3:  "))


if num1==num2==num3:
    print(" NUMBER1 and NUMBER2 and NUMBER3 are equal")
elif num1 and num2 and num3 <0:
    print("Negative Number ")
elif num1==num2:
    print(" Number 1 and Number 2 are equal ")
elif num2==num3:
    print(" Number2 and Number3 are equal ")
elif num1==num3:
    print("Number1 and Number2 are equal ")
elif num1>num2 and num3:
    print(" NUMBER1 IS GREATER ")
elif num2>num1 and num3:
    print("Number2 IS GREATER ")
elif num3>num2 and num1:
    print("Number3 IS GREATER ")
else: print(" ENTER A VALID NUMBER")

#-----------------------------------------------------------------------------------------------------------------------------

# 8.	Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.

# LOGIC =
# Cold: Less than 15°C 
# Warm: Between 15°C and 30°C (inclusive) 
# Hot: Greater than 30°C 


# Why This Works
# ConditionRange Coveredtemp < 15Below 15°C → Coldtemp <= 3015°C to 30°C → Warm (only reached if first check failed, so temp ≥ 15 is implied)elseAbove 30°C → Hot


# temp= int(input(" Enter the temperature in degree celcius"))

# if temp<15:
#         print(" YOU ARE HAVING A COLD WEATHER ")

# elif temp<=30 :                   # BETWEEN 15 AND 30 INCLUSIVE
#         print(" YOU ARE HAVING WARM WEATHER")

# else:                              # Greater than 30
#         print(" YOU ARE HAVING HOT WEATHER")



#---------------------------------------------------------------------------------------------

# 9.	Take a character and check if it’s a vowel or consonant.


# STRING = input("Enter the string: ").lower()
# CHECKLIST = 'aeiou'
# COUNT = 0

# for char in STRING:
#     if char in CHECKLIST:
#         COUNT += 1

# # Logical Check
# if COUNT > 0:
#     print(f"I found {COUNT} vowel(s) in the string!")
# else:
#     print("This string is a CONSONANT-only string (No vowels found).")




# 10.	Take a character and check whether it’s uppercase, lowercase, a digit, or a special character


# char = input("Enter a single character: ")

# if len(char) != 1:
#     print("Please enter only a single character.")
    
# elif char.isdigit():
#     print(f"'{char}' is a DIGIT.")

# elif char.isupper():
#     print(f"'{char}' is an UPPERCASE letter.")

# elif char.islower():
#     print(f"'{char}' is a LOWERCASE letter.")

# else:
#     print(f"'{char}' is a SPECIAL CHARACTER.")



