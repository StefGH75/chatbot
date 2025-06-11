from canvasvg import saveall
from tkinter import *
from random import choice
from time import asctime

def neue_farbe():
    z = "0123456789ABCDEF"
    return "#" + choice(z) + choice(z) + choice(z)

def malen():
    global id0, id1, id2
    id0 = bild.create_rectangle(0, 0, 250, 300, fill=neue_farbe(), outline="")
    id1 = bild.create_rectangle(100, 0, 250, 300, fill=neue_farbe(), outline="")
    id2 = bild.create_rectangle(0, 100, 250, 200, fill=neue_farbe(), outline="")

def loeschen():
    bild.delete(id0)
    bild.delete(id1)
    bild.delete(id2)

def speichern():
    zeitstempel=asctime()
    for ch in ":.":
        zeitstempel = zeitstempel.replace(ch, "")
        saveall("bild_" + zeitstempel + ".svg", bild)
    #import os
    #print("Gespeichert in:", os.getcwd())
        
fenster = Tk()

malen_button = Button(fenster, text="Malen", command=malen)
löschen_button = Button(fenster, text="Löschen", command=loeschen)
speichern_button = Button(fenster, text="Speichern", command=speichern)

bild = Canvas(fenster, width=250, height=300)
bild.pack()
malen_button.pack(side=LEFT)
löschen_button.pack(side=LEFT)
speichern_button.pack(side=LEFT)

fenster.mainloop()

