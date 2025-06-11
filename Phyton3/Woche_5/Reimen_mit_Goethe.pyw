from tkinter import *

def suche_reime():
    endung = entry.get() #string im Eingabefeld der Variablen endlung zugewiesen
    reime = {wort for wort in woerter if wort.endswith(endung)} #Mengenabstraktion, Menge enthält alle Wörter aus der Menge Wörter, die auf die 
    #angegebe Endung enden (die Menge reime enthält die Wörter aus Goethes Faust, die sich auf endung reimen)
    ergebnis_text = ",".join(reime) #Wörter aus Menge reime werden zu einem langen String verbudnen, zwischen Wörtern steht jeweils ","
    text.delete(1.0, END) #Inhalt des Textfeldes, vom ersten bis zum letzten Zeichen gelöscht
    text.insert(END, ergebnis_text) #Auflistung der Reimwörter wird in das Textfeld geschrieben

#Hauptprogramm:
f = open("faust.txt", "r", encoding="utf-8")
text = f.read()
f.close()
for p in ".,:-?!()_/[]":
    text = text.replace(p," ")
text = text.split()
woerter = set(text)

#Widgets:
fenster = Tk()
entry = Entry(master=fenster, font=("Arial", 12))
button = Button(master=fenster, font=("Arial", 12), text="Suche Reime!", command=suche_reime)
text = Text(master=fenster, font=("Arial", 12), width=40, height=7, wrap=WORD)

#Layout:
text.pack()
entry.pack(side=LEFT)
button.pack(side=LEFT)
fenster.mainloop()

    