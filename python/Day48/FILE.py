file = open('C:/Users/BHARTI/OneDrive/Desktop/cat_download.jfif', 'r', buffering=-1)  # default=4096 bytes

text = file.read(5)
print(text)

text = file.read(3)
print(text)

text = file.read(10)
print(text)

file.close()