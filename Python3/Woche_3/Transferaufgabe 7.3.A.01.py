#a) Importiere das Modul random und das Modul math. Verwende aus dem Modul random die Funktion randint und 
# aus math die Funktion sqrt.
# b) Erstelle eine Funktion erzeuge_zufallszahlen_liste(n), die eine Liste mit n zufälligen ganzen Zahlen 
# zwischen 1 und 100 zurückgibt.
# c) Erstelle eine Funktion berechne_wurzeln(liste), die für jede Zahl in der übergebenen Liste die 
# Quadratwurzel berechnet und die Wurzeln in einer neuen Liste speichert. Gib diese Liste zurück.
# d) Erstelle eine Funktion sortiere_und_erzeuge_tupel(liste), die die Liste von Quadratwurzeln aufsteigend 
# sortiert und ein Tupel aus (Originalzahl, Quadratwurzel) für jede Zahl in der ursprünglichen Liste erzeugt. 
# Speichere diese Tupel in einer Liste und gib sie zurück.
# e) Erstelle eine Funktion erstelle_dictionary(tupel_liste), die ein Dictionary erstellt, wobei der Schlüssel
#  die Originalzahl und der Wert die Quadratwurzel ist. Gib dieses Dictionary zurück.
# f) Verwende alle oben erstellten Funktionen in einer Hauptfunktion main(), um eine Liste mit 10 zufälligen 
# Zahlen zu erzeugen, die Quadratwurzeln zu berechnen, die Liste zu sortieren, das Tupel zu erstellen und 
# schließlich das Dictionary zu erstellen und auszugeben.
# g) Gib am Ende des Programms das erstellte Dictionary aus. 

from random import randint
from math import sqrt

def erzeuge_zufallszahlen_liste(n):
    return [randint(1,100) for _ in range(n)]

def berechne_wurzeln(liste):
    return[sqrt(zahl) for zahl in liste]

def sortiere_und_erzeuge_tupel(liste):
    tupel_liste = [(zahl, sqrt(zahl)) for zahl in liste]
    return sorted(tupel_liste, key= lambda x: x[1])

def erstelle_dictionary(tupel_liste):
    return {tupel[0]: tupel[1] for tupel in tupel_liste}

def main():
    zufallszahlen = erzeuge_zufallszahlen_liste(10)
    wurzeln = berechne_wurzeln(zufallszahlen)
    tupel_liste = sortiere_und_erzeuge_tupel(zufallszahlen)
    dictionary = erstelle_dictionary(tupel_liste)
    print(dictionary)
main()


