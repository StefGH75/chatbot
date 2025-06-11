# a) Erstelle eine Funktion erstelle_verzeichnis, die als Argument einen Verzeichnisnamen (String) nimmt. 
# Die Funktion soll mithilfe des os-Moduls überprüfen, ob das Verzeichnis bereits existiert. Falls nicht, 
# soll das Verzeichnis erstellt werden. Gib eine Bestätigung aus, dass das Verzeichnis erstellt wurde oder 
# bereits existiert.
# b) Erstelle eine Funktion speichere_text_in_datei, die zwei Argumente nimmt: den Dateinamen (String) und 
# den zu speichernden Text (String). Die Funktion soll den Text in der angegebenen Datei speichern. Verwende 
# die with-Anweisung, um die Datei zu öffnen und sicherzustellen, dass sie korrekt geschlossen wird.
# c) Erstelle eine Funktion lese_datei, die als Argument einen Dateinamen (String) nimmt und den Inhalt der
#  Datei ausgibt. Fange mögliche Ausnahmen ab, die beim Versuch, die Datei zu lesen, auftreten können (z.B. 
# wenn die Datei nicht existiert), und gib eine entsprechende Fehlermeldung aus.
# d) Erstelle eine Funktion liste_dateien_in_verzeichnis, die als Argument einen Verzeichnisnamen (String)
#  nimmt und alle Dateien in diesem Verzeichnis auflistet. Verwende das os-Modul, um auf das Dateisystem 
# zuzugreifen.
# e) Schreibe ein Hauptprogramm, das die Funktionen in folgender Reihenfolge aufruft: erstelle_verzeichnis 
# mit dem Verzeichnisnamen "MeineDaten", speichere_text_in_datei mit einem beliebigen Text in einer Datei 
# namens "beispiel.txt" im Verzeichnis "MeineDaten", lese_datei für "beispiel.txt" und liste_dateien_in_verzeichnis für das Verzeichnis "MeineDaten". 

import os

def erstelle_verzeichnis(verzeichnisname):
    if os.path.exists(verzeichnisname):
        print("Verzeichnis existiert bereits")
    else: 
        os.mkdir(verzeichnisname)
        print(f"Verzeichnis '{verzeichnisname}' wurde erstellt.")

def speichere_text_in_datei(dateiname, text):
    with open(dateiname, "w", encoding="UTF-8") as datei:
        datei.write(text)
    print(f"Text wurde in '{dateiname}' gespeichert.")

def lese_datei(dateiname):
    try:
        with open(dateiname, "r", encoding="UTF-8") as datei:
            inhalt = datei.read()
            print(f"Inhalt von '{dateiname}':\n{inhalt}")
    except FileNotFoundError:
        print(f"Die Datei '{dateiname}' wurde nicht gefunden.")

def liste_dateien_in_verzeichnis(verzeichnisnamen):
    verzeichnis= os.listdir(verzeichnisnamen)
    print(f"Das sind alle Dateien in {verzeichnisnamen}: {verzeichnis}")

verzeichnisnamen = "Meine Dateien"
dateiname = os.path.join(verzeichnisnamen, "beispiel.txt")
text = "Das ist ein Beispieltext. Neu"

erstelle_verzeichnis(verzeichnisnamen)
speichere_text_in_datei(dateiname, text)
lese_datei(dateiname)
liste_dateien_in_verzeichnis(verzeichnisnamen)