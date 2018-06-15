# GPS-Display

## The Functions and Methods per Files

//Start_GPS.sh : Just a command

### Recuperation_Determination.py :

#### degrees_to_decimal(data, hemisphere)
This function is used to convert the Raw data received by the GPS USB stick in a workable format.
```
def degrees_to_decimal(data, hemisphere)
```
#### parse_GPRMC(data)
This function is used to parse the GPRMC data frame but alson is used to tidy up the data received and store those data in some Variable.
In our project, we will use three variables : "Validite", "Decimal_latitude", "Decimal_longitude", and we will return them for a future use and the project
```
def parse_GPRMC(data)
	
	global Validite
	global Decimal_latitude    #VARIABLE GLOBAL CONVERTIS LATITUDE
	global Decimal_longitude   #VARIABLE GLOBAL CONVERTIS LONGITUDE
	
	Validite = dict['Validite']
	Decimal_latitude = dict['decimal_latitude']   #DICTIONNAIRE VARIABLE LATITUDE CONVERTIS
    	Decimal_longitude = dict['decimal_longitude'] #DICTIONNAIRE VARIABLE LONGITUDE CONVERTIS
	
	return Decimal_latitude,Decimal_longitude,Validite #RETOURNE LES VARIABLES CONVERTIS LATITUDE,LONGITUDE
	
```
#### etat_trame()

This function will be usefull to check if the data frame receive from the GPS Stick and the "parse_GPRMC(data)" method are correct or not.
```
def etat_trame()
```
In this function , we will check 5 cases :
##### The First One
In this case , we will check if the variable "Validite" got a string as 'A' . 
WHY ?
Because in the NMEA standard , it's says that when we received the 'A' char , it's mean that the data trame is correct.
```
if Validite == 'A' and Decimal_latitude_valid == True and Decimal_longitude_valid == True :   #Si la variable est valide alors...
```
We will also check that the Decimal_latitude has got a variable that is a float and the same for Decimal_longitude.
HOW?
```
Decimal_latitude_valid = isinstance(Decimal_latitude,float) #<-- TEST
Decimal_longitude_valid = isinstance(Decimal_longitude,float) #<-- TEST
```
	
Those instruction will test if the Decimal_latitude and Decimal_longitude are float or not.
If they're float , isinstance() will return a boolean equal as True.
True for FLOAT,
False for Anything else.

So , in this case , if everything are okay , the program will continue his work.

##### The Second case
In this case we will check if the variable are undefined .
During tests , we got some bugs with undefined variables as "Validite" for example .
So to avoid this kind of problem , I decide to let the system check if those variable are defined or not.
```
elif Validite == None or Decimal_latitude == None or Decimal_longitude == None  : #Sinon alors...
```

To avoid any bugs , we initialize those 3 variables at begining of the file at None , so if the system detect those 3 variables haven't been defined , the program will restart the Main Menu.
```
#---DEBUT---Variables Par Défault---
Validite = None
Decimal_latitude = None
Decimal_longitude = None
#---FIN---Variables Par Défault---
```
##### The Third case
In this case , we will check if the "Decimal_latitude" is a float or Not.
If "Decimal_latitude" isn't a float , the program will restart the Main Menu.
```
elif Decimal_latitude_valid == False : #Sinon alors...
```
##### The Fourth case
In this case , we will check if the "Decimal_longitude" is a float or Not.
If "Decimal_longitude" isn't a float , the program will restart the Main Menu.
```
elif Decimal_longitude_valid == False  : #Sinon alors...
```
##### The Fifth case
In this case , if an unexpected problem occured , the program will restart the Main Menu.
```
else :                                                  #Sinon alors...
```

#### retourne_latitude()
This function , will be used for return the latitude variable to another python file
```
return Retourne_latitude #Retourne la nouvelle Valeur LATITUDE   
```
#### retourne_longitude()
This function , will be used for return the longitude variable to another python file
```
return Retourne_longitude #Retourne la nouvelle Valeur LONGITUDE
```
#### determine()
```
def determine()
```
This function is used for determine the exact position of where you are , by using the "Google Maps" API.

To check if the 3 majors variables are correct, the function nammed "etat_trame()" will be called.

As answer , you will receive a JSON file that the function will parse to find the information that you need.
The function we will print the result in the console and return the result if you need to use it.

