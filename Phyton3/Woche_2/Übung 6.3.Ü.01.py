#Erstelle ein Python-Programm, das folgende Aufgaben erfüllt:
# a) Importiere das Modul random und das Modul math.
# b) Definiere eine Variable zahl, die eine zufällige Ganzzahl zwischen 1 und 100 speichert.
# c) Schreibe eine Funktion quadratwurzel, die die Quadratwurzel einer Zahl berechnet und zurückgibt. 
# Verwende dafür eine Funktion aus dem Modul math.
# d) Verwende eine if-else-Kontrollstruktur, um zu überprüfen, ob die zahl größer als 50 ist. Wenn ja, 
# rufe die Funktion quadratwurzel mit zahl als Argument auf und drucke das Ergebnis aus. Andernfalls drucke
#  "Zahl ist 50 oder kleiner".
# e) Erstelle eine for-Schleife, die Zahlen von 1 bis 5 durchläuft, und für jede Zahl die Funktion 
# quadratwurzel aufruft und das Ergebnis ausdruckt. 

import random
import math

zahl = random.randint(1,100)

def quadratwurzel(zahl):
  return math.sqrt(zahl)

if zahl > 50: 
  print(quadratwurzel())
else:
  print("Zahl ist 50 oder kleiner")

for i in range(1,6):
  print({quadratwurzel(i)})