## SET OF CHARACTERS

import re

text='''Python is a funny language created by Guido VAN Rossum in 1991.
It is widely used in AI & Automation.
ChatGPT,Claude,Gemini are based on Python.
'''
#pattern='i.'
pattern='[iI].'

li=re.findall(pattern,text)
print(li)


# ##===============================================================================================
# [ ]  →  "in se koi ek character match karo"
# [iI] →  ya to 'i' (small)  ya  'I' (capital)


# +----------+----------------------------------------+
# | Pattern  |           Matlab                       |
# +----------+----------------------------------------+
# |  'i.'    | sirf small 'i' + koi bhi ek char       |
# |  '[iI].' | small 'i' YA capital 'I' + koi bhi char|
# +----------+----------------------------------------+

##===============================================================================================


# +------------+----------------------------------+
# |  Pattern   |           Matlab                 |
# +------------+----------------------------------+
# | [iI]       | i ya I (case insensitive)        |
# | [aeiou]    | koi bhi vowel                    |
# | [0-9]      | koi bhi digit 0 se 9             |
# | [a-z]      | koi bhi small letter             |
# | [A-Z]      | koi bhi capital letter           |
# | [a-zA-Z]   | koi bhi letter (upper ya lower)  |
# | [^aeiou]   | vowel NAHI (^ = not)             |
# +------------+----------------------------------+

##===============================================================================================

# [ ] ko officially kehte hain — "Character Class" ya "Character Set"

# [ ] ke andar jo bhi characters likho
# unka ek SET ban jaata hai
# us SET me se koi BHI ek character match karega

#EXAMPLE:

# [iI]     →  Set = {i, I}        → koi ek match karega
# [aeiou]  →  Set = {a,e,i,o,u}   → koi ek vowel match karega
# [0-9]    →  Set = {0,1,2,3,4,5,6,7,8,9} → koi ek digit match karega
# [a-z]    →  Set = {a,b,c,...,z} → koi ek small letter match karega
# [A-Z]    →  Set = {A,B,C,...,Z} → koi ek capital letter match karega
# [a-zA-Z] →  Set = {a,b,c,...,z,A,B,C,...,Z} → koi ek letter match karega
# [^aeiou] →  Set = {sab kuch jo vowel nahi hai} → koi ek non-vowel match karega

##===============================================================================================

# [ ] = Character Set / Character Class ✅
# Andar se sirf EK character match hota hai ek baar
# - use karo range ke liye → [0-9], [a-z]
# ^ use karo NOT ke liye → [^0-9] = digit nahi