class cal:
    def __init__(self,a,b) :
        self.x=a
        self.y=b

    def add(self):
            print(self.x +self.y)

    def mul(self):
            print(self.x*self.y)

c= cal(4,5)       
# self object k sath jata hai

c.add()
c.mul()

