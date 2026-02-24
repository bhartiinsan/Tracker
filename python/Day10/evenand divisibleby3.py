num = int(input(" enter your num="))
if num%2 == 0:
    print("EVEN")
    if num%3 == 0:
        print(" divisible by 3")
    else:
        print(" The number is divisible by not 3")
else:
    print('odd')