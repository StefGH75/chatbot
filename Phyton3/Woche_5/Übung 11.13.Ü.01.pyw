#Entwickle ein Python-Programm, das ein Tkinter-Anwendungsfenster erstellt. In diesem Fenster sollen 
# Nutzer*innen aus drei verschiedenen Obstsorten (Äpfel, Bananen, Orangen) über Radiobuttons auswählen können.
#  Nach der Auswahl und einem Klick auf eine Schaltfläche "Bestätigen" soll der ausgewählte Wert in einem Label
#  angezeigt werden. Zusätzlich soll eine Funktion implementiert werden, die es ermöglicht, über eine Dialogbox
#  eine Textdatei zu öffnen, deren Inhalt dann in einem Text-Widget dargestellt wird. Die Anwendung soll auch 
# einen Button zum Schließen des Fensters enthalten. Berücksichtige die Verwendung von Threads, um 
# sicherzustellen, dass die GUI reaktionsfähig bleibt, während die Datei geladen wird. 

from tkinter import *
from threading import Thread
from tkinter import filedialog

def bestaetigen():
    auswahl = obst.get()
    if auswahl == 'A':
        label.config(text='Ausgewählt: Äpfel')
    elif auswahl == 'B':
        label.config(text='Ausgewählt: Bananen')
    elif auswahl == 'O':
       label.config(text='Ausgewählt: Orangen')

def schliessen():
    fenster.destroy()

def Datei_laden():
    def laden():
        pfad = filedialog.askopenfilename() #Dialogbox zur Auswahl einer Datei zum Lesen geöffnet.
        #zurückgegeben wird ein string mit vollständigem Pfad zur ausgewählten Datei
        stream = open(pfad, encoding="UTF-8") #Datei wird zum Lesen unter der Codierung utf-8 geöffnet, stream zurückgegeben
        dateiname.delete(1.0, END) #Textfeld wird komplett gelöscht
        dateiname.insert(1.0, stream.read()) #Text im Stream vollständig gelesen und auf Textfeld dargestellt
        stream.close() 
    thread = Thread(target=laden)
    thread.start()

fenster = Tk()

dateiname = Text(master=fenster, width=40, height=10, wrap=WORD, font=("Arial", 10))

obst = StringVar()
obst.set(None)

rb_apfel = Radiobutton(fenster, text="Äpfel", variable=obst, value="A")
rb_banane = Radiobutton(fenster, text="Bananen", variable=obst, value="B")
rb_orange = Radiobutton(fenster, text="Orangen", variable=obst, value="O")

bestaetigen_button = Button(fenster, text="Bestätigen", command=bestaetigen)
label = Label(fenster, text="Bitte wähle eine Obstsorte.")

button_laden = Button(master=fenster, text="Datei öffnen", command=Datei_laden)

schliessen_button = Button(fenster, text="Schliessen", command=schliessen)

rb_apfel.pack()
rb_banane.pack()
rb_orange.pack()
bestaetigen_button.pack()
label.pack()
button_laden.pack()
dateiname.pack()
schliessen_button.pack()

fenster.mainloop()

# #Skript Lösung:
# import tkinter as tk
# from tkinter import filedialog
# from threading import Thread

# def datei_laden():
#     def laden():
#         pfad = filedialog.askopenfilename()
#         if pfad:
#             with open(pfad, "r", encoding="utf-8") as file:
#                 text = file.read()
#                 text_widget.delete('1.0', tk.END)
#                 text_widget.insert('1.0', text)
#     thread = Thread(target=laden)
#     thread.start()

# def auswahl_anzeigen():
#     ausgewaehlte_obstsorte = obst_var.get()
#     auswahl_label.config(text="Ausgewählt: " + ausgewaehlte_obstsorte)

# fenster = tk.Tk()
# fenster.title("Obstauswahl und Dateiöffner")

# obst_var = tk.StringVar()
# radiobuttons = [("Äpfel", "Äpfel"), ("Bananen", "Bananen"), ("Orangen", "Orangen")]
# for obst, value in radiobuttons:
#     rb = tk.Radiobutton(fenster, text=obst, variable=obst_var, value=value, command=auswahl_anzeigen)
#     rb.pack(anchor=tk.W)

# auswahl_label = tk.Label(fenster, text="Bitte wähle eine Obstsorte.")
# auswahl_label.pack()

# oeffnen_button = tk.Button(fenster, text="Datei öffnen", command=datei_laden)
# oeffnen_button.pack()

# text_widget = tk.Text(fenster, height=10, width=50)
# text_widget.pack()

# schliessen_button = tk.Button(fenster, text="Schließen", command=fenster.destroy)
# schliessen_button.pack()

# fenster.mainloop()