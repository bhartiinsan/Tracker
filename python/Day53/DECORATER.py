import time

def mydeco(fun):                    #decorator
    def nested():
        fun()
        print(time.strftime("%d-%b-%Y %r"))
    return nested

def register():
    print('this is register')

def login():
    print('this is login')

register = mydeco(register)
register()

login = mydeco(login)
login()

# Decorator kya hai:

# Ek function jo DOOSRE function ko
# WRAP karke uski functionality
# BINA code change kiye BADHATA hai ✅

# +------+---------------------------+--------------------------------+
# | Step |          Code             |           Kya hua              |
# +------+---------------------------+--------------------------------+
# |  1   | mydeco(fun)               | register function andar gayi   |
# |  2   | def nested()              | nested define hua              |
# |  3   | fun()                     | original register() chali      |
# |  4   | print(strftime...)        | date/time print hua            |
# |  5   | return nested             | nested return hua              |
# |  6   | register = mydeco(register)| register ab nested hai        |
# |  7   | register()                | nested() execute hua           |
# +------+---------------------------+--------------------------------+


# +-------------------------+---------------------------+
# |    Without Decorator    |     With Decorator        |
# +-------------------------+---------------------------+
# | Har function me         | Ek baar decorator banao   |
# | time print karo ❌      | sab pe apply karo ✅      |
# |                         |                           |
# | def register():         | register=mydeco(register) |
# |   print('register')     | login=mydeco(login)       |
# |   print(time...)        |                           |
# |                         |                           |
# | def login():            | Code repeat nahi ✅       |
# |   print('login')        |                           |
# |   print(time...)        |                           |
# +-------------------------+---------------------------+


# @ shortcut — Sugar Syntax:

# Yahi kaam @ se hota hai — short way
# @mydeco
# def register():
#     print('this is register')

# @mydeco
# def login():
#     print('this is login')

# register = mydeco(register) likhne ki zarurat nahi!
