#a) Definiere Variablen für jeden der folgenden Datentypen: int, float, complex, str, tuple, list, und set. Weise jeder Variablen einen repräsentativen Wert zu. Zum Beispiel könnte die Variable für den Datentyp int den Wert 42 haben.
zahl = 42
dezimalzahl = 7.7
komplex = 42 + 7j
wort = "hoffnung"
tuple_beispiel = (42, "Antwort auf alles")
liste = [1, 2, 3, 4]
menge = {3, 4, 5, 6}

#b) Für jede definierte Variable, verwende die type() Funktion, um den Datentyp der Variable zu überprüfen. 
#Gib das Ergebnis mit der print() Funktion aus, sodass für jede Variable eine Zeile in der Form "Der Datentyp von [Variable] ist: [Datentyp]" ausgegeben wird.

print(f"Der Datentyp von zahl ist {type(zahl)}")
print(f"Der Datentyp von dezimalzahl ist {type(dezimalzahl)}")
print(f"Der Datentyp von komplex ist {type(komplex)}")
print(f"Der Datentyp von wort ist {type(wort)}")
print(f"Der Datentyp von tuple_beispiel ist {type(tuple_beispiel)}")
print(f"Der Datentyp von liste ist {type(liste)}")
print(f"Der Datentyp von menge ist {type(menge)}")

#c) Konvertiere die float Variable in einen int Datentyp und gib das Ergebnis aus. 
#Erkläre in einem Kommentar, was bei der Konvertierung passiert.

neue_zahl = int(dezimalzahl)
print(f"neue Zahl: {neue_zahl}")
#es wird eine neue Zahl erstellt, bei der die Nachkommastellen abgeschnitten werden

#d) Erstelle eine neue Liste, die aus den ersten zwei Elementen der ursprünglichen Liste und dem letzten Element des Tupels besteht. 
#Gib diese neue Liste aus
liste_neu=liste[0:2] + [tuple_beispiel[-1]] #liste_neu = [liste[0], liste[1], tuple_beispiel[-1]]
print(f"neue Liste: {liste_neu}")

#e) Füge der Menge ein neues Element hinzu, das nicht in der Menge enthalten ist, und gib die aktualisierte Menge aus. 
menge.add(9)
print(f"neue Menge: {menge}")

#fffff
name = input("Name: ")
gruß = "Hallo " + name + "!"
print(gruß)
type(gruß)
