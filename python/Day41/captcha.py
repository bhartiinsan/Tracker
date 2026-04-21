import random
print(ord('a'))
print(ord('A'))

print(chr(100))

li_chs=[]
for i in range(97,123):
    li_chs.append(chr(i))

#print(li_chs)

for i in range(65,91):
    li_chs.append(chr(i))

#print(li_chs)

for i in range(10):
    li_chs.append(i)
    li_chs.append(chr(i))

#print(li_chs)

captcha=random.choices(li_chs,k=6)
print(captcha)

final_captcha=''
for c in captcha:
    final_captcha+=str(c)
print(final_captcha)


#=================================================================

captcha=random.choices(li_chs,k=6)
print(captcha)

final_captcha=''
for c in captcha:
    final_captcha+=str(c)
print(final_captcha)