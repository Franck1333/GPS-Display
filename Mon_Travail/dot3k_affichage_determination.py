#!/usr/bin/env python
# -*- coding: cp1252 -*-

import dot3k.lcd as lcd
import time

from Recuperation_Determination import recup_affichage
from Recuperation_Determination import determine_less
from Recuperation_Determination import parse_GPRMC

print("""
Ce fichier va afficher sur le DOT3K, la localisation determiné de la ZONE dont la valeur a été recuperer par d'autre fichier pythons.
""")

def determination_dot3k():

    recup_affichage()               #Demarrage du fichier python Recuperation_Determination.py 
    global ville                    #Déclaration de la variable GLOBAL 'ville'
    ville = determine_less()        #L'information dtermine par un autre fichier python est stocker dans la variable pour être utiliser apès

    #Using the 'lcd.write' way
    lcd.clear()                     #Nettoyage de la Zone Affichable
    
    lcd.set_cursor_position(0,0)    #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Nous somme ici:")          #Affichage du String entre guillemet
    
    lcd.set_cursor_position(0,1)    #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(ville)            #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable

if __name__ == "__main__":
    determination_dot3k() #Fonction Affichage sur le DOT3K

