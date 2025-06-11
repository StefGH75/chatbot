#bauwerk

from Phyton3.Woche_2.modul_volumen import * #Vom Modul Volumen, das wir vorher erstellt haben, werden alle Namen importiert
summe = 0 #Variable summe wird das Gesamtvolumen des Gebäudes. Anfangs hat es Wert 0 und wird sukkzessive erhöht
eingabe = input("(Q)uader, (K)uppel, (E)nde: ") #das Programm wartet darauf, dass sich Benutzer entscheidet und Buchstaben eingibt
while eingabe in "kKqQ":
    if eingabe in "kK":
        h = float(input("Höhe (m): "))
        r = float(input("Radius (m): "))
        n = float(input("Anzahl dieser Kuppeln: "))
        summe += n * kuppel(h,r)
    elif eingabe in "qQ":
        l = float(input("Länge (m): "))
        b = float(input("Breite (m): "))
        h = float(input("Höhe (m): "))
        n = float(input("Anzahl dieser Quader: "))
        summe += n * quader(l,b,h)
    eingabe = input("(Q)uader, (K)uppel, (E)nde: ")
print("Das Volumen des Gebäudes ist:" , round(summe, 2), "m2")