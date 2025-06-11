#Entwickle ein Python-Programm, das folgende Aufgaben erfüllt:
# a) Importiere das Modul random und das Modul time.
# b) Definiere eine Funktion wuerfeln(), die eine zufällige Zahl zwischen 1 und 6 generiert und diese 
# zurückgibt. Verwende dafür die Funktion randint() aus dem Modul random.
# c) Definiere eine Funktion aktueller_timestamp(), die den aktuellen Unix-Timestamp zurückgibt. Verwende 
# dafür die Funktion time() aus dem Modul time.
# d) Schreibe eine Hauptschleife, die fünfmal läuft. In jedem Durchlauf soll die Funktion wuerfeln() aufgerufen
#  und das Ergebnis zusammen mit dem aktuellen Unix-Timestamp ausgegeben werden. Nutze dafür die Funktion 
# aktueller_timestamp().
# e) Sorge dafür, dass zwischen jedem Würfelwurf eine Pause von 2 Sekunden liegt. Verwende dafür die Funktion 
# sleep() aus dem Modul time. 

import random, time

def wuerfeln():
    return random.randint(1,6)
#ergebnis = wuerfeln()
#print(f"Du hast eine {ergebnis} gewürfelt!")

def aktueller_timestamp():
    return time.time()
#print(f"Die aktuelle Unix-Zeit ist:{aktueller_timestamp}")

for i in range(5):
    print("Du hast eine", wuerfeln(), "gewürfelt!")
    print("Die aktuelle Unix-Zeit ist:", aktueller_timestamp())
    time.sleep(2)