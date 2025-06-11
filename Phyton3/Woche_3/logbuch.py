
from time import asctime

Menue = """
n: Neuer Eintrag
l: Logbuch lesen
e: Ende"""

def neuer_eintrag():
    with open("text.txt", "a") as logbuch: #Öffnet die Datei "text.txt" im Anfügemodus ("a"), d.h. neue Einträge werden angehängt
        zeitstempel = asctime() #erzeugt einen Zeitstempel als String
        eingabe = input("Neuer Eintrag: ") #fragt Nutzer nach Eintrag
        eintrag = zeitstempel + ": " + eingabe #Kombiniert Zeitstempel und Benutzereingabe mit einem Leerzeichen dazwischen
        logbuch.write(eintrag + "\n") #Schreibt Eintrag in die Datei, gefolgt von einem Zeilenumbruch

def logbuch_lesen():
    with open("text.txt", "r") as logbuch: #öffnet Datei im Lesemodus
        text = logbuch.read() #liest den gesamten Inhalt der Datei
        print(text) #gibt den Inhalt im Terminal aus
    
auswahl = "x" #Initialer Dummy-Wert für die auswahl
while auswahl != "e":
    print(Menue)
    auswahl = input("Auswahl: ")
    if auswahl == "n":
        neuer_eintrag()
    elif auswahl == "l":
        logbuch_lesen()
print("Auf Wiedersehen")
input()

