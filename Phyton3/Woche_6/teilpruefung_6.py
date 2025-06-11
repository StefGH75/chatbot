"""Teilprüfung 6
Autorin: Stefanie Millow
Buchladen"""

#a)
class Buch:
    def __init__(self, titel, autor, kategorie, preis):
        self.titel = titel
        self.autor = autor
        self.kategorie = kategorie
        self.preis = preis

    def __str__(self):
        return f"{self.titel} von {self.autor} ({self.kategorie}) - {self.preis:.2f}€"
        
#b)
class Buchladen:
    def __init__(self):
        self.inventar = []

    def hinzufuegen(self, buch):
        self.inventar.append(buch)
        print(f"Buch hinzugefügt: {buch}")

    def durchsuchen(self, kategorie):
        # gefundene_buecher =[]
        # for buch in self.inventar:
        #     if buch.kategorie.lower() == kategorie.lower():
        #         gefundene_buecher.append(buch)
        # return gefundene_buecher
        return [buch for buch in self.inventar if buch.kategorie.lower() == kategorie.lower()] #List Comprehension aus Schleife

    def berechnen_preis(self, buchliste):
        # summe = 0
        # for buch in buchliste:
        #     summe += buch.preis
        # return summe
        return sum(buch.preis for buch in buchliste) #List Comprehension statt Schleife
    
#c) Beispielnutzung:
buchladen = Buchladen()

#Einige Bücher erstellen und zum Inventar hinzufügen:
buch_1 = Buch("Der Schatten des Windes", "Carlos Ruiz Zafón", "Roman", 12.00)
buch_2 = Buch("Der Alchimist", "Paulo Coelho", "Roman", 12.99)
buch_3 = Buch("1984", "George Orwell", "Roman", 10.00)
buch_4 = Buch("Das Universum in der Nussschale", "Stephen Hawking", "Wissenschaft", 18.50)
buch_5 = Buch("Sapiens", "Yuval Noah Harari", "Sachbuch", 15.99)
buch_6 = Buch("Schnelles Denken, Langsames Denken", "Daniel Kahnemann", "Sachbuch", 16.00)
buch_7 = Buch("Eine kurze Geschichte der Menschheit", "Yuval Noah Harari", "Sachbuch", 14.99)

buchladen.hinzufuegen(buch_1)
buchladen.hinzufuegen(buch_2)
buchladen.hinzufuegen(buch_3)
buchladen.hinzufuegen(buch_4)
buchladen.hinzufuegen(buch_5)
buchladen.hinzufuegen(buch_6)
buchladen.hinzufuegen(buch_7)

#Suche nach Kategorie:
suche_kategorie = input("\nNach welcher Kategorie suchen: ")
print(f"\nBücher der Kategorie {suche_kategorie}:")
gefundene_buecher = buchladen.durchsuchen(suche_kategorie)
for buch in gefundene_buecher:
    print(buch)

#Berechne Gesamtpreis einer Auswahl:
auswahl = [buch_1, buch_4, buch_5]
gesamtpreis = buchladen.berechnen_preis(auswahl)
print("\nAuswahl Bücher zum Berechnen:")
for buch in auswahl:
    print(f"- {buch.titel}: {buch.preis:.2f} €")
print(f"\nGesamtpreis der Auswahl = {gesamtpreis:.2f} €")