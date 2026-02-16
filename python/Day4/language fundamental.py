
# What are language fundamental
#
#*//
#*Language fundamentals are the basic building blocks of a programming language. They include concepts such as keywords,
#*// identifiers, variables, operators, type casting, user input, decision making, loops, string handling, and container data types.


# Keywords

'''Keywords are reserved words in a programming language that have a predefined meaning and cannot be used as identifiers
 (variable names, function names, etc.). They are the building blocks of the language and are used to define the structure 
 and syntax of the code.

 35 keywords are there
 32 are small
 3 are capitalize
 
 
 
 Keywords are reserved words with predefined meanings that cannot be used as identifiers.
 Keywords are reserved words that have predefined meanings in a language.
 You cannot use them as variable names.

 EXAMPLE:
 if, else, elif, for, while, break, def, return, continue, True, False, None

 
 '''




#Comment

'''Identifier / Definition:
Comments are non-executable notes used to explain code. They are ignored by the interpreter.
Comment is for logic

EXAMPLE
"""
This is a 
multi-line comment
"""
print("Hello") 
# This is a single-line comment


'''




#Variable
'''
A variable is a named storage location that holds a value. 

#Variable is for identifying andstoring

Variables are used to store data. They can be of various types such as integers, floats, strings, etc.
 
EXAMPLE:
x = 10
name = "Bhartii"
print(x, name)





'''


#Operator
'''  Operators perform operations on variables and values (arithmetic, logical, comparison, etc.).


EXAMPLE:
Arithmetic operators: +, -, *, /, %, **, //
Comparison operators: ==, !=, >, <, >=, <=
Logical operators: and, or, not
Assignment operators: =, +=, -=, *=, /=, %=, **=, //

a = 5
b = 2
print(a + b)   # Addition
print(a > b)   # Comparison
print(a > 3 and b < 3)  # Logical
a += 3  # Assignment







'''


#Type casting
'''Type casting is the process of converting a variable from one data type to another. This can be done using built-in functions
 like int(), float(), str(), etc.

 MEANS Type casting converts one data type into another.
 
 EXAMPLE:
x = "10"
y = int(x)  # Type casting from string to integer
print(y)  # Output: 10
print(type(y))  # Output: <class 'int'> 


x = "100"
y = int(x)   # Convert string to integer
print(y + 50)

 
 
 '''





#User input
''''User input allows the program to receive data from the user during runtime. 
In Python, the input() function is used to get user input as a string.
Allows users to enter data during program execution.

EXAMPLE:
name = input("Enter your name: ")
print("Hello, " + name + "!")

name = input("Enter your name: ")
print("Hello", name)



'''


#Decision 

'''Decision making allows the program to execute certain blocks of code based on conditions.


Used to execute code based on conditions (if, elif, else).


EXAMPLE:
age = 18
if age >= 18:   
    print("You are an adult.")                  
else:           
    print("You are a minor.")

    


'''
# Loop

'''Loops are used to repeat a block of code multiple times. In Python, we have for loops and while loops.



Loops repeat execution of a block of code (for, while).

EXAMPLE:
for i in range(5):  # For loop
    print(i)
      i = 0

 
   while i < 5:         # While loop      
         print(i)
         i += 1  


        
    
    --------------------
for i in range(3):
    print("Iteration", i)





'''


#String Handling


'''String handling refers to the manipulation and processing of strings in programming.


String handling involves manipulating and processing text data.
Operations performed on strings (concatenation, slicing, methods).

EXAMPLE:
name = "Bhartii"   


# Concatenation
greeting = "Hello, " + name + "!"   
print(greeting)  # Output: Hello, Bhartii!  



# Slicing
print(name[0:3])  # Output: Bha (slices the first three characters
print(name[-3:])  # Output: rii (slices the last three characters)
    
    
    # Methods
    # 
    #   Methods are built-in functions that perform specific operations on strings. Examples include:

    #  - upper(): Converts a string to uppercase.
    #  - lower(): Converts a string to lowercase.
    #  - strip(): Removes leading and trailing whitespace from a string.
    # - split(): Splits a string into a list of substrings based on a specified delimiter.
    # - replace(): Replaces occurrences of a specified substring with another substring.



    # EXAMPLE:
    name = "  Bhartii  "        
    

    
    print(name.upper())  # Output: BHARTII
    print(name.lower())  # Output: bhartii
    print(name.strip())  # Output: Bhartii
    print(name.split())  # Output: ['Bhartii'] (splits on whitespace)
    print(name.replace("a", "o"))  # Output: Bhortii (replace   places 'a' with 'o')    
    
    '''                     
        
            
                
                


#Container datatypes
'''Container data types are data structures that can hold multiple values. Examples include lists, tuples, sets, and dictionaries.


Container data types can hold multiple values (lists, tuples, sets, dictionaries).




EXAMPLE:
# List
# A list is an ordered, mutable collection of items. It is defined using square brackets [].
# Lists can contain elements of different data types and can be modified after creation.
my_list = [1, "Hello", 3.14, True]
print(my_list)  # Output: [1, 'Hello', 3.14, True]
my_list.append("World")  # Adding an element to the list
print(my_list)  # Output: [1, 'Hello', 3.14, True, 'World'] 



# Tuple
# A tuple is an ordered, immutable collection of items. It is defined using parentheses ().
# Tuples can contain elements of different data types but cannot be modified after creation.
my_tuple = (1, "Hello", 3.14, True)
print(my_tuple)  # Output: (1, 'Hello', 3.14, True)

# Set
# A set is an unordered collection of unique items. It is defined using curly braces {}.
# Sets do not allow duplicate elements and are mutable.
my_set = {1, "Hello", 3.14, True}
print(my_set)  # Output: {1, 'Hello', 3.14, True}

# Dictionary
# A dictionary is an unordered collection of key-value pairs. It is defined using curly braces {}.
# Each key in a dictionary must be unique and immutable.
my_dict = {"name": "Bhartii", "age": 25, "city": "Delhi"}
print(my_dict)  # Output: {'name': 'Bhartii', 'age': 25, 'city': 'Delhi'}



------------

my_list = [1, 2, 3]
my_tuple = (10, 20)
my_set = {5, 6, 7}
my_dict = {"name": "Bhartii", "age": 21}

print(my_list)
print(my_dict["name"])



'''













help('keywords')
print( 10,2.5,True, False, None) # use t/f as value
help('if')
print('#bye')
