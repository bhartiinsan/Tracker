Weight= int(input("ENTER THE WEIGHT kg :"))
if Weight>=0 and Weight<40:
    print("UNDERWEIGHT")
elif Weight>=40 and Weight <60:
    print(" normal weight") 
elif Weight>=60 and Weight <80:
    print("OVERWEIGHT")
elif Weight>=80 and Weight <=100:
    print("OBESE")
else:
    print("invalid weight")


# reviewed code