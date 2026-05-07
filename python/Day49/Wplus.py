

file = open('players.txt', 'w+')    #create/replace write seek read
file.write('ishan')
file.seek(0)
text = file.read()
print(text)
file.close()

##===============================================================================================

# 'w+' mode — Create/Replace + Write + Read

# Flow step by step:
# Step          Code         Cursor            Kya hua
# 1            open('w+')     0                  File khuli — purana content DELETE ❌
# 2            write('ishan') 5                  ishan likha, cursor END pe
# 3            seek(0)        0                  Cursor wapas START pe
# 4            read()        END                 Poora content padha
# 5            print         (text)              —ishan print hua


###===============================================================================================

# seek(0) kyun zaruri tha?
# write() ke baad cursor END pe tha
# agar seek(0) nahi karte:
#   read() → "" empty string (kyunki cursor END pe tha)

# seek(0) ke baad:
#   read() → "ishan" ✅

##===============================================================================================

# ```
# +----------------+-----------+-----------+
# |   Condition    |   'r+'    |   'w+'    |
# +----------------+-----------+-----------+
# | File nahi hai  | ❌ Error  | ✅ Create |
# | Purana data    | ✅ Safe   | ❌ DELETE |
# | Cursor start   | 0 (Start) | 0 (Start) |
# | Read + Write   |    ✅     |    ✅     |
# +----------------+-----------+-----------+
# ```