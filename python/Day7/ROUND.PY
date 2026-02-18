p=8
c=8
m=9
avg = (p+c+m)/3
print(avg)


a=18.6
b=round(a)
print(b)


a=18.4  
b=round(a)
print(b)

a=18.5             # ODD.5 IS ROUNDED TO NEXT VALUE 
b=round(a)      
print(b)



a=18.5             # EVEN.5 IS ROUNDED TO PREVIOUS VALUE
b=round(a)         # odd.5 is rounded
print(b)


res=round(avg,2)  # 2 is for 2 decimal places
print(res)

a=3.146789
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
