#!/usr/bin/env python
# -*- coding: cp1252 -*-

#Aides : https://blog.mozilla.org/webdev/2015/10/27/eradicating-those-nasty-pyc-files/

import serial
import time
import os
import sys

#Supprime les fichiers CACHE du language PYTHON
def clear_cache():
    print("On commence par effacer les fichiers CACHE de Python contenant des informations perimees")
    print("\n")
    #print("Execution de la commande")
    os.system("sudo find . -name '*.pyc' -delete")
    #"Obviously, this can be used for any file type that you wish to eradicate, not just .pyc files."

if __name__ == '__main__':
    clear_cache() #Fonctionnalité qui permet de supprimer les fichiers CACHE produit par l'utilisation du language PYTHON
    
