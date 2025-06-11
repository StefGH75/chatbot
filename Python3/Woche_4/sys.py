# #plattform.py

import sys
print("Ihre Systemplattform ist", sys.platform)
print("Python-Verzeichnis: ")
print("Python" + sys.version)

#Modul soll nur importiert und genutzt werden, wenn das Python-Programm unter Windows läuft
#gibt Beep-Ton us

# import sys
# if sys.platform == "win32":
#     from winsound import Beep
#     Beep(770, 1000)
# else: 
#     print("Beep!")

#zufall.py
import sys, random
if len(sys.argv) == 1: #wenn Liste nur ein item enthält, wurde kein Argument übergeben
    print(random.randint(0,1000)) #dann Zufallszahl zwischen 0 und 1000
elif len(sys.argv) > 2: #wenn Liste mehr als zwei items enthält, wurden zuviele Argumente übergeben
    print("Aufrufformat: python zufall.py n")#dann Hinweis zum erwarteten Format
else: #ansonsten genau zwei items
    try:
        n = int(sys.argv[1]) #zweite item ist Kommandozeilenargument, aus dem string und ganze Zah gebildet wird
        print(random.randint(0,n))
    except:
        print("Argument muss eine natürliche Zahl sein.")

import sys
a = range(1000000)
sys.getsizeof(a)

b = list(range(1000000))
sys.getsizeof(b)

a = [1, 2, 3]
sys.getrefcount(a) #Mit der Funktion sys.getrefcount() kannst du ermitteln, wie viele Referenzen es zu einem 
#Objekt gibt.Eine Referenz ist nichts anderes als ein Name, über den du auf das Objekt zugreifen kannst
#scheint immer um eins zu hoch zu sein, weil der Aufruf der Funktion eine zusätzliche Referenz darstellt.

#Zugriff auf Module
import sys
sys.path

#Standardausgabe in eine Datei umleiten
import sys, random
orginial_stdout = sys.stdout #aktueller Stream, auf den der Name sys.stdout verweist, wird gespeichert, damit 
#Änderungen später rückgängig gemacht werden können
with open("zahlen.txt", "w") as sys.stdout: #Datei wird zum Schreiben geöffnet. Der Name sys.stdout ist nun 
                                            #nicht mehr mit der Ausgabe auf dem Display verbunden
    print("Zufallszahlen zwischen 1 und 1000")
    for i in range(5):
        print(i, random.randint(1,1000))
sys.stdout = orginial_stdout #der Name sys.stdout wird wieder mit der Ausgabe auf dem Display verbunden. 
                            #Ursprünglicher Zustand wieder hergestellt
print("Zufallszahlen wurden in eine Datei geschrieben")