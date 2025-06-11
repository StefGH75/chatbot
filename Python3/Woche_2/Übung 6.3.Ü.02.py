#Erstelle ein Python-Programm, das folgende Aufgaben erfüllt:
# a) Importiere das Modul random und verwende eine Funktion aus diesem Modul, um eine Zufallszahl zwischen 1 
# und 10 zu generieren. Speichere diese Zahl in einer Variablen.
# b) Definiere eine Funktion namens berechne_quadrat, die einen Parameter nimmt, dessen Quadrat berechnet 
# und das Ergebnis zurückgibt.
# c) Verwende eine if-Kontrollstruktur, um zu überprüfen, ob die generierte Zufallszahl größer als 5 ist. 
# Falls ja, rufe die Funktion berechne_quadrat mit der Zufallszahl als Argument auf und gib das Ergebnis aus.
#  Falls nein, gib eine Nachricht aus, die besagt, dass die Zahl kleiner oder gleich 5 ist.
# d) Implementiere eine Schleife, die von 1 bis zur generierten Zufallszahl läuft und dabei jedes Mal die 
# aktuelle Zahl ausgibt. 

import random
zahl = random.randint(1,10) ## Es wird eine Zufallszahl zwischen 1 und 10 (inklusive) erzeugt und in der Variable 'zahl' gespeichert.
print(zahl)

def berechne_quadrat(zahl):
    return zahl * zahl #Diese Funktion nimmt eine Zahl als Argument und gibt ihr Quadrat zurück (also Zahl * Zahl).

if zahl > 5:
    ergebnis = berechne_quadrat(zahl) #Wenn die Zahl größer als 5 ist, wird ihr Quadrat berechnet
    print(ergebnis)
else:
    print("Die Zahl ist kleiner als 5")

for i in range(1,zahl + 1): #Eine Schleife, die alle Zahlen von 1 bis einschließlich der Zufallszahl ausgibt, Achtung: +1 notwendig
    print(i)