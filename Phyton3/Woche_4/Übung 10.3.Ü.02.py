# a) Erstelle eine Funktion erstelle_datei, die eine neue Textdatei mit einem vorgegebenen Namen und Inhalt 
# in einem spezifischen Verzeichnis erstellt. Verwende dazu die with-Anweisung und stelle sicher, dass Fehler, 
# wie z.B. fehlende Schreibberechtigungen, mit try und except abgefangen werden.
# b) Implementiere eine Funktion listdir_filter, die alle Dateien eines Verzeichnisses auflistet, die eine
#  bestimmte Dateiendung haben (z.B. .txt). Nutze dazu das Modul os und eine List Comprehension.
# c) Schreibe eine Funktion umbenennen_dateien, die alle Dateien eines Verzeichnisses, die eine bestimmte
#  Endung haben, umbenennt, indem sie ein Präfix hinzufügt. Verwende dazu das Modul os.
# d) Entwickle eine Funktion json_speichern, die eine Liste von Dictionaries in eine Datei im JSON-Format 
# speichert. Verwende dazu das Modul json.
# e) Implementiere eine Funktion json_laden, die eine JSON-Datei liest und den Inhalt als Python-Objekt 
# zurückgibt.
# f) Erstelle eine Funktion regex_suche, die in allen .txt-Dateien eines Verzeichnisses nach einem regulären 
# Ausdruck sucht und die Namen der Dateien zurückgibt, in denen die Suche erfolgreich war.
# Für jede dieser Funktionen sollst du ein kurzes Beispiel für deren Aufruf und Verwendung schreiben. 

import os
import json
# # def erstelle_datei(dateiname=None, inhalt=None, verzeichnis="."):
# #     if dateiname is None:
# #         dateiname = input("Name der Datei: ")
# #     if inhalt is None:
# #         inhalt = input("Inhalt: ")

# #     pfad = os.path.join(verzeichnis, dateiname)
    
# #     try:
# #         with open(pfad,"w", encoding="UTF-8") as datei:
# #             datei.write(inhalt)
# #             print(f"Datei '{dateiname}' wurde erfolgreich erstellt.")
# #     except PermissionError:
# #          print(f"Keine Berechtigung zum Schreiben in: {verzeichnis}")
# #     except Exception as e:
# #         print("Fehler", e)

# # erstelle_datei()

# def listdir_filter(verzeichnis, endung):
#     #endung = ".txt"
#     return [datei for datei in os.listdir(verzeichnis) if datei.endswith(endung)]
# print(listdir_filter(".", ".txt"))

# def umbenennen_dateien(verzeichnis, alte_endung, praefix):
#     for datei in os.listdir(): #Inhaltsverzeichnis durchlaufen
#         if datei.endswith(alte_endung): #wenn Datei mit Endung wie beim Aufruf später angegeben
#             neuer_name = praefix + NameError
#             os.rename(os.path.join(verzeichnis, datei), os.path.join(verzeichnis, neuer_name))
            
#     print("Dateien wurden umbenannt")

# umbenennen_dateien('.', '.txt', 'neu_')

# def json_speichern(daten, dateiname):
#     with open(dateiname, "w", encoding="UTF-8") as datei:
#         json.dumpd(daten, datei)

# meine_daten = ({"name": "Anna", "Alter": "30",}, {"name":"Bernd", "Alter": "45"})
# json_speichern(meine_daten, "daten_test.json")

# def json_laden(dateiname):
#     with open(dateiname, "r") as datei:
#         json.load(datei)

# geladene_daten = json_laden('daten_test.json')
# print(geladene_daten)

import re
def regex_suche(verzeichnis, regex):
    passende_dateien = []
    for datei in os.listdir(verzeichnis):
        if datei.endswith('.txt'):
            with open(os.path.join(verzeichnis, datei), 'r', encoding="UTF-8", errors='ignore') as datei:
                inhalt = datei.read()
                if re.search(regex, inhalt):
                    passende_dateien.append(datei)
    return passende_dateien

print(regex_suche('.', r'\bBeispiel\b'))