from tkinter import *
from time import sleep
from _thread import start_new_thread

def countdown():
    start_new_thread(zählen, ()) #eine neue Funktion wird als Eventhandler für den Button definiert,
    #enthält als einzige Anweisung den Aufruf start_new_thread, als Argumente übergibst du zunächst Namen
    #der Funktion, die in einem neuen Thread gestartet werden soll und leeres Tupel, da zählen ohne
    #Argumente aufgerufen wird

def zählen():
    for zahl in ["3", "2", "1", "Los!"]:
        label.config(text=zahl)
        sleep(1)
    sleep(2)
    label.config(text="")

fenster = Tk()
label = Label(fenster, font=("Arial", 12), width=6)
button = Button(fenster, command=countdown, text="Start") #als Eventhandler wird nun neue Funktion countdown() festgelegt
label.pack()
button.pack()

fenster.mainloop()