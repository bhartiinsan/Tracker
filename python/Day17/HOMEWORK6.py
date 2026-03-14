# 6. WAP to check prime number entered through keyboard.

num= int(input(" Enter the number"))

if num>1:                       # beacuse we can't take negative number
    for i in range (2,num):    # num also num-1 cause it iterate the exclusive value
        if num %i ==0:
            print(" IT IS not A PRIME NUMBER")
            break
        else:
            print("It's a prime number")
else:
    print(num," is not a prime number")

# when a number is not prime the remainder is 0

