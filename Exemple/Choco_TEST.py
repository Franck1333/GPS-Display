#!/usr/bin/env python
# -*- coding: cp1252 -*-

import serial
import time
import os
import sys


#global mot
mot = "ChoColAt"
#mot = 2

#---DIALOGUE DEBUT---
print("Passe moi le Chocolat , plz!!!")
time.sleep(3)
print("Heu...")
time.sleep(2)
print("Attend...")
time.sleep(4)
print("Je l'ai...")
print("Tient!!!")
time.sleep(2)
#---DIALOGUE FIN---

mot_valid = isinstance(mot,str) #<-- TEST

if mot_valid == True :
    print(mot)
else :
    print("mdr Franck, C'est de la Chantilly !!!")


#PROGRAMME DE TESTING D'UNE VARIABLE SI ELLE EST STRING OU PAS
#La methode isinstance retourne un Boolean si Valide = True sinon False 
