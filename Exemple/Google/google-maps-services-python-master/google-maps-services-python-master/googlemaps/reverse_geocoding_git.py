import json
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCbcLmcGDUQlhvZhAkdE0IUFh90rjJ7rrw')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((47.22239, -0.7298675))

#Accessing the needed part of the response
#reverse_geocode_result[0] # This is a dict
#reverse_geocode_result[0]['address_components'][3]['long_name'] # Return La Region
#reverse_geocode_result[0]['address_components'][4]['long_name'] # Return country 
#reverse_geocode_result[0]['address_components'][2]['long_name'] # Return sublocality
#reverse_geocode_result[0]['address_components'][1]['long_name'] # Return route
#reverse_geocode_result[0]['address_components'][0]['long_name'] # Return street number

#Affichage CONSOLE
print("On se trouve a :")
#print(reverse_geocode_result) Format JSON
print (reverse_geocode_result[0]['formatted_address']) #JSON Parse (trie)



