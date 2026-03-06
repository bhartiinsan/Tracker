cp= float(input(" Enter cost price ="))
sp= float(input(" Enter selling price"))

print("profit" if sp>cp else ("loss" if sp<cp else " no profit no loss"))

'''
TERNARY OPERATOR
> IT WAS ADDED IN PYTHON 2.5 VERSION TO WRITE IF ELSE IN A SINGLE STATEMENT
SYNTAX:
        true_value if condition else false_value

> WE CAN NOT USE ELIF DIRECTLY WITH TERNARY OPERATOR BUT SAME CAN BE IMPLEMENTED USING NESTED TERNARY
SYNTAX:
        true_value if condition else (true_value if condition else false_value)

> It is widely useful in comprehension
list comprehension



COMPLEX DATATYPE
> It is used to represent a value in the form of a+bj
 where
    a------------> real part(int,float)
    b------------> imaginary part

    where 
    b --- real
    j---- imaginary unit

    > it is widely used in IOT and Emmbedded applications to represent circuit



'''