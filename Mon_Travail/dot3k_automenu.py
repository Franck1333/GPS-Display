#!/usr/bin/env python
# -*- coding: cp1252 -*-

from dot3k_affichage_determination import determination_dot3k
from dot3k_affichage_meteo import meteo_dot3k
from nettoyage_du_cache import clear_cache

import dot3k.lcd as lcd
import time

print("""
Ce fichier va afficher sur le DOT3K, Le Menu.
""")

while True:
    
    print("""
    Demarrage ordonee des Fonctions.
    """)
    
    #print("Nettoyage de Printemps des Fichiers caches du Projet")
    
    time.sleep(13)
    determination_dot3k()
    time.sleep(13)
    meteo_dot3k()
    time.sleep(1)
    clear_cache()
    time.sleep(3)
