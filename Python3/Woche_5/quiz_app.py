import tkinter as tk
from tkinter import filedialog
import threading
import time
import json

# Fragenliste
FRAGEN = [
    {
        "Frage": "Was ist die Hauptstadt von Deutschland?",
        "Antwort-Optionen": ["Berlin", "München", "Hamburg", "Köln"],
        "Antwort": "Berlin"
    },
    {
        "Frage": "Welche Farbe entsteht aus Blau und Gelb?",
        "Antwort-Optionen": ["Grün", "Lila", "Orange", "Braun"],
        "Antwort": "Grün"
    },
    {
        "Frage": "Wie heißt das größte Organ des menschlichen Körpers?",
        "Antwort-Optionen": ["Leber", "Haut", "Lunge", "Darm"],
        "Antwort": "Haut"
    },
    {
        "Frage": "Welche Programmiersprache ist bekannt für ihre Einfachheit und klare Syntax?",
        "Antwort-Optionen": ["Python", "Java", "C++", "Assembly"],
        "Antwort": "Python"
    }
]

# Zustände
aktuelle_frage = 0
gewaehlte_antwort = None
nutzer_antworten = []
zeit_übrig = 30
timer_thread = None
timer_läuft = False

def frage_laden():
    global aktuelle_frage, gewaehlte_antwort, zeit_übrig, timer_läuft
    if aktuelle_frage < len(FRAGEN):
        frage = FRAGEN[aktuelle_frage]
        frage_label.config(text=frage["Frage"])
        gewaehlte_antwort.set(" ")
        index = 0
        for option in frage["Antwort-Optionen"]:
            auswahl_buttons[index].config(text=option, value=option)
            index += 1
        zeit_übrig = 30
        timer_label.config(text=f"Zeit: {zeit_übrig}")
        timer_starten()
    else:
        gui_ausgabe("Du hast alle Fragen beantwortet!")

def timer_starten():
    global timer_läuft, timer_thread
    timer_läuft = True
    if timer_thread and timer_thread.is_alive():
        return
    timer_thread = threading.Thread(target=timer_ablauf)
    timer_thread.daemon = True
    timer_thread.start()

def timer_ablauf():
    global zeit_übrig, timer_läuft, aktuelle_frage
    while zeit_übrig > 0 and timer_läuft:
        time.sleep(1)
        zeit_übrig -= 1
        timer_label.config(text=f"Zeit: {zeit_übrig}")
    if zeit_übrig == 0:
        timer_läuft = False
        gui_ausgabe("Zeit abgelaufen! Weiter zur nächsten Frage.")
        antwort_speichern()
        aktuelle_frage += 1
        frage_laden()

def antwort_speichern():
    global aktuelle_frage
    ausgewaehlt = gewaehlte_antwort.get()
    frage = FRAGEN[aktuelle_frage]
    nutzer_antworten.append({
        "Frage": frage["Frage"],
        "Gewählt": ausgewaehlt,
        "Richtig": frage["Antwort"]
    })

def naechste_frage():
    global aktuelle_frage, timer_läuft
    if not gewaehlte_antwort.get().strip():
        gui_ausgabe("Bitte wähle eine Antwort aus, bevor du fortfährst.")
        return
    timer_läuft = False
    antwort_speichern()
    aktuelle_frage += 1
    frage_laden()

def ergebnisse_speichern():
    dateipfad = filedialog.asksaveasfilename()
    if dateipfad:
        with open(dateipfad, 'w') as datei:
            json.dump(nutzer_antworten, datei, indent=4)
        gui_ausgabe(f"Ergebnisse wurden gespeichert unter:\n{dateipfad}")

def ergebnisse_laden():
    dateipfad = filedialog.askopenfilename()
    if dateipfad:
        with open(dateipfad, 'r') as datei:
            ergebnisse = json.load(datei)
        ergebnis_text = "\n\n".join([
            f"Frage: {e['Frage']}\nDeine Antwort: {e['Gewählt']}\nRichtige Antwort: {e['Richtig']}"
            for e in ergebnisse
        ])
        gui_ausgabe("Geladene Ergebnisse:\n\n" + ergebnis_text)

def gui_ausgabe(text):
    ausgabe_feld.config(state="normal")
    ausgabe_feld.delete("1.0", tk.END)
    ausgabe_feld.insert(tk.END, text)
    ausgabe_feld.config(state="disabled")

# GUI-Aufbau
fenster = tk.Tk()
fenster.title("Quiz-Anwendung")
fenster.geometry("600x600")
fenster.resizable(False, False)

frage_label = tk.Label(fenster, text="", wraplength=560, font=("Arial", 14), justify="left", anchor="w")
frage_label.pack(pady=20, padx=10, fill="x")

gewaehlte_antwort = tk.StringVar()
gewaehlte_antwort.set(" ")
auswahl_buttons = []
for _ in range(4):
    rb = tk.Radiobutton(fenster, text="", variable=gewaehlte_antwort, value="", font=("Arial", 12))
    rb.pack(anchor="w", padx=20)
    auswahl_buttons.append(rb)

timer_label = tk.Label(fenster, text="Zeit: 30", font=("Arial", 12))
timer_label.pack(pady=10)

naechste_button = tk.Button(fenster, text="Nächste Frage", command=naechste_frage)
naechste_button.pack(pady=5)

speichern_button = tk.Button(fenster, text="Ergebnisse speichern", command=ergebnisse_speichern)
speichern_button.pack(pady=5)

laden_button = tk.Button(fenster, text="Ergebnisse laden", command=ergebnisse_laden)
laden_button.pack(pady=5)

ausgabe_feld = tk.Text(fenster, height=10, width=70, font=("Arial", 12), bg="#f7f7f7")
ausgabe_feld.pack(pady=10)
ausgabe_feld.config(state="disabled")

frage_laden()
fenster.mainloop()
