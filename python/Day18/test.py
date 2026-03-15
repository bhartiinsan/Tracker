# hello
# for column in range(0,3):
#     # for row in range(0,4):
#     #     print("*", end="")
#     print("*",end="\n") #by default it will print new line

# for column in range(0,3):
#     # for row in range(0,4):
#     #     print("*", end="")
#     print("*") #by default it will print new line

# for column in range(0,3):
#     for row in range(0,3):
#         print("row")
#     print("column")

# for abc in range(0,3):
#     for ab in range(0,2):
#         for a in range(0,1):
#             print("a", end=" ")
#         print("ab", end=" ")
#     print("abc")

for abc in range(0,5):
    for ab in range(0,2):
        for a in range(0,abc):
            print(a, end=" ")
        print(ab, end=" ")
    print()
