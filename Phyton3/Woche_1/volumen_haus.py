#Berechnung für Volumen eines Hauses 
#v1 = a * b * h1
#v2 = (a * b * h2) / 2

hoehe_haus = float(input("Wie hoch ist das Haus ohne Dach: "))
breite = float(input("Wie breit ist Haus: "))
laenge = float(input("Wie lang ist das Haus: "))
hoehe_dach = float(input("Wie hoch ist das Dach: "))

a = breite
b = laenge
h1 = hoehe_dach
h2 = hoehe_haus
volumen_dach = breite * laenge *hoehe_dach
volumen_haus = (breite * laenge * hoehe_haus) / 2
gesamt_volumen = volumen_dach + volumen_haus

print("Das Volumen des Hauses beträgt: ", round(gesamt_volumen), "m3")

