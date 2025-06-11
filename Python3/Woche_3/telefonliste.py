TEL = [("Matthias", "0201 46134488"), ("Bea", "0201 3341999"), ("Marius", "0177 494949")] #Telefonliste als Tupel definiert
MENÜ = '''(T)elefonnumer suchen 
(N)amen suchen
(E)nde
''' #enthält Text, der an mehreren Stellen ausgegeben werden soll. Durch Definition Konstante wird Programm kürzer

def suche_nummern(suchwort): #Funktion, die in TEL nach allen Namen sucht, die das suchwort enthalten
    for name, nummer in TEL: #alle Tupel der Liste werden durchlaufen. Variable name enhält das erste item und nummer enthält das zweite item (auspacken)
        if suchwort in name: #wenn suchwrit im string name vorkommt:
            print(name, nummer) #vollständiger Namen und zugehörige Nummern werden ausgegeben

def suche_namen(ziffern): #Funktion, die in TEL nach Ziffern sucht.
    for name, nummer in TEL: #alle Tupeln der Liste werden durchlaufen. Variable name enthält das erste item, nummer das zweite
        if ziffern in nummer: #wenn die ziffern in der zweiten Variable nummern enthalten sind
            print(name, nummer) #vollständiger Namen und zugehörige Nummer werden ausgegeben

print(MENÜ) #Test mit Auswahlmenü ausgegeben
eingabe = input("Auswahl (t, n, e): ") #Benutzer gebeten eine Option auszuwählen

while eingabe != "e": #while-Schleife solange durchlaufen bis ein e eingegeben worden ist
    if eingabe == "n":
        suchwort = input("Suchwort: ")
        suche_nummern(suchwort)
    elif eingabe == "t":
        ziffern = input("Ziffern: ")
        suche_namen(ziffern)
    print(MENÜ)
    eingabe = input("Auswahl (t, n, e): ")

print("Bis bald!")