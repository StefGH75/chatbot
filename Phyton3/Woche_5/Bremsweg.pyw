from tkinter import *

D = {('asphalt', 'trocken'):8.0,  #Dictionary ordnet zu
     ('asphalt', 'nass'):6.0, 
     ('Kopf', 'trocken'):6.0, 
     ('Kopf', 'nass'):5.0,}

def rechnen(): #Funktion ist Eventhandler und wird aufgerufen, wenn schaltfläche gedrückt wird
    v = float(eingabe.get()) #string des Eingabefelds wird gelesen und Gleitkommazahl gewonnen
    a = D[(fahrbahn.get(), zustand.get())] #Kontrollvariablen fahrbahn und zustand gelesen. Tupel aus
    #beiden repräsentiert eine Straßenbeschaffenheit, dieser Tupel wird als Schlüssel für den Zugriff
    #auf das Dictionary verwendet. Dieser Wert dann Variable a zugewiesen
    ergebnis = (v**2/(2*a))
    ergebnis = round(ergebnis, 2) 
    ausgabetext = str(ergebnis) + ' m' 
    label_ausgabe.config(text=ausgabetext)

fenster = Tk()
fenster.title("Bremsweg berechnen")

fahrbahn = StringVar()
zustand = StringVar()

rb_asphalt = Radiobutton(fenster, text="Asphalt", value="asphalt", variable=fahrbahn)
rb_kopfstein = Radiobutton(fenster, text="Kopfsteinpflaster", value="Kopf", variable=fahrbahn)
rb_trocken = Radiobutton(fenster, text="trocken", value="trocken", variable=zustand)
rb_nass = Radiobutton(fenster, text="nass", value="nass", variable=zustand)

label_ausgabe = Label(fenster,bg='white', font=('Arial', 25), width=15, text = " ")

label_fahrbahn = Label(fenster, text="Fahrbahn: ")
label_zustand = Label(fenster, text="Zustand: ")
label_eingabe = Label(master=fenster, text="Geschwindigkeit in (km/h): ")

rb_asphalt.select()
rb_trocken.select()

eingabe = Entry(master=fenster)
button_rechnen = Button(fenster, text="Rechnen", command=rechnen)

label_ausgabe.pack(pady=10)

label_fahrbahn.pack(anchor=W) 
rb_asphalt.pack(anchor=W) 
rb_kopfstein.pack(anchor=W) 

label_zustand.pack(anchor=W) 
rb_trocken.pack(anchor=W)
rb_nass.pack(anchor=W)

label_eingabe.pack(side=LEFT)
eingabe.pack(side=LEFT)
button_rechnen.pack(padx=5, pady=5)

fenster.mainloop()


#fahrbahn = StringVar(value="Kopfsteinpflaster") #Variable zur Speicherung der aktuellen Radiobutton Auswahl
#                                                 #Startwert= Guten Tag, dort ist die Auswahl voreingestellt
# fahrbahnen_liste = ["Asphalt", "Kopfsteinpflaster"] #Liste der Zeiten, die zur Verfügung stehen
# #Schleife erstellt für jede Begrüßungszeit Radiobutton:
# for i, fahrbahn_option in enumerate(fahrbahnen_liste):
#     rb = Radiobutton(fenster, text=fahrbahn_option, variable=fahrbahn, value=fahrbahn_option,
#                      anchor="w",width=20)
#     #value=zeit: bestimmt den Text, der bei der Auswahl gespeichert wird
#     rb.grid(row=i+1, column=1, padx=10, pady=5, sticky="w", columnspan=5) #über 5 Spalten

# zustand = StringVar(value="nass") #Variable zur Speicherung der aktuellen Radiobutton Auswahl
#                                                 #Startwert= Guten Tag, dort ist die Auswahl voreingestellt
# zustand_liste = ["trocken", "nass"] #Liste der Zeiten, die zur Verfügung stehen
# #Schleife erstellt für jede Begrüßungszeit Radiobutton:
# for i, zustand_option in enumerate(zustand_liste):
#     rb = Radiobutton(fenster, text=zustand_option, variable=zustand, value=zustand_option,
#                      anchor="w",width=20)
#     #value=zeit: bestimmt den Text, der bei der Auswahl gespeichert wird
#     rb.grid(row=i+1, column=1, padx=10, pady=5, sticky="w", columnspan=5) #über 5 Spalten