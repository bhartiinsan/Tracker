x=float(input("Emter 1st num :"))
y=float(input(" Enter 2nd num :"))

option = input ( 
    
"""A .addition,\n B. multiply, \n C. substraction, \n D . Division""")


if option =="A" or option =="a":  
    print( x+y)
elif option =="B" or option =="b":  
    print( x*y)
elif option =="C" or option == "c":  
    print( x-y)
elif option =="D" or option== "d":  
    print( x/y)                                    # in python divide by zero is not possible
else:
    print(" invalid option")