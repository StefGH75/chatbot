#Aufgabe: Module
# a) Gebe an, wie du das Modul math in Python importierst und verwende eine Funktion aus diesem Modul, um 
# die Quadratwurzel von 256 zu berechnen.
# b) Erstelle eine Variable radius mit dem Wert 7. Berechne den Umfang eines Kreises unter Verwendung der 
# Variable radius und der Konstante pi aus dem Modul math. Schreibe das Ergebnis in eine neue Variable umfang 
# und gib sie aus.
# c) Beschreibe, wie du eine eigene Funktion namens fahrenheit_zu_celsius definierst, die eine Temperatur in
#  Fahrenheit entgegennimmt und die entsprechende Temperatur in Celsius zurückgibt. Verwende diese Funktion 
# anschließend, um die Temperatur 68°F in Celsius umzurechnen und das Ergebnis auszugeben.
# d) Erkläre, wie eine einfache for-Schleife in Python aussieht, die die Zahlen von 1 bis einschließlich 5 
# ausgibt. Verwende dazu eine Schleife und die print-Funktion.
# e) Benenne die zwei grundlegenden Arten, wie Funktionen aus Modulen in Python importiert werden können, 
# und gib für jede Art ein Beispiel an.

import math
math.sqrt(256)

import math
radius = 7
umfang = 2 * math.pi * radius
print(umfang)

def fahrenheit_zu_celsius(fahrenheit):
    return fahrenheit * 9 / 5 + 32
fahrenheit_zu_celsius(68)

for i in range(1,6):
    print(i)

import math # math.sqrt
from math import *
