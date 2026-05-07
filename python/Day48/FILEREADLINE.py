file = open("C:/Users/BHARTI/OneDrive/Desktop/msg.txt", 'r')
print(file.tell())      #0
file.seek(5)
line = file.readline()
print(line)

line = file.readline()
print(line, len(line))

file.close()