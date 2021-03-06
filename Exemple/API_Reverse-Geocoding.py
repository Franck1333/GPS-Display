#Aide API Reverse-Geocoding
#https://gist.github.com/bradmontgomery/5397472

#import requests


#from urllib2 import urlopen
from urllib.request import urlopen

def traitement():
    # grab some lat/long coords from wherever. For this example,
    # I just opened a javascript console in the browser and ran:
    #
    # navigator.geolocation.getCurrentPosition(function(p) {
    #   console.log(p);
    # })
    #
    latitude = 35.1330343
    longitude = -90.0625056

    # Did the geocoding request comes from a device with a
    # location sensor? Must be either true or false.
    sensor = 'true'

    # Hit Google's reverse geocoder directly
    # NOTE: I *think* their terms state that you're supposed to
    # use google maps if you use their api for anything.
    base = "http://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&sensor={sen}".format(
        lat=latitude,
        lon=longitude,
        sen=sensor
    )
    url = "{base}{params}".format(base=base, params=params)
 
    global response
    response = requests.get(url)
    print(response.json()['results'][0]['formatted_address'])

    return response.json()['results'][0]['formatted_address']
    return response

#while True:
   #print (response)
