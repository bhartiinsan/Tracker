#     1
#    12
#   123
#  1234
# 12345


for i in range(1,6):          # loop for rows

    for s in range(5,i,-1):      # loop for spaces  # else we can write 5-i
        print(" ", end="")

    for j in range(1,i+1):    # loop for numbers
        print(j, end="")

    print()





# for i in range(2,7):
#     for j in range(6,i,-1):
#         print("",end="")
#     for k in range(1,i):
#         print(k,end="")
#     print()