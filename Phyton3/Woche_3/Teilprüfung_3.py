# Teilprüfung_3.py
#Autorin: Stefanie Millow

import json

def lese_namen_aus_datei(dateiname):
    """Funktion, die Liste von Namen aus Textdatei liest"""
    try:
        with open(dateiname, "r") as datei: # Öffnet die Datei im Lesemodus
            namen = [zeile.strip() for zeile in datei if zeile.strip()] #Liest jede Zeile, strip() entfernt 
                        #Leerzeichen und filtert leere Zeilen, dann wird geprüft, ob noch etwas übrig ist (if zeile.strip)
        return namen #Gibt die Liste der Namen zurück
    except FileNotFoundError: #Falls die Datei nicht gefunden wird
        print(f"Die Datei '{dateiname}' wurde nicht gefunden.")
        return [] #gibt leere Liste zurück, damit Programm nicht abstürzt
    except Exception as e:  #wenn allgemeiner Fehler beim Lesen
        print("Fehler beim Lesen der Datei:", e)
        return [] #gibt leere Liste zurück, damit Programm nicht abstürzt

def speichere_namen_als_json(namenliste, zieldatei):
    """Funktion, die gelesenen Namen in ein JSON-Format umwandelt und in einer neuen Datei speichert"""
    try:
        with open(zieldatei, "w", encoding='utf-8') as datei: #öffnet die Datei im Schreibmodus mit
                    #UTF-8-Kodierung, damit auch Sonderzeichen wie Umlaute korrekt gespeichert werden
            json.dump(namenliste, datei, ensure_ascii=False, indent=4) #Speichert Liste im JSON-Format
                                            #ensure_ascii=False: Umlaute und Sonderzeichen bleiben erhalten
                                            #indent=4: rückt ein für bessere Lesbarkeit
        print(f"Namen erfolgreich in '{zieldatei}' gespeichert.") #Bestätigung für den Nutzer, dass Speichern erfolgreich
    except Exception as e: #Fehlerbehandlung beim Schreiben
        print("Fehler beim Schreiben der JSON-Datei:", e)

def benutzeroberflaeche():
     """Funktion für Benutzeroberfläche in der Konsole, die  Benutzer erlaubt zwischen den Funktionen zu wählen"""
     while True:
        print("\n--- Menü ---")
        print("1. Namen aus Datei lesen")
        print("2. Namen in JSON-Datei speichern")
        print("3. Beenden")
        
        auswahl = input("Bitte wähle eine Option (1,2 oder 3): ") #Nutzer wird um Auswahl gebeten

        if auswahl == "1": #Option 1: Namen aus Textdatei lesen und anzeigen
            dateiname = input("Dateiname zum Einlesen der Datei(z.B. namen.txt): ") #Nutzer wird nach Dateinamen der txt-Datei gefragt
            namen = lese_namen_aus_datei(dateiname) #Funktion wird aufgerufen, um Namen zu lesen
            if namen:
                print("\nGelesene Namen:")
                for n in namen:
                    print(f"{n}") #jeder Name wird ausgegeben
            else:
                print("Keine Namen gefunden oder Fehler beim Einlesen.")
        
        elif auswahl == "2": #Option 2: Namen aus Textdatei lesen und als JSON speichern
            quelle = input("Wie lautet der Name der txt-Datei(z.B. namen.txt): ") #Fragt nach vorhandender txt.Datei
            ziel = input("Wie soll die JSON-Zieldatei heißen (z.B. namen.json): ") #Fragt nach Namen, unter dem die json-Datei gespeichert werden soll
            namen = lese_namen_aus_datei(quelle) #Namen werden aus der Quelldatei gelesen
            if namen: #wenn Namen vorhanden sind
                speichere_namen_als_json(namen, ziel) #wird funktion aufgerufen und Inhalt aus genannter Datei in genannet json-Datei gespeichert
            else:
                print("Es konnten keine Namen gelesen werden. JSON-Datei wurde nicht erstellt.")
        
        elif auswahl == "3":
            print("Programm beendet.")
            break #Schleife beendet und damit Programmende
    
        else:
            print("Ungültige Eingabe. Bitte wähle 1, 2 oder 3.")

if __name__ == "__main__": #Startpunkt des Programms, nur ausführen, wenn Skript direkt gestartet wird
    benutzeroberflaeche() #Startet die Benutzeroberfläche (Menü)