```
PARSING:
  resultat_Ville = reverse_geocode_result[0]['formatted_address'] #STRING LOCALISATION DETERMINE
  print (resultat_Ville) #JSON Parse (trie)
  
  return resultat_Ville #RETOURNE LE STRING DE LA LOCALISATION DETERMINE
```

#### determine_less()
```
def determine_less()
```
This function doing the same work as "determine()" function but the Parsed data are not the same.
In the first function we parsed the data to get the exact adress of your position but in this function , you will only get the town of where you're !!!

```
PARSING:
   resultat_Ville_less = reverse_geocode_result[0]['address_components'][2]['long_name'] #STRING LOCALISATION DETERMINE
   print (resultat_Ville_less) #JSON Parse (trie)
    
   return resultat_Ville_less #RETOURNE LE STRING DE LA LOCALISATION DETERMINE
```

### Meteo.py :

#### main_meteo()
In this function, we will use the OWM weather API and we will use a method to send the coordinates and we will get the result through another method.

We will parse the data received and store it into a variable and then print the data .

```
observation = owm.weather_at_coords(retourne_latitude(),retourne_longitude())     #Recuperation des Coordonnees du lieu cible
    z = observation.get_weather()                           #Obtention des donnees meteorologique via les coordonees
    #print(z)                                               #Affichage du Status de l'état de la Meteo et du reference temporelle                      
    z.get_temperature('celsius')['temp']                   #Enregistrement des variables de température dans un objet
    dot3k = z.get_temperature('celsius')['temp']                    #Stockage de la temperature dans une variable dot3k
    print("La Temperature actuel est de:", z.get_temperature('celsius')['temp'])  
    
    return dot3k
```

### dot3k_clear.py :

#### lcd.clear()
We this method , we will be able to clean the DOT3K display area.

### dot3k_automenu.py :
This file , is the MAIN MENU will launch the 3 majors functions of this project as in loop [while True:] : 
- determination_dot3k() --> To display the place where you are on the DOT3K after use the python file 'dot3k_affichage_determination .py' 
- meteo_dot3k() --> To display the Weather of the place you're after use the python file 'dot3k_affichage_meteo.py '
- clear_cache() --> To clean the python cache files by using the python file 'nettoyage_du_cache.py'

We will use some timer between each function to let the user have the time to read the information and also to not make too much request to the API's than possible with the free plan.

### dot3k_affichage_meteo.py :
####  meteo_dot3k()
```
def meteo_dot3k():
```
In this function , we will display the Weather data on the DOT3K display.

Firstly , we will store the weather data received which come from a function 'main_meteo()' come from the Meteo.py file into a variable called 'temp'
```
global temp
temp = main_meteo()
```
After that , we will clean the screen with this function:
```
lcd.clear()                     #Nettoyage de la Zone Affichable
```

Now , we will start to write the data on the display DOT3K:

With this method taht allow us to set the cursor at the column '0' and the line '0' :
```
lcd.set_cursor_position(0,0)    #Positionnement du Curseur à la colonne 0 et ligne 0
```
And we will write a small sentence with this method:
```
lcd.write("Temp Ambiante:")          #Affichage du String entre guillemet
```

And we will continue to set the cursor at the column '0' but at the line '1' for write the weather on the DOT3K screen:
```
lcd.set_cursor_position(0,1)    #Positionnement du Curseur à la colonne 0 et ligne 1
lcd.write(str(temp))            #Affichage de la valeur convertis de FLOAT à STRING via une valeur retourné qui a stocker dans une variable
```

### dot3k_affichage_determination :
#### determination_dot3k()
```
def determination_dot3k():
```
In this function , we will do the same as "dot3k_affichage_meteo.py" python file do but for the place where you are.
```
recup_affichage()               #Demarrage du fichier python Recuperation_Determination.py 
    global ville                    #Déclaration de la variable GLOBAL 'ville'
    ville = determine_less()        #L'information dtermine par un autre fichier python est stocker dans la variable pour être utiliser apès

    #Using the 'lcd.write' way
    lcd.clear()                     #Nettoyage de la Zone Affichable
    
    lcd.set_cursor_position(0,0)    #Positionnement du Curseur à la colonne 0 et ligne 0
    lcd.write("Nous sommes ici:")          #Affichage du String entre guillemet
    
    lcd.set_cursor_position(0,1)    #Positionnement du Curseur à la colonne 0 et ligne 1
    lcd.write(ville)
```
