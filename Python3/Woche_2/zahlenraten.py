#Übung 2: Zahlenraten *
#beim Spiel Zahlenraten versucht der Benutzer, durch geschicktes Fragen möglichst rasch eine unbekannte 
# Zufallszahl zwischen 0 und 100 zu erraten. Schreibe ein Python-Programm!

from random import *

zahl = randint(0,100)
print("Errate durch geschicktes Fragen möglichst rasch eine unbekannte Zahl")

antwort = int(input("Bitte geben sie eine Zahl zwischen 0 und 100 ein. Zahl:  "))
while antwort != zahl:
    if antwort > zahl:
        print("zu groß!")
    elif antwort < zahl:
        print("zu klein!")
    antwort = int(input("Zahl: "))
print("Herzlichen Glückwunsch! Du hast die Zahl gefunden!")


