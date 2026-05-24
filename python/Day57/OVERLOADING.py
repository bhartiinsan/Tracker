class point2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        newx=self.x+other.x
        newy=self.y+other.y
        p=point2d(x=newx,y=newy)
        return p

    def __mul__(self,other):        # multiplication method
        newx=self.x*other.x
        newy=self.y*other.y
        p=point2d(x=newx,y=newy)
        return p

p1=point2d(x=2,y=4)
p2=point2d(x=5,y=3)

p3=p1+p2                           #p1.__add__(p1,p2)
print(p3.x,p3.y)

p4=p1+p2+p3
print(p4.x,p4.y)

p5=point2d(x=1,y=1)

p6=p1+p2+p3+p4+p5
print(p6.x,p6.y)

print(p1*p2)                       #p1.__mul__(p1,p2)