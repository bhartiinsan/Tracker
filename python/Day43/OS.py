import os           # file & folder related automation
# path=os.getcwd()   # get current working directory
# print(path)

#=======================================================
# LIST FILES AND FOLDERS
# # how to do with python
# items=os.listdir()   # list of all files and folders in current working directory
# print(type(items),len(items))
# for i in items:
#     print(i)

# # it does not return hidden files and folders
# # .vscode
# # .ipynb_checkpoints        

# #========================================================
# #if we want to get hidden files and folders also
# items=os.listdir(path)
# print(type(items),len(items))
# for i in items:
#     print(i)

# =======================================================

# SPECIFIC ITEMS IN A FOLDER
# C DRIVE MAI KITNE FILES HAI
#1,2,3
# @also can write noida instead of Noida and NOIDA TOO IN PATH, but it is case sensitive


# items = os.listdir("C:\\Users\\BHARTI\\Downloads\\Noida\\today")
items = os.listdir("C:/Users/BHARTI/Downloads/Noida/today")   # forward slash bhi use kar sakte hai

# items = os.listdir(r"C:\Users\BHARTI\Downloads\Noida\today")
print(type(items),len(items))
for i in items:
    print(i)

#==========================================================

 
