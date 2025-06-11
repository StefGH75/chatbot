from tkinter import *

def farbe_anzeigen():
    ausgewaehlte_farbe = farbwahl.get()
    farbanzeige_label.config(text=f"Ausgewählte Farbe: {ausgewaehlte_farbe}")
    canvas.config(bg=ausgewaehlte_farbe.lower())

fenster = Tk()
fenster.title("Farbwahl")

farbwahl = StringVar()
farbwahl.set("Rot")  # Standardauswahl

# Widgets
label = Label(fenster, text="Wähle deine Lieblingsfarbe:")
label.grid(row=0, column=0, columnspan=2)

rot_rb = Radiobutton(fenster, text="Rot", variable=farbwahl, value="Rot")
rot_rb.grid(row=1, column=0)

gruen_rb = Radiobutton(fenster, text="Grün", variable=farbwahl, value="Grün")
gruen_rb.grid(row=1, column=1)

blau_rb = Radiobutton(fenster, text="Blau", variable=farbwahl, value="Blau")
blau_rb.grid(row=1, column=2)

bestaetigen_button = Button(fenster, text="Bestätigen", command=farbe_anzeigen)
bestaetigen_button.grid(row=2, column=0, columnspan=3)

farbanzeige_label = Label(fenster, text="Ausgewählte Farbe: Rot")
farbanzeige_label.grid(row=3, column=0, columnspan=3)

canvas = Canvas(fenster, width=200, height=100, bg="red")
canvas.grid(row=4, column=0, columnspan=3)

fenster.mainloop()


