#!/usr/bin/env python
# -*- coding: cp1252 -*-

from dot3k_affichage_determination import determination_dot3k
from dot3k_affichage_meteo import meteo_dot3k

import dot3k.lcd as lcd
import time

print("""
Ce fichier va afficher sur le DOT3K, Le Menu.
""")

while True:

    print("""
    Demarrage ordonee des Fonctions.
    """)
    
    time.sleep(13)
    determination_dot3k()
    time.sleep(13)
    meteo_dot3k()
    time.sleep(1)
