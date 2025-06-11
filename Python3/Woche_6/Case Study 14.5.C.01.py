# Du arbeitest als Softwareentwickler in einem Unternehmen, das sich auf die Entwicklung von 
# Unternehmenssoftware spezialisiert hat. Dein aktuelles Projekt beinhaltet die Entwicklung einer Anwendung 
# zur Verwaltung von Mitarbeiterdaten. Die Anwendung soll es ermöglichen, Mitarbeiterdaten zu erfassen, zu 
# aktualisieren, zu löschen und zu durchsuchen. Die Mitarbeiterdaten umfassen Name, Position, Abteilung,
# Gehalt und Einstellungsdatum. Du sollst eine objektorientierte Lösung in Python entwerfen, die folgende 
# Anforderungen erfüllt:
# a) Entwerfe eine Klasse Mitarbeiter, die die Attribute Name, Position, Abteilung, Gehalt und
#  Einstellungsdatum speichert. Implementiere Methoden zum Setzen und Abrufen dieser Attribute sowie eine 
# Methode zeige_daten(), die alle Daten eines Mitarbeiters in einem formatierten String ausgibt.
# b) Entwickle eine Klasse MitarbeiterVerwaltung, die eine Liste von Mitarbeiter-Objekten verwaltet. Diese 
# Klasse soll Methoden zum Hinzufügen, Aktualisieren (basierend auf dem Namen), Löschen (basierend auf dem 
# Namen) und Suchen (basierend auf dem Namen oder der Abteilung) von Mitarbeitern beinhalten.
# c) Implementiere eine einfache Benutzeroberfläche unter Verwendung des tkinter-Moduls, die es dem Benutzer 
# ermöglicht, Mitarbeiterdaten einzugeben, zu aktualisieren, zu löschen und zu durchsuchen. Die 
# Benutzeroberfläche sollte auch eine Ausgabebereich haben, in dem die Ergebnisse von Suchoperationen oder die
#  Daten eines neu hinzugefügten oder aktualisierten Mitarbeiters angezeigt werden.

from tkinter import *
from tkinter import messagebox

class Mitarbeiter:
    def __init__(self, name, position, abteilung, gehalt, einstellungsdatum):
        assert isinstance(abteilung, str), "Abteilung muss ein String sein!"
        self.name = name 
        self.position = position
        self.abteilung = abteilung
        self.gehalt = gehalt
        self.einstellungsdatum = einstellungsdatum
    
    def zeige_daten(self):
        return f"Name: {self.name}, Position: {self.position}, Abteilung: {self.abteilung}, Gehalt: {self.gehalt}, Einstellungsdatum: {self.einstellungsdatum}"

class MitarbeiterVerwaltung:
    def __init__(self):
        self.mitarbeiter_liste = []

    def daten_hinzufuegen(self, mitarbeiter):
        self.mitarbeiter_liste.append(mitarbeiter)

    def daten_aktualisieren(self, name, neue_position, neue_abteilung, neues_gehalt, neues_datum):
        for mitarbeiter in self.mitarbeiter_liste:
            if mitarbeiter.name == name:
                mitarbeiter.position = neue_position
                mitarbeiter.abteilung = neue_abteilung 
                mitarbeiter.gehalt = neues_gehalt
                mitarbeiter.einstellungsdatum = neues_datum
                return True
        return False

    def loeschen(self, name):
        for mitarbeiter in self.mitarbeiter_liste:
            if mitarbeiter.name == name:
                self.mitarbeiter_liste.remove(mitarbeiter)
                return True
        return False

    def suchen(self, name_suche=None, abteilung_suche=None):
        ergebnisse = [] 
        for mitarbeiter in self.mitarbeiter_liste:
            if name_suche and name_suche.lower() in mitarbeiter.name.lower():                
                ergebnisse.append(mitarbeiter)
            elif abteilung_suche and abteilung_suche.lower() in mitarbeiter.abteilung.lower():
                ergebnisse.append(mitarbeiter)
        return ergebnisse
    

class App:
    def __init__(self, fenster):
        self.fenster = fenster
        self.verwaltung = MitarbeiterVerwaltung()
        self.fenster.title("Mitarbeiterverwaltung")

        #Eingabefelder:
        self.label = Label(fenster, text="Name").grid(row=0, column=0)
        self.name_entry = Entry(fenster)
        self.name_entry.grid(row=0, column=1)

        self.label = Label(fenster, text="Position").grid(row=1, column=0)
        self.position_entry = Entry(fenster)
        self.position_entry.grid(row=1, column=1)

        self.label = Label(fenster, text="Abteilung").grid(row=2, column=0)
        self.abteilung_entry = Entry(fenster)
        self.abteilung_entry.grid(row=2, column=1)

        self.label = Label(fenster, text="Gehalt").grid(row=3, column=0)
        self.gehalt_entry = Entry(fenster)
        self.gehalt_entry.grid(row=3, column=1)

        self.label = Label(fenster, text="Einstellungsdatum").grid(row=4, column=0)
        self.einstellungsdatum_entry = Entry(fenster)
        self.einstellungsdatum_entry.grid(row=4, column=1)

        
        #Ausgabe:
        self.ausgabe = Text(fenster, height=10, width=50)
        self.ausgabe.grid(row=7, column=0, columnspan=2, pady=10)

        #Buttons:
        self.hinzufuegen_button = Button(fenster, text="Hinzufügen", command=self.hinzufuegen).grid(row=5, column=0, padx=5)
        self.aktualisieren_button = Button(fenster, text="Aktualisieren", command=self.aktualisieren).grid(row=5, column=1)
        self.loeschen_button = Button(fenster, text="Löschen", command=self.loeschen).grid(row=6, column=0, pady=5)
        self.suchen_button = Button(fenster, text="Suchen", command=self.suchen).grid(row=6, column=1)


         
    def get_eingabedaten(self):
        return (
            self.name_entry.get(),
            self.position_entry.get(),
            self.abteilung_entry.get(),
            self.gehalt_entry.get(),
            self.einstellungsdatum_entry.get()
        )

    def hinzufuegen(self):
        name, position, abteilung, gehalt, datum = self.get_eingabedaten()
        try:
            gehalt = float(gehalt)
            mitarbeiter = Mitarbeiter(name, position, abteilung, gehalt, datum)
            self.verwaltung.daten_hinzufuegen(mitarbeiter)
            self.zeige_ausgabe(f"Hinzugefügt:\n{mitarbeiter.zeige_daten()}")
        except ValueError:
            messagebox.showerror("Fehler", "Gehalt muss eine Zahl sein.")

    def aktualisieren(self):
        name, position, abteilung, gehalt, datum = self.get_eingabedaten()
        try:
            gehalt = float(gehalt)
            erfolg = self.verwaltung.daten_aktualisieren(name, position, abteilung, gehalt, datum)
            if erfolg:
                self.zeige_ausgabe(f"Aktualisiert: {name}")
            else:
                self.zeige_ausgabe(f"{name} nicht gefunden.")
        except ValueError:
            messagebox.showerror("Fehler", "Gehalt muss eine Zahl sein.")

    def loeschen(self):
        name = self.name_entry.get()
        erfolg = self.verwaltung.loeschen(name)
        if erfolg:
            self.zeige_ausgabe(f"{name} wurde gelöscht.")
        else:
            self.zeige_ausgabe(f"{name} nicht gefunden.")

    def suchen(self):
        name = self.name_entry.get()
        abteilung = self.abteilung_entry.get()
        ergebnisse = self.verwaltung.suchen(name_suche=name if name else None,
                                            abteilung_suche=abteilung if abteilung else None)
        if ergebnisse:
            ausgabe_text = "\n\n".join([m.zeige_daten() for m in ergebnisse])
        else:
            ausgabe_text = "Keine Ergebnisse gefunden."
        self.zeige_ausgabe(ausgabe_text)

    def zeige_ausgabe(self, text):
        self.ausgabe.delete(1.0, END)
        self.ausgabe.insert(END, text)

if __name__ == "__main__":
    fenster = Tk()
    gui = App(fenster)
    fenster.mainloop()

# verwaltung = MitarbeiterVerwaltung()

# # Mitarbeiter hinzufügen
# m1 = Mitarbeiter("Anna Müller", "Entwicklerin", "IT", 60000, "2022-03-01")
# m2 = Mitarbeiter("Bernd Schmitt", "Projektleiter", "IT", 75000, "2021-07-15")
# verwaltung.daten_hinzufuegen(m1)
# verwaltung.daten_hinzufuegen(m2)

# print("Alle Mitarbeiter:")
# for m in verwaltung.mitarbeiter_liste:
#     print(m.zeige_daten())

# # Aktualisieren (ohne kwargs!)
# verwaltung.daten_aktualisieren("Anna Müller", "Senior Entwicklerin", "IT", 65000, "2022-03-01")

# print("\nNach Aktualisierung:")
# for m in verwaltung.mitarbeiter_liste:
#     print(m.zeige_daten())

# # Suchen
# print("\nGefundene Mitarbeiter in IT:")
# ergebnisse = verwaltung.suchen(abteilung_suche="IT")
# for m in ergebnisse:
#     print(m.zeige_daten())

# # Löschen
# verwaltung.loeschen("Bernd Schmitt")

# print("\nNach dem Löschen:")
# for m in verwaltung.mitarbeiter_liste:
#     print(m.zeige_daten())
