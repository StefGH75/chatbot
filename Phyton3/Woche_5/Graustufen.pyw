from tkinter import *

DATEINAME="portrait_150x200_exact.png"
S1, S2 = 255, 510 #Definition der Schwellwerte

def bearbeiten():#Die Funktion verändert da Foto Pixel für Pixel
    for x in range (bild.width()): #zwei verschachtelte for-Anweisungen. es wird dafür gesorgt, dass jedes Pixel bearbeitet wird
        for y in range(bild.height()):
            c = bild.get(x, y) #die Variable c enthält ein Tupel aus drei Zahlen zwischen 0 und 255
            helligkeit = sum(c) #die Helligkeit ist die Summe der drei Farbwerte
            if helligkeit < S1: #wenn Helligkeit unter Schwellwert, wird Farbe auf schwarz gesetzt
                bild.put("black", (x, y)) #durch .put() ermöglicht
            elif helligkeit < S2:
                bild.put("grey", (x, y))
            else:
                bild.put("white", (x, y))

fenster = Tk()

bild = PhotoImage(file=DATEINAME)
button = Button(fenster, command=bearbeiten, font=("Arial", 14), text="Bearbeiten")

label = Label(fenster, image=bild)
label.pack()
button.pack(fill=X)

fenster.mainloop()
