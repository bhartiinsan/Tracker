import os
import shutil

if os.path.exists('for loop'):
    pass
else:
    os.mkdir('for loop')

files = os.listdir()
for file in files:
    if file.endswith('.py'):
        f = open(file)    #default mode 'r'
        text = f.read()
        if 'for' in text:
            shutil.copy(file, 'for loop/')


# #===============================================================================================

# +------+----------------------+------------------------------------------+
# | Line |        Code          |              Kya hua                     |
# +------+----------------------+------------------------------------------+
# |  4   | os.path.exists()     | 'for loop' folder hai? -> pass,          |
# |      |                      | nahi hai? -> create karo                 |
# |  8   | os.listdir()         | Current folder ki saari files ki list lo |
# |  9   | for file in files:   | Har file pe loop                         |
# | 10   | file.endswith('.py') | Sirf Python files check karo             |
# | 11   | open(file)           | File kholo (default 'r' mode)            |
# | 12   | f.read()             | Poora content padho                      |
# | 13   | if 'for' in text:    | Content me 'for' word hai?               |
# | 14   | shutil.copy()        | Copy karo 'for loop/' folder me          |

# +------+----------------------+-----------------------------------------

# #===============================================================================================
 # simple code se samajh lo:

# "Current folder ki saari .py files me se
# jo files me 'for' word likha ho
# unhe 'for loop' folder me copy karo"

##===============================================================================================

#FUNCTIONS USED

# +----------------------+--------------------------------+
# |      Function        |           Kaam                 |
# +----------------------+--------------------------------+
# | os.path.exists()     | Folder/file exist karta hai?   |
# | os.mkdir()           | Naya folder banao              |
# | os.listdir()         | Folder ki files list lo        |
# | file.endswith('.py') | Extension check karo           |
# | shutil.copy()        | File copy karo                 |
# +----------------------+--------------------------------+