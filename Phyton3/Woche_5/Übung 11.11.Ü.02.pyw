# Entwickle ein Python-Skript, das ein einfaches GUI (Graphical User Interface) mit Tkinter erstellt. 
# Deine Anwendung soll ein kleines Quiz darstellen, in dem der Nutzer zwischen drei Optionen (A, B, C) 
# mittels Radiobuttons wählen kann. Jede Option soll eine andere Farbe repräsentieren (Rot, Grün, Blau).
#  Nach der Auswahl und einem Klick auf eine Schaltfläche "Bestätigen" soll das Hintergrundfarbe des 
# Anwendungsfensters entsprechend der Auswahl geändert werden. Nutze dazu die Kontrollvariable der 
# Radiobuttons, um die Auswahl zu ermitteln und die Hintergrundfarbe anzupassen. Implementiere zudem 
# eine Funktion, die die Farbänderung durchführt. Die GUI soll außerdem eine Schaltfläche "Zurücksetzen"
#  enthalten, die die Hintergrundfarbe auf die Standardfarbe zurücksetzt und die Auswahl der
# Radiobuttons aufhebt.
# a) Definiere die GUI-Elemente und die notwendigen Variablen.
# b) Implementiere die Funktion zur Änderung der Hintergrundfarbe basierend auf der Auswahl.
# c) Füge Eventhandler für die Schaltflächen "Bestätigen" und "Zurücksetzen" hinzu.
# d) Organisiere die Widgets im Fenster mithilfe des Raster-Layouts. 

from tkinter import *

def bestaetigen():
    auswahl = farbe_var.get()
    if auswahl == 'A':
        fenster.config(bg='red')
    elif auswahl == 'B':
        fenster.config(bg='green')
    elif auswahl == 'C':
        fenster.config(bg='blue')
def zurueck():
    farbe_var.set(None)
    fenster.config(bg=standardfarbe)

   
fenster = Tk()
fenster.title("Farben-Quiz")
fenster.geometry("300x250")
standardfarbe = fenster.cget("bg")

farbe_var = StringVar()
farbe_var.set(None)

label = Label(fenster, text="Wähle eine Farbe:", anchor=CENTER)
label.grid(row=0, column=0, columnspan=2, pady=10)

rb_rot = Radiobutton(fenster, text="A - rot", variable=farbe_var, value="A")
rb_gruen = Radiobutton(fenster, text="B - grün", variable=farbe_var, value="B")
rb_blau = Radiobutton(fenster, text="C - blau", variable=farbe_var, value="C")

bestaetigen_button = Button(fenster, text="Bestätigen", command=bestaetigen)
zuruecksetzen_button = Button(fenster, text="Zurücksetzen", command=zurueck)

rb_rot.grid(row=1, column=0, sticky="w", padx=15)
rb_gruen.grid(row=1, column=1, sticky="w", padx=15)
rb_blau.grid(row=1, column=2, sticky="w", padx=15)

bestaetigen_button.grid(row=4, column=0, pady=10, )
zuruecksetzen_button.grid(row=4, column=1, pady=10)

fenster.mainloop()

#Lösung Skript:

# from tkinter import *

# def farbe_aendern():
#     wahl = farbwahl.get()
#     if wahl == 'A':
#         fenster.config(bg='red')
#     elif wahl == 'B':
#         fenster.config(bg='green')
#     elif wahl == 'C':
#         fenster.config(bg='blue')

# def zuruecksetzen():
#     fenster.config(bg='SystemButtonFace')
#     farbwahl.set(None)

# fenster = Tk()
# fenster.title("Farbwahl Quiz")

# farbwahl = StringVar(value=None)

# rb_rot = Radiobutton(fenster, text="Rot", variable=farbwahl, value='A')
# rb_gruen = Radiobutton(fenster, text="Grün", variable=farbwahl, value='B')
# rb_blau = Radiobutton(fenster, text="Blau", variable=farbwahl, value='C')
# btn_bestätigen = Button(fenster, text="Bestätigen", command=farbe_aendern)
# btn_zuruecksetzen = Button(fenster, text="Zurücksetzen", command=zuruecksetzen)

# rb_rot.grid(row=0, column=0)
# rb_gruen.grid(row=1, column=0)
# rb_blau.grid(row=2, column=0)
# btn_bestätigen.grid(row=3, column=0)
# btn_zuruecksetzen.grid(row=3, column=1)

# fenster.mainloop()


