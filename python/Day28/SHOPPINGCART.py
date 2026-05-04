Price_kg= (60,200,250)
Qty_kg= (2,3,4)
fruits = ["apple", "banana", "grapes"]

Gst= 0.05 # 5%
tot_bill=0
for p,q,f in zip(Price_kg, Qty_kg, fruits):
    amt= p*q
    tot_bill+=amt

gst_amt= tot_bill*Gst
final_bill= tot_bill+gst_amt

print(tot_bill)
print(gst_amt)
print(final_bill)

# SHORTEST LENGTH ITERATION KRTA HAI  IF YOU ADD ORANGES THEN IT WILL IGNORE THAT VALUE CAUSE IT IS NOT IN THE OTHER ITERABLES


