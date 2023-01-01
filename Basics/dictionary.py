#social media post 

post = {"user_id": 900, "title": "My first post", "lang": "en", "date": "27/09/2022"},
print(type(post)) # Output {'user_id': 900, 'title': 'My second post', 'lang': 'en'}

post2 = dict (user_id = 900, title = "My second post", lang = "en")
print(post2) # Output 

post2["message"] ="I am learning about dictionary"
post2["datetime"] = "27/12/2022"
print(post2) # Output {'user_id': 900, 'title': 'My second post', 'lang': 'en', 'message': 'I am learning about dictionary', 'datetime': '27/12/2022'}

#Accessing values in dictionary
print(post2['message'])

# Accessing a value that isnt in dictionary
loc = post2.get('location', None)
print(loc) #Output: None

#Looping through values in dictionary

# for key in post2.keys():
#     value = post2[key]
#     print(key, "=", value)

# #OR 
for key, value in post2.items():
    print(key, "=", value)

#Remove an item from the dictionary
value = post2.pop("user_id")
print(value)