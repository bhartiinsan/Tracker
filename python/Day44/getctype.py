import os
timestamp=os.path.getctime("python")  # c for creation time
print(timestamp)

import time
p=time.localtime(timestamp)
print(p)

fdate= time.strftime("%d-%m-%Y %r", p)
print(fdate)
#%r - time

#===================================================================

