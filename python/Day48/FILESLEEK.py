file = open("C:/Users/BHARTI/OneDrive/Desktop/msg.txt", 'r')

text = file.read(5)
print(text)

text = file.read(3)
print(text)

text = file.read(10)
print(text)

text = file.read()
print(text)

text = file.read()
print(text)

# Cats are fascinating and 
file.seek(12)

#cin (after 12 words 3 char will be read)
text = file.read(3)
print(text)

file.seek(0)  # it will take us to the starting of the file
text = file.read()
print(text)



file.close()