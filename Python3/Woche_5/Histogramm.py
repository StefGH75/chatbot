# Entwickle eine Anwendung zur Datenvisualisierung. In das Eingabefeld werden einige Zahlen eingegeben. 
# Nach dem Klick auf die Schaltfläche wird ein passendes Histogramm ausgegeben

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def zeige_histogramm():
    eingabe = eingabe_feld.get()
    try:
        # Zahlen aus Eingabe extrahieren
        zahlen = [float(x) for x in eingabe.replace(",", " ").split()]
        if not zahlen:
            raise ValueError
    except ValueError:
        messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben – getrennt durch Leerzeichen oder Kommas.")
        return
    
    # Histogramm erstellen
    plt.figure(figsize=(6, 4))
    plt.hist(zahlen, bins='auto', edgecolor='black')
    plt.title("Histogramm der eingegebenen Zahlen")
    plt.xlabel("Werte")
    plt.ylabel("Häufigkeit")
    plt.grid(True)
    plt.show()

# GUI erstellen
fenster = tk.Tk()
fenster.title("Datenvisualisierung: Histogramm")

anleitung = tk.Label(fenster, text="Zahlen eingeben (getrennt durch Leerzeichen oder Kommas):")
anleitung.pack(padx=10, pady=5)

eingabe_feld = tk.Entry(fenster, width=50)
eingabe_feld.pack(padx=10, pady=5)

button_anzeigen = tk.Button(fenster, text="Histogramm anzeigen", command=zeige_histogramm)
button_anzeigen.pack(pady=10)

fenster.mainloop()
