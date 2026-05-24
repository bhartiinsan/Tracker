#NESTED HAS A RELATIONSHIP

class person:
    name="bharti"
    class brain:
        def thinking(self):
            print(person.name ,"this is thinking")

b= person.brain()
b.thinking()


p1=person()
b1=p1.brain()

p2=person()
b2=p2.brain()

b1.thinking()
b2.thinking()

# NAME SHOULD BE DIFFERENT
# MADE BY USE OF CONSTRUCTOR



