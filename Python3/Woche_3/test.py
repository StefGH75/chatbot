
import json

def lese_namen_aus_datei(dateiname):
    try:
        with open("namensliste.txt", "r") as datei: # Öffnet die Datei im Lesemodus
            namen = [zeile.strip() for zeile in datei if zeile.strip()] #Liest jede Zeile, entfernt Leerzeichen (strip) und leere Zeilen
        return namen #Gibt die Liste der Namen zurück
    except FileNotFoundError: #Falls die Datei nicht gefunden wird
        print(f"Die Datei '{dateiname}' wurde nicht gefunden.")
        return []
    except Exception as e:  #wenn allgemeiner Fehler beim Lesen
        print("Fehler beim Lesen der Datei:", e)
        return []

def speichere_namen_als_json(namenliste, zieldatei):
    try:
        with open(zieldatei, "w", encoding='utf-8') as datei: #öffnet die Datei im Schreibmodus, in 
                    #UTF-8-Kodierung,  wichtig, damit auch Sonderzeichen wie Umlaute korrekt gelesen werden
            json.dump(namenliste, datei, ensure_ascii=False, indent=4) #Speichert die Liste im JSON-Format
                                            #ensure_ascii=False: Umlaute und Sonderzeichen bleiben erhalten
                                            #indent=4: rückt ein für bessere Lesbarkeit
        print(f"Namen erfolgreich in '{zieldatei}' gespeichert.")
    except Exception as e:
        print("Fehler beim Schreiben der JSON-Datei:", e)

def benutzeroberflaeche():
    while True:
        print("\n--- Menü ---")
        print("1. Namen aus Datei lesen")
        print("2. Namen in JSON-Datei speichern")
        print("3. Beenden")
        
        auswahl = input("Bitte wähle eine Option (1,2 oder 3): ") #Nutzer wird um Auswahl gebeten

        if auswahl == "1": #Option 1: Namen aus Textdatei lesen und anzeigen
            dateiname = input("Dateiname zum Einlesen (z.B. namen.txt): ") #Nutzer wird nach Dateinamen gefragt
            namen = lese_namen_aus_datei(dateiname)
            if namen:
                print("\nGelesene Namen:")
                for n in namen:
                    print(f"- {n}") #jeder Name wird ausgegeben
            else:
                print("Keine Namen gefunden oder Fehler beim Einlesen.")
        
        elif auswahl == "2": #Option 2: Namen aus Textdatei lesen und als JSON speichern
            quelle = input("Dateiname mit den Namen (z.B. namen.txt): ") #Fragt nach vorhandender txt.Datei
            ziel = input("Ziel-Dateiname für JSON (z.B. namen.json): ") #Fragt nach Namen, unter dem die json-Datei gespeichert werden soll
            namen = lese_namen_aus_datei(quelle)
            if namen:
                speichere_namen_als_json(namen, ziel) #ruft funktion auf und speichert Inhalt aus genannter Datei in genannet json-Datei 
            else:
                print("Es konnten keine Namen gelesen werden. JSON-Datei wurde nicht erstellt.")
        
        elif auswahl == "3":
            print("Programm beendet.")
            break #Programm wird beendet
    
        else:
            print("Ungültige Eingabe. Bitte wähle 1, 2 oder 3.")

if __name__ == "__main__": # Startpunkt des Programms
    benutzeroberflaeche() #Startet das Menü
