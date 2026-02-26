weight= float(input(" enter weight"))

if weight>=0 and weight<40:
    print("UNDERWEIGHT")
elif weight>=40 and weight <60:
    print(" normal weight")
elif weight>=60 and weight <80:
    print("OVERWEIGHT")
else:
    if weight>=80 and weight <=100:
        print("OBESE")
    else:
        print("invalid weight")