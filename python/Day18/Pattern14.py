#         5
#       5 4 5
#     5 4 3 4 5
#   5 4 3 2 3 4 5
# 5 4 3 2 1 2 3 4 5
#   5 4 3 2 3 4 5
#     5 4 3 4 5
#       5 4 5
#         5

n = 5

# Top half (including middle row)
for i in range(1, n + 1):
    print("  " * (n - i), end="")      # Leading spaces
    for j in range(n, n - i, -1):      # Decreasing from 5
        print(j, end=" ")
    for j in range(n - i + 2, n + 1):  # Increasing back to 5
        print(j, end=" ")
    print()

# Bottom half
for i in range(n - 1, 0, -1):
    print("  " * (n - i), end="")      # Leading spaces
    for j in range(n, n - i, -1):      # Decreasing from 5
        print(j, end=" ")
    for j in range(n - i + 2, n + 1):  # Increasing back to 5
        print(j, end=" ")
    print()




