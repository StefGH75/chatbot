# a) Ein Eingabefeld (Entry-Widget), in den Benutzerinnen ihren Namen eingeben können.
# b) Eine Schaltfläche (Button), die bei Klick eine Begrüßungsnachricht zusammen mit dem eingegebenen Namen in 
# einem Label-Widget anzeigt.
# c) Ein Radiobutton-Widget, mit dem Benutzerinnen ihre bevorzugte Begrüßungszeit auswählen können: 
#   "Guten Morgen", "Guten Tag", "Guten Abend". Die Auswahl soll die Begrüßungsnachricht beeinflussen.
# d) Ein Text-Widget, das als Log dient, in dem jede durchgeführte Begrüßung mit Zeitstempel gespeichert wird.
# e) Verwende das Raster-Layout (Grid), um die Widgets im Anwendungsfenster anzuordnen.
# f) Implementiere eine Funktion, die die aktuelle Zeit und Datum als String zurückgibt, und verwende diese, um den Zeitstempel im Log zu generieren.
# g) Gestalte das Anwendungsfenster und die Widgets ansprechend, indem du Größen, Farben und Schriftarten anpasst. 

from tkinter import *
from datetime import datetime

def aktuelle_zeit(): #Funktion, die das aktuelle Datum und die Uhrzeit im Format DD-MM-YYYY HH:MM:SS als String zurückgibt.
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def begruessung():
    name = name_entry.get() #holt Namen aus Eingabefeld
    begruessungstext = begruessungszeit.get() #holt ausgewählten Radiobutton-Wert (z.B. Guten Tag)

    aktueller_zeitstempel = aktuelle_zeit() #Zeitstempel über Funktion aktuelle_zeit erzeugt
    nachricht = f"{begruessungstext}, {name}!" #Begrüßungsnachricht aus beiden erstellt
    label_ausgabe.config(text=nachricht) #die Nachricht wird im Label angezeigt

    log_text.config(state=NORMAL) #gleichzeitig wird sie im Textfeld (log_text) protokolliert, state=NORMAL: aktiviert Textfeld für Änderungen
    log_text.insert(END, f"[{aktueller_zeitstempel}] {nachricht}\n") #fügt Nachricht ein
    log_text.see(END) #scrollt automatisch nach unten zum neuesten Eintrag
    log_text.config(state=DISABLED) #sperrt das Textfeld wieder, damit der Nutzer nichts daran ändern kann

#Fenster:   
fenster = Tk()
fenster.title("Begrüßungsprogramm")
fenster.geometry("600x400")
fenster.configure(bg="#f0f8ff") #helles blau

#Fonts & Farben:
standard_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")
label_font = ("Arial", 14)
bg_farbe = "#e6f2ff"

#Name & Label:
label = Label(master=fenster, text="Dein Name: ", font=standard_font).grid(row=0, column=0, padx=10, 
                                                                           pady=10, sticky="e")
#erstellt Label mit Text "Dein Name: " linksbündig ausgereichtet (sticky=e)
name_entry = Entry(master=fenster, font=standard_font, width=30) #Textfeld für Namenseingabe direkt rechts neben Label
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w") #sticky=w > links ausgerichtet

# Begrüßungszeit (Radiobuttons)
Label(fenster, text="Begrüßungszeit:", font=standard_font, bg=bg_farbe).grid(row=1, column=0, padx=10, pady=10, sticky="e")

begruessungszeit = StringVar(value="Guten Tag") #Variable zur Speicherung der aktuellen Radiobutton Auswahl
                                                #Startwert= Guten Tag, dort ist die Auswahl voreingestellt
zeiten = ["Guten Morgen", "Guten Tag", "Guten Abend"] #Liste der Zeiten, die zur Verfügung stehen
#Schleife erstellt für jede Begrüßungszeit Radiobutton:
for i, zeit in enumerate(zeiten):
    rb = Radiobutton(fenster, text=zeit, variable=begruessungszeit, value=zeit, font=standard_font, 
                     anchor="w",width=20, bg=bg_farbe)
    #value=zeit: bestimmt den Text, der bei der Auswahl gespeichert wird
    rb.grid(row=i+1, column=1, padx=10, pady=5, sticky="w", columnspan=5) #über 5 Spalten

button = Button(master=fenster, text = "Begrüßen", font=button_font, width=20,command=begruessung)
#beim Klicken wird die begruessungs-Funktion aufgerufen
button.grid(row=6, column=0, columnspan=5, pady=5)

# Begrüßungs-Ausgabe
label_ausgabe = Label(fenster, text="", font=label_font, fg="#006699", bg=bg_farbe) #leeres Label, 
    #das später Begrüßung zeigt, Schriftfarbe=dunkelblau
label_ausgabe.grid(row=7, column=0, columnspan=2, pady=5)

#Log-Textfeld
Label(fenster, text="Begrüßungs-Log:", font=standard_font, bg=bg_farbe).grid(row=7, column=0, 
                                                                columnspan=2, sticky="w", padx=10)

log_text = Text(fenster, height=8, width=70, font=("Courier", 10), state=DISABLED, bg="white")
#state=DISABLED verhindert Bearbeitung durch Nutzer
log_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

fenster.mainloop() #Hält das Fenster offen und wartet auf Benutzerinteraktionen (z. B. Button-Klicks oder Texteingabe)

#Lösung Skript:
# from tkinter import Tk, Label, Button, Entry, Radiobutton, Text, StringVar, END
# from datetime import datetime

# def aktuelle_zeit_als_string():
#     return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def begruessung():
#     name = name_entry.get()
#     zeit = zeit_var.get()
#     begruessungstext = f"{zeit}, {name}!"
#     begruessungslabel.config(text=begruessungstext)
#     log.insert(END, f"{aktuelle_zeit_als_string()}: {begruessungstext}\n")

# app = Tk()
# app.title("Begrüßungs-App")

# name_entry = Entry(app)
# name_entry.grid(row=0, column=1, padx=10, pady=10)

# begruessungslabel = Label(app, text="", font=('Arial', 16))
# begruessungslabel.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# begrussungsbutton = Button(app, text="Begrüßen", command=begruessung)
# begrussungsbutton.grid(row=0, column=2, padx=10, pady=10)

# zeit_var = StringVar()
# zeit_var.set("Guten Tag")

# Radiobutton(app, text="Guten Morgen", variable=zeit_var, value="Guten Morgen").grid(row=2, column=0)
# Radiobutton(app, text="Guten Tag", variable=zeit_var, value="Guten Tag").grid(row=2, column=1)
# Radiobutton(app, text="Guten Abend", variable=zeit_var, value="Guten Abend").grid(row=2, column=2)

# log = Text(app, height=10, width=50)
# log.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# app.mainloop()