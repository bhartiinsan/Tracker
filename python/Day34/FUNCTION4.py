# def even_odd(num):
#     if num%2==0:
#         return"even"
#     else: 
#         return"odd"
    
# r= even_odd(12)
# print(r)

#==============================================================================

# TYPE AANOTATION ( INTRODUCED IN 3,5)

def even_od(num: int) -> str:
        if num %2 == 0:
            return "even"
        else: 
            return "odd"

    
r= even_od(12)
print(r)     # Output: even

