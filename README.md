# GPS-Display
This project aims to use Satellite's Data (GPS) to determine a High precice localization and do more stuff with that .
## Getting Started
To get a copy of the project , you can go on the GitHub's webpage of the project and click on the green button to download as a .ZIP file.
However , if you're using a prompt on a unix machine use this line :
```
git clone https://github.com/Franck1333/GPS-Display.git
```
### Prerequisites
To use the project , you will need some Hardware:
```
A Raspberry Pi
A USB G.P.S (Ublox-7) -->  http://amzn.eu/aG9vR3t
A Micro S.D card (8 Gb Minimum)
A screen (Diplayotron 3000 or other lcd)
```
And you will also need some libraries and softwares :
```
- Python version 2 and 3
	- Python Libraries:
		-serial
		-time
		-os
		-sys
		- from urllib2 import urlopen
		-json
		-googlemaps (API GOOGLEMAPS pip install -U googlemaps)
		-datetime
		-pyowm (API METEO // pip install pyowm)
    { FOR THE DOT3K in python files :
      import dot3k.lcd as lcd
      import dot3k.backlight as backlight
    }
	- Raspian Wheezy/STRETCH or later
```
Now especially for the Display'O'Tron 3000 in our case
```
	- The Github page : https://github.com/pimoroni/displayotron
	- The command line Setup (need to be install) : curl -sS get.pimoroni.com/displayotron | bash
	- Directory 'plugins'
	- Directory 'utils'
	- File 'dot3k.cfg'
	- Directory 'library'
  ```
  
  ### Installing
  To get and install the files , use this line : git clone https://github.com/Franck1333/GPS-Display.git
  
  ### RUN
  #### First Way to run the project : 
  To run the project , you can run the small script file called "Start_GPS.sh" ; it's will launch the project in the background
  #### Second Way to run the project : 
  To run the project ; if you want to see the console activities , you can launch the file called "Start_GPS.sh" into the Command Line  Prompt with "./Start_GPS.sh"
  #### Third Way to run the project :
  To run the project ; if you want to see the console activities , you can launch the file called "dot3k_automenu.py" into the Command Line  Prompt with "sudo python dot3k_automenu.py"
  #### The Fourth Way to run the project :
  To run the project ; if you want the project run automatically when system start-up :
  Go to launch a Prompt and type:
  ```
  >>sudo nano /etc/rc.local

  AND WRITE before exit 0:
  >> sleep 35  #Give time to the system to boot and get all the data necessary
  >> bash /home/pi/GPS_Display/Mon_Travail/Start_GPS.sh &
  ```
  ## Running the tests
  To test if I received a GPS signals , i used the python files called :
  ```
  Recuperation_GPS.py (English Ver)
  Recuperation_FR_GPS.py (French Ver)
  ```
  ## The Folders and Files
  In this project we've got two Directories
  #### Directories
  "Exemple" : It's show you which examples i used or made to make my project;
  "Mon_Travail" (My Work) : It's Show you the source code of the project
  #### Files in "/GPS-Display/Mon_Travail/"
  ```
  Start_GPS.sh : Allow to launch the project in the entirety

  Recuperation_GPS.py : Allow to display the information come from the GPS USB stick in English

  Recuperation_FR_GPS.py : Allow to display the information come from the GPS USB stick in French

  Recuperation_Determination.py : Allow to get information come from the GPS USB stick and determinate where we are and what to do with variables states

  Meteo.py : Processing of GPS coordinates to get the local weather in real time
  
  nettoyage_du_cache.py : Delete the Python Cache files (*.pyc)

  dot3k_clear.py : Delete the diplayable area of the DOT3K

  dot3k_automenu.py : Main HOME use for the project and to use the DOT3K 

  dot3k_affichage_meteo.py : Processing of the data display that had been get and determinated by the python file called "Meteo.py"

  dot3k_affichage_determination : Processing of the display of the data come from the python file called "Recuperation_Determination.py"

  dot3k.cfg : Configuration file for the DOT3K display 
  ```
  ## Authors

* **Franck ROCHAT** - *Initial work* - [Franck ROCHAT](https://github.com/Franck1333)
