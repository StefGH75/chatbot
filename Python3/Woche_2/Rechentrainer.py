#Der Rechentrainer funktioniert folgendermaßen: Dem Benutzer werden fünf Rechenaufgaben gestellt. 
# Nach jeder Aufgabe wartet das Programm auf die Eingabe des Ergebnisses. Wenn das Ergebnis falsch ist, 
# gibt es eine entsprechende Rückmeldung, und es wird eine neue Antwort erwartet. Die nächste Aufgabe wird 
# erst dann gestellt, wenn zuvor das richtige Ergebnis eingegeben worden ist. Nach erfolgreichem Absolvieren 
# der Aufgaben wird dem Benutzer mitgeteilt, wie viel Zeit benötigt wurde

print ("Multiplikationstrainer")
from random import randint #randint aus modul random wird importiert
import time #Modul time wird importiert
startzeit = time.time() #Startzeit wird als unix-Zeit gespeichert. Es ist Die Anzahl der Sekunden seit dem 01.01.1970
for i in range(5): #für 5 Durchgänge
    a = randint(1,20) #Zufallszahl a aus ganzen zahlen zwischen 1 und 20
    b = randint(1,20) #Zufallszahl b aus ganzen zahlen zwischen 1 und 20
    loesung = -1 #Variable loesung erhält Anfangswert, der nicht das korrekt Ergebnis ist. Damit ist garantiert, dass die while-Schleife mindestens einmal durchlaufen wird
    while loesung != a * b: #while-Schleife so lange durchlaufen bis Ergebnis richtig eingegeben
        prompt = str(a) + "*" + str(b) + "=" #prompt-String für Benutzereingabe (Parameter der Input-Funktion) berechnet. Rechenaufgaben aus Zufallszahlen
        loesung = int(input(prompt)) #promptstring mit Rechenaufgabe erscheint. Dahinter gibt Benutzer Lösung ein. Aus str wird int und der Variablen loesung zugewiesen.
        if loesung == a * b:
            print("Richtig!")
        else:
            print("Falsch. Versuchen sie es noch einmal!")

zeit = round(time.time() - startzeit) #von der aktuellen unox-Zeit wird die gespeicherte Startzeit abgezogen. Das ist die inszwischen verstrichene Zeit
print("Für die Aufgaben hast du", zeit, "Sekunden benötigt")