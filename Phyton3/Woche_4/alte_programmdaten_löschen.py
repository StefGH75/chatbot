import os
import time

def finde_alte_programme(p):
    '''Liefert Liste mit 2-Tupeln der Form (datei, alter) Mit Name und Alter von Python-Programmdateien in 
    Ordner p, die älter als 30 Tage sind'''
    alte_programme = [] #Leere Liste wird erzeugt, wird später 2 Tupeln der Form (datei, alter) aufnehmen
    os.chdir(p) #das Verzeichnis, dessen Pfad als Argument übergeben worden ist, wird zum Arbeitsverzeichnis
    for name in os.listdir(): #die Liste der Namen von Dateien und Unterverzeichnissen wird im Arbeitsverzeichnis durchlaufen
        alter_s = time.time() - os.path.getmtime(name) #Alter ist Differenz aus aktuellem Zeitpunkt und Zeitpunkt letzte Änderung
        alter = alter_s / (24 * 3600) # Umwandlung von Sekunden in Tage
        if name.endswith(".py") and (alter > 25): #wenn aktueller Name auf py endet und alter > x
            alte_programme.append((name, alter)) #wird ein Tupel aus dateiname und Alter an Liste alte.programme gehängt
    return alte_programme

pfad = input("Verzeichnis: ")
if os.path.exists(pfad): #Wenn Pfad denn der Benutzer eingegeben hat, gültig ist
    alt = finde_alte_programme(pfad) #wird Funktion mit diesem Pfad aufgerufen
    for programm, alter, in alt: #python entpackt jedes Tupel aus "alt", programm bekommt den ersten Wert, alter den zweiten
        print(programm, round(alter), "Tage alt") #und für jeden Eintrag Dateiname und Alter in Tage ausgegeben
    print(len(alt), "Dateien gefunden")
else:
    print("Ungültiger Pfad")
