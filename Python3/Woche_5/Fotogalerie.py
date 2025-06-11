from tkinter import Label, Button, Tk, PhotoImage
from PIL import Image, ImageTk
from random import choice

BILDER = ["atomium.jpg", "london.jpg", "mars.jpg", "prag.jpg"]
BREITE = 400

def neues_bild():
    global bild_tk
    pfad = choice(BILDER)
    bild_pil = Image.open(pfad)
    b, h = bild_pil.size
    hoehe = int(BREITE/b * h)
    bild_pil = bild_pil.resize(size=(BREITE, hoehe))
    bild_tk = ImageTk.PhotoImage(bild_pil)
    label_bild.config(image=bild_tk)

fenster = Tk()
logo_neu = PhotoImage(file="neues_bild.png")
button_neu = Button(master=fenster, font=("Arial", 20), image=logo_neu, command=neues_bild)
label_bild = Label(fenster)
button_neu.pack(padx=10, pady=10)
label_bild.pack()

neues_bild()
fenster.mainloop()