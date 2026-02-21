#THEORY OF BITWISE OPERATORS

'''

Bitwise operators work on binary bits (0 & 1) of integers instead of normal decimal values.

 Computers store numbers in binary, so these operators are useful in:

👉Hardware control (Raspberry pi)

👉Flags & permissions

👉Embedded systems

👉Performance optimizations

👉Set Theory Implementation (Union, Intersection, etc.)

👉Masking (filtering rows) in NUMPY & PANDAS LIBRARY

👉Chaining in langchain framework (GenAI)

👉Faster execution (left / right shifts) than (arithmetic)

👉IOT / Embedded coding (IOT is where internet  is used to operate devices/ appliances/sensors) and Embedded coding is done by without usage of internet 

🧠 First, Understand Binary

| Decimal | Binary |
| ------- | ------ |
| 1       | 0001   |
| 2       | 0010   |
| 3       | 0011   |
| 4       | 0100   |
| 5       | 0101   |
| 6       | 0110   |
| 7       | 0111   |
| 8       | 1000   |
| 9       | 1001   |
| 10      | 1010   |
| 11      | 1011   |
| 12      | 1100   |
| 13      | 1101   |
| 14      | 1110   |
| 15      | 1111   |
| 16      | 10000  |
| 17      | 10001  |
| 18      | 10010  |
| 19      | 10011  |
| 20      | 10100  |

they are represented in 4 bits (nibble) or 8 bits (byte) or more depending on the size of the number.
the rightmost bit is the least significant bit (LSB) and the leftmost bit is the most significant bit (MSB).
the value of each bit is determined by its position, with the LSB having a value of 1, the next bit having a value of 2, then 4, 8, and so on, doubling for each position to the left.
so the binary representation of 5 (0101) can be calculated as:
(0 * 8) + (1 * 4) + (0 * 2) + (1 * 1) = 0 + 4 + 0 + 1 = 5

so these are the 6 bitwise operators in python:
1. Bitwise AND (&)
2. Bitwise OR (|)
3. Bitwise XOR (^)
4. Bitwise NOT (~)
5. Left Shift (<<)
6. Right Shift (>>)

and binary literals in python are represented with a prefix '0b' followed by the binary digits. for example:
x = 0b1010  # This is the binary representation of the decimal number 10
y = 0b1100  # This is the binary representation of the decimal number 12

whereas hexadecimal literals are represented with a prefix '0x' followed by the hexadecimal digits. for example:
a = 0x1A  # This is the hexadecimal representation of the decimal number 26
b = 0x2F  # This is the hexadecimal representation of the decimal number 47

OCTAL literals are represented with a prefix '0o' followed by the octal digits. for example:
c = 0o17  # This is the octal representation of the decimal number 15
d = 0o25  # This is the octal representation of the decimal number 21





THEIR USES IN PYTHON:
1. Bitwise AND (&): Used to check if specific bits are set in a number. For example, to check if the 2nd bit is set in a number, you can use (number & 0b10).
2. Bitwise OR (|): Used to set specific bits in a number. For example, to set the 3rd bit in a number, you can use (number | 0b100).
3. Bitwise XOR (^): Used to toggle specific bits in a number. For example, to toggle the 1st bit in a number, you can use (number ^ 0b1).
4. Bitwise NOT (~): Used to invert all bits in a number. For example, to invert the bits of a number, you can use (~number).
5. Left Shift (<<): Used to shift bits to the left, effectively multiplying the number by 2 for each shift. For example, to shift a number left by 2 bits, you can use (number << 2).
6. Right Shift (>>): Used to shift bits to the right, effectively dividing the number by 2 for each shift. For example, to shift a number right by 3 bits, you can use (number >> 3).


✅ 1. AND Operator (&)

Compares bits → 1 only if BOTH bits are 1
x = 0b1010  # 10 in decimal
y = 0b1100  # 12 in decimal

a = 5   # 101
b = 3   # 011

print(a & b)  # Output: 1 (001 in binary) 
print(x & y)  # Output: 8 (1000 in binary) 

print(5 & 3) # Output: 1 (001 in binary)
print(10 & 12) # Output: 8 (1000 in binary)

✅ 2. OR Operator (|)
Compares bits → 1 if at least ONE bit is 1
1 if either bit is 1, otherwise 0
x = 0b1010  # 10 in decimal 
y = 0b1100  # 12 in decimal

a = 5   # 101
b = 3   # 011

print(a | b)  # Output: 7 (111 in binary)
print(x | y)  # Output: 14 (1110 in binary)


print(5 | 3) # Output: 7 (111 in binary)
print(10 | 12) # Output: 14 (1110 in binary)


✅ 3. XOR Operator (^)

Compares bits → 1 if bits are DIFFERENT, otherwise 0
x = 0b1010  # 10 in decimal
y = 0b1100  # 12 in decimal

a = 5   # 101
b = 3   # 011

print(a ^ b)  # Output: 6 (110 in binary)
print(x ^ y)  # Output: 6 (0110 in binary)

print(5 ^ 3) # Output: 6 (110 in binary)
print(10 ^ 12) # Output: 6 (0110 in binary)


✅ 4. NOT Operator (~)
Flips bits (inverts 0 ↔ 1)
Inverts bits → 0 becomes 1, and 1 becomes 0
x = 0b1010  # 10 in decimal
y = 0b1100  # 12 in decimal

a = 5   # 101
b = 3   # 011

print(~a)  # Output: -6 (in binary: ...11111010)
print(~b)  # Output: -4 (in binary: ...11111100)

print(~5)
Why result is -6?

Because Python uses 2’s complement representation.


✅ 5. Left Shift (<<)
Shifts bits to the left, filling with 0s on the right
x = 0b1010  # 10 in decimal
y = 0b1100  # 12 in decimal
a = 5   # 101
b = 3   # 011
print(a << 1)  # Output: 10 (1010 in binary)
print(a << 2)  # Output: 20 (10100 in binary)
print(5 << 1) # Output: 10 (1010 in binary)
print(5 << 2) # Output: 20 (10100 in binary)
print(x << 1)  # Output: 20 (10100 in binary)
print(x << 2)  # Output: 40 (101000 in binary)
print(y << 1)  # Output: 24 (11000 in binary)
print(y << 2)  # Output: 48 (110000 in binary)

✅ 6. Right Shift (>>)
Shifts bits to the right, filling with 0s on the left (for positive numbers)
x = 0b1010  # 10 in decimal
y = 0b1100  # 12 in decimal
a = 5   # 101
b = 3   # 011
print(a >> 1)  # Output: 2 (10 in binary)
print(a >> 2)  # Output: 1 (1 in binary)
print(5 >> 1) # Output: 2 (10 in binary)
print(5 >> 2) # Output: 1 (1 in binary)
print(x >> 1)  # Output: 5 (101 in binary)
print(x >> 2)  # Output: 2 (10 in binary)
print(y >> 1)  # Output: 6 (110 in binary)
print(y >> 2)  # Output: 3 (11 in binary)





'''

