price_kg=(60,200,250)
qty_kg=(2,3,4)
fruits=["apple","banana","grapes", "orange", "mango"]

gst=0.05
tot_bill=0

print("fruits\tprice/kg\tqty/kg\tamt", sep="\t")
for p,q,f in zip(price_kg, qty_kg, fruits):
    amt=p*q
    tot_bill+=amt
    
    print(f"{f} \t{p} \t\t{q}\t{amt}", sep="\t")

gst_amt=tot_bill*gst
final_bill=tot_bill+gst_amt

print(f"\nTotal Bill={tot_bill}")
print(f"Gst Amount={gst_amt}")
print(f"Final Bill={final_bill}")

#============================================================================

# WHAT IS FROZEN SET
# IT IS IMMUTABLE SET
# IT IS CREATED BY FROZENSET() BUILT IN FUNCTION
s= {10,20,30}
fs= frozenset(s)
print(fs)  # frozenset({10, 20, 30})
print(type(fs))  # <class 'frozenset'>
