# FILTER FUNCTION
marks=[56, 87, 67, 88, 47,54,69,55]
res=filter(lambda m:m>=60,marks)
print(list(res))  # filter object ko list me convert karne ke baad hi hum uske elements ko access kar sakte hain

##===================================================================
# NOW FOR EVEN NUMBERS
marks=[56, 87, 67, 88, 47,54,69,55]
res=filter(lambda m:m%2==0,marks)
print(list(res))  # filter object ko list me convert karne ke baad hi hum uske elements ko access kar sakte hain   

#===================================================================

#high order function: jo function dusre function ko as an argument ke roop me accept karta hai ya fir function ko return karta hai usse high order function kehte hain

# that take other function as srgument or return a function as a result are called high order function
#exp= map,filter, decorater, sorted, reduce, etc.