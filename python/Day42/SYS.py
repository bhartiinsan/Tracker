# INTERPRETER 

import sys
print(sys.version)

# 3.13.13

# platform-- os info
k=sys.platform
print(k)

# win32

# where the python is installed
print(sys.prefix)
# C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3568.0_x64__qbz5n2kfra8p0

# where the interpreter dudhega
print(sys.path)

# ['c:\\Users\\BHARTI\\OneDrive\\Desktop\\Ducat\\python\\Day42', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.3568.0_x64__qbz5n2kfra8p0\\python313.zip', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.3568.0_x64__qbz5n2kfra8p0\\DLLs', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.3568.0_x64__qbz5n2kfra8p0\\Lib', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.3568.0_x64__qbz5n2kfra8p0', 'C:\\Users\\BHARTI\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python313\\site-packages', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.3568.0_x64__qbz5n2kfra8p0\\Lib\\site-packages']
# PS C:\Users\BHARTI\OneDrive\Desktop\Ducat>

# INDEX MAXIMUM LIMIT
print(sys.maxsize)

# theoritical maximum value of python index( practically depends it is less.)
# \9223372036854775807

#===============================================================

print(sys.implementation)

# ironpython interpreter- microsoft
# jython
#pypy

