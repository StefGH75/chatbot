zahl = float(input("Zahl: "))
genauigkeit = float(input("Genauigkeit (z.B. 0.0001): "))
zahl_alt = (zahl + 1) / 2
d= 10000 # beliebig großer Wert zugewiesen, damit d überhaupt definiert ist

while d > genauigkeit:# solange Wert zahl_alt und zahl_neu noch größer als Genauigkeit ist, wird Schleife durchlaufen
    zahl_neu = zahl_alt - (zahl_alt ** 2 - zahl) / (2 * zahl_alt) # entsprechend Heron-Verfahren aus zahl_alt ein neues Folgeglied zahl_neu berechnet
    d = abs(zahl_neu - zahl_alt) # Abstand zwischen beiden Zahlen ermittelt, um sicherzustellen, dass Wert nicht negativ ist
    zahl_alt = zahl_neu

print("Die Quadratwurzel aus", zahl, "ist ungefähr", zahl_alt)