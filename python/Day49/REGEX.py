#Regular Expression(Regex)
    #pattern based searching
    #data validation
    #data cleaning
    #compiler/interpreter

import re

text='''Python is a funny language created by Guido VAN Rossum in 1991.
It is widely used in AI & Automation.
ChatGPT,Claude,Gemini are based on Python.
'''
pattern='i.'

li=re.findall(pattern,text)
print(li)

#===============================================================================================

# +------------------------+------------------------------+
# |       Use Case         |           Example            |
# +------------------------+------------------------------+
# | Pattern based searching| 'i.' - i ke baad koi bhi char|
# | Data validation        | Email, phone number check    |
# | Data cleaning          | Extra spaces, symbols hatao  |
# | Compiler/Interpreter   | Code syntax check            |
# +------------------------+------------------------------+

#===============================================================================================

# re.findall(pattern, text) kya karta hai:

# Text me se pattern se match hone wali saari strings dhundh ke list me return karta hai

##===============================================================================================

# +----------+---------------------------+
# | Symbol   |        Matlab             |
# +----------+---------------------------+
# |   .      | Koi bhi EK character      |
# |   i.     | i + koi bhi ek char       |
# |   \.     | Literal dot (escape karo) |
# +----------+---------------------------+


##===============================================================================================

