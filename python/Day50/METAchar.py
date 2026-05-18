# +------------+---------------------------+------------------+------------------+
# | Meta Char  |        Matlab             |    Pattern       |    Match         |
# +------------+---------------------------+------------------+------------------+
# |     .      | Koi bhi EK char           |   'i.'           | 'is','in','it'   |
# |    [ ]     | Character Set/Class       |   '[iI]'         | 'i' ya 'I'       |
# |    [^ ]    | NOT - ye char NAHI        |   '[^aeiou]'     | consonant,digit  |
# |    [-]     | Range define karo         |   '[a-z]'        | a,b,c...z        |
# |     ^      | String ka START           |   '^Python'      | 'Python...'      |
# |     $      | String ka END             |   'Python$'      | '...Python'      |
# |     *      | 0 ya zyada baar           |   'ab*'          | 'a','ab','abb'   |
# |     +      | 1 ya zyada baar           |   'ab+'          | 'ab','abb'       |
# |     ?      | 0 ya 1 baar (optional)    |   'ab?'          | 'a' ya 'ab'      |
# |    {n}     | Exactly n baar            |   'a{3}'         | 'aaa'            |
# |   {n,m}    | n se m baar               |   'a{2,4}'       | 'aa','aaa','aaaa'|
# |     |      | OR (ya to ye ya wo)       |   'cat|dog'      | 'cat' ya 'dog'   |
# |    ( )     | Group banana              |   '(ab)+'        | 'ab','abab'      |
# |     \      | Escape / Special seq      |   '\.'           | literal dot '.'  |
# +------------+---------------------------+------------------+------------------+


#===============================================================================================

# It finds non-overlapping matches of the pattern in the string and returns them as a list.
# - re.findall(pattern, string)


import re

text='''Python is a funny language created by Guido VAN Rossum in 1991.
It is widely used in AI & Automation.
ChatGPT,Claude,Gemini are based on Python.
'''
#pattern='i.'
#pattern='[iI].'
#pattern='[iI][aeiou]'
#pattern='[iI][^aeiou]'
#pattern='[iI][^aeiou]'
#pattern='[ABCDEFGHIJKLMNOPQRSTUVWXYZ][aeiou][abcdefghijklmnopqrstuvwxyz][abcdefghijklmnopqrstuvwxyz]'
#pattern='[A-Z][aeiou][a-z][a-z]'
#pattern='[a-z][aeiou][a-z]'
#pattern='[A-Z][a-z][a-z][a-z][a-z]'
pattern='[A-Z][a-z]{4}'  #['Pytho', 'Guido', 'Rossu', 'Autom', 'Claud', 'Gemin', 'Pytho']
pattern='[A-Z][a-z]{1,4}'     #['Python',   'Guido', 'Rossum', 'Automation', 'ChatGPT', 'Claude', 'Gemini', 'Python']

li=re.findall(pattern,text)
print(li)

# ##===============================================================================================
# +--------------------------------+----------------------------------------+
# |           Pattern              |              Matlab                    |
# +--------------------------------+----------------------------------------+
# | '[ABCD...Z][aeiou][abcd...z]'  | Manually sab letters likhna — boring!  |
# | '[A-Z][aeiou][a-z][a-z]'       | Capital + vowel + 2 small = 4 char word|
# | '[a-z][aeiou][a-z]'            | small + vowel + small = 3 char         |
# | '[A-Z][a-z][a-z][a-z][a-z]'   | Capital + 4 small = 5 char word        |
# | '[A-Z][a-z]{4}'                | Same — but SHORT way using {4}  ✅     |
# +--------------------------------+----------------------------------------+


#QUANTIFIERS: {4}

# [a-z]{4}  =  [a-z][a-z][a-z][a-z]
#              exactly 4 small letters


##===============================================================================================

# +----------+-------------------------+-------------------+
# | Symbol   |        Matlab           |     Example       |
# +----------+-------------------------+-------------------+
# |  {n}     | Exactly n baar          | [a-z]{4} = 4 char |
# |  {n,}    | n ya zyada baar         | [a-z]{2,} = 2+    |
# |  {n,m}   | n se m baar             | [a-z]{2,4} = 2-4  |
# |  *       | 0 ya zyada ({0,})       | [a-z]*            |
# |  +       | 1 ya zyada ({1,})       | [a-z]+            |
# |  ?       | 0 ya 1 baar ({0,1})     | [a-z]?            |
# +----------+-------------------------+-------------------+