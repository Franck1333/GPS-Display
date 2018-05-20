#!/usr/bin/env python
# -*- coding: cp1252 -*-

from dot3k_affichage_determination import determination_dot3k
from dot3k_affichage_meteo import meteo_dot3k

import dot3k.lcd as lcd
import time

print("""
Ce fichier va afficher sur le DOT3K, les valeurs des autre fichier pythons.
""")

while True:

    print("""
    Ce fichier va afficher sur le DOT3K, les valeurs des autre fichier pythons.
    """)
    
    time.sleep(13)
    determination_dot3k()
    time.sleep(50)
    meteo_dot3k()
    time.sleep(1)
