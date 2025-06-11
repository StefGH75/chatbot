import tkinter as tk

def farbe_aendern():
    # auswahl = farbe.get()
    # if auswahl == 'red':
    #     label_farbe.config(bg='red')
    #     canvas.config(bg='red')
    # elif auswahl == 'green':
    #     label_farbe.config(bg='green')
    #     canvas.config(bg='green')
    # elif auswahl == 'blue':
    #     label_farbe.config(bg='blue')
    #     canvas.config(bg='blue')

    ausgewaehlte_farbe = farbe.get()
    label_farbe.config(text=f"Ausgewählte Farbe: {ausgewaehlte_farbe}", bg=ausgewaehlte_farbe)
    canvas.config(bg=ausgewaehlte_farbe.lower())

fenster = tk.Tk()
fenster.title=("Farbwahl")

label = tk.Label(fenster, text="Wähle deine Lieblingsfarbe")

farbe = tk.StringVar()
farbe.set(None)

rb_rot = tk.Radiobutton(fenster, text="Rot", variable=farbe, value="red")
rb_gruen = tk.Radiobutton(fenster, text= "Grün",variable=farbe, value="green")
rb_blau = tk.Radiobutton(fenster, text="Blau", variable=farbe, value="blue")

bestaetigen_button = tk.Button(fenster, text="Bestätigen", command=farbe_aendern)

label_farbe = tk.Label(fenster, text="Farbe")

canvas = tk.Canvas(fenster, width=200, height=200, bg="white")

label.grid(row=0, column=0, columnspan=2)
rb_rot.grid(row=1, column=0)
rb_gruen.grid(row=1, column=1)
rb_blau.grid(row=1, column=2)
bestaetigen_button.grid(row=2, column=0, columnspan=3)
label_farbe.grid(row=3, column=0, columnspan=3)
canvas.grid(row=4, column=0, columnspan=3)

fenster.mainloop()
