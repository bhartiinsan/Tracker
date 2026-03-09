# BREAK KEYWORD STOPPING THE CONDITION WHILE

a=1
while a<=3:
    pin= int(input(" Enter pin="))
    a+=1
    if pin == 1234:
        print("valid")
        break
    elif a==4 :                                 # greater than ;  a>3
        print(" max attempts completed")
        
    else:
        print(" invalid attempt")