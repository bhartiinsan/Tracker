


print('/n')
print("/n")

print('\n')  # \n is for new line
print(r'\n') # r is for raw string and it will print as it is
print('\\n') # \\ is for single \ and then n will be printed as it is
print(r'\\n') # r is for raw string and it will print as it is
print(r'bharti') 


a=18.6   #19
b=round(a)
print(b)


a=18.4     #18
b=round(a)
print(b)

a=18.5             # ODD.5 IS ROUNDED TO NEXT VALUE 
b=round(a)      
print(b)


#FLOAT VALUE TO INTEGER VALUE ROUND SCENARIO


a=17.5             # EVEN.5 IS ROUNDED TO PREVIOUS VALUE OR BASE INTEGER
b=round(a)         # odd.5 is rounded TO NEXT VALUE INTEGER
print(b)           # IT IS CALLED BANKER'S ROUNDING OR ROUND HALF TO EVEN

a= 3.5
b= round(a)
print(b)

a= 6.5
b= round(a) 
print(b)

a= 3.4
b= round(a)
print(b)

print('\n')

#----------------------------------
p= 8
c= 8
m= 9
avg = (p+c+m)/3
print(avg)


res=round(avg,2)  # 2 is for 2 decimal places and after value of equals to 5 or greater than 5 next value will be printed 
print(res)                                #and if less than 5 then previous value will be printed


print('\n')


a=3.146789
res=round(a,2)
print(res)

a=3.145789
res=round(a,2)
print(res)

print('\n')

a=3.143789
res=round(a,2)
print(res)


#-----------------------------


price= 4999
less = 15.5
discount = price * less / 100
print(discount)

actual_price = price - discount
print(actual_price)

round_price = round(actual_price) # you have to convert in to integer
print(round_price)

#or we can directly round the actual price without storing in variable

actual_price = round(price - (price * less / 100))  
print(actual_price)

print('\n')

# MY INVENTION

short_price =(round( (price - discount)))
print(short_price)

print('\n')



#question 2

income = 1256797 
tax = 7
cess = 2.5 

amount_after_tax = income - (income * tax / 100)
print(amount_after_tax)

amount_after_cess = amount_after_tax - (amount_after_tax * cess / 100)
print(amount_after_cess)

round_amount = round(amount_after_cess)
print(round_amount)

#------------------------------

#in short
round_amount = round(income - (income * tax / 100) - ((income - (income * tax / 100)) * cess / 100))
print(round_amount)


#--------------------------------
amount_after_tax = income - (income * tax / 100)

amount_after_cess = amount_after_tax - (amount_after_tax * cess / 100)

print
