G = {1:[2, 4], 2:[1, 3, 5], 3:[2, 5], 4:[1, 5], 5:[4, 2, 3, 6], 6:[5]}

def suche_weg(aktuell, ziel, besucht): #rekursive Funktion zur Wegsuche, ruft sich selbst auf, aktuell=aktuell
                                        #besuchter Knoten, besucht= Liste besuchter Knoten
    besucht = besucht + [aktuell] #Knoten aktuell wird als besucht markiert, neue Liste erstellt, die aus 
                                    #übergebener liste besucht , an die die Nummer des aktuellen Knoten gehangen wird
    if aktuell == ziel: #wenn Knoten Zielknoten entspricht Ziel erreicht
        return besucht # kann dann als Ergebnis zurückgegeben werden
    else: 
        wege = [] #in dieser Liste werden Wege vom aktuellen Knoten zum Ziel gesammelt
        for k in G[aktuell]: #Iteration über die Liste der Nachbarknoten des aktuellen Knoten, Laufvariable ist k
            if k not in besucht: #wenn k noch nicht besucht wurde
                weg = suche_weg(k, ziel, besucht) #wird Funktion rekursiv aufgerufen, übergebenen Argumente sind 
                                                    #Knoten k, erweiteerte Liste besuchter Knoten und unveränderte Nummer Ziel
                if weg: #wenn es einen Weg gibt
                   wege.append(weg) #wenn ein Weg gefunden wurde, wird er der Liste hinzugefügt
        if wege:
            längen = [len(w) for w in wege] #mit dieser list comprehension wird Liste erzeugt, die Längen aller gefunden Wege enthält
            for weg in wege:
                if len(weg) == min(längen): #der gefundene Weg mit der kleinsten Länge wird zurückgegeben
                    return(weg) #wird Weg geliefert
        else:
            return [] #wenn es keinen Weg gibt, leere Liste, Ausführung beendet

while True:
    start = int(input("Start: "))
    ziel = int(input("Ziel: "))
    weg = suche_weg(start, ziel, []) #erster Aufruf der Funktion, dritter Parameter ist leere Liste, da bisher noch kein Knoten besucht
    print("Weg: ", weg)

    