# 'r+' kaise kaam karta hai:
# StepCodeKya hua1open('players.txt', 'r+')File khuli — exist karni chahiye warna Error ❌
# 2file.read()Poora content padha, cursor END pe gaya
# 3print(text)Purana content print hua
# 4file.write('dhoni\n')Cursor END pe hai, to end me dhoni add hua
# 5file.close()File band



file = open('players.txt', 'r+')    #read then write
text = file.read()
print(text)
file.write('dhoni\n')
file.close()

# 'r+' = read bhi, write bhi — but file pehle se exist karni chahiye
# read() ke baad cursor END pe hota hai → write end me hoti hai
# Agar start me likhna ho → file.seek(0) karo pehle ya read() mat karo, cursor start pe hi rahega

# when we write this so dhoni will be written at the end of the file, not at the beginning. 
# So, it will not overwrite sachin but will be added after virat. 




###===============================================================================================

# Agar read() nahi likha:
# pythonfile = open('players.txt', 'r+')
# # read() nahi kiya — cursor position 0 pe hai!
# file.write('dhoni\n')
# file.close()

# dhoni       ← dhoni ne sachin ko OVERWRITE kar diya!
# viru
# rohit
# virat


##===============================================================================================

#file = open('players.txt', 'r+')
# file.seek(0, 2)          # cursor → END of file
# file.write('dhoni\n')
# file.close()

# seek(0, 2) — Secret trick! 🎯
# seek(offset, whence)

# whence value       Matlab
# 0                 Start se count karo (default)
# 1                 Current position se count karo
# 2                 End se count karo