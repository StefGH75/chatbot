# Erstelle eine Klasse Auto, welche folgende Attribute besitzt: marke (String), modell (String), 
# kilometerstand (Integer) und tankfüllung (in Prozent als Integer). Die Klasse soll zwei Methoden haben: 
# fahren(kilometer) und tanken(prozent). Die Methode fahren(kilometer) soll den Kilometerstand um die
#  gefahrenen Kilometer erhöhen und die Tankfüllung basierend auf einer Annahme, dass das Auto pro 100 
# Kilometer 5% des Tanks verbraucht, reduzieren. Die Methode tanken(prozent) soll die Tankfüllung um den 
# angegebenen Prozentsatz erhöhen, darf aber 100% nicht überschreiten.

class Auto:
    def __init__(self, marke, modell, kilometerstand, tankfuellung):
        self.marke = marke
        self.modell = modell
        self.kilometerstand = kilometerstand
        self.tankfuellung = tankfuellung

    def fahren(self, kilometer):
        verbrauch = kilometer * 0.05
        if self.tankfuellung < verbrauch:
            print("Nicht genügend Treibstoff für Strecke")
            return
        self.kilometerstand += kilometer
        self.tankfuellung -= verbrauch
        print(f"{kilometer}km gefahren. Neuer Kilometerstand: {self.kilometerstand}, Tankfüllung: {self.tankfuellung:.2f}%")        

    def tanken(self, prozent):
        if prozent < 0:
            print("ungültiger Tankwert")
            return
        self.tankfuellung += prozent
        if self.tankfuellung > 100:
            self.tankfuellung = 100
        print(f"Getankt. Aktuelle Tankfüllung: {self.tankfuellung:.2f}%")

mein_auto = Auto("Toyota", "Corolla", 50000, 50)

mein_auto.fahren(200)   # sollte 10% verbrauchen
mein_auto.tanken(20)    # sollte auf 70% erhöhen (oder max. 100%)
