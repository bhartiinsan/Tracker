''''
1. WAP to tell whether a student is qualifying for admission or not.
rules:

Marks in Mathematics are greater than or equal to 60 
and marks in physics are greater than or equal to 50 
and marks in chemistry are greater than or equal to 40

OR

Total marks in mathematics, physics and chemistry are greater than
or equal to 200.

OR

Total marks in mathematics and physics are greater than or equal to
150.
'''



m3 = int(input(" Give me the marks of chemistry= "))

if m3>=40:
    print(" You are eligible for further process")

    m2 = int(input(" Give me the marks of physics= "))
    if m2>=50:
        print(" You are eligible for further process")

        m1 = int(input(" Give me the marks of maths= "))
        if m1>=60:
            print(" You are eligible for further process")
            if (m1 + m2) >=150:
                print(" you are eligible for admission , please continue with your last step")
            if ( m1 + m2 + m3 ) >= 200:
                print (" HEY, CONGRATULATIONS, YOU ARE QUALIFIED FOR THE ADMISSION")
            else:
                print(" THANKYOU FOR YOUR TIME, YOU ARE NOT ELIGIBLE")
        else:
            print(" not eligible for final process, thankyou")        
    else:
        print(" not eligible for final process ,thankyou")
else:
    print(" not eligible for final process, thanyou")


    # what i did mistake is that i wrote m1 and m2 and m3 which means, so it is checking the true value of the input and printing the last value
    # example: M1=90, M2= 67, M3 45    :90 -> true, 67-> true and 45 -> true , SO IT WILL RESULT THE THIRD VALUE 45























    
    
    
    m1 = int(input("Give me the marks of Maths: "))
    m2 = int(input("Give me the marks of Physics: "))
    m3 = int(input("Give me the marks of Chemistry: "))

   
if (m1 >= 60 and m2 >= 50 and m3 >= 40) or (m1 + m2 + m3 >= 200) or (m1 + m2 >= 150):
    print("CONGRATULATIONS, YOU ARE ELIGIBLE FOR ADMISSION")
else:
    print("SORRY, YOU ARE NOT ELIGIBLE")
    
    
    
    
    
