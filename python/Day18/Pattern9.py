# *   **Pattern 4: Decreasing Sequence (Row-wise) (e.g., 1, 21, 321)**
#     *   Each row `i` (from 1 to 5) prints numbers from `i` down to 1. Output for 5 rows:
#         ```
#         1
#         21
#         321
#         4321
#         54321


for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end="")
    print()