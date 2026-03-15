#     1
#    12
#   123
#  1234
# 12345







# for i in range(2,7):
#     for j in range(6,i,-1):
#         print(" ",end="")
#     for k in range(1,i):
#         print(k,end="")
#     print()


#----------------------------------------------------









# PATTERN8


# 12345
#  1234
#   123
#    12
#     1


for i in range(5,0,-1):
    
    for j in range(1,6-i):   # spaces
        print(" ", end="")
        
    for k in range(1,i+1):   # numbers
        print(k, end="")
        
    print()

















#     Pattern 2: Increasing Sequence (e.g., 1, 12, 123)
# Each row i (from 1 to 5) prints numbers from 1 up to i. Output for 5 rows





# PATTERN2

# 1
# 12
# 123
# 1234
# 12345
    

# for i in range(1, 6):      # rows
#     for j in range(1, i+1):  # numbers in each row
#         print(j, end="")
#     print()