from tkinter import Tk, Label, Button
from random import choice

def zufallsfarbe(): #liefert den RGB-Code einer Farbe, der folgendermaßen konstruiert wird: Auf das Zeichen # folgen drei zufällig gewählte Hexadezimalziffern.
    z = "0123456789abcdef"
    return "#" + choice(z) + choice(z) + choice(z)

def farben_aendern(): #Liste der 25 Label-Widgets wird durchlaufen.
    for feld in felder:
        feld.config(bg=zufallsfarbe()) #Jedes Label erhält eine neue, zufällige Hintergrundfarbe

fenster=Tk()
felder=[] #eine (noch leere) Liste für die Farbfelder (Label-Widgets) angelegt
for i in range(5): #in zwei verschachtelten for-Schleifen werden nacheinander alle 25 Zahlenpaare (0, 0; 0, 1; 0, 2; ... bis 4, 4) erzeugt. 
                    #Diese Zahlenpaare werden als Positionen in einem 5x5-Raster verwendet.
    for j in range(5):
        feld = Label(master=fenster, width=8, height=2) #Label-Widget ohne Inhalt, aber mit vorgegebener Breite (8 Zeichen) und Höhe (2 Zeilen) 
                                    #erzeugt. Es wird noch keine Farbe bestimmt,sodass es die voreingestellte Hintergrundfarbe (hellgrau) behält
        felder.append(feld) #neues Label-Widget an Liste angehangen
        feld.grid(column=i, row=j, padx=1, pady=1) #Label-Widget wird im Raster an der Position (i, j) platziert. Mit den Optionen padx=1 und pady=1
        #wird in waagerechter und senkrechter Richtung ein kleiner Abstand zum Rand der Zelle eingerichtet. Dadurch entstehen hellgraue Linien 
        # zwischen den Feldern.
button = Button(master=fenster, text="Neue Farben",command=farben_aendern) #eine Schaltfläche definiert. Wenn sie angeklickt wird, ruft sie die 
                                                        #Funktion farben_ändern() auf. Die 25 Label-Widgets erhalten dann neue Hintergrundfarben.
button.grid(column=0, row=5, columnspan=5, pady=10)
fenster.mainloop()
    

