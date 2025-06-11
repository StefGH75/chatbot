#a) Benenne die vier Hauptdatentypen in Python und gib für jeden Datentyp ein Beispiel an.
# Ganzzahl = 7 (int)
# Dezimalzahl = 7.7 (float)
# Zeichenkette = "Wort" (str) string
# Boolescher Wert = True (bool)

#b) Erstelle eine Liste mit mindestens drei verschiedenen Datentypen und zeige, 
# wie man den Typ jedes Elements in der Liste bestimmt.
liste = [1, "wort", 8.5]
for element in liste:
    print(type(element))

#c) Beschreibe, wie man eine Ganzzahl (int) in eine Gleitkommazahl (float) umwandelt 
# und gib ein Beispiel dafür.
# eine Ganzzahl wird in eine gleitkommazahl umgewandelt, in dem eine neue Variable mit dem Typ float erstellt wird
zahl = 7 
zahl_neu = float(zahl)
print(zahl_neu)

#d) Erkläre, was ein Tupel ist und vergleiche es kurz mit einer Liste hinsichtlich 
# der Änderbarkeit der Elemente.
# # Ein Tupel ist eine Zusammensetzung aus Objekten, die unterschiedliche Typen sein können und geordnet sind.
# Es ist nicht veränderbar im Gegensatz zu einer Liste.


#e) Schreibe ein kurzes Python-Programm, das eine Zeichenkette (str) und eine Ganzzahl (int) 
# nimmt, die Ganzzahl in eine Zeichenkette umwandelt und beide Zeichenketten zusammenfügt. 
# Kommentiere jede Zeile deines Codes, um das EVA-Prinzip (Eingabe, Verarbeitung, Ausgabe) 
# zu demonstrieren.
zeichenkette = "wort " #Eingabe
zahl = 7
zahl_neu = str(zahl) #Verarbeitung
zeichenkette_neu = zeichenkette + zahl_neu
print(zeichenkette_neu) # Ausgabe
