n = 5

for i in range(n,0,-1):      # controls rows
    for s in range(0,n-i):   # prints spaces
        print(" ", end="")
        
    for j in range(i,0,-1):  # prints decreasing numbers
        print(j, end="")
        
    print()











# opposite

n = 5

for i in range(n,0,-1):      # controls rows
    for s in range(0,n-1):   # prints spaces
        print("", end="")
        
    for j in range(i,0,-1):  # prints decreasing numbers
        print(j, end="")
        
    print()
