#!/usr/bin/env python

import time

import dot3k.backlight as backlight
import dot3k.lcd as lcd


print("""
This example shows you different ways of setting the bargraph.
You should see the graph light up in sequence and then fade in.

Press CTRL+C to exit.
""")


# Clear the LCD and display Hello World
lcd.clear()
lcd.write("Hello World")

# Turn off the backlight
backlight.rgb(254, 254, 254)

"""
set_graph accepts a float between 0.0 and 1.0
and lights up the LEDs accordingly
"""
#PARAMETRAGE BARGRAPH --DEBUT--
for i in range(30):
    backlight.set_graph(i / 30.0)
    time.sleep(0.05)
#PARAMETRAGE BARGRAPH --FIN--

"""
set_bar will set a specific bargraph LED to
a brightness between 0 and 255
"""
#for i in range(256):
    #backlight.set_bar(0, [255 - i] * 9)
    #time.sleep(0.01)

backlight.set_graph(0)
