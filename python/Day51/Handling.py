print('hello')
li=[10,20,30,40]
try:
    # print(1/0)
    index=int(input('enter index[0-3]: '))
    print(li[index])
except IndexError:
    print(" index out of range, but using default value 0 ")
    index=0
except ValueError:
    print(" invalid input, but using default value -1 ")
    index=-1

except:
    print(" something went wrong, but using default value ")
print("bye", index)


# ##======================================================================================
#  Exception as e handles 
# loop one 
# and ctrl+c

# it will catch all the exceptions and store the exception message in variable e
# and we can print the message using print(f" something went wrong due to 


## how to run zero division error
# print(1/0)


#bitblock

