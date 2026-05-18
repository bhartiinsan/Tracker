def show():                           #top level(outer) fun
    i = 10
    print('this is show before disp', i)
    def disp():                       #closure fun
        nonlocal i
        i = 'hello'
        print('this is disp', i)
    
    disp()
    print('this is show after disp', i)

show()



# +------+------------------------------+---------------------------+
# | Step |           Code               |         Output            |
# +------+------------------------------+---------------------------+
# |  1   | i = 10                       | i = 10                    |
# |  2   | print('before disp', i)      | this is show before disp 10|
# |  3   | nonlocal i                   | ab disp, show ka i change |
# |      |                              | kar sakta hai             |
# |  4   | i = 'hello'                  | i ab 'hello' ho gaya ✅   |
# |  5   | print('this is disp', i)     | this is disp hello        |
# |  6   | print('after disp', i)       | this is show after disp hello|
# +------+------------------------------+---------------------------+

# +------------+--------------------------------+----------------------+
# |  Keyword   |         Kaam                   |      Scope           |
# +------------+--------------------------------+----------------------+
# | global     | File level variable modify karo| Local → Global       |
# | nonlocal   | Outer function variable modify | Local → Enclosing    |
# +------------+--------------------------------+----------------------+




#============================

# Nonlocal ka use karne se inner function outer function ki variable ko modify kar sakta hai ✅
# example me, disp() ke andar nonlocal i likhne se, disp() show() ke i ko modify kar sakta hai.
#  Isse pehle, disp() ke andar i = 'hello' likhne se ek naya local variable i ban jaata, aur show() ke i ko koi farak nahi padta tha.
#  Ab nonlocal ke saath, disp() ke andar i = 'hello' likhne se show() ke i bhi 'hello' ho jaata hai!


# Bina nonlocal kya hota:


# def disp():
#     i = 'hello'   # naya LOCAL i ban jaata
#                   # outer i = 10 change nahi hota ❌

# # Output hota:
# # this is show before disp 10
# # this is disp hello
# # this is show after disp 10  ← 10 hi rehta!