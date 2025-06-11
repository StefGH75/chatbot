#testen mit: C:\Users\Stefa\OneDrive\Dokumente\Weiterbildung\velpTec\Developer\Testordner

import os
print("Unterverzeichnisse: ")
inhalt = os.listdir()
for item in inhalt:
    if os.path.isdir(item): #Wenn ein String in dieser Kollektion der Name eines Verzeichnisses ist,wird dieser auf dem Bildschirm ausgegeben.
        print(item)

BERICHT = '''
Ich habe {} Verzeichnisse durchsucht.
Der gesamte Speicherbedarf beträht {} Bytes.''' #Formatstring mit zwei Platzhaltern für die Ausgabe des Berichts. 

def berechne_platzbedarf(wurzel): #der Verzeichnisbaum mit der Wurzel wurzel wird vollständig durchlaufen und 
        #die Dokumentation, bestehend aus einer Folge von 3-Tupeln, wird der Variablen durchlauf zugewiesen.
    durchlauf = os.walk(wurzel)
    anzahl = 0 #Anzahl besuchter Dateien
    platz = 0 #Platzbedarf der besuchten Dateien
    for v, uv, d in durchlauf: #Jedes Element der Folge durchlauf ist ein 3-Tupel, das den Besuch eines 
        #Verzeichnisses dokumentiert. Bei der Iteration (for-Schleife) wird jedes dieser 3-Tupel verarbeitet.
        # Dabei werden den drei Komponenten des aktuellen Tupels die Namen v, uv und d zugewiesen (Abkürzungen für Verzeichnis, Unterverzeichnisse und Dateien)
        anzahl += 1 #Die besuchten Verzeichnisse werden gezählt. Deshalb wird der Wert der Variablen anzahl um 1 erhöht
        os.chdir(v) #Das aktuelle Verzeichnis v der Folge durchlauf wird zum Arbeitsverzeichnis gemacht.
        for datei in d: #Nun wird die Liste d mit den Namen aller Dateien im aktuellen Verzeichnis v (das jetzt auch das Arbeitsverzeichnis ist) durchlaufen.
            platz += os.path.getsize(datei) #Die Größe der aktuellen Datei wird ermittelt, und dieser Wert wird zur Variablen platz addiert.
    return anzahl, platz

wurzel = input("Wurzelverzeichnis (z.B. /python310): ")
if os.path.exists(wurzel):#handelt es sich um einen gültigen Pfad, wird die Funktion berechne_platzbedarf() aufgerufen
    anz_verz, speicher = berechne_platzbedarf(wurzel) #gibt zwei Zahlen zurück: die Anzahl besuchter Verzeichnisse und den gesamten Platzbedarf der
#Dateien in diesen Verzeichnissen. Diese beiden zurückgegebenen Zahlen werden zwei Variablen zugewiesen.
    print(BERICHT.format(anz_verz, speicher))
else: 
    print("Ungültiger Pfad")
input()

#umbenennen.py
import os
EXTENSIONS = [".png", ".bmp", ".jpg"]

def umbenennen(praefix, verzeichnis):
    anzahl = 0
    os.chdir(verzeichnis) #Arbeitsverzeichnis ist Verzeichnis, das später über input übergeben wird
    for name in os.listdir(): #Inhaltsverzeichnis durchlaufen
        _, ext = os.path.splitext(name) #splitext spaltet Dateinamen in ein Tupel aus zwei Teilen: name und 
        #Namenserweiterung (einschließlich punkt). Nur das zweite item wird verwendet und unter ext gespeichert
        #füe erstes item wird fast unsichtbarer Name gewählt, der nue aus Unterstrich_ besteht.
        if ext in EXTENSIONS: #wenn es eine Bilddatei wie in Extensions aufgelistet, handelt
            os.rename(name, praefix + "_" + name) #wird Name umbenannt
            anzahl += 1
    return anzahl

praefix = input("Geben sie ein Präfix an: ")
verzeichnis = input("Zielverzeichnis: ")
while not os.path.exists(verzeichnis):
    print("Pfad existiert nicht.")
    verzeichnis = input("Zielverzeichnis: ")
n = umbenennen(praefix, verzeichnis)
print("Es wurden {} Dateien umbenannt",format(n))
