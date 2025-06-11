# a) Definiere Variablen für jeden der folgenden Datentypen: int, float, complex, str, tuple, list und set. 
# Verwende für die Definition dieser Variablen Werte deiner Wahl, aber achte darauf, dass die Werte repräsentativ für den jeweiligen Datentyp sind.

zahl = 7
dezimalzahl = 7.7
komplex = 3 + 7j
zeichenkette = "liebe"
tuple_beispiel = ("liebe", "hass")
liste = [2, 4, 6, 8]
menge = {1, 3, 5, 7}

#b) Für jede der definierten Variablen, verwende die Funktion type() und drucke den Datentyp der Variable in der Konsole aus.
zahl = 7
type(zahl)

#c) Konvertiere die int Variable in einen float und einen str Datentyp und drucke das Ergebnis aus.
zahl_float = int(zahl)
zahl

zahl_float = str(zahl)
zahl
#d) Erstelle eine neue Liste, die aus den ersten zwei Elementen der ursprünglichen Liste und dem letzten Element der Tupel-Variable besteht. Prüfe, ob das letzte Element des Tupels bereits in der neuen Liste vorhanden ist, bevor du es hinzufügst. Drucke die neue Liste aus.
liste_neu=liste[0:2]
liste_neu
tuple_beispiel[1:2]

liste_neu = liste[:2]
if tuple_beispiel[-1] not in liste_neu:
  liste_neu.append(tuple_beispiel[-1])
  print(liste_neu)

#e) Verwende die set Variable, um ein Element hinzuzufügen, das bereits existiert, und ein neues Element, das noch nicht in der Menge vorhanden ist. Drucke die veränderte Menge aus. 
menge.add(3)
menge 
menge.add(9)
menge