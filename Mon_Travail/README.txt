Pour que ce projet fonctionne on a besoin : 

HARDWARE :	

	- Une Raspberry Pi
	- Un G.P.S USB (Ublox-7)
	- Une Carte Micro S.D (8 Gb Minimum)
	- Un écran (Diplayotron 3000 ou autre lcd)

SOFTWARE :

	- Python version 2 et 3
	- Bibliothèques Python :
		-serial
		-time
		-os
		-sys
		- from urllib2 import urlopen
		 #from urllib.request import urlopen
		-json
		-googlemaps (API GOOGLEMAPS pip install -U googlemaps)
		-datetime
		-pyowm (API METEO // pip install pyowm)

	- Raspian Wheezy/Strentch ou ultérieur
	
Display'O'Tron 3000
	- Github : https://github.com/pimoroni/displayotron
	- Setup : curl -sS get.pimoroni.com/displayotron | bash
	- Repertoire 'plugins'
	- Repertoire 'utils'
	- Fichier 'dot3k.cfg'
	- Repertoire 'library'
_____________________________________________________________________________________________________________________________
Voici les différents fichiers utiles dans le dossier /Mon_Travail/ :

Start_GPS.sh : Permet de Lancer le Projet dans son entierté

Recuperation_GPS.py : Permet d'afficher les information reçu du Stick GPS en Anglais

Recuperation_FR_GPS.py : Permet d'afficher les information reçu du Stick GPS en Français

Recuperation_Determination.py : Permet de Recuperer les informations reçu provenant du Stick GPS et Determiné où nous sommes puis d'agir en conséquence des résultats

Meteo.py : Traitement des Coordonées GPS pour obtenir la Météo local en temps réel

dot3k_clear.py : Efface la Zone affichable du DOT3K

dot3k_automenu.py : Menu Principal pour le projet et l'utilisation du DOT3K

dot3k_affichage_meteo.py : Traitement de l'affichage des données recuperer et determine par le Fichier Meteo.py

dot3k_affichage_determination : Traitement de l'affichage des données recuperer et determine par le Fichier Recuperation_Determination.py

dot3k.cfg : Fichier de Configuration de l'afficheur DOT3K 