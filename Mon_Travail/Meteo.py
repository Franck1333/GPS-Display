#!/usr/bin/env python
# -*- coding: cp1252 -*-

#Aides :
#https://github.com/csparpa/pyowm #pip install pyowm
#http://pyowm.readthedocs.io/en/latest/index.html

import serial
import time
import os
import sys

from Recuperation_Determination import retourne_latitude
from Recuperation_Determination import retourne_longitude
from Recuperation_Determination import meteo

import pyowm

def main_meteo():
    
    owm = pyowm.OWM('7435ea1b7ee5e31fe1f524a922202510',language = "fr")
    # You MUST provide a valid API key
    # Have a pro subscription? Then use:
    # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
    # Search for current weather in London (Great Britain)
    #observation = owm.weather_at_place('London,GB')
    #w = observation.get_weather()
    #print(w)                      # <Weather - reference time=2013-12-18 09:20,
                                  # status=Clouds>
    # Weather details
    #w.get_wind()                  # {'speed': 4.6, 'deg': 330}
    #w.get_humidity()              # 87
    #w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    #print (w.get_temperature('celsius'))
    # Search current weather observations in the surroundings of
    # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)

    #----------------------------------------------------------------------------------------------------------------------------
    meteo() #MAIN DU FICHIER Recuperation_Determination.py
    observation = owm.weather_at_coords(retourne_latitude(),retourne_longitude())     #Recuperation des Coordonnees du lieu cible
    z = observation.get_weather()                           #Obtention des donnees meteorologique via les coordonees
    #print(z)                                               #Affichage du Status de l'état de la Meteo et du reference temporelle                      
    z.get_temperature('celsius')['temp']                   #Enregistrement des variables de température dans un objet
    dot3k = z.get_temperature('celsius')['temp']                    #Stockage de la temperature dans une variable dot3k
    print("La Temperature actuel est de:", z.get_temperature('celsius')['temp'])             #Selection des informations voulu

    return dot3k
    #----------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main_meteo()   
