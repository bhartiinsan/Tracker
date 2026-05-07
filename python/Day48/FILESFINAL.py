file = open("C:/Users/BHARTI/OneDrive/Desktop/msg.txt", 'r')
print(file.tell())      #0

text = file.read(5)     #5
print(text)

text = file.read(3)     #8
print(text)

text = file.read(10)    #18
print(text)

text = file.read()      #EOF(-1)
print(text)

text = file.read()      #EOF
print(text)

file.seek(12)           #12

text = file.read(3)     #15
print(text)

file.seek(0)            #0
text = file.read()      #EOF
print(text)

file.close()