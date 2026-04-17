# PACKAGE IS USED TO PROVIDE A IDENTITY  TO A MODULE USING LABELS.
# ORGANISING SIMKILR TYPE MODULE.

import python.Day39.science.maths.calculator as calc
res= calc.add(10,5)
print(res)

# package module
from python.Day39.science.maths import calculator as calc
res= calc.add (10,5)
print(res)

#package module's function
from python.Day39.science.maths.calculator import add
res=add(10,5)
print(res)

#---------------------------------------
# WHEN WE RUN WE WILL GET BHARA ODF USEPACK OF MODULE

import python.Day39.science.maths.calculator
res= python.Day39.science.maths.calculator.add(10,5)
print(res)


#===============================================================================

import science.maths.calculator as calc
res= calc.add(2,4)
print(res)

#================================================

