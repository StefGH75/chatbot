# Entwickle eine Python-Klasse Auto, die verschiedene Attribute wie marke, modell, baujahr und kilometerstand
#  hat. Die Klasse sollte folgende Methoden beinhalten: 
# a) Eine Initialisierungsmethode, die es ermöglicht, bei der Erstellung eines Auto-Objekts die Marke, das 
# Modell und das Baujahr anzugeben, während der Kilometerstand standardmäßig auf 0 gesetzt wird. 
# b) Eine Methode fahren, die den Kilometerstand um die gefahrenen Kilometer erhöht, die als Parameter 
# übergeben werden. 
# c) Eine Methode anzeigen, die die Details des Autos (Marke, Modell, Baujahr, Kilometerstand) in einer 
# lesbaren Form ausgibt.
# Stelle sicher, dass du die Konzepte der objektorientierten Programmierung korrekt anwendest, insbesondere 
# die Definition von Klassen, die Initialisierung von Objekten und das Aufrufen von Methoden. Teste deine 
# Klasse, indem du mindestens zwei Auto-Objekte erstellst, mit der Methode fahren den Kilometerstand änderst 
# und schließlich die Details jedes Autos mit der Methode anzeigen ausgibst. 

class Auto:
    
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.kilometerstand = 0

    def fahren(self, kilometer):
        self.kilometerstand += kilometer

    def anzeigen(self):
        print(f"Marke: {self.marke}, Modell: {self.modell}, Baujahr: {self.baujahr}, Kilometerstand: {self.kilometerstand}")

auto_1 = Auto("Toyota", "Corolla", 2018)
auto_2 = Auto("Volkswagen", "Golf", 2020)           

auto_1.fahren(100000)
auto_2.fahren(50000)

auto_1.anzeigen()
auto_2.anzeigen()