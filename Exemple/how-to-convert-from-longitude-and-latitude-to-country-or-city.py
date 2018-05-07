# https://stackoverflow.com/questions/20169467/how-to-convert-from-longitude-and-latitude-to-country-or-city

from urllib2 import urlopen
import json
def getplace(lat, lon):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    v = urlopen(url).read()
    j = json.loads(v)
    components = j['results'][0]['address_components']
    country = town = None
    for c in components:
        if "country" in c['types']:
            country = c['long_name']
        if "postal_town" in c['types']:
            town = c['long_name']
    return town, country


print(getplace(51.1, 0.1))
print(getplace(51.2, 0.1))
print(getplace(51.3, 0.1))