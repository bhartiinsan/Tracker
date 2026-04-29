import os
import shutil
import time

li_items=os.listdir()
for i in li_items:
    if os.path.isfile(i):
        ts= os.path.getctime(i)
        month= time.strftime("%B", time.localtime(ts))
        if os.path.exists(month):
            pass
        else:
            os.mkdir(month)
            shutil.copy(i,f" {month}/ {i}")
print('done')