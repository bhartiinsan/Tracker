# help(list)

# POSITIONAL ONLY PARAMETERS / ISSE PHLE KE PARAMETER POSITIONAL HOTE HAIN

# POSITIONAL=> POSITIONAL ONLY PARAMETERS
# show(10,20) # 10 and 20 are positional arguments
# show(a=10,b=20) # 10 and 20 are keyword arguments
# show(10,b=20) # 10 is positional argument and 20 is keyword

def show(a,b,/):
    print(a,b)

show(10,20) # 10 and 20 are positional arguments
# show(a=10,b=20) # error because a and b are positional only parameters


#====================================================

# help(str)

class ac:
    def cooling(self):
        print("Cooling is a method")

class bike:
    def run(self):
        print("Run is a method")

a= ac()
a.cooling() # method call using object a

# a.run() # error because ac class does not have run method

b=bike()
b.run() # method call using object b

# but if we store as a to bike
# a=bike()
# a.run() # method call using object a

# we can't able to call cooling method using a because a is now reference variable of bike class and cooling
# method is not present in bike class

# a.cooling() # error because cooling method is not present in bike class 

## but now cooling will run
a.cooling() # method call using object a
