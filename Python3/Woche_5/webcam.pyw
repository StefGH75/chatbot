from tkinter import Label, Button, Tk
from urllib.request import urlopen
from PIL import Image, ImageTk

URL = "https://cs3.wettercomassets.com/thumbnails/variants/5151d99524566/16x9_player.jpg"

def neues_bild():
    global bild_tk #Variable bild_tk muss als global deklariert werden, da sonst die Mechanik des Tk-Fensters
    #nicht funktioniert
    stream = urlopen(URL) #URL geöffnet und bytestream mit Bild-daten erzeugt
    bild_pil = Image.open(stream) #es wird PIL.Image gewonnen
    bild_tk = ImageTk.PhotoImage(bild_pil) #aus PIL.Image-Objekt ein Objekt gewonnen, das mit tkinter kompatibel
    label.config(image=bild_tk) #Bild auf Label angezeigt

fenster = Tk()

button = Button(fenster, font=("Arial", 20), text="Neues Bild", command=neues_bild)
label = Label(fenster)
button.pack(padx=10, pady=10)
neues_bild() #dafür gesorgt, dass nach Start des Programs direkt Bild der Webcam gezeigt wird
label.pack()

fenster.mainloop()