#🎯 Practical Use Case — Bit Masking
#Bit masking is a technique used to manipulate specific bits in a binary number. It involves using bitwise operators 
# to set, clear, or toggle specific bits while leaving others unchanged.


##Extract specific bit:

num = 5  # 101

print(num & 1)  # Check last bit

#✔ Output → 1 (odd number)

#WHAT IT IS DOING?
# It is performing a bitwise AND operation between the number (5) and 1 (which is 0001 in binary).
# The result will be 1 if the last bit of the number is 1 (indicating an odd number) and 0 if the last bit is 0 (indicating an even number).


#------------------------------------------------------------------------------------------------------

#🎯 Practical Use Case — Setting a Bit
#Setting a bit means changing a specific bit to 1 without affecting the other bits. 
# This can be done using the bitwise OR operator (|) along with a bit mask that has the target bit set to 1.


num = 4  # 100
num = num | (1 << 0)  #LEFT SHIFT (1 << 0) = 1 (0001 in binary)

print(num)

#✔ Output → 5 (101 in binary, last bit set to 1)

#WHAT IT IS DOING?
# It is performing a bitwise OR operation between the number (4) and the result of (1 << 0).
# The expression (1 << 0) shifts the binary representation of 1 to the left by 0 positions, resulting in 1 (0001 in binary).
# The bitwise OR operation sets the last bit of the number to 1, resulting in 5 (101 in binary).


#-------------------------------------------------------------------------------------------------------

#🎯 Practical Use Case — Clearing a Bit

#Clearing a bit means changing a specific bit to 0 without affecting the other bits. 
# This can be done using the bitwise AND operator (&) along with a bit mask that has the target bit set to 0 and all other bits set to 1.


num = 5  # 101
num = num & ~(1 << 0)

print(num)

#✔ Output → 4 (100 in binary, last bit cleared to 0)

#WHAT IT IS DOING?
# It is performing a bitwise AND operation between the number (5) and the result of ~(1 << 0).
# The expression (1 << 0) shifts the binary representation of 1 to the left by 0 positions, resulting in 1 (0001 in binary).
# The bitwise NOT operator (~) inverts the bits of 1, resulting in -2 (in binary: ...11111110).
# The bitwise AND operation clears the last bit of the number, resulting in 4 (100 in binary).



'''
| Operator    | Symbol | Meaning             |              |
| ----------- | ------ | ------------------- | ------------ |
| AND         | `&`    | Both bits must be 1 |              |
| OR          | `|`    | Any bit is 1        |              |
| XOR         | `^`    | Bits different      |              |
| NOT         | `~`    | Flip bits           |              |
| Left Shift  | `<<`   | Shift left (×2)     |              |
| Right Shift | `>>`   | Shift right (÷2)    |              |



'''