#  **Pattern 3: Sequential Number Pyramids (e.g., 1, 2 3, 4 5 6)**
#     *   A global counter increments sequentially across rows. Each row `i` (from 1 to 5) prints `i` numbers from the counter. Output for 5 rows:
#         ```








#         1
#         2 3
#         4 5 6
#         7 8 9 10
#         11 12 13 14 15





x=1
for i in range(1,6):
    for j in range(0,i):
        print(x, end=" ")
        x+=1
    print()