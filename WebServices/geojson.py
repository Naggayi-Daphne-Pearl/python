import urllib.request, urllib.parse, urllib.error
import json 

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location:', )

    #This line checks if the user entered an empty string and, if so, exits the loop using the break statement.
    if len(address) < 1: break

    # This line creates a full URL for the API request by appending the encoded address parameter to the base URL. The urlencode function from the urllib.parse module is used to encode the address as a URL parameter.
    url = serviceurl + urllib.parse.urlencode({'address': address})

    #This line prints the URL of the API request.
    print('Retrieving:', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved:', len(data), 'characters')

    try: 
        js = json.loads(data)
    except: 
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK' :
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print ('lat', lat, 'lng', lng)
    location = js["results"][0]["formatted_address"]
    print('Location:', location)

    print('==== Success To Retrieve ====')