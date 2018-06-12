#!/usr/bin/env python
# -*- coding: cp1252 -*-

import serial
import time
import os
import sys
import datetime

import dot3k.lcd as lcd
import dot3k.backlight as backlight

#Méthode gérant le BARGRAPH du DOT3K
# Clear the LCD and display Hello World
lcd.clear()
lcd.write("Hello World")

# Turn off the backlight
backlight.rgb(254, 254, 254)

#PARAMETRAGE BARGRAPH --DEBUT--
for i in range(13):
    backlight.set_graph(i / 13.0)
    time.sleep(0.05)
#PARAMETRAGE BARGRAPH --FIN--
