#!/usr/bin/env python
# -*- coding: cp1252 -*-

import serial
import time
import os
import sys
import datetime
import dot3k.lcd as lcd

#OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
#-- DEBUT -- Heure,Minute,Seconde
tt = time.time()
system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
print (system_time)
print ("Temps système affiché")
#-- FIN -- Heure,Minute,Seconde

#-- DEBUT --IMPRESSION DU TEMPS SUR L'AFFICHEUR
lcd.clear()                         #Nettoyage de la Zone Affichable

lcd.set_cursor_position(0,0)        #Positionnement du Curseur à la colonne 0 et ligne 0
lcd.write("Temps Systeme")          #Affichage du String entre guillemet

lcd.set_cursor_position(0,1)        #Positionnement du Curseur à la colonne 0 et ligne 1
lcd.write(system_time)              #Affichage du String entre guillemet

lcd.set_cursor_position(0,2)        #Positionnement du Curseur à la colonne 0 et ligne 1
lcd.write("A l'heure!!!")           #Affichage du String entre guillemet
#-- FIN --IMPRESSION DU TEMPS SUR L'AFFICHEUR

