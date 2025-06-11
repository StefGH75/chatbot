farbe = input("Farbe (rot, grün, gelb): ")
durchmesser = float(input("Durchmesser in cm: "))
stein = input("Hat die Frucht einen Stein? (j/n): ")
if (farbe == "grün") and (durchmesser > 15) and (stein=="n"):
    frucht = "Wassermelone"
elif (farbe == "gelb") and (durchmesser < 10):
     frucht = "Zitrone"
elif (farbe in {"rot","grün"}) and (5 < durchmesser < 15):
     frucht = "Apfel"
elif (farbe in {"rot","grün"}) and \
     durchmesser <=5 and not stein:
     frucht = "Traube"
elif (farbe == "rot") and stein:
     frucht = "Kirsche"
else:
     frucht = "Unbekannte Frucht"

print("Es handelt sich um folgende Frucht:")
print(frucht)
    