# s= input(" enter the integer")
# len= int(input(" enter the index"))
# if s >len(s):
#     print(s[0:len:2])
# else: 
#     print(" not valid")

# ALTERNATIVE CHAR
# s= input(" enter the integer")
# print(s[0:len(s):2])
s="python"
print(s[1:3:1])
print(s[1:3:])
print(s[1:3])

print(s[:2:1]) # zero hogi start if the step is positive
print(s[:2:-1]) # -1 hogi start , if the step is negative

print(s[2::1]) # defaultstop, it depends on step size sign , if positive default STOP IS INCLUSIVE OF LAST CHARACTER IN FORWARD
print(s[2::-1]) # defaultstop, it depends on step size sign , if NEGATIVE default STOP IS INCLUSIVE OF LAST CHARACTER IN REVERSE

print(s[::2]) # alternative chars
# AGAR STOP LIKTE HO TOH EXCLUSIVE HOTA HAI MINUS1
print(s[::1]) # reverse string
print(s[1:-1]) # middle chars (except first and last)

print(s[2:5:-1]) # empty substring
print(s[5:0]) # empty substring

print(s[1:7])