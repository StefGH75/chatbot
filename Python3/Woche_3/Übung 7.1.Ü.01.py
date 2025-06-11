#Entwickele ein Python-Programm, das folgende Aufgaben erfüllt:
# a) Importiere das Modul random und verwende es, um eine Liste von 10 zufälligen Ganzzahlen zwischen 1 und 100
#  zu erzeugen.
# b) Erstelle eine Funktion namens sortiere_und_zähle, die eine Liste von Zahlen als Argument nimmt. Die 
# Funktion soll die Liste aufsteigend sortieren und die Anzahl der Elemente in der Liste zurückgeben.
# c) Erstelle eine weitere Liste, die Tupel aus den ursprünglichen zufälligen Zahlen und dem Quadrat jeder 
# Zahl enthält (z.B. [(Zahl, Quadrat der Zahl), ...]).
# d) Verwende eine Schleife, um über die Liste der Tupel zu iterieren, und drucke für jedes Tupel eine
#  formatierte Zeichenkette aus, die besagt: "Die Zahl X hat das Quadrat Y".
# e) Schreibe eine Kontrollstruktur, die prüft, ob die Anzahl der Elemente in der sortierten Liste größer
#  als 5 ist. Wenn ja, drucke "Mehr als 5 Elemente", ansonsten "5 oder weniger Elemente". 

import random

zufallszahlen = [random.randint(1,100) for _ in range(10)]
zufallszahlen

def sortiere_und_zähle(liste):
    liste.sort()
    return liste

anzahl_elemente = sortiere_und_zähle(zufallszahlen)

tupel_liste = [(zahl, zahl**2) for zahl in zufallszahlen]

for zahl, quadrat in tupel_liste:
    print(f"Die Zahl {zahl} hat das Quadrat {quadrat}")