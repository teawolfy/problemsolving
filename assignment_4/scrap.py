import urllib.request
import json
from pprint import pprint

url = "https://maps.googleapis.com/maps/api/geocode/json?address=Prudential%20Tower&key=AIzaSyCf8_TxB2ELtA2kgDQZoVmZJHZZaufoK5w"
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint(response_data)
print(response_data['results'][0]['geometry']['location']['lat'])
