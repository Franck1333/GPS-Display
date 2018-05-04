#!/usr/bin/env python


#Aides :
#https://gist.github.com/Lauszus/5785023
#https://raspberry-pi.developpez.com/cours-tutoriels/projets-rpi-zero/traceur-gps/

import serial
import time
import os
import sys

# Set up serial Configure le Recepteur G.P.S :
#ser = serial.Serial(
    #port='/dev/ttyACM0',\ #A CHANGER!!!
    #baudrate=4800,\						#Vitesse de Transmission du Recepteur G.P.S
    #parity=serial.PARITY_NONE,\			#Parite [Serie]
    #stopbits=serial.STOPBITS_ONE,\		#Bit de Stop [Serie]
    #bytesize=serial.EIGHTBITS,\			#Taille des Bits [Serie]
        #timeout=1)						#Temps d'attente

ser = serial.Serial('/dev/ttyACM0',4800,timeout=1) # Open Serial port Configure le Recepteur G.P.S 

#Recuparation des informations de la Trame GPRMC contenant les coordonnees GPS principales

# Helper function to take a $GPRMC sentence, and turn it into a Python dictionary.
# This also calls degrees_to_decimal and stores the decimal values as well.
def parse_GPRMC(data):
    data = data.split(',')
    dict = {
            'fix_time': data[1],
            'validity': data[2],
            'latitude': data[3],
            'latitude_hemisphere' : data[4],
            'longitude' : data[5],
            'longitude_hemisphere' : data[6],
            'speed': data[7],
            #'true_course': data[8],
            #'fix_date': data[9],
            #'variation': data[10],
            #'variation_e_w' : data[11],
            'checksum' : data[12]
    }

    return dict

def envoie():

    print (gpsData)
    return gpsData

while True:

    line = ser.readline() #Lecture Ligne par Ligne

    if "$GPRMC" in line: # This will exclude other NMEA sentences the GPS unit provides.       SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line) # Turn a GPRMC sentence into a Python dictionary called gpsData #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE

        envoie();
