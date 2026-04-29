import random
num=random.randint(1,10)
print(num)

otp=random.randint(1000,9999)
print(otp)

num=random.uniform(1,10)
print(num)

print(round(num,2))
print(f"{num:.2f}")

roll=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(roll)
print(roll)

coupons=[1,2,3,4,5,6,7,8,9,10]
winner=random.choice(coupons)
print(winner)

coupons=[1,2,3,4,5,6,7,8,9,10]
winners=random.choices(coupons,k=3)  #same element may be picked multiple times
print(winners)                        #(sampling with replacement)

winners=random.sample(coupons,k=3)   #same element is picked only one time
print(winners)                        #(sampling without replacement)