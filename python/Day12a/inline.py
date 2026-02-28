'''
Num=int(input(" Enter the num"))
if Num%2 ==0: print(" even")  # only single statement is allowed # INLINE 
else: print("odd"); print(" thankyou")   # readability get poor

'''

SP= int(input(" Enter the selling price"))
CP= int(input(" Enter the cost price"))
if SP>CP: print(" Profit" , SP-CP)
elif SP<CP: print(" Loss ", CP-SP)
else: print(" no profit no loss")