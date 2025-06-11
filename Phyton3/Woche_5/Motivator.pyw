#Motivator:
from tkinter import *
from random import choice
SPRÜCHE = ["Du siehst heute gut aus.", "Du schaffst es!", "Heute ist dein Tag!", "Alles wird gelingen!"]

def auswaehlen(): #Eventhandler für die Schaltfläche. Diese Funktion wird aufgerufen, wenn die Schaltfläche angeklickt wird.
    text = choice(SPRÜCHE) #Aus der Liste wird ein Spruch zufällig ausgewählt und der variablen text zugewiesen
    label.config(text=text) #Das Label wird neu konfiguriert. Das Label zeigt nun den String mit dem ausgewählten Spruch

fenster = Tk() #Ein Anwendungsfenster wird erzeugt und angezeigt. Es bekommt den Namen fenster.
button = Button(master=fenster, text="Neue Motivation", command=auswaehlen) #Eine neue Schaltfläche wird erzeugt. Die Beschriftung lautet Neue Motivation. Als Eventhandler wird die Funktion auswählen() zugeordn
label = Label(master=fenster, width=25, height=2, font=("Arial", 16), text=SPRÜCHE[0])
button.pack(side=LEFT, padx=10)
label.pack() #Label und Button werden untereinander in das Anwendungsfenster gesetzt
fenster.mainloop()