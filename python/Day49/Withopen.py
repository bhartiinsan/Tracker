#with statement --> auto close
with open('colors.txt', 'w') as file:
    file.write('black\n')
    file.write('white\n')
print('done')

# file.write('green')   #error

# Naya concept — with statement

# with kya karta hai:

# File ko automatically close kar deta hai — close() likhne ki zarurat nahi
# Block khatam hote hi file auto band ho jaati hai
# Best practice hai file handling me

# ##===============================================================================================

# +------------------+-------------------------+
# |   Normal way     |      with statement     |
# +------------------+-------------------------+
# | file = open()    | with open() as file:    |
# | file.write()     |     file.write()        |
# | file.close()  ← | # auto close ✅         |
# | (bhool gaye? ❌) | (bhoolna possible nahi) |
# +------------------+-------------------------+

#===============================================================================================


# +------+----------------------------+----------------------------------+
# | Step |           Code             |            Kya hua               |
# +------+----------------------------+----------------------------------+
# |  1   | with open(...) as file:    | File khuli, file variable        |
# |      |                            | me store                         |
# |  2   | file.write('black\n')      | black likha                      |
# |  3   | file.write('white\n')      | white likha                      |
# |  4   | print('done')              | with block khatam -> auto        |
# |      |                            | close ✅                         |
# |  5   | file.write('green')        | ValueError ❌ file band ho chuki |
# +------+----------------------------+----------------------------------+