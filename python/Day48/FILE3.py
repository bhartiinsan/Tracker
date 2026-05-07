# ### READ PADHEGA

# file = open("C:/Users/BHARTI/OneDrive/Desktop/msg.txt", 'r')

# text = file.read(5)
# print(text)

# text = file.read(3)
# print(text)

# text = file.read(10)
# print(text)

# text = file.read() ## IT RETURNS BLANK STRING ( A SPACE) BECAUSE WE HAVE REACHED THE END OF THE FILE. TOH BACHE HUE CHARACTER PADHEGA.
# print(text)

# file.close()

###====================================================================================

# 2ND SCENARIO

file = open("C:/Users/BHARTI/OneDrive/Desktop/msg.txt", 'r')
text = file.read()
print(text)  # IT WILL READ THE WHOLE FILE AND PRINT THE WHOLE FILE.

text = file.read(5)
print(text)

text = file.read(3)
print(text)

text = file.read(10)
print(text)

file.close()