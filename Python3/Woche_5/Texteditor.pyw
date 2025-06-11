from tkinter import *
from tkinter import filedialog #Untermodul muss in separater Importanweisung importiert werden

def laden():
    pfad = filedialog.askopenfilename() #Dialogbox zur Auswahl einer Datei zum Lesen geöffnet.
    #zurückgegeben wird ein string mit vollständigem Pfad zur ausgewählten Datei
    stream = open(pfad, encoding="UTF-8") #Datei wird zum Lesen unter der Codierung utf-8 geöffnet, stream zurückgegeben
    text.delete(1.0, END) #Textfeld wird komplett gelöscht
    text.insert(1.0, stream.read()) #Text im Stream vollständig gelesen und auf Textfeld dargestellt
    stream.close() 

def speichern():
    stream = filedialog.asksaveasfile() #Dialogbox zur Bestimmung der Datei zum Schreiben geöffnet
    if stream: #falls Öffnen der Datei gelungen ist (wenn stream nicht None ist)
        stream.write(text.get(1.0, END)) #wird Inhalt des Textfelds in Datei gespeichert
        stream.close()

fenster = Tk()
text = Text(master=fenster, width=40, height=10, wrap=WORD, font=("Arial", 10))

button_laden = Button(master=fenster, text="Laden", command=laden)
button_speichern = Button(master=fenster, text="Speichern", command=speichern)

text.pack()
button_laden.pack(side=LEFT, padx=5, pady=5)
button_speichern.pack(side=LEFT, padx=5, pady=5)
fenster.mainloop()
