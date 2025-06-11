# Erstelle ein einfaches Python-Programm mit Tkinter, das folgende Elemente enthält:
# a) Ein Hauptfenster mit dem Titel "Mein GUI-Programm".
# b) Im Hauptfenster soll ein Label mit dem Text "Hallo Welt!" angezeigt werden.
# c) Unter dem Label soll eine Schaltfläche (Button) platziert werden, die beim Klicken den Text des Labels 
# in "Button wurde geklickt!" ändert.
# d) Füge einen Radiobutton hinzu, der es ermöglicht, zwischen zwei Farben für den Hintergrund des Labels zu 
# wechseln: Rot und Blau. Die Auswahl des Radiobuttons soll sofort den Hintergrund des Labels entsprechend der 
# Auswahl ändern.
# e) Verwende ein Canvas-Widget, um eine einfache Linie und einen Kreis zu zeichnen.

from tkinter import *

def label_aendern():
    label.config(text="Button wurde geklickt!")

def hintergrundfarbe_aendern(farbe):
    label.config(bg=farbe)

fenster = Tk()
fenster.title("Ein GUI-Programm")

farbe = StringVar()
farbe.set(None)

label = Label(fenster, text="Hallo Welt!")
button = Button(fenster, text="Klicken", command=label_aendern)
rb_rot = Radiobutton(fenster, text="rot", variable=farbe, value="red", command=lambda:hintergrundfarbe_aendern("red"))
rb_blau = Radiobutton(fenster, text="blau", variable=farbe, value="blue",command=lambda:hintergrundfarbe_aendern("blue"))
 
canvas = Canvas(fenster, width=200, height=200, bg="white")
nr = canvas.create_oval(50, 50, 150, 150, fill="blue", outline="")

canvas.create_line(10,10,200,50,width=6)

label.pack()
button.pack()
rb_rot.pack()
rb_blau.pack()
canvas.pack()

fenster.mainloop()

#Lösung Skript
# from tkinter import *

# def aendere_label_text():
#     label.config(text="Button wurde geklickt!")

# def aendere_label_farbe(farbe):
#     label.config(bg=farbe)

# def zeichne_canvas():
#     canvas.create_line(10, 10, 200, 50)
#     canvas.create_oval(50, 50, 150, 100, fill="yellow")

# fenster = Tk()
# fenster.title("Mein GUI-Programm")

# label = Label(fenster, text="Hallo Welt!")
# label.pack()

# button = Button(fenster, text="Klick mich", command=aendere_label_text)
# button.pack()

# radiobutton_var = StringVar()
# radiobutton_var.set("rot")  # Setzt die Standardfarbe auf Rot

# radiobutton_rot = Radiobutton(fenster, text="Rot", variable=radiobutton_var, value="red", command=lambda: aendere_label_farbe("red"))
# radiobutton_rot.pack()

# radiobutton_blau = Radiobutton(fenster, text="Blau", variable=radiobutton_var, value="blue", command=lambda: aendere_label_farbe("blue"))
# radiobutton_blau.pack()

# canvas = Canvas(fenster, width=200, height=150)
# canvas.pack()
# zeichne_canvas()

# fenster.mainloop()

#chatgpt:
# import tkinter as tk

# def button_geklickt():
#     label.config(text="Button wurde geklickt!")

# def farbe_gewechselt():
#     farbe = farbwahl.get()
#     if farbe == "rot":
#         label.config(bg="red")
#     elif farbe == "blau":
#         label.config(bg="blue")

# # Hauptfenster erstellen
# fenster = tk.Tk()
# fenster.title("Mein GUI-Programm")

# # Label
# label = tk.Label(fenster, text="Hallo Welt!", bg="white", font=("Arial", 14), width=30, height=2)
# label.pack(pady=10)

# # Button
# button = tk.Button(fenster, text="Klick mich!", command=button_geklickt)
# button.pack(pady=5)

# # Radiobuttons für Farbauswahl
# farbwahl = tk.StringVar(value="weiß")  # Standardfarbe

# radio_rot = tk.Radiobutton(fenster, text="Rot", variable=farbwahl, value="rot", command=farbe_gewechselt)
# radio_blau = tk.Radiobutton(fenster, text="Blau", variable=farbwahl, value="blau", command=farbe_gewechselt)

# radio_rot.pack()
# radio_blau.pack()

# # Canvas mit einer Linie und einem Kreis
# canvas = tk.Canvas(fenster, width=200, height=150, bg="white")
# canvas.pack(pady=10)

# # Linie zeichnen
# canvas.create_line(10, 10, 190, 10, fill="black", width=2)

# # Kreis zeichnen
# canvas.create_oval(50, 50, 150, 120, fill="lightblue", outline="black")

# # GUI starten
# fenster.mainloop()
