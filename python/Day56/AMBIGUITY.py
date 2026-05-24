#ambiguity(conflict) with multiple inheritance
    #solution--->MRO(Method Resolution Order)
class A:
    def m1(self):
        print('m1 in A')

class B:
    def m1(self):
        print('m1 in B')

class C(A,B):
    pass

obj=C()
obj.m1()

class C(B,A):
    pass

obj=C()
obj.m1()

# Problem — Ambiguity in Multiple Inheritance:

# A aur B dono me m1() hai
# C dono se inherit karta hai
# C ka obj.m1() call kare to — KONSA m1() chalega? 🤔

#============================================================================

#FLOW OF INHERITANCE

# +------+---------------+------------------+--------------------+
# | Step |     Code      |   MRO Order      |     Output         |
# +------+---------------+------------------+--------------------+
# |  1   | class C(A,B)  | C → A → B        | 'm1 in A' ✅       |
# |      | obj.m1()      | A pehle check hua|                    |
# +------+---------------+------------------+--------------------+
# |  2   | class C(B,A)  | C → B → A        | 'm1 in B' ✅       |
# |      | obj.m1()      | B pehle check hua|                    |
# +------+---------------+------------------+--------------------+

##==============================================================================
