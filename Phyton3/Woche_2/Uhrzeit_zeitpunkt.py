#Uhr:
from time import localtime, sleep #aus Modul time werden Funktionen localtime und sleep importiert

while True: #Endlosschleife, Abbrcuh mit Strg + C
    zeit = localtime() #es wird ein Zeit-Objekt mit Namen zeit erzeugt
    print(zeit.tm_hour, "Uhr", zeit.tm_min, "und", zeit.tm_sec, "Sekunden") #Ausgabe der aktuellen Stunde, minute, sekunde
    sleep(10) #10 Sekunden warten