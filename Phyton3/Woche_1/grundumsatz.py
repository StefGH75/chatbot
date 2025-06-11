print("Wenn du mir ein paar Daten gibst, kann ich deinen Grundumsatz berechnen")
geschlecht = input("Bist du ein Mann oder eine Frau (m/w): " )
alter = int(input("Wie alt bist du: "))
groeße = float(input("Wie groß bist du in cm: "))
gewicht = float(input("Wieviel wiegst du in kg: "))
if geschlecht == "m":
    grundumsatz_mann = 66.5 + 13 * gewicht + 5 * groeße - 6.8 * alter
    print("Dein Grundumsatz liegt bei: ", round(grundumsatz_mann), "Kalorien")
else:
    grundumsatz_frau = 655 + 9.6 * gewicht + 1.8 * groeße - 4.7 * alter
    print("Dein Grundumsatz liegt bei", round(grundumsatz_frau), "Kalorien")