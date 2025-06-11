liste_tupel = [(1,"a"),(2,"b"),(3,"c"),(4,"d"),(5,"f")]

def pruefe_elemente(zahl, buchstabe):
    if (zahl, buchstabe) in liste_tupel:
        print(f"Element gefunden: ({zahl},{buchstabe})")
    else: 
        print("Element nicht gefunden")

def zeichenkette_in_zahl(zeichenkette):
    zahl = int(zeichenkette)
    print(f"Umwandlung erfolgreich: {zahl}")
    return zahl

while True:
    auswahl = input("Wähle eine Option: 'suchen', 'umwandeln', 'beenden': ")
    if auswahl == "suchen":
        buchstabe = input("Gib den Buchstaben des Elements an: ")
        zahl = int(input("Gib die Zahl des Elements an: "))
        pruefe_elemente(zahl, buchstabe)
        
    elif auswahl =="umwandeln":
        zeichenkette = input("Gib eine Zeichenkette ein, die in eine Zahl umgewandelt werden soll: ")
        umgewandelte_zahl= zeichenkette_in_zahl(zeichenkette)
        if umgewandelte_zahl is not None:
            if umgewandelte_zahl > 0:
                print("Die Zahl ist positiv")
            elif umgewandelte_zahl < 0:
                print("Die Zahl ist negativ")
            else:
                print("Die Zahl ist Null")
        
    elif auswahl =="beenden":
        break
    else:
        print("Ungültige Eingabe. Bitte versuche es erneut")

    
