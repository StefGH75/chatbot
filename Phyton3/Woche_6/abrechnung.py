from geld import Geld
from tkinter import Button, Tk, Text, LEFT, END

class App():
    def __init__(self):
        self.fenster = Tk()
        self.text = Text(master=self.fenster, width=30, height=6)
        self.button = Button(master=self.fenster, text="Abrechnen", command=self.abrechnen)
        self.text.pack()
        self.button.pack(side=LEFT, padx=5, pady=5)
        self.fenster.mainloop()

    def abrechnen(self):
        text = self.text.get(1.0, END) #aus Text wird Liste von strings erzeugt 
        zeilen = text.split("\n") #und der Variablen zeilen zugewiesen
        summe = Geld("EUR", 0) #neues Geld-Objekt erzeugt, das 0 EUr repräsentiert mit Namen summe
        for z in zeilen:
            try:
                währung, betrag = z.split() #Zeile z in zwei Teile aufgesplittet
                summe = summe + Geld(währung, betrag) #neues Objekt erzeugt und Betrag summiert
            except:
                pass
        self.text.insert(END, "\n\nSumme: " + str(summe)) #hinter letztes Zeichen im textfeld Summe angefügt

App() #Klasse aufgerufen und anonymes Objekt davon erzeugt
