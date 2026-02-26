marks = float(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 60:
    print("First Division")

elif marks >= 50:
    print("Second Division")

elif marks >= 40:
    print("Third Division")

else:
    print("Fail")