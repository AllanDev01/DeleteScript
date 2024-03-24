from colorama import Fore
import os

nom_dossier = "Data1D"
chemin_fichier = ""
liste_donnees = []
contenu_dossier =  os.listdir(nom_dossier)
size_dossier = len(contenu_dossier)
count_fichier = 0
pourcentage_progression = 0


# Parcourir tous les fichiers CSV du dossier, triés par ordre alphabétique
for fichier in sorted(os.listdir(nom_dossier)):
    pourcentage_progression = round( (count_fichier*100/size_dossier),2)
    print("PROGRESSION :",Fore.RED,str(pourcentage_progression)+" %",Fore.RESET,end="\r")
    count_fichier+=1
    

    chemin_fichier = os.path.join(nom_dossier, fichier)

    if os.path.exists(chemin_fichier):
        # Supprimez le fichier
        os.remove(chemin_fichier)
    else:
        print("Le fichier n'existe pas.")

