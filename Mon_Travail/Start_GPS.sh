#!/bin/bash

sudo python /home/pi/GPS_Display/Mon_Travail/dot3k_automenu.py &

#Pour démarrer le projet , il faut démarrer le petit script shell/bash appelé "Start_GPS.sh".
#Pour une meilleure compatibilité , veuillez faire en sorte que tout les droits sont attribuer à tous dans le système d'exploitation pour ne pas avoir de surpises .
#Par ailleurs dans le programme , l'accès aux autres fichiers pythons se font par accès absolu donc , si vous avez changer vos paramètre par défaut sur votre carte raspberry où alors vous utiliser Mes programmes sur une autre plateforme , il vous faut MODIFIER les lignes contenant le méthode suivante : os.system(sudo python FICHIERs).
<<<<<<< HEAD
#Et voilà ^^ , plus facile n'est ce pas .
=======
#Et voilà ^^ , plus facile n'est ce pas .
>>>>>>> 9cd1eb8ef74dcec2cb7527a230ef53625d39e794
