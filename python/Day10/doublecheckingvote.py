#NESTED LOOP

nationality =input(" Nation=")  
if nationality == 'India':
    print("Welcome")
    age= int(input("Enter you age = "))
    if age >=18:
        print("eligible to vote , COME")
    else:
        print("NOT ELIGIBLE, YOU ARE UNDER 18")
else:
    print("NOT ELIGIBLE TO VOTE AS YOU'RE NOT INDIAN")
print("thank you")
