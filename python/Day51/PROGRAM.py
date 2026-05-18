print('hello')
li=[10,20,30,40]
try:
    index=int(input('enter index[0-3]: '))
    print(li[index])
except Exception as e:
    print(f" something went wrong due to ---   {e}   ")
print("bye")

# this is know as parent exception
# it will catch all the exceptions
#========================================================================================


