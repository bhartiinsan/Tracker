def sqr(num):
    return num ** 2

li=[1,2,3,4,5,6,7,8,9,10]


#1st way ================

sqr(li[0])
sqr(li[1])
sqr(li[2])
#2nd way ================   

li2=[]
for i in li:
    li2.append(sqr(i))
print(li2)

#3rd way ================
map(sqr,li)  # map function me pehla argument function hota hai aur dusra argument iterable hota hai
li2= list(map(sqr,li))
print(li2)

#4th way ================
li2= list(map(lambda x: x**2,li))  # lambda function me hum ek hi expression ko evaluate kar sakte hain
print(li2)
