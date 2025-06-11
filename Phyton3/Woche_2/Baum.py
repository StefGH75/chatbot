#Übung 1: Wie hoch ist der Baum?
#Entwickle ein interaktives Programm, das die Höhe eines Baums berechnen kann. Es sollen folgende Daten
#  eingegeben werden: Entfernung zum Baum, Augenhöhe, Blickwinkel alpha zur Spitze des Baums

from math import *
entfernung = float(input("Entfernung zum Baum (m): "))
augenhoehe = float(input("Augenhöhe (m): "))
blickwinkel = float(input("Grad: "))

baumhoehe = augenhoehe + tan(radians(blickwinkel)) * entfernung

print("Höhe des Baums: ", round(baumhoehe, 2), "m")