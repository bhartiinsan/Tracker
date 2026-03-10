# infinite loop
while True:
    a=int(input(" Enter the a"))
    b=int(input(" Enter the b"))
    print(a*b)
    c= input(" do you want to run it again(y/n)")
    if c=="y":
        continue
    else :
        break
