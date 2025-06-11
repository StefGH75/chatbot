from tkinter import *
from random import randint

def würfeln():
    global summe #die globale Variable summe wird innerhalb dieser Funktion verändert (Seiteneffekt). Deshalb
                    #muss sie als global deklariert werden.
    text = label.cget("text") #der momentane Text des Labels wird gelesen und in Variable text gespeichert
    zahl = randint(1,6) #Zufallszahl zwischen 1 und 6 erstellt
    summe += zahl #zur Summe der bereits gewürfelten Zahlen wird die neue Zahl hinzuaddiert
    label.config(text=text + " " + str(zahl)) #der Text des labels wird neu konfiguriert. Neue Text ist der
    #bisherige Text plus Leerzeichen und ein String mit der neuen Zufallszahl
    if summe > 21:
        label.config(bg="yellow") #wenn Summe größer 21 wird der Hintergrund gelb

def löschen():
    global summe
    summe = 0 #die globale Variable summe wird auf 0 gesetzt. Da ihr Wert verändert wird, musste sie zuvor
    #innerhalb der Funktionsdefinition als global deklariert werden
    label.config(text="", bg="white") #Label wird in den Anfangszustand zurückgesetzt. Hintergrund wird weiß.
    #alle Zahlen werden entfernt

summe = 0 #die globale Variable summe wird durch diese Zuweisung definiert und erhält ihren Anfangswert. Das
#ist notwendig, weil in der Funktion würfeln auf diese Variable zugegriffen wird. Der Name summe muss dann bekannt sein.

fenster = Tk()

bild_würfeln=PhotoImage(file="Würfel.png") #für die Logos der Schaltflächen werden PhotoImage Objekte erzeugt
bild_löschen=PhotoImage(file="Eimer.png")
label = Label(fenster, width=16, font=("Arial", 30), text="", bg="white")
b_würfeln = Button(fenster, image=bild_würfeln, command=würfeln) #Button Images erhalten keinen Text, sondern Bilder
b_löschen = Button(fenster, image=bild_löschen, command=löschen)

label.pack()
b_würfeln.pack(side=LEFT, padx=30, pady=10)
b_löschen.pack(side=RIGHT, padx=30, pady=10)

fenster.mainloop()