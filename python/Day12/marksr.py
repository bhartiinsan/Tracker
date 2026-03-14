marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))
marks4 = int(input("Enter marks of subject 4: "))
marks5 = int(input("Enter marks of subject 5: "))

if marks1>=40:
    if marks2>=40:
        if marks3>=40:
            if marks4>=40:
                if marks5>=40:
                 total = marks1 + marks2 + marks3 + marks4 + marks5
                percentage = (total / 500) * 100

                if percentage >= 60:
                    print("First Division ")

                elif percentage >= 50 and percentage<=59:
                    print("Second Division ")

                elif percentage >= 40 and percentage<50:
                    print("Third Division ")

                else:
                    print(" You have failed ")
    
            else:
                print(" fail in 5th subject")
        else:
            print(" fail in 4th subject")
    else:
        print(" fail in 3 rd subject")

else:
    print(" fail inn 1st subject")            

