file = open('players.txt', 'a+')    #create/append seek read
file.write('\nsachin')
file.seek(0)
text = file.read()
print(text)
file.close()

# open('a+') karte hi cursor END pe hota hai
# write() → hamesha END me likhta hai (overwrite impossible!) ✅
# seek(0) → read ke liye cursor start pe lana padta hai

#===============================================================================================

# 'a+' mode — Create/Append + Seek + Read

# Step          Code             Cursor      Kya hua
# 1             open('a+')       END         File khuli — purana data SAFE ✅
# 2              write('sachin') END         sachin END me add hua
# 3              seek(0)          0          Cursor START pe gaya
# 4              read()          END         Poora content padha
# 5              print           (text)      —Sab print hua

#===============================================================================================



# +--------+-------+-------+------------+-------------+-----------+
# |  Mode  | Read  | Write | File nahi  |  Purana     |  Cursor   |
# +--------+-------+-------+------------+-------------+-----------+
# |  'r'   |  ✅   |  ❌   |  ❌ Error  |  Safe       |  Start    |
# |  'w'   |  ❌   |  ✅   |  ✅ Create |  ❌ DELETE  |  Start    |
# |  'a'   |  ❌   |  ✅   |  ✅ Create |  ✅ Safe    |  End      |
# |  'r+'  |  ✅   |  ✅   |  ❌ Error  |  ✅ Safe    |  Start    |
# |  'w+'  |  ✅   |  ✅   |  ✅ Create |  ❌ DELETE  |  Start    |
# |  'a+'  |  ✅   |  ✅   |  ✅ Create |  ✅ Safe    |  End      |
# +--------+-------+-------+------------+-------------+-----------+



