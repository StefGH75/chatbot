#a) Ein Label-Widget, das "Hallo Welt!" anzeigt. Verwende dabei eine Schriftart deiner Wahl mit einer Größe von 14 Punkten.
# b) Ein Entry-Widget, in das Nutzer Text eingeben können.
# c) Zwei Button-Widgets: Der erste Button soll den Text im Entry-Widget löschen, wenn er geklickt wird. Der zweite Button soll das Anwendungsfenster schließen.
# d) Verwende Schleifen, um eine Liste von Tupeln zu erstellen, die jeweils die Texte für die Buttons und die zugehörigen Funktionen (zum Löschen des Textes und zum Schließen des Fensters) enthalten. Füge die Buttons basierend auf dieser Liste ins Anwendungsfenster ein.
# e) Gestalte das Anwendungsfenster so, dass das Label oben erscheint, das Entry-Widget darunter und die Buttons am unteren Rand des Fensters angeordnet sind.
# f) Verwende die pack()-Methode für das Layoutmanagement aller Widgets.
# g) Schreibe Kommentare zu deinem Code, um die Funktionsweise der verschiedenen Teile zu erklären.
# h) Stelle sicher, dass das Programm fehlerfrei läuft und alle Widgets wie beschrieben funktionieren. 

from tkinter import *

def loeschen():
    entry.delete(0, "end") #löscht den Inhalt des entry-Felds

def schliessen():
    fenster.destroy() #schließt das Fenster

fenster=Tk()
fenster.title("Meine GUI")

label = Label(master=fenster, text="Hallo Welt!", font=("Courier", 14), height=2, width=15)
label.pack(side=TOP, pady=20) #Label oben

entry = Entry(master=fenster, font=("Courier", 20), justify=CENTER)
entry.pack(pady=10)

button_frame = Frame(fenster)
button_frame.pack(side=BOTTOM, pady=30) #Buttons unten

buttons = [
    ("Text löschen", loeschen),
    ("Beenden", schliessen)
]

for text, funktion in buttons:
    button = Button(master=fenster, text=text, command=funktion)
    button.pack(pady=5)

#button_loeschen = Button(master=fenster, text="Text löschen", command=loeschen)
#button_loeschen.pack(pady=5)

#button_schliessen = Button(master=fenster, text="Beenden", command=schliessen)
#button_schliessen.pack(pady=5)

fenster.mainloop()