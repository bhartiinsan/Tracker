#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
#   1 2 3 4 3 2 1
#     1 2 3 2 1
#       1 2 1
#         1

n = 5

# upper half
for i in range(1,n+1):

    for s in range(n-i):
        print(" ",end=" ")

    for j in range(1,i+1):
        print(j,end=" ")

    for j in range(i-1,0,-1):
        print(j,end=" ")

    print()

# lower half
for i in range(n-1,0,-1):

    for s in range(n-i):
        print(" ",end=" ")

    for j in range(1,i+1):
        print(j,end=" ")

    for j in range(i-1,0,-1):
        print(j,end=" ")

    print()



# n = 5

# # Top half (including middle row)
# for i in range(1, n + 1):
#     print("  " * (n - i), end="")  # Leading spaces
#     for j in range(1, i + 1):      # Increasing part
#         print(j, end=" ")
#     for j in range(i - 1, 0, -1):  # Decreasing part
#         print(j, end=" ")
#     print()

# # Bottom half
# for i in range(n - 1, 0, -1):
#     print("  " * (n - i), end="")  # Leading spaces
#     for j in range(1, i + 1):      # Increasing part
#         print(j, end=" ")
#     for j in range(i - 1, 0, -1):  # Decreasing part
#         print(j, end=" ")
#     print()
