#!/usr/bin/env python
# -*- coding: cp1252 -*-

import serial
import time
import os
import sys
import datetime

import dot3k.lcd as lcd
import dot3k.backlight as backlight

#Méthode gérant la lumière du DOT3K

while True :

    #ROUGE
    #Affichage ROUGE pour les ERREURS
    print("Affichage ROUGE")
    backlight.rgb(255, 0, 0)    #Paramètre RGB Lumiere

    lcd.clear()
    lcd.write("ROUGE")
    time.sleep(3)

    #VERT
    #Affichage VERT pour les SUCCES
    print("Affichage VERT")
    backlight.rgb(0, 255, 0)    #Paramètre RGB Lumiere

    lcd.clear()
    lcd.write("VERT")
    time.sleep(3)

    #BLEU
    #Affichage BLEU pour AUTRES
    print("Affichage BLEU")
    backlight.rgb(0, 0, 255)    #Paramètre RGB Lumiere

    lcd.clear()
    lcd.write("BLEU")
    time.sleep(3)

    #BLANC
    #why not
    print("Affichage BLANC")
    backlight.rgb(255, 255, 255)    #Paramètre RGB Lumiere

    lcd.clear()
    lcd.write("BLANC")
    time.sleep(3)

    #BLANC + ROUGE
    print("Affichage BLANC + ROUGE")
    backlight.rgb(255, 240, 255)    #Paramètre RGB Lumiere

    lcd.clear()
    lcd.write("BLANC + RED")
    time.sleep(3)

    #BLANC + VERT
    print("Affichage BLANC + VERT")
    backlight.rgb(240, 255, 255)    #Paramètre RGB Lumiere

    lcd.clear()
    lcd.write("BLANC + VERT")
    time.sleep(3)

    #BLANC + JAUNE
    print("Affichage BLANC + JAUNE")
    backlight.rgb(255, 255, 240)    #Paramètre RGB Lumiere

    lcd.clear()
    lcd.write("BLANC + JAUNE")
    time.sleep(3)

    #SWAGG MODE
    print("Affichage SWAGG")
    backlight.left_rgb(255, 0, 0)   #Paramètre RGB Lumiere (GAUCHE)
    backlight.mid_rgb(255, 0, 255)  #Paramètre RGB Lumiere(CENTRE)
    backlight.right_rgb(0, 0, 255)  #Paramètre RGB Lumiere (DROITE)

    lcd.clear()
    lcd.write("SWAGG MODE ENABLED")
    time.sleep(3)
