## indexerror occurs when we try to access an index that is out of range for a list or other sequence types.
# For example, if we have a list of 4 elements and we try to access the 5th element (index 4), it will raise an IndexError.

print('hello')
li=[10,20,30,40]
try:
    index=int(input('enter index[0-3]: '))
    print(li[index])
except IndexError as e:
    print(f" something went wrong due to ---   {e}   ")
print("bye")


##======================================================================================

