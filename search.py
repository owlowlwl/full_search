import sys
from io import BytesIO
import requests
from PIL import Image
from scale import get_spn

toponym_to_find = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
delta = "0.005"
spn = ','.join(get_spn(toponym))
map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": spn,
    "l": "map",
    "pt": f"{toponym_longitude},{toponym_lattitude},pm2rdm"}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(response.content)).show()
