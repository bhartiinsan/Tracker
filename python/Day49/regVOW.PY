import re

text='''Python is a funny language created by Guido VAN Rossum in 1991.
It is widely used in AI & Automation.
ChatGPT,Claude,Gemini are based on Python.
'''
#pattern='i.'
#pattern='[iI].'
#pattern='[iI][aeiou]'
pattern='[iI][^aeiou]'

li=re.findall(pattern,text)
print(li)