#Schreibe ein Programm, das die Ermittlung der Verkehrsdichte an einer Straße unterstützt. Der Benutzer 
# zählt jedes vorbeikommende Auto, jedes Fahrrad und jede Person durch Eingabe der Buchstaben f, a und p. 
# Nach einer Minute wird die Zählung beendet und das Ergebnis ausgegeben.

import time

Tastenbelegung = {"f": "Fahrräder", "a": "Autos", "p": "Personen"}

zähler = {"f":0, "a": 0, "p":0}

def eingabe():
    for taste in zähler.keys():
        print(taste + ":" + Tastenbelegung[taste])
    auswahl = input("Auswahl: ")
    print()
    return auswahl

def zählen(taste):
    global zähler
    if taste in zähler.keys():
        anzahl = zähler[taste]
        zähler[taste] = anzahl + 1

def ausgabe():
    print("Verkehrszählung (1min)")
    for t in zähler.keys():
        print(Tastenbelegung[t] + ":", str(zähler[t]))
    print()

startzeit = time.time()
while time.time() < startzeit + 60:
    auswahl = eingabe()
    zählen(auswahl)
ausgabe()
