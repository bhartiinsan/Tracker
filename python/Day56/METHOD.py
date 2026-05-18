#CLASS K ANDAR FUNCTION DEFINE IS CALLED METHOD

# METHOD IS OF 3 TYPES
# INSTANCE METHOD
# CLASS METHOD
# STATIC METHOD



#INSTANCE METHOD
class test:          # instance  method
    def ml(self):
        print("this is ml")

# class method

    @classmethod
    def m2(cls):    #class method
        print(" this is m2")

        

    @staticmethod
    def m3():         # static method
        print("this is m3")

    def m4():         # static method
        print(" this is m4")


t=test()
t.ml()    # interpreter       t.m1
test.m2() # interpreter     test.m2
test.m3() # by interpreter  test.m3()
test.m4() # by interpreter   test.m4()




