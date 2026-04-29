import os
li= os.listdir()  #cwd
count=0
for i in li:
    # print(i, os.path.isfile(i))
    if os.path.isfile(i):
        count+=1
print(count)

