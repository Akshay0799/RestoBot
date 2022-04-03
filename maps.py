from asyncore import dispatcher
import requests

# def fetch_restaurant(food):



# url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=45.401540%2C-75.666020&radius=1500&type=restaurant&keyword=burgers&key=AIzaSyAgxrEnF8tod4nqz58axdrI4xWr5zydeJQ"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
#     # return restaurants

import requests
from requests.structures import CaseInsensitiveDict

def fetch_restaurant(food):
    url = "https://api.geoapify.com/v2/places?categories=catering.restaurant."+food+"&filter=circle:-75.665214,45.40205,8000&bias=proximity:-75.665214,45.40205&limit=5&apiKey=daca2f31ca5b4f6a8fb56dea4b85f26d"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    resp = requests.get(url, headers=headers)
    # a ={"type":"FeatureCollection","features":[{"type":"Feature","properties":{"name":"The Works","street":"Bank Street","suburb":"The Glebe","district":"Capital","city":"(Old) Ottawa","county":"Ottawa","state_district":"Eastern Ontario","state":"Ontario","postcode":"K1S 3T4","country":"Canada","country_code":"ca","lon":-75.6913625,"lat":45.4078283,"formatted":"The Works, Bank Street, (Old) Ottawa, ON K1S 3T4, Canada","address_line1":"The Works","address_line2":"Bank Street, (Old) Ottawa, ON K1S 3T4, Canada","categories":["catering","catering.restaurant","catering.restaurant.burger","wheelchair","wheelchair.yes"],"details":["details","details.catering","details.facilities"],"datasource":{"sourcename":"openstreetmap","attribution":"© OpenStreetMap contributors","license":"Open Database Licence","url":"https://www.openstreetmap.org/copyright"},"distance":2146,"place_id":"5191cb7f483fec52c059435abeb733b44640f00103f90189ada9b50000000092030954686520576f726b73"},"geometry":{"type":"Point","coordinates":[-75.69136249999998,45.40782830042419]}},{"type":"Feature","properties":{"name":"Cafe nostalgica","street":"Laurier Avenue East","neighbourhood":"Byward Market","suburb":"Sandy Hill","district":"Rideau-Vanier","city":"(Old) Ottawa","county":"Ottawa","state_district":"Eastern Ontario","state":"Ontario","postcode":"K1N 1K5","country":"Canada","country_code":"ca","lon":-75.683922,"lat":45.4240305,"formatted":"Cafe nostalgica, Laurier Avenue East, (Old) Ottawa, ON K1N 1K5, Canada","address_line1":"Cafe nostalgica","address_line2":"Laurier Avenue East, (Old) Ottawa, ON K1N 1K5, Canada","categories":["catering","catering.restaurant","catering.restaurant.burger"],"details":["details.catering"],"datasource":{"sourcename":"openstreetmap","attribution":"© OpenStreetMap contributors","license":"Open Database Licence","url":"https://www.openstreetmap.org/copyright"},"distance":2848,"place_id":"51f4c0c760c5eb52c059f8e8a5a146b64640f00103f901f72e3b360100000092030f43616665206e6f7374616c67696361"},"geometry":{"type":"Point","coordinates":[-75.683922,45.42403050042225]}},{"type":"Feature","properties":{"name":"The King Eddy","housenumber":"45","street":"Clarence Street","neighbourhood":"Byward Market","suburb":"Lowertown","district":"Rideau-Vanier","city":"(Old) Ottawa","county":"Ottawa","state_district":"Eastern Ontario","state":"Ontario","postcode":"K1N 5P4","country":"Canada","country_code":"ca","lon":-75.6940676,"lat":45.4288022,"formatted":"The King Eddy, 45 Clarence Street, (Old) Ottawa, ON K1N 5P4, Canada","address_line1":"The King Eddy","address_line2":"45 Clarence Street, (Old) Ottawa, ON K1N 5P4, Canada","categories":["catering","catering.restaurant","catering.restaurant.burger"],"details":["details.catering","details.facilities"],"datasource":{"sourcename":"openstreetmap","attribution":"© OpenStreetMap contributors","license":"Open Database Licence","url":"https://www.openstreetmap.org/copyright"},"distance":3734,"place_id":"51a4cd829a6bec52c059c8a191fde2b64640f00103f901db780e230000000092030d546865204b696e672045646479"},"geometry":{"type":"Point","coordinates":[-75.69406759999998,45.42880220042167]}},{"type":"Feature","properties":{"name":"Bite Burger House","housenumber":"108","street":"Murray Street","neighbourhood":"Byward Market","suburb":"Lowertown","district":"Rideau-Vanier","city":"(Old) Ottawa","county":"Ottawa","state_district":"Eastern Ontario","state":"Ontario","postcode":"K1N 5M5","country":"Canada","country_code":"ca","lon":-75.6929002,"lat":45.4298428,"formatted":"Bite Burger House, 108 Murray Street, (Old) Ottawa, ON K1N 5M5, Canada","address_line1":"Bite Burger House","address_line2":"108 Murray Street, (Old) Ottawa, ON K1N 5M5, Canada","categories":["catering","catering.restaurant","catering.restaurant.burger"],"details":["details","details.catering","details.contact","details.facilities"],"datasource":{"sourcename":"openstreetmap","attribution":"© OpenStreetMap contributors","license":"Open Database Licence","url":"https://www.openstreetmap.org/copyright"},"distance":3773,"place_id":"511499147a58ec52c059a41dc11605b74640f00103f9011594fe0901000000920311426974652042757267657220486f757365"},"geometry":{"type":"Point","coordinates":[-75.6929002,45.42984280042154]}},{"type":"Feature","properties":{"name":"Wellington Eatery","housenumber":"1008","street":"Wellington Street West","commercial":"Hintonburg Shopping Area","suburb":"Hintonburg","district":"Kitchissippi","city":"(Old) Ottawa","county":"Ottawa","state_district":"Eastern Ontario","state":"Ontario","postcode":"K1Y 2X9","country":"Canada","country_code":"ca","lon":-75.723403,"lat":45.4048816,"formatted":"Wellington Eatery, 1008 Wellington Street West, (Old) Ottawa, ON K1Y 2X9, Canada","address_line1":"Wellington Eatery","address_line2":"1008 Wellington Street West, (Old) Ottawa, ON K1Y 2X9, Canada","categories":["catering","catering.restaurant","catering.restaurant.burger","internet_access"],"details":["details.catering","details.contact","details.facilities"],"datasource":{"sourcename":"openstreetmap","attribution":"© OpenStreetMap contributors","license":"Open Database Licence","url":"https://www.openstreetmap.org/copyright"},"distance":4567,"place_id":"5102b5183c4cee52c059ad490829d3b34640f00103f901672ef87f0000000092031157656c6c696e67746f6e20456174657279"},"geometry":{"type":"Point","coordinates":[-75.72340299999999,45.40488160042455]}}]}
    resp = resp.json()
    rest = []
    for i in resp['features']:
        restaurant = i['properties']['name']
        street = (i['properties']['street'])
        distance = (i['properties']['distance'])
        address = (i['properties']['formatted'])
        place_id = (i['properties']['place_id'])
        rest.append([restaurant, street, distance, address, place_id])
    # print(rest[0])
    return rest

def fetch_contact(place_id):
    phone = ""
    url1 = "https://api.geoapify.com/v2/place-details?id="+place_id+"&features=details,radius_500,radius_500.restaurant&apiKey=daca2f31ca5b4f6a8fb56dea4b85f26d"
    # print(restaurant)
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    respo = requests.get(url1, headers=headers)
    respo = respo.json()

    if 'contact' in respo['features'][0]['properties'].keys():
        phone = respo['features'][0]['properties']['contact']['phone']
    else:
        phone = "+1-613-461-6787"

    return phone



