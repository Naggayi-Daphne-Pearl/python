import json

data = '''{
    "name": "Daphne", 
    "age": 25, 
    "gender": "Female", 
    "address": {
        "country": "Uganda",
        "city": "Kampala", 
        "village": "Kira"
    },
    "phone_number": {
        "country": "Uganda",
        "area_code": "256",
        "number": "123123123"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data)
print('Name:', info['name'])
print('Age:', info['age'])
print('Gender:', info['gender'])
print('Address:', info['address'])
print('Hide:', info['email'])
