a=3.4
b='2.1'
#print(a+b)  #error

#str to float
c=float(b)
print(a+c)

#float to str
d=str(a)
print(d+b)

a='4'
b=5
#print(a+b)  #error

#str to int
c=int(a)
print(c+b)

#int to str
d=str(b)
print(a+d)


#-------------------------------------------------



#float to int
a=4.1
b=int(a)
print(a)
print(b)

#print(2+3+int("4+5"))
print(2+3+int("4"+"5"))
print(2+3+int("4")+int("5"))

print("4"+str(5+6))





#--------------------------------------------------


a=4
b=6.7
print(a+b)      #implicit type casting(int to float)

print(a+int(b)) #explicit(float to int)


print(True+5)   #implicit(bool to int)

#True--->1
#False-->0


#--------------------------------------------------


a=input('enter 1st num=')
b=input('enter 2nd num=')
#print(a+b)
c=int(a)
d=int(b)
print(c+d)



#--------------------------------------------------


a=input('enter 1st num=')
b=input('enter 2nd num=')
#print(a+b)
print(int(a)+int(b))




#--------------------------------------------------





a=int( input('enter 1st num=') )
b=int(input('enter 2nd num='))
print(a+b)




#------------------------------------------------



a=float(input('enter 1st num='))
b=float(input('enter 2nd num='))
print(a+b)




#--------------------------------------------------


#avg of 3 subject using input upto 2 decimal places
m1=float(input("enter marks in P="))
m2=float(input("enter marks in C="))
m3=float(input("enter marks in M="))

avg=(m1+m2+m3)/3
print(round(avg,2))


#--------------------------------------------------














'''


Type Casting
===========
	>It is a technique to convert a datatype into another
	Note:Actual type is never converted rather a new copy is created

2 types
----------
A.	Explicit type casting---->programmer is responsible
B.	Implicit type casting---->language is responsible

str to float(explicit)
-------------------------
		float_data=float(str_data)

float to str(explicit)
-------------------------
		str_data=str(float_data)

str to int(explicit)
-----------------------
		int_data=int(str_data)

int to str(explicit)
-----------------------
		str_data=str(int_data)

float to int(explicit)
-------------------------
		int_data=int(float_data)

int to float(implicit)
--------------------------
		float_data=float(int_data)

boolean to int(implicit)
------------------------------
		int_data=int(bool_data)
		True--->1
		False-->0
etc.

Note:type casting fails if source & target types are not compatiable
	exp:	'4.5k'------>float----->fails
		'45k'------->int------->fails


User Input
=========
	>It is a technique to read value from user during execution of program
		str_data=input('prompt')

	Note:input() always return user data as str and if we need to perform required operations then we have
	to use type casting.

user input as int
---------------------
		int_data=int(input('prompt'))

user input as float
------------------------
		float_data=float(input('prompt'))









 




































'''