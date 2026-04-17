# from calculator import add, mul
from calculator import *

res = add(10, 5)
print(res)

res = mul(10, 5)
print(res)

res = sub(10, 5)
print(res)

res = div(10, 5)
print(res)

#=====================================================================
# WHEN USE import *, ALL THE FUNCTIONS IN THE MODULE ARE IMPORTED, BUT IT IS NOT RECOMMENDED BECAUSE IT CAN CAUSE NAME CLASHES.
# IT IS BETTER TO USE import calculator AS calc, THEN YOU CAN USE calc.add(), calc.mul(), ETC.
# MAIN FUNCTION IN THE MODULE IS EXECUTED ONLY WHEN THE MODULE IS RUN AS A SCRIPT, NOT WHEN IT IS IMPORTED.
#BASICALLY IT HIDES THE TESTING CODE IN THE MODULE, SO IT IS NOT EXECUTED WHEN THE MODULE IS IMPORTED.


def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

if __name__ == "__main__":
    print(add(5, 2))
    print(mul(5, 2))
    print(sub(5, 2))
    print(div(5, 2))