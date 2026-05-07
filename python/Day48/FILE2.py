# import time

# start = time.perf_counter()          # line 2

# file = open("C:/Users/BHARTI/OneDrive/Desktop/msg.txt", 'r', buffering=4096)

# text = file.read(5)
# print(text)

# text = file.read(3)
# print(text)

# text = file.read(10)
# print(text)

# end = time.perf_counter()            # line 14

# print("Time Taken=", end - start)   # line 16
# file.close()

# Time Taken= 0.0006588000105693936
##====================================================================================


# file = open("C:/Users/BHARTI/OneDrive/Desktop/msg.txt", 'r', buffering=-1)  # default buffer=4096

# text = file.read(5)
# print(text)

# text = file.read(3)
# print(text)

# text = file.read(10)
# print(text)

# file.close()

# text = file.read(10)
# print(text)

# ValueError: I/O operation on closed file.
# file.close()  # when we close the file then we can't read the file. It will give error. 
# So, we have to read the file before closing the file.