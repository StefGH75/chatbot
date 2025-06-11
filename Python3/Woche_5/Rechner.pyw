from tkinter import Tk, Label, Button, Entry, LEFT

def rechnen(): #Eventhandler für Schaltfläche
    ausdruck = eingabe.get() #Variable ausdurck erhält string aus Eingabefeld
    try: #mathematischer Ausdruck wird versuchsweise ausgewertet und das Ergebnis der Variablen ergebnis zugewiesen
        ergebnis = eval(ausdruck)
    except: #wenn Auswertung misslingt (eingegebener Ausdruck fehlerhaft)
        ergebnis = "Ungültiger Ausdruck" #erhält ergebnis Fehlermeldung
    ausgabe.config(text = ergebnis) 

fenster = Tk()
fenster.title("Rechner")

button = Button(master=fenster, text="Rechnen", font=("Arial", 12), command=rechnen) #erzeugt Schaltfläche und verbindet sie mit Funktion rechnen()
ausgabe = Label(master=fenster, font=("Arial", 12)) 
eingabe = Entry(master=fenster, font=("Arial", 12)) #erzeugt ein eingabefeld
ausgabe.pack()
eingabe.pack(side=LEFT, padx=5, pady=5) #Eingabe und Schaltfläche werden links nebeneinander gesetzt
button.pack(side=LEFT, padx=5, pady=5)

fenster.mainloop()