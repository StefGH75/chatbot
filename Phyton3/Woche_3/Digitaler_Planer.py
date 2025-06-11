Menue = '''
n: neue Aktivität eingeben
d: dringenste Aktivität eingeben
e: Ende'''

def neue_aktivitaet():
    aktivitaet = []
    with open("digitalplaner.txt", "a") as datei:
        for zeile in datei:
            aktivitaet, zeit = zeile.strip().split(": ") #entfernt das Zeilenende und trennt Name und Alter anhand Trennzeichen
            aktivitaet.append({"Aktivität": aktivitaet, "Zeit": int(zeit)}) #fügt Dictionary ein mit Name und Alter als int zur Liste hinzu
        return aktivitaet #gibt die Liste zurück

    aktivitaet = input("Aktivität: ")
    wann = input("In wie vielen Stunden zu erledigen: ")

print("Noch {time} Minuten für: {aktivitaet}")

def main():
    auswahl = input("Auswahl: ")
    
print("Bis bald!")