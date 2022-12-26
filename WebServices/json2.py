import json

data = '''[
    {
        "id": "1",
        "name": "Naggayi"
    }, 
    {
        "id": "2",
        "name": "Daphne"
    }
]'''

info = json.loads(data)
for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
