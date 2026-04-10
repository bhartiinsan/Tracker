#QUESTIONS

#1. IMPLEMENT DIVISION LOGIC BASZED ON MARKS AS PARAMETER
# #  #DIVISION(56)-->2ND
# #  #DIVISION(12)-->FAIL 


# def division(a):
#     if a < 25:
#         print("FAIL")
#     elif 25 <= a < 50:
#         print("3RD POSITION")
#     elif 50 <= a < 75:
#         print("2ND POSITION")
#     elif 75 <= a <= 100:
#         print("1ST POSITION")
#     else:
#         print("Invalid Marks")


#========================================================
# # Test cases
# division(56) # Output: 2ND POSITION
# division(100) # Output: 1ST POSITION
# division(24) # Output: FAIL


# division(25) 3RD POSITION
#========================================================


#2. IMPLEMENT BILL DETAILS LOGIC FOR BILL AND GST PARAMETERS
    #BILL_DETAIL(245,5)
    #---BILL
    #---GST
    #---FINAL BILL


def bill_details(a,b):
    # a= int(input(" ENTER THE AMOUNT "))
    b= a*b/100
    c=b
    bill=a+c
    print(bill)

bill_details(2000,5)

#===========================================================================

