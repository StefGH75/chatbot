from tkinter import *

D =  {"USD": 1.22,"GBP":0.91, "JPY":126.7} #Dictionary für Währungen

def berechnen(): #Funktion wird aufgerufen wenn Schaltfläche (Button Rechnen) angeklickt wird
    euros = float(eingabe.get(),2) #Text im Eingabefeld in Gleitkommazahl umgewandelt, die der variablen euros zugewiesen wird
    ergebnis = euros * D[währung.get()] #Kontrollvariable währung enthält Kürzel der mit dem Radiobutton
    #ausgewählten Währung. im Dictionary wird der Wert von einem Euro in diese Währung ermittelt. Dieser
    #Betrag wird mit eingegebener Zahl euros multipliziert. Ergebnis wird Variabel ergebnis übergeben
    ausgabetext ="{} {}".format(ergebnis, währung.get()) #Ausgabetext besteht aus Ergebnis, Leerzeichen
    #und der gewählten Währung
    ausgabe.config(text=ausgabetext)

fenster = Tk()
fenster.title("Währungsrechner")
fenster.geometry("300x200")

währung = StringVar() #Objekt währung ist Kontrollvariable für strings.
#alle drei Radiobuttons verwenden dieselbe Kontrollvariable währung. Wenn ein Button angeklickt wird,
#wird Währungskürzel in Kontrollvariablen gespeichert (value)
usd = Radiobutton(master=fenster, text="Dollar", value="USD",variable=währung)
gbp = Radiobutton(master=fenster, text="Britischer Pfund",value="GBP", variable=währung)
jpy = Radiobutton(master=fenster, text= "Japanischer Yen", value="JPY",variable=währung)

ausgabe = Label(master=fenster, bg="blue", fg="white", font=("Arial",25), width=15)

label = Label(master=fenster, text="Euros: ")
usd.select() #Radiobutton wird selektiert

eingabe = Entry(master=fenster)
button = Button(master=fenster, text="Rechnen", command=berechnen)

ausgabe.pack()
usd.pack()
gbp.pack()
jpy.pack()
label.pack(side=LEFT)
eingabe.pack()
button.pack(side=RIGHT)

fenster.mainloop()
