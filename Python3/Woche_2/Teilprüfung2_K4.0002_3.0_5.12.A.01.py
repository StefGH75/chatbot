#Autorin: Stefanie Millow
#Teilprüfung 2 (K4.0002_3.0_5.12.A.01)

#Beispiel-Datenbank:
buecherei_datenbank = [
    {"Titel": "Python lernen", "Autor": "Max Mustermann", "Jahr": 2020},
    {"Titel": "Fortgeschrittene Python-Programmierung", "Autor": "Erika Musterfrau", "Jahr": 2021},
    {"Titel": "Python lernen", "Autor": "John Doe", "Jahr": 2019}
] 

#Aufgabe a:
def suche_buch(titel, autor=None):
    """
    Sucht Bücher in Bibliotheksdatenbank basierend auf Titel und optionalem Autor.
    Parameter: titel, autor (wenn None, dann nur nach Titel gesucht)
    Rückgabe: Liste von Büchern, die Suchkriterien entsprechen
    """
    suche = [] #leere Liste zur Speicherung der Suchergebnisse
    for buch in buecherei_datenbank: #durchläuft jedes Buch in der Datenbank
        if buch["Titel"].lower() == titel.lower(): #vergleicht den Titel (durch lower unwichtig ob groß oder klein)
            if autor is None or buch["Autor"].lower() == autor.lower(): #wenn kein Autor angegeben oder Autor übereinstimmt...
                suche.append(buch) #füge das Buch zum Suchergebnis hinzu
    return suche #gibt liste der Bücher mit passenden Suchergebnissen aus
    
#print(suche_buch("Python lernen")) #Beispiel-Suche, gibt zwei Bücher aus, da nicht nach Autor gesucht wurde
#print(suche_buch("Python lernen", "John Doe")) #Beispiel-Suche, gibt nur ein Buch aus, da zusätzlich nach Autor gesucht

#Aufgabe b:
def fuege_buch_hinzu(titel, autor, jahr):
    """
Fügt neues Buch zur Datenbank hinzu.
    """
    neu = {"Titel": titel, "Autor": autor, "Jahr": jahr}
    
    buecherei_datenbank.append(neu) #Hängt das neue Buch an die vorhandene Datenbank-Liste 

#fuege_buch_hinzu("Python 3 Lernen", "Peter Soundso", 2024) #Beispiel: Hinzufügen von Buch
#print(buecherei_datenbank) #Test ob neues Buch nun in Datenbank enthalten

#Aufgabe c:
def buecher_nach_jahr(jahr):
    """
    Gibt alle Bücher zurück, die im angegeben Jahr veröffentlicht wurden
    """
    suche_nach_jahr = filter(lambda buch:buch["Jahr"] == jahr, buecherei_datenbank) #Filter nutzt Lambda-Funktion
    #um nur passende Bücher beizubehalten. "buch" ist jedes einzelne Element der Datenbank, Rückgabe True wenn 
    # das Jahr des Buches gleich gesuchtem Jahr, sonst False
    return list(suche_nach_jahr) #Ausgabe, die in Liste umgewandelt wird (notwendig, da filter-Objekt Iterator)
    print("Buch erfolgreich hinzugefügt!")

#print(buecher_nach_jahr(2020)) #Beispiel: alle Bücher aus 2020 ausgeben lassen

#Aufgabe d:
def zeige_datenbank():
  """
  Gibt alle Bücher in der Bücherei-Datenbank aus, wobei das Feld 'Jahr' als 'Erscheinungsjahr' angezeigt wird.
  """
  print("Aktuelle Bücherei-Datenbank:")
  print("-" * 50) #fügt Trennlinie ein für bessere Lesbarkeit (50 mal Trennstrich)
  for buch in buecherei_datenbank:
       
    print(f"Titel: {buch['Titel']}") #gibt Titel des Buches aus
    print(f"Autor: {buch['Autor']}") #gibt Autor des Buches aus
    print(f"Erscheinungsjahr: {buch['Jahr']}") #gibt Jahr als Erscheinungsjahr aus
    print("-" * 50) #fügt Trennlinie ein für bessere Lesbarkeit (50 mal Trennstrich)

#zeige_datenbank() #Funktion wird aufgerufen

#Aufgabe e:
while True: #Endlosschleife läuft so lange bis der Benutzer "ende" eingibt
    print("\nVerwaltung der Bücherei Datenbank:\n")
    funktion = input("Welche der genannten Funktionen möchtest du gern durchführen: \n"
                 "Suche nach Buchtitel (S), Buch Hinzufügen (H), Filtere Bücher nach Jahr (F) "
                 "Anzeige der Bücherei-Datenbank (A). \n"
                 "Bitte gib einen der jeweiligen Buchstaben S, H, F oder A an "
                 "oder gib 'ende' ein, um das Programm zu beenden. \n"
                 "Deine Auswahl: ").upper() #Benutzer wird aufgefordert Aktion auszuwählen. Umwandlung in Großbuchstaben.

    if funktion == 'ENDE': #wenn der Benutzer "ende" eingibt (egal ob groß oder klein), wird Schleife beendet.
        print("Programm beendet.")
        break
    
    elif funktion == "S":
        titel = input("Bitte gib den Buchtitel ein: ")
        autor = input("Bitte gib den Autor ein oder Enter zum Überspringen: ")
        autor = autor if autor.strip() else None #Wenn kein Autor eingegeben wird (nur Enter), wird 'autor' auf None gesetzt
        ergebnisse = suche_buch(titel, autor) #Suche durchgeführt
        if ergebnisse: #Wenn Ergebnisse gefunden, Ausgabe
            print("Such-Ergebnisse: ")
            for buch in ergebnisse:
                print(f"Titel: {buch['Titel']}, Autor: {buch['Autor']}, Jahr: {buch['Jahr']}")
        else:
            print("Kein Buch gefunden. ") #Wenn keine Ergebnisse gefunden, Ausgabe       
    
    elif funktion == "H":
        titel = input("Bitte gib den Buchtitel ein: ")
        autor = input("Bitte gib den Autor ein: ")
        jahr = int(input("Bitte gib das Erscheinungsjahrs ein: ")) #Aufforderung Benutzereingabe und Umwandlung in Zahl
        fuege_buch_hinzu(titel, autor, jahr) #Buch wird zur Datenbank hinzugefügt
        print("Buch erfolgreich hinzugefügt. ")
    
    elif funktion == "F":
        jahr = int(input("Nach welchem Erscheinungsjahr soll gefiltert werden? ")) #Aufforderung Benutzereingabe und Umwandlung in Zahl
        gefiltert = buecher_nach_jahr(jahr) #Filterfunktion angewendet
        if gefiltert: #Wenn Liste gefiltert nicht leer ist
            print(f"Bücher aus dem Jahr {jahr}: ")
            for buch in gefiltert: #über jedes Buch in der gefiltert Liste iteriert und
                print(f"Titel: {buch['Titel']}, Autor: {buch['Autor']}") #formatierte Ausgabe erstellt
        else: 
            print("Keine Bücher für dieses Erscheinungsjahr gefunden.")
    
    elif funktion == "A":
        zeige_datenbank() #Aufruf Funktion zur Anzeige aktueller Datenbank
  
    else:
        print("Ungültige Eingabe. Bitte gib einen gültigen Buchstaben S, H, F oder A ein")