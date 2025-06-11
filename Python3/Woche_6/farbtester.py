from tkinter import Button, Label, Tk, LEFT

class Taste(Button): #Klasse Taste wird von Basisklasse Button (aus tkinter) abgeleitet
    """Schaltfläche , die eine Hexadezimalziffer anzeigt"""
    ziffern = "0123456789ABCDEF"
    
    def __init__(self, app): #Parameter app ist Objekt der Klasse App, die von Tk abgeleitet ist
        self.i = 0 #i ist der Index des Zeichens auf der Schaltfläche
        self.app = app
        Button.__init__(self, master=app, text=self.ziffern[self.i], command=self.druecken,
                        font=("Arial", 16), width=3)
        
    def druecken(self):
        self.i = (self.i + 1) % 16 #i ist Index der aktuellen Ziffer, Wert wird um 1 erhöht und vom Ergebnis 
        #der Rest einer ganzzählichen Division durch 16 berechnet. Damit wird gewährleistet, dass die i zyklisch
        #die Werte 0 bis 15 durchläuft. Nach 15 kommt wieder 0.
        self.config(text=self.ziffern[self.i]) #auf dem Button wird die Ziffer mit index i geschrieben (nächste Ziffer)
        self.app.farbe_anzeigen()

    def ziffer(self):
        return self.ziffern[self.i] #liefert Hexadezimalzahl, die auf Schaltfläche zu sehen ist
    
class App(Tk):
    """Anwendungsfenster"""

    def __init__(self):
        Tk.__init__(self)
        self.label = Label(master=self, width=20, height=6)
        self.tasten = [Taste(self) for i in range(3)] #Liste mit drei Objekten der Klasse Taste erzeugt

        self.label.pack()
        for t in self.tasten: #die 3 Taste-Objekte werden nebeneinander uner das Lebel gesetzt
            t.pack(side=LEFT, padx=5, pady=5)
        self.farbe_anzeigen() 
        self.mainloop()

    def farbe_anzeigen(self): #sorgt dafür, dass Farbe auf Label angezeigt wird
     
        r, g, b = [t.ziffer() for t in self.tasten] #r g b sind die 3 Hexadezimalziffern auf der Schaltfläche
        code = "#" + r + g + b #auf das Label wir mit Hilfe des Farbcodes aus den drei Ziffern 
        self.label.config(bg=code) #eine neue Farbe als Hintergrundfarbe gesetzt
App()