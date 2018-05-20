#!/usr/bin/env python
# -*- coding: cp1252 -*-

#Aides :
#https://gist.github.com/Lauszus/5785023
#https://raspberry-pi.developpez.com/cours-tutoriels/projets-rpi-zero/traceur-gps/
#https://stackoverflow.com/questions/20169467/how-to-convert-from-longitude-and-latitude-to-country-or-city
#https://github.com/googlemaps/google-maps-services-python

import serial
import time
import os
import sys
from urllib2 import urlopen
#from urllib.request import urlopen
import json
import googlemaps #pip install -U googlemaps
from datetime import datetime

ser = serial.Serial('/dev/ttyACM0',4800,timeout=1) # Open Serial port Configure le Recepteur G.P.S

#Recuparation des informations de la Trame GPRMC contenant les coordonnees GPS principales
# Helper function to take HHMM.SS, Hemisphere and make it decimal:
#-------------------------------
def degrees_to_decimal(data, hemisphere):
    try:
        decimalPointPosition = data.index('.')
        degrees = float(data[:decimalPointPosition-2])
        minutes = float(data[decimalPointPosition-2:])/60
        output = degrees + minutes
        if hemisphere is 'N' or hemisphere is 'E':
            return output
        if hemisphere is 'S' or hemisphere is 'W':
            return -output
    except:
        return ""
#-------------------------------    
# Helper function to take a $GPRMC sentence, and turn it into a Python dictionary.
def parse_GPRMC(data):    
    data = data.split(',')
    dict = {
            'Temps_Capture': data[1],
            'Validite': data[2],
            'Latitude': data[3],
            'Latitude_Hemisphere' : data[4],
            'Longitude' : data[5],
            'Longitude_Hemisphere' : data[6],
            'Vitesse': data[7],
            #'Angle': data[8],
            #'fix_date': data[9],
            #'variation': data[10],
            #'variation_e_w' : data[11],
            'Checksum' : data[12]
    }
    dict['decimal_latitude'] = degrees_to_decimal(dict['Latitude'], dict['Latitude_Hemisphere'])
    dict['decimal_longitude'] = degrees_to_decimal(dict['Longitude'], dict['Longitude_Hemisphere'])

    global Validite
    global Latitude
    global Longitude

    global Decimal_latitude    #VARIABLE GLOBAL CONVERTIS LATITUDE
    global Decimal_longitude   #VARIABLE GLOBAL CONVERTIS LONGITUDE

    Validite = dict['Validite']	
    Latitude = dict['Latitude']
    Longitude = dict['Longitude']

    Decimal_latitude = dict['decimal_latitude']   #DICTIONNAIRE VARIABLE LATITUDE CONVERTIS
    Decimal_longitude = dict['decimal_longitude'] #DICTIONNAIRE VARIABLE LONGITUDE CONVERTIS
    
   # return Validite
   # return Latitude
   # return Longitude
   
    return Decimal_latitude,Decimal_longitude #RETOURNE LES VARIABLES CONVERTIS LATITUDE,LONGITUDE
    
   #return dict #Retourne le dictionnaire principale
#-------------------------------

#-------------------------------
def retourne_latitude():
    
    Retourne_latitude = Decimal_latitude #Initialisation de la nouvelle variable � la Latitude pour le partage avec un autre fichier python
    
    return Retourne_latitude #Retourne la nouvelle Valeur LATITUDE   
#-------------------------------
#-------------------------------
def retourne_longitude():
        
    Retourne_longitude = Decimal_longitude #Initialisation de la nouvelle variable � la Longitude pour le partage avec un autre fichier python

    return Retourne_longitude #Retourne la nouvelle Valeur LONGITUDE
#-------------------------------
def determine():
    gmaps = googlemaps.Client(key='AIzaSyCbcLmcGDUQlhvZhAkdE0IUFh90rjJ7rrw') #Cle d'acces A.P.I

# Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((Decimal_latitude, Decimal_longitude)) #Envoie et Recuperation des Donnees

#Accessing the needed part of the response
#reverse_geocode_result[0] # This is a dict
#reverse_geocode_result[0]['address_components'][3]['long_name'] # Return La Region
#reverse_geocode_result[0]['address_components'][4]['long_name'] # Return country 
#reverse_geocode_result[0]['address_components'][2]['long_name'] # Return sublocality
#reverse_geocode_result[0]['address_components'][1]['long_name'] # Return route
#reverse_geocode_result[0]['address_components'][0]['long_name'] # Return street number
    
    print("On se trouve a :")
    #print(reverse_geocode_result) Format JSON

    resultat_Ville = reverse_geocode_result[0]['formatted_address'] #STRING LOCALISATION DETERMINE
    print (resultat_Ville) #JSON Parse (trie)
    
    return resultat_Ville #RETOURNE LE STRING DE LA LOCALISATION DETERMINE
    #return reverse_geocode_result #RETOURNE LA LOCALISATION OBTENUE AU FORMAT JSON
#-------------------------------

#-------------------------------
#NOUS INDICONS UNIQUEMENT LA VILLE ICI
def determine_less():
    gmaps = googlemaps.Client(key='AIzaSyCbcLmcGDUQlhvZhAkdE0IUFh90rjJ7rrw') #Cle d'acces A.P.I

# Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((Decimal_latitude, Decimal_longitude)) #Envoie et Recuperation des Donnees

#Accessing the needed part of the response
#reverse_geocode_result[0] # This is a dict
#reverse_geocode_result[0]['address_components'][3]['long_name'] # Return La Region
#reverse_geocode_result[0]['address_components'][4]['long_name'] # Return country 
#reverse_geocode_result[0]['address_components'][2]['long_name'] # Return sublocality
#reverse_geocode_result[0]['address_components'][1]['long_name'] # Return route
#reverse_geocode_result[0]['address_components'][0]['long_name'] # Return street number
    
    print("Ici c'est :")
    #print(reverse_geocode_result) Format JSON

    resultat_Ville_less = reverse_geocode_result[0]['address_components'][2]['long_name'] #STRING LOCALISATION DETERMINE
    print (resultat_Ville_less) #JSON Parse (trie)
    
    return resultat_Ville_less #RETOURNE LE STRING DE LA LOCALISATION DETERMINE
    #return reverse_geocode_result #RETOURNE LA LOCALISATION OBTENUE AU FORMAT JSON
#-------------------------------

#-------------------------------
def meteo():
    line = ser.readline() #Lecture de la liason serie Ligne par Ligne

    if "$GPRMC" in line: #SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line) #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
#-------------------------------
def recup_affichage():
    line = ser.readline() #Lecture de la liason serie Ligne par Ligne

    if "$GPRMC" in line: #SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line) #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
#-------------------------------        

#---MAIN---
def main():
    line = ser.readline() #Lecture de la liason serie Ligne par Ligne

    if "$GPRMC" in line: #SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line) #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
        
        print(Decimal_latitude)  #AFFICHAGE DE LA VARIABLE CONVERTIS LATITUDE
        print(Decimal_longitude) #AFFICHAGE DE LA VARIABLE CONVERTIS LONGITUDE
        determine(); #FONCTION PERMETTANT DE DETERMINER LA LOCALISATION GRACE AU G.P.S

if __name__ == "__main__":
    main()   