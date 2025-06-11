# a) Erstelle eine Funktion speichere_kontakt, die als Parameter die Daten eines Kontakts (Name, E-Mail, 
# Telefonnummer) entgegennimmt und diese in einer JSON-Datei speichert. Verwende dabei das JSON-Format. 
# Achte darauf, dass bei jedem Aufruf der Funktion ein neuer Kontakt zur Datei hinzugefügt wird, ohne die 
# bestehenden Daten zu überschreiben.
# b) Implementiere eine Funktion lade_kontakte, die die gespeicherten Kontaktdaten aus der JSON-Datei liest 
# und als Liste von Dictionaries zurückgibt. Jedes Dictionary in der Liste soll die Daten eines Kontakts 
# repräsentieren.
# c) Erstelle eine Fehlerbehandlung für beide Funktionen, um sicherzustellen, dass das Programm nicht 
# abstürzt, falls die Datei nicht existiert oder beschädigt ist. Gib in solchen Fällen eine entsprechende 
# Fehlermeldung aus.
# d) Schreibe eine einfache Benutzeroberfläche (CLI), über die ein Benutzer neue Kontakte hinzufügen und 
# die gespeicherten Kontakte anzeigen lassen kann. Verwende dazu die Funktionen speichere_kontakt und 
# lade_kontakte.

import json

def speichere_kontakt(name, email, telefon):

    kontakt = {'Name': name, 'E-Mail': email, 'Telefonnummer': telefon} #ein Kontakt besteht aus einem Dictionary mit Name, E-Mail und Telefonnummer
    try:
        with open('kontakte.json', 'r+') as datei: #versucht die bestehende JSON-Datei im Lese- und Schreibmodus zu öffnen
            daten = json.load(datei) #vorhandene Kontakte aus Datei geladen
            daten.append(kontakt) #neuer Kontakt zur bestehenden Liste hinzugefügt
            datei.seek(0) #bewegt Cursor an Anfang der Datei (um alles zu überschreiben)
            json.dump(daten, datei, indent=4) #überschreibt Datei mit aktualisierter Kontaktliste
    except (FileNotFoundError, json.JSONDecodeError): #falls Datei nicht existiert oder beschädigt ist
        with open('kontakte.json', 'w') as datei: #erstellt neue Datei
            json.dump([kontakt], datei, indent=4) #speichert neuen Kontakt als erste und einzige Liste in der neuen Datei
        print("Neue Datei wurde erstellt, da keine vorhanden war.")

def lade_kontakte():
    try:
        with open('kontakte.json', 'r') as datei: #öffnet Datei im Lesemodus
            return json.load(datei) #liest json-DAtei und gibt sie zurück
    except (FileNotFoundError, json.JSONDecodeError): #Fehler Datei existiert nicht oder ist beschädigt
        print("Fehler beim Laden der Kontakte. Datei existiert nicht oder ist beschädigt.")
        return [] #gibt leere Liste zurück, damit Programm weiterläuft

def benutzeroberflaeche():
    while True: #Endlosschleife bis Nutzer Programm beendet
        aktion = input("Möchten Sie einen neuen Kontakt speichern (s) oder vorhandene Kontakte anzeigen (a)? (s/a/beenden): ")
        if aktion.lower() == 'beenden':
            break
        elif aktion.lower() == 's':
            name = input("Name: ")
            email = input("E-Mail: ")
            telefon = input("Telefonnummer: ")
            speichere_kontakt(name, email, telefon)
            print("Kontakt gespeichert.")
        elif aktion.lower() == 'a':
            kontakte = lade_kontakte() #lädt alle Kontakte aus der Datei
            if kontakte: #falls Kontakte 
                for kontakt in kontakte: #vorhanden sind, zeige sie an
                    print(f"Name: {kontakt['Name']}, E-Mail: {kontakt['E-Mail']}, Telefonnummer: {kontakt['Telefonnummer']}")
            else:
                print("Keine Kontakte gefunden.")
        else:
            print("Ungültige Eingabe.")

if __name__ == "__main__": #Startpunkt des Programms
    benutzeroberflaeche() #startet die Benutzeroberfläche


