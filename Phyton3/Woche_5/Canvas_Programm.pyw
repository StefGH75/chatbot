from tkinter import *
from time import *
import time

fenster = Tk()
canvas = Canvas(fenster, width=200, height=200, bg="white")
nr = canvas.create_oval(50, 50, 150, 150, fill="blue", outline="") #setzt auf den Canvas eine blaue Kreisfläche
#mit unsichtbarer Randlinie. Die linke obere Ecke der Bounding Box hat die Koordinaten 50, 50 und die rechte
# untere Ecke hat die Koordinaten 150, 150 im Koordinatensystem des Canvas. Zurückgegeben wird eine ganze
#Zahl zur Identifikation des grafischen Elements

canvas.create_line(0,50,100,150,200,100, fill="lightgrey", smooth=True, width=6)
#punkte = [0,50,100,50,200,150]
#canvas.create_line(punkte)

canvas.pack()
fenster.update()
#nr = canvas.create_oval(50, 50, 150, 150, fill="blue", outline="")
time.sleep(1)
canvas.delete(nr)

fenster.mainloop()
