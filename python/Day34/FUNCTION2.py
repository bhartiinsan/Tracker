# vARIABLE LENGTH KEYWORD

# def show(**a):
#     print(a)
# show() # dict
# show(roll=101, name="sonu", course="DA")
# show(matches=50, ruma=5000, sv= 123.54,
#      team="india", name="sonu")

#***********************************

# ARGUMENTS- TUPLE
#KEYWORDS = DICT

# def sh(*args,**kwargs):
#     print(args)
#     print(kwargs)
# sh(10,20,30,a=40,b=50)

# # (10, 20, 30)
# {'a': 40, 'b': 50}

#======================================================

# ARGUMENTS- TUPLE
#KEYWORDS = DICT

# def sho(a,b,*args,**kwargs):
#     print(a,b)
#     print(args)   #tuple
#     print(kwargs) #dic

# sho(1,2,3,4,x=10,y=20,z=30)

#=========================================================
#/ -- this forces to pass positional arguments
#  (/) ISKE AAGE SAB 


# def sh(a,b,/):
#     print(a,b)
# sh(10,20)
# sh(a=10,b=20) --- keyword arguments are not allowed


#=====================================================================
#* -- this forces to give keyword arguments
# (*) ISKE PICHE SAB

# def s(*,a,b):
#     print(a,b)
# s(a=10,b=20)

# s(1,2) ---- [positional arg not allowed]

#=====================================================================

#a,b----> positional values only (/) ISKE AAGE SAB 
#c,d---->positional or keyword  (NOTHING IS PAASES)
#e,f----> keyword only (*) ISKE PICHE SAB


def l(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)

# l (1,2,c=3,4,e=5,f=6) ------ YOU CAN'T GIVE KEYWORD ARGS c=3 before positional args(4)
l(1,2,3,4,e=5,f=6)
l(1,2,3,d=4,e=5,f=6)

#=====================================================================






