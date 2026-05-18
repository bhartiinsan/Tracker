def show():              #top level(outer) fun
    i = 10
    print('this is show', i)
    def disp():          #closure fun
        print('this is disp', i)
    
    disp()

show()


# Inner function (disp) jo outer function (show) ki
# variable (i) ko ACCESS kar sake —
# even though 'i' disp() me define nahi hai!

# Ye hi CLOSURE hai ✅

#============================

# +------+------------------------+-------------------------+
# | Step |        Code            |        Kya hua          |
# +------+------------------------+-------------------------+
# |  1   | show() call            | show execute shuru      |
# |  2   | i = 10                 | i define hua (local)    |
# |  3   | print('this is show',i)| this is show 10         |
# |  4   | def disp()             | disp define hua         |
# |  5   | disp() call            | disp execute            |
# |  6   | print('this is disp',i)| i=10 — outer se liya ✅ |
# +------+------------------------+-------------------------+


# +---------------------------+---------------------------+
# |      Normal Function      |     Closure Function      |
# +---------------------------+---------------------------+
# | Apne scope ki variable    | Outer function ki         |
# | access karta hai          | variable bhi access       |
# |                           | kar sakta hai ✅          |
# +---------------------------+---------------------------+


##==========================


# L → Local       (disp ke andar)
# E → Enclosing   (show ke andar) ← 'i' yahan hai ✅
# G → Global      (file level)
# B → Built-in    (Python built-in)

# Python pehle L dhundta hai, nahi mila to E, phir G, phir B