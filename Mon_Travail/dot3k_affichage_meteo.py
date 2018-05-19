#!/usr/bin/env python
# -*- coding: cp1252 -*-

import dot3k.lcd as lcd
import time
from dot3k.menu import MenuOption,Menu

from Recuperation_Determination import meteo
from Meteo import main_meteo

import pyowm


print("""
Ce fichier va afficher sur le DOT3K, la temperature exterieur de la ZONE dont la valeur a été recuperer par d'autre fichier pythons.
""")


#-----------------------------------------------------------------------------------------------------------------------------------------------
def meteo_dot3k():
    global temp
    temp = main_meteo()

    #Using the 'lcd.write' way
    lcd.clear()                     #Nettoyage de la Zone Affichable
    
    lcd.set_cursor_position(0,0)    #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Temp EXT:")          #Affichage du String entre guillemet
    
    lcd.set_cursor_position(0,1)    #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(str(temp))            #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable
#-----------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------
#https://github.com/pimoroni/displayotron/tree/master/examples/plugins
#Or use an different way , but i don't succeed to make it works LOL
#Using the 'menu.write_row(x,value)'
#class plugin(MenuOption):
    #def meteo_dot3k(self, menu):
        #temp = main_meteo()        
        #Using the 'menu.write_row(0, 'txt or value here')'
        #menu.write_row(0, 'Temp EXT')
        #menu.write_row(1, temp)
        #menu.clear_row(2)
#-------------------------------------------------------------------


if __name__ == "__main__":
    #plugin.meteo_dot3k(self,menu) #TRY
    meteo_dot3k() #Fonction Affichage sur le DOT3K
       
