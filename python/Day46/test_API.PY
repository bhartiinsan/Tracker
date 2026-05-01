# PK MOVIE INFO

# API= "http://www.omdbapi.com/?i=tt2338151&apikey=f4a48be6"
# import requests
# response = requests.get(API)
# data = response.json()  # dictinoary
# print(data['Title'])
# print(data['Released'])
# print(data['Runtime'])
# print(data['Actors'])

#============================================================

# API= "http://www.omdbapi.com/?i=tt0248126&apikey=f4a48be6"
# import requests
# response = requests.get(API)
# data = response.json()  # dictinoary
# print(data)

## How to do by naming a movie name
API= "http://www.omdbapi.com/?t=3%20Idiots&apikey=f4a48be6"
import requests         
response = requests.get(API)
data = response.json()  # dictinoary
print(data)

#3 Idiots logic of writing api 3%20Idiots
# space is not allowed in api so we have to write %20 instead of space