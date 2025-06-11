eingabe = "j" # Die Variable eingabe erhält den Anfangswert 'j', damit die Schleife wenigstens einmal durchlaufen wird.
gesamtflaeche = 0
while eingabe == "j": # Solange eingabe den Wert 'j' enthält, wird die Schleife durchlaufen, und es werden weitere Fenster in die Rechnung einbezogen.
    breite = float(input("Breite des Fensters (m): "))
    hoehe = float(input("Höhe des Fensters (m): "))
    anzahl = int(input("Anzahl der Fenster dieser Größe: "))
    gesamtflache = breite * hoehe * anzahl
    print("Gesamtfläche: ", round(gesamtflache,2), "m2") # Die Gesamtfläche wird auf zwei Stellen nach dem Komma gerundet und ausgegeben.

    eingabe = input("Weitere Fenster? (j/n): ")
print("Auf Wiedersehen!")
input() # Der Computer wartet darauf, dass die (Enter)-Taste gedrückt wird. Erst dann wird das Programm beendet.
