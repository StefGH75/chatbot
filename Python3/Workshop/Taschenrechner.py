# import math
# from random import choice, sample

# print(dir(math))

# # import math
# # for name in dir(math):
# #   print(name, end=" ")

# my_list = [1,2,3,4,5,6,7,8,9, 10]
# print(sample(my_list, 5))


"""Ein einfacher grafischer Taschenrechner mit tkinter."""

import tkinter as tk

root = tk.Tk()
root.title("Taschenrechner")

def button_klick(ziffer):
    """Button Klick"""

    eingabe.insert(tk.END, ziffer)

def button_clear():
    """Löschen ermöglichen."""

    eingabe.delete(0,tk.END)

def button_rechnen():
    """Berechnung"""

    try:
        ergebnis = eval(eingabe.get())
        eingabe.delete(0, tk.END)
        eingabe.insert(0,ergebnis)
    except Exception:
        eingabe.delete(0, tk.END)
        eingabe.insert(0,"Fehler")

eingabe = tk.Entry(root, width=30, borderwidth=5)
eingabe.grid(row=0, columnspan=4)

button = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("x",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (",",4,1), ("=",4,2), ("+",4,3),
    ("C",5,0)
]

for (text, row, col) in button:
    action = lambda x=text:button_klick(x) if x not in ["=", "C"] else (button_rechnen() if x =="=" else(button_clear()))
    tk.Button(root, text=text, width=10, height=2, command=action).grid(row=row, column=col)

root.mainloop()
