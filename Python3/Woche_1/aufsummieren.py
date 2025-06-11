summe = 0 #Die Variable summe enthält die Summe der eingegebenen Zahlen. Sie wird hier mit einem Anfangswert belegt. Ohne diese Initialisierung gäbe es in Zeile #5 eine Fehlermeldung, weil dann der Name summe noch nicht definiert wäre.
anzahl = 0 # siehe summe
zahl = input("Zahl: ") #achtung hier kann noch kein casting stattfinden, aus leerem String (Enter) kann keine Zahl gewonnen werden.
while zahl: #der string hat den assozierten Wahrheitswert True, wenn nicht leer (Enter)
    summe += float(zahl) # aus dem String wird Gleitkommazahl & aktueller Wert um diese Zahl erhöht
    anzahl += 1 # der Wert von anzahl wird um 1 erhöht
    zahl = input("Zahl: ") # erneut wird auf Eingabe gewartet, Schleife wird erneut durchlaufen oder Stopp

print ("Die Summe der ", anzahl, "Zahlen ist ", summe)