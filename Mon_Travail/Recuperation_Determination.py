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
import datetime

import dot3k.lcd as lcd

#---DEBUT---Variables Par Défault---
Validite = None
Decimal_latitude = None
Decimal_longitude = None
#---FIN---Variables Par Défault---

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
      
    return Decimal_latitude,Decimal_longitude,Validite #RETOURNE LES VARIABLES CONVERTIS LATITUDE,LONGITUDE
    
   #return dict #Retourne le dictionnaire principale
#-------------------------------

#-------------------------------
def etat_trame(): #Verification de la conformite de la Trame NMEA reçu

    #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
    #-- DEBUT -- Heure,Minute,Seconde
    tt = time.time()
    system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
    #print (system_time)
    #-- FIN -- Heure,Minute,Seconde

    #Zone de TEST --DEBUT--
    #Validite_valid = isinstance(Validite,str) #<-- TEST
    Decimal_latitude_valid = isinstance(Decimal_latitude,float) #<-- TEST
    Decimal_longitude_valid = isinstance(Decimal_longitude,float) #<-- TEST
    #Zone de TEST --FIN--


    #Cette fonction va verifie la conformite de la Trame NMEA reçu par le Stick GPS et relance le Menu Principal si une erreur est detecte en testant la variable 'Validite'
    if Validite == 'A' and Decimal_latitude_valid == True and Decimal_longitude_valid == True :   #Si la variable est valide alors...
        print(Validite)                 #Affichage de la Variable "Validite" dans la console
        print("Trame NMEA Valide")      #Affichage du String entre guillemet
        print("Signal GPS Obtenue")     #Affichage du String entre guillemet
        print (system_time)
        pass #<--   
    

    elif Validite == None or Decimal_latitude == None or Decimal_longitude == None  : #Sinon alors...
        print("elif Variables == None")
        print("Variables Non Utilisable")                           #Affichage du String entre guillemet
        print("Signal GPS Perdue")                                  #Affichage du String entre guillemet
        print("Redemarrage en cours du Programme MENU PRINCIPAL")
        print (system_time)

        #DOT3K CHECK ERROR DISPLAY --DEBUT--
        lcd.clear()                         #Nettoyage de la Zone Affichable

        lcd.set_cursor_position(0,0)        #Positionnement du Curseur à la colonne 0 et ligne 0
        lcd.write("CHECKING VAR")           #Affichage du String entre guillemet
        
        lcd.set_cursor_position(0,1)        #Positionnement du Curseur à la colonne 0 et ligne 1
        lcd.write(system_time)              #Affichage du String entre guillemet

        lcd.set_cursor_position(0,2)        #Positionnement du Curseur à la colonne 0 et ligne 1
        lcd.write("Restart!!!")             #Affichage du String entre guillemet
        #DOT3K CHECK ERROR DISPLAY --FIN--
        
        #Execution du fichier MENU 'dot3k_automenu.py'
        time.sleep(5)
        os.system('python dot3k_automenu.py') #Redemarre le Menu et les fonctions dans le Menu avec <--

    elif Decimal_latitude_valid == False : #Sinon alors...
        print("elif Decimal_latitude_valid == False ")
        print("Variables Non Utilisable")                           #Affichage du String entre guillemet
        print("Signal GPS Perdue")                                  #Affichage du String entre guillemet
        print("Redemarrage en cours du Programme MENU PRINCIPAL")
        print (system_time)

        #DOT3K CHECK ERROR DISPLAY --DEBUT--
        lcd.clear()                         #Nettoyage de la Zone Affichable

        lcd.set_cursor_position(0,0)        #Positionnement du Curseur à la colonne 0 et ligne 0
        lcd.write("CHECKING VAR")           #Affichage du String entre guillemet
        
        lcd.set_cursor_position(0,1)        #Positionnement du Curseur à la colonne 0 et ligne 1
        lcd.write(system_time)              #Affichage du String entre guillemet

        lcd.set_cursor_position(0,2)        #Positionnement du Curseur à la colonne 0 et ligne 1
        lcd.write("Restart!!!")             #Affichage du String entre guillemet
        #DOT3K CHECK ERROR DISPLAY --FIN--
        
        #Execution du fichier MENU 'dot3k_automenu.py'
        time.sleep(5)
        os.system('python dot3k_automenu.py') #Redemarre le Menu et les fonctions dans le Menu avec <--

    elif Decimal_longitude_valid == False  : #Sinon alors...
        print("elif Decimal_longitude_valid == False ")
        print("Variables Non Utilisable")                           #Affichage du String entre guillemet
        print("Signal GPS Perdue")                                  #Affichage du String entre guillemet
        print("Redemarrage en cours du Programme MENU PRINCIPAL")
        print (system_time)

        #DOT3K CHECK ERROR DISPLAY --DEBUT--
        lcd.clear()                         #Nettoyage de la Zone Affichable

        lcd.set_cursor_position(0,0)        #Positionnement du Curseur à la colonne 0 et ligne 0
        lcd.write("CHECKING VAR")           #Affichage du String entre guillemet
        
        lcd.set_cursor_position(0,1)        #Positionnement du Curseur à la colonne 0 et ligne 1
        lcd.write(system_time)              #Affichage du String entre guillemet

        lcd.set_cursor_position(0,2)        #Positionnement du Curseur à la colonne 0 et ligne 1
        lcd.write("Restart!!!")             #Affichage du String entre guillemet
        #DOT3K CHECK ERROR DISPLAY --FIN--
        
        #Execution du fichier MENU 'dot3k_automenu.py'
        time.sleep(5)
        os.system('python dot3k_automenu.py') #Redemarre le Menu et les fonctions dans le Menu avec <--
 
    else :                                                  #Sinon alors...
        print("else conditions")
        print(Validite)                                     #Affichage de la Variable "Validite" dans la console
        print("Trame NMEA NON VALIDE")                      #Affichage du String entre guillemet
        print("Signal GPS Perdue")                          #Affichage du String entre guillemet
        print("Redemarrage en cours du Programme MENU PRINCIPAL")
        print (system_time)

        #DOT3K CHECK ERROR DISPLAY --DEBUT--
        lcd.clear()                         #Nettoyage de la Zone Affichable

        lcd.set_cursor_position(0,0)        #Positionnement du Curseur à la colonne 0 et ligne 0
        lcd.write(system_time)              #Affichage du String entre guillemet
        
        lcd.set_cursor_position(0,1)        #Positionnement du Curseur à la colonne 0 et ligne 1
        lcd.write("Signal GPS Perdue")      #Affichage du String entre guillemet

        lcd.set_cursor_position(0,2)        #Positionnement du Curseur à la colonne 0 et ligne 1
        lcd.write("Restart en cours...")    #Affichage du String entre guillemet        
        #DOT3K CHECK ERROR DISPLAY --FIN--

        #Execution du fichier MENU 'dot3k_automenu.py'
        time.sleep(13)
        os.system('python dot3k_automenu.py') #Redemarre le Menu et les fonctions dans le Menu avec <--

#-------------------------------

#-------------------------------
def retourne_latitude():
    
    Retourne_latitude = Decimal_latitude #Initialisation de la nouvelle variable à la Latitude pour le partage avec un autre fichier python
    
    return Retourne_latitude #Retourne la nouvelle Valeur LATITUDE   
#-------------------------------
#-------------------------------
def retourne_longitude():
        
    Retourne_longitude = Decimal_longitude #Initialisation de la nouvelle variable à la Longitude pour le partage avec un autre fichier python

    return Retourne_longitude #Retourne la nouvelle Valeur LONGITUDE
#-------------------------------
def determine():
    gmaps = googlemaps.Client(key='AIzaSyCbcLmcGDUQlhvZhAkdE0IUFh90rjJ7rrw') #Cle d'acces A.P.I

    etat_trame() #Validation de la conformite de la Trame NMEA <--

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
    etat_trame() #Validation de la conformite de la Trame NMEA <--
    
    gmaps = googlemaps.Client(key='AIzaSyCbcLmcGDUQlhvZhAkdE0IUFh90rjJ7rrw') #Cle d'acces A.P.I    

# Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((Decimal_latitude, Decimal_longitude)) #Envoie et Recuperation des Donnees
    
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
        etat_trame() #Validation de la conformite de la Trame NMEA <--
        determine(); #FONCTION PERMETTANT DE DETERMINER LA LOCALISATION GRACE AU G.P.S

if __name__ == "__main__":
    main()   
