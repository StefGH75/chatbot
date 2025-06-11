# Entwickle eine Python-Klasse namens Buch, die zur Verwaltung einer kleinen Bibliothek dient. Die Klasse 
# soll folgende Attribute und Methoden haben:
# a) Die Klasse soll drei Attribute haben: titel (String), autor (String) und ausgeliehen (Boolean), wobei 
# ausgeliehen standardmäßig auf False gesetzt ist.
# b) Schreibe eine Initialisierungsmethode __init__, die titel und autor als Parameter erhält und diese 
# zusammen mit dem Standardwert für ausgeliehen setzt.
# c) Füge eine Methode ausleihen hinzu, die das Attribut ausgeliehen auf True setzt, falls das Buch nicht 
# bereits ausgeliehen ist. Falls das Buch bereits ausgeliehen ist, soll eine Nachricht "Buch bereits 
# ausgeliehen" ausgegeben werden.
# d) Füge eine Methode zurueckgeben hinzu, die das Attribut ausgeliehen auf False setzt, falls das Buch 
# ausgeliehen war. Falls das Buch nicht ausgeliehen ist, soll eine Nachricht "Buch war nicht ausgeliehen" 
# ausgegeben werden.
# e) Schreibe eine Methode status, die den Titel, Autor und den Ausleihstatus des Buches in einem Satz ausgibt. 

class Buch():

    def __init__(self, titel, autor):
        self.titel = titel
        self.autor = autor
        self.ausgeliehen = False

    def ausleihen(self):
        if self.ausgeliehen:
            print("Buch bereits ausgeliehen")
        else:
            self.ausgeliehen = True
            print(f"Das Buch '{self.titel}' von {self.autor} wurde ausgeliehen.")

    def zurueckgeben(self):
        if self.ausgeliehen:
            self.ausgeliehen = False
            print(f"Das Buch '{self.titel}' von {self.autor} wurde zurückgegeben.")
        else:
            print("Buch war nicht ausgeliehen")

    def status(self):
        if self.ausgeliehen:
            print(f"Das Buch {self.titel} von: {self.autor} ist ausgeliehen.")
        else:
            print(f"Das Buch: {self.titel} von: {self.autor} ist zurückgegeben.")


buch_1 = Buch("Python lernen","Max Mustermann")

buch_1.status()
buch_1.ausleihen()
buch_1.status()
buch_1.zurueckgeben()
buch_1.status()