# 54321
# 5432
# 543
# 54
# 5


n = 5
for i in range(n, 0, -1):      # Controls the number of elements (5, 4, 3, 2, 1)
    for j in range(n, n - i, -1): # Starts at 5 and counts down 'i' times
        print(j, end="")
    print()                    # Moves to the next line















# for i in range(5,0,-1):        # row control
#     for j in range(5,i-1,-1):  # decreasing numbers
#         print(j,end="")
#     print()
