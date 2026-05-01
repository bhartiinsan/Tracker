#file input/output
import io

# "C:\Users\BHARTI\OneDrive\Desktop\msg.txt"

# STEP =1 OPEN TEXT FILE IN READ MODE
file = open("C:/Users/BHARTI/OneDrive/Desktop/msg.txt", "r")  #Yeh file ko read mode me khol raha hai
# file= io.open("C:/Users/BHARTI/OneDrive/Desktop/msg.txt", "r")  #Yeh file ko read mode me khol raha hai

# STEP =2 READ THE CONTENT OF FILE 
# IT WORKS LIKE STRING METHODS
content = file.read(10)  #Yeh file ke content ko read kar raha hai  #-1 = LAST CHARACTER TAK READ KARNE KE LIYE
print(content)  #Yeh file ke content ko print kar raha hai

# STEP =3 CLOSE THE FILE
file.close()  #Yeh file ko close kar raha hai

#===========================================
