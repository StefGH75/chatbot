#a) Definiere eine Funktion speichere_daten, die als Parameter eine Liste von Tupeln entgegennimmt. Jedes 
# Tupel enthält zwei Werte: einen Namen (String) und ein Alter (Integer). Die Funktion soll diese Daten in 
# einer Datei namens personen.txt speichern. Verwende dabei die with-Anweisung und den Modus 'w' zum Öffnen 
# der Datei. Jedes Tupel soll in einer neuen Zeile in folgendem Format gespeichert werden: Name: Alter.
# b) Definiere eine weitere Funktion lade_daten, die die zuvor gespeicherten Daten aus der Datei personen.txt 
# liest und als Liste von Dictionaries zurückgibt, wobei jedes Dictionary einen Namen und ein Alter enthält.
# c) Implementiere eine Fehlerbehandlung in beiden Funktionen, um mit möglichen Laufzeitfehlern umzugehen,
#  z.B. wenn die Datei nicht existiert oder ein Schreib-/Lesefehler auftritt. Gib in solchen Fällen eine 
# aussagekräftige Fehlermeldung aus.
# d) Schreibe eine Kontrollstruktur, die überprüft, ob die zurückgegebene Liste von lade_daten leer ist oder 
# nicht. Wenn sie nicht leer ist, gib die geladenen Daten formatiert in der Konsole aus. Verwende dazu eine 
# Schleife. 

def speichere_daten(tupel_liste): 
    try:
        with open("personen.txt", "a") as datei: #öffnet Datei im Anhangmodus, das heißt neue Daten werden angehangen
            for name, alter in tupel_liste: #iteriert über jedes Tupel in der Liste
                datei.write(f"{name}: {alter} \n") #schreibt jeden Namen und Alter formatiert in Datei, jeweils in neue Zeile (\n)
    except Exception as e: #gibt Fehlermeldung aus, falls beim Schrieben ein Fehler auftritt
        print(f"Ein Fehler ist aufgetreten beim Speichern der Daten: {e}")

def lade_daten():
    try:
        personen = [] #Liste zum Speichern der geladnenen Daten als Dictionary
        with open("personen.txt", "r") as datei: #öffnet Datei im Lesemodus
            for zeile in datei: #liest Datei zeilenweise aus
                name, alter = zeile.strip().split(": ") #entfernt das Zeilenende und trennt Name und Alter anhand Trennzeichen
                personen.append({"Name": name, "Alter": int(alter)}) #fügt Dictionary ein mit Name und Alter als int zur Liste hinzu
        return personen #gibt die Liste zurück
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten beim Laden der Daten: {e}")
        return []
    
def main():
    tupel_liste = [("Anna", 30), ("Bernd", 25), ("Carla", 20)] #Liste von Beispieldaten
    speichere_daten(tupel_liste) #speichert die Daten in der Datei ab
    geladene_daten = lade_daten() #lädt die Daten wieder aus der Datei
    if geladene_daten:
        for person in geladene_daten:
            print(f"Name: {person['Name']}, Alter: {person['Alter']}")
    else: 
        print("Keine Daten geladen")

#if __name__ == "__main__": #Startpunkt des Programms: nur ausgeführt wenn das Skript direkt gestartet wird
main()
