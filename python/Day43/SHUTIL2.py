import shutil
total, used, free= shutil.disk_usage("C:/")
print(total)
print(used)
print(free)

#==================================================
# for finding free space in c drive
# in gb  
print(total/1024/1024/1024)

