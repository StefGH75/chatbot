#Entwickle ein Python-Programm, das folgende Funktionen umfasst:
#a) Eine Funktion buch_daten_speichern, die als Parameter den Titel eines Buches (String), den Namen des Autors
#  (String), das Veröffentlichungsjahr (Integer), und optional die Anzahl der Seiten (Integer, Defaultwert 0) 
# erhält. Die Funktion soll alle diese Daten in einem Dictionary speichern, wobei die Schlüssel titel, autor,
#  jahr, und seiten sind. Die Funktion gibt dieses Dictionary zurück.
# b) Eine Funktion buecher_sammlung, die eine Liste von Bücher-Dictionaries (erstellt von buch_daten_speichern)
#  als Parameter erhält und die Gesamtanzahl der Seiten aller Bücher in der Liste berechnet. Die Funktion gibt
#  die Gesamtseitenzahl zurück.
#c) Verwende eine Schleife, um den Benutzer zur Eingabe von Daten für drei verschiedene Bücher aufzufordern. 
# Nutze dabei die Funktion buch_daten_speichern für jedes Buch und speichere jedes resultierende Dictionary 
# in einer Liste.
# d) Nachdem alle Bücher eingegeben wurden, rufe die Funktion buecher_sammlung mit der Liste der 
# Bücher-Dictionaries als Argument auf, um die Gesamtanzahl der Seiten aller Bücher zu berechnen.
# e) Gib die Gesamtanzahl der Seiten aller Bücher aus. 

#Funktion zum Speichern der Buchdaten in einem Dictionary
def buch_daten_speichern(titel, autor, jahr, seiten="0"): #Defaultwert für seiten=0
    buch_dict = {"titel":titel, "autor":autor, "jahr":jahr, "seiten":seiten} #Schlüssel bekommen Wert der jeweiligen Parameter
    return buch_dict #gibt das erstellte Dictonary zurück

#Funktion zur Berechnung der Gesamt-Seitenanzahl aller Bücher:
def buecher_sammlung(buecherliste):
    gesamtseiten = sum(buch["seiten"] for buch in buecherliste) #summiert die Seitenanzahl jedes Buches in der übergebenen Liste
    return gesamtseiten #gibt Seitenanzahl zurück

buecher_liste = [] #erstellt leere Liste zur Speicherung der Buch-Dictionaries
for _ in range(3): #wiederhole die Eingabe für 3 Bücher
    titel = input("Titel des Buches: ") #Benutzer wird nach Titel gefragt
    autor = input("Autor des Buches: ") #Benutzer wird nach Autor gefragt
    jahr = int(input("Veröffentlichungsjahr des Buches: ")) #Benutzer wird nach Jahr gefragt
    seiten = int(input("Anzahl Seiten des Buches: ")) #Benutzer wird nach Seiten gefragt
    seiten = int(seiten) if seiten else 0 #Wenn Benutzer eine Zahl eingibt wird sie umgewandelt, sonst 0 als Standard
    buch_dict = buch_daten_speichern(titel, autor, jahr, seiten) #ruft die Funktion auf um buch_dict zu erstellen
    buecher_liste.append(buch_dict) #fügt das buch_dict zur Bücherliste hinzu
gesamtseiten = buecher_sammlung(buecher_liste) # berechnet gesamtseiten aller eingegeben Bücher
print(f"Gesamtzahl der Seiten aller Bücher beträgt: {gesamtseiten}") #gibt Ergebnis aus