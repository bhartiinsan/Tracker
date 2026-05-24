#hybrid = multiple + multilevel
class A:
    def m1(self):
        print('m1 in A')

class B(A):
    def m2(self):
        print('m2 in B')

class C:
    def m3(self):
        print('m3 in C')

class D(B,C):
    def m4(self):
        print('m4 in D')

obj=D()
obj.m1()
obj.m2()
obj.m3()
obj.m4()


#=============================================================================
# diagram

#         A
#         |
#         B          C
#         |         /
#         └────────┘
#              |
#              D


# +-------------+------------+---------------------------+
# |    Type     |  Classes   |        Relation           |
# +-------------+------------+---------------------------+
# | Multilevel  |  A → B     | B inherits A              |
# | Multiple    |  B,C → D   | D inherits B and C both   |
# | Hybrid      |  A→B→D, C→D| Dono ka mix = Hybrid ✅   |
# +-------------+------------+---------------------------+

