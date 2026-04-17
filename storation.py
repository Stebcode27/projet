import csv
from serial import Serial
import time

PORT = "COM8"   #À vérifier sur ta machine
speed = 115200  #Ca c'est la vitesse de communication que nous avons mis dans le Serial.begin()
fichier = "stockage.csv"    #Le fichier dans lequel les données seront enregistrées

def main():
    ser = Serial(PORT, speed)   #connection à l'interface serie

    print("Enregistrement en cours (Crtl+C pour arrêter)")

    try:
        with open(fichier, "w+", newline='') as file:    #creation et ouverture du fichier de stockage
            writer = csv.writer(file)
            writer.writerow(["Valeur"])     #en-tête

            while True:     #boucle de lecture
                if ser.in_waiting:      #si il y a des données disponibles sur le registre
                    valeur = ser.readline().decode().strip()

                    try:
                        v = int(valeur)
                    except ValueError:
                        continue

                    if valeur:  #si la chaine n'est pas vide
                        writer.writerow([valeur])   #On ecrit la valeur dans une liste ou un tableau

                        file.flush()

                        print("Valeur reçu: {valeur}".format(valeur=valeur))
    except KeyboardInterrupt as e:  #si on arrête le programme par commande
        print("Programme Arrêté!!")
    finally:
        ser.close()

if __name__ == "__main__":
    main()