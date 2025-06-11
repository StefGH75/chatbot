# a) Definiere eine Funktion filtere_gerade_zahlen, die eine Liste von Zahlen als Argument nimmt und eine 
# neue Liste zurückgibt, die nur die geraden Zahlen enthält. Verwende dazu eine Schleife, um durch die Liste 
# zu iterieren.
# b) Füge am Anfang der Funktion eine Zusicherung ein, die sicherstellt, dass das übergebene Argument eine 
# Liste ist. Falls das Argument keine Liste ist, soll das Programm mit einer AssertionError enden.
# c) Schreibe eine zweite Funktion sortiere_liste, die eine Liste von Zahlen nimmt und diese mit dem 
# Quicksort-Algorithmus sortiert. Du kannst die Implementierung des Quicksort-Algorithmus selbst wählen, 
# achte aber darauf, dass du den Algorithmus korrekt implementierst.
# d) Verwende die Funktion filtere_gerade_zahlen, um eine Liste von Zahlen zu filtern, und verwende dann 
# die Funktion sortiere_liste, um die gefilterte Liste zu sortieren. Gib das Ergebnis aus.
# e) Füge am Ende des Skripts eine Testroutine ein, die deine Funktionen mit einer vorgegebenen Liste von 
# Zahlen testet. Die Liste soll sowohl positive als auch negative Zahlen sowie Null enthalten. 


def filtere_gerade_zahlen(zahlen):
    assert isinstance(zahlen, list), "Das Argument muss eine Liste sein" #Sicherstellen, dass das Argument eine Liste ist
    gerade_zahlen = [] #Leere Liste zur Speicherung gerader Zahlen
    for zahl in zahlen:
        if zahl % 2 == 0:  #Wenn die Zahl durch 2 teilbar ist (gerade), zur Liste hinzufügen
            gerade_zahlen.append(zahl)
    return gerade_zahlen

def sortiere_liste(zahlen):
    if len(zahlen) <= 1:  #Abbruchbedingung: Liste mit 0 oder 1 Element ist schon sortiert
        return zahlen
    else:
        pivot = zahlen[0] #Erstes Element als "Pivot" auswählen
        kleiner_als_pivot = [x for x in zahlen[1:] if x < pivot]
        groesser_als_pivot = [x for x in zahlen[1:] if x >= pivot]
        return sortiere_liste(kleiner_als_pivot) + [pivot] + sortiere_liste(groesser_als_pivot)
        # Rekursiver Aufruf für beide Teillisten, und Zusammenfügen
def main():
    test_liste = [17, -3, 0, 4, 5, 2, 18, -11, 8]
    gefilterte_liste = filtere_gerade_zahlen(test_liste) #Nur gerade Zahlen herausfiltern
    sortierte_liste = sortiere_liste(gefilterte_liste) #Diese gefilterte Liste sortieren
    print("Gefilterte und sortierte Liste: ", sortierte_liste)

if __name__ =="__main__": #Nur ausführen, wenn das Skript direkt gestartet wird (nicht beim Import)
    main()
