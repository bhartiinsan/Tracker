# 1. Write a Python program to calculate the length of a string without using len(). 

# s=input(" Enter the string")

# count= 0

# for char in s:
#     count+=1

# print(f"LENGTH OF A STRING is {count}")

#----------------------------------------------------------------------------------------

# 2. Write a Python program to change a given string to a new string where the first and last
# chars have been exchanged. 


# s = input("Enter the string: ")

# result = s[-1] + s[1:-1] + s[0]

# print("Original :", s)
# print("Swapped  :", result)
# #==================================================================================================

# s = input("Enter the string: ")

# # Step 1: Check string has at least 2 characters
# if len(s) < 2:
#     print("String too short to swap!")

# else:
#     first  = s[0]       # Grab first character
#     middle = s[1:-1]    # Grab everything in between
#     last   = s[-1]      # Grab last character

#     # Step 2: Rebuild string — put last first, first last
#     result = last + middle + first

#     print(f"Original string : {s}")
#     print(f"After swap      : {result}")

#---------------------------------------------------------------------------------------------------------




# 3. Write a Python program that takes input from the user and displays that output in upper
# and lower cases. 

# s = input("Enter the string: ")
# upper= s.upper()
# lower= s.lower()

# print(f"THIS IS THE UPPER STRING  :{upper}   and THIS IS THE LOWER STRING:    {lower}")




# 4. Write a Python program to convert a given string to all uppercase if it contains at least 2
# uppercase characters in the first 4 characters. 


# string= input(" Enter the string ")
# count=0
# for char in string[:4] :
#     if char.isupper():
#         count+=1

# if count >=2:
#     print(f" It is qualified for the process {string.upper()}")
# else:
#     print(f" you string is  {string}")

#-------------------------------------------------------------------------------------------


# WORKING:

# START
#   │
#   ▼
# Input a string
#   │
#   ▼
# Grab first 4 characters → s[:4]
#   │
#   ▼
# Count uppercase letters in those 4 chars
#   │
#   ▼
# Is count >= 2?
#   │              │
#  YES             NO
# #   │              │
# #   ▼              ▼
# # Convert       Keep string
# # to UPPER      as it is
# #   │              │
# #   ▼              ▼
# # # Print          Print



#----------------------------------------------------------------------------



# 5. Write a Python program to reverse a string. 
# s = input("Enter the string: ")
# reverse=s[::-1]
# print(reverse)

#----------------------------------------------------------------------------



# 6. Write a Python program to print the index of each character in a string.



# s = input("Enter the string: ")

# for i in range(len(s)):
#     print(f"Character '{s[i]}' is at index {i}")


#------------------------------------------------------------------------------

# s = input("Enter the string: ")

# count = 0
# for char in s:                                  
#     print(f"Character '{char}' is at index {count}")
#     count += 1                                   


# #--------------------------------------------------------------------------------


# THIS CONCEPT WE WILL LEARN IN FURTHER CLASSES
# s = input("Enter the string: ")

# for index, char in enumerate(s):
#     print(f"Character '{char}' is at index {index}")

#-------------------------------------------------------------------------------------


# 7. Write a Python program to check if a string contains all vowels of the alphabet. 
#CAN'T DO THE LOGIC OF IF WE FIND ANY OF THEM PRINT ----AND NONE THAN PRINT ITS A CONSTANT

# STRING= input(" Enter the string ").lower()
# CHECKLIST= 'aeiou'
# COUNT=0

# for char in STRING:
#     if char in CHECKLIST:
#         COUNT+=1

# if COUNT ==5:
#     print( f" THIS IS A VOWELS CHECKLIST {COUNT}, ALL FOUND IN STRING  : {STRING}")
# else:
#     print(f" This is the string which have {COUNT}VOWELS in {STRING}")

#--------------------------------------------------------------------------------------

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

#----------------------------------------------------------------------------------------

# 8. Write a Python program to lowercase first n characters in a string. 


# STRING = input(" Enter the string ")
# n= int(input(" HOW MANY CHARACTERS YOU WANT TO LOWERCASE: "))


# result = STRING[:n].lower() + STRING[n:]

# print(f" LOWERCASING THE STRING RESULT , {result}")



#==========================================================================================


# # 9.Write a Python program to remove spaces from a given string. 
# STRING = input(" Enter the string ")
# result= STRING.replace(" ", '')
# print(result)

# ================================================================================================



# 10.WAP that reads a string from keyboard and determine whether the string is palindrome
# or not.

STRING = input(" Enter the string ")
key=STRING[::-1]
if STRING==key:
    print( f"  {STRING}  IS A PALINDROME ")
else: print(f" {STRING}  IS NOT PALINDROME")

