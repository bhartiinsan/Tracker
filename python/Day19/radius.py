# r= float(input(" enter r =  "))
# print(f"Area of circle = {3.14*r*2:.3f}")
# print(f"Area of circle = {3.14*r*2:.4f}")
# print(f"Area of circle = {3.14*r*2}")


#==========================================================================


# # fstring
# x=7

# print(f" value = {x}")
# print(f" value = {x:3}") # space padding to make 3 chars wide
# print(f" value = {x:03}") # space padding to make 3 chars wide
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

num = int(input("Enter a number from 1 to 100: "))

while num <= 100:
    print(f"value = {num:03}")
    num += 1