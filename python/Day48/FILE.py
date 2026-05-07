
file = open("C:/Users/BHARTI/OneDrive/Desktop/msg.txt", 'r' , buffering=-1)  # default=4096 bytes
# when we put 0 as buffering then it will not use buffer and read the file directly (DON'T USE THIS)

text = file.read(5)
print(text)

text = file.read(3)
print(text)

text = file.read(10)
print(text)

file.close()

#====================================================================================

file = open("C:/Users/BHARTI/OneDrive/Desktop/msg.txt", 'r' , buffering= 2)  # default=4096 bytes
# WHEN WE USE 2 THEN FIRST IT GENERATE 2 BYTES IN PAIR TILL 6 THEN USE 5 CHAR TO PRINT

text = file.read(5)
print(text)

text = file.read(3)
print(text)

text = file.read(10)
print(text)

file.close()