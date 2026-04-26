






import os
# print('done')
# it is used to rename a file or folder
# os.rename(old name, new name)
# it can be run at once, if we run it again it will give error because A.txt is not there, it is renamed to arti.txt
import time
date= time.strftime("%d-%m-%Y")
i=1
import os
items=os.listdir (r"C:\Users\BHARTI\Downloads\Noida\today")
for file in items:
    os.rename (f"C:/Users/BHARTI/Downloads/Noida/today/{file}",
                f"C:/Users/BHARTI/Downloads/Noida/today/{date} File-{i}.txt")
    i+=1
print("done")









# #================================================================================

# import os
# import time

# # 1. Folder ka rasta (Path)
# folder = r"C:\Users\BHARTI\Downloads\Noida\today"

# # 2. Aaj ki date
# date = time.strftime("%d-%m-%Y")

# # 3. Files ki list nikaalein
# items = os.listdir(folder)

# i = 1
# for file in items:
#     old_file = folder + "/" + file
#     new_name = folder + "/" + f"{date} File-{i}.txt"
    
#     # Check: Agar naya naam pehle se nahi hai, tabhi rename karo
#     if not os.path.exists(new_name):
#         os.rename(old_file, new_name)
#         i += 1

# print("Kaam ho gaya!")

# #================================================================================
# import os
# import time

# date = time.strftime("%d-%m-%Y")
# # Path vahi jo aapki image mein hai
# path = r"C:\Users\BHARTI\Downloads\Noida\today"
# items = os.listdir(path)

# i = 1
# for file in items:
#     # Sir wala simple tarika
#     old_name = f"{path}/{file}"
#     new_name = f"{path}/{date} File-{i}.txt"
    
#     # Bas yeh ek choti si line error rokne ke liye
#     if not os.path.exists(new_name):
#         os.rename(old_name, new_name)
#         i += 1

# print("done")