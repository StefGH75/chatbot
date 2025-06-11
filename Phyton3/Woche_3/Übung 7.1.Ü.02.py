#a) Importiere das Modul random und das Modul math.
# b) Erstelle eine Funktion namens erzeuge_zufallszahlen_liste, die zwei Parameter akzeptiert: anzahl 
# (die Anzahl der Zufallszahlen in der Liste) und max_wert (der maximale Wert einer Zufallszahl). Die Funktion 
# soll eine Liste von anzahl Zufallszahlen generieren, wobei jede Zufallszahl zwischen 1 und max_wert 
# (inklusive) liegt. Nutze die Funktion randint aus dem Modul random zur Generierung der Zufallszahlen.
# c) Erstelle eine Funktion namens berechne_durchschnitt, die eine Liste von Zahlen als Parameter akzeptiert 
# und den Durchschnittswert dieser Zahlen zurückgibt.
# d) Erstelle eine Funktion namens sortiere_und_teile, die eine Liste von Zahlen akzeptiert und die Liste in
#  zwei Hälften teilt. Die Funktion soll zunächst die Liste aufsteigend sortieren. Dann soll die Funktion 
# zwei Listen zurückgeben: die erste Hälfte und die zweite Hälfte der ursprünglichen Liste. Wenn die Liste 
# eine ungerade Anzahl von Elementen hat, soll das mittlere Element zur ersten Hälfte hinzugefügt werden.
# e) Verwende die Funktion erzeuge_zufallszahlen_liste, um eine Liste mit 10 Zufallszahlen zu erzeugen, wobei 
# max_wert 100 ist.
# f) Gib die erzeugte Liste aus.
# g) Berechne und gib den Durchschnittswert der Zufallszahlenliste mit der Funktion berechne_durchschnitt aus.
# h) Verwende die Funktion sortiere_und_teile, um die Zufallszahlenliste zu sortieren und in zwei Hälften 
# zu teilen. Gib beide Hälften aus. 

import math
import random

def erzeuge_zufallszahlen_liste(anzahl, max_wert):
    zufallszahlen = [random.randint(1,max_wert) for _ in range(anzahl)]
    return zufallszahlen

def berechne_durchschnitt(zahlen):
    return sum(zahlen) / len(zahlen)

def sortiere_und_teile(zahlen):
    zahlen.sort()
    mitte = len(zahlen) // 2
    if len(zahlen) % 2:
        return zahlen[:mitte+1], zahlen[mitte+1:]
    else:
        return zahlen[:mitte], zahlen[mitte:]

zufallszahlen = erzeuge_zufallszahlen_liste(10, 100)
print(zufallszahlen)

durchschnitt = berechne_durchschnitt(zufallszahlen)
print(durchschnitt)

erste_haelfte, zweite_haelfte = sortiere_und_teile(zufallszahlen)
print("Erste Hälfte: ", erste_haelfte)
print("Zweite Hälfte: ", zweite_haelfte)