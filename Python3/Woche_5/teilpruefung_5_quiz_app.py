"""
Autorin: Stefanie Millow
Teilprüfung 5
teilpruefung_5_quiz_app.py
Quiz App mit Multiple-Choice-Fragen
"""

import tkinter as tk
from tkinter import messagebox, filedialog
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
AKTUELLE_FRAGE = 0
GEWAEHLTE_ANTWORT = None
NUTZER_ANTWORTEN = []
ZEIT_UEBRIG = 30
TIMER_THREAD = None
TIMER_LAEUFT = False

def frage_laden():
    """Holt aktuelle Frage, setzt alles zurück, zeigt neue Antworten und startet Timer neu"""    
    global ZEIT_UEBRIG #als global definiert um auch auf außerhalb definierte Werte zugegriffen werden kann
    if AKTUELLE_FRAGE < len(FRAGEN): #prüft, ob es noch Fragen gibt (z.B. aktelle_frage=2, len(FRAGEN)== 4)
        frage = FRAGEN[AKTUELLE_FRAGE] #holt AKTUELLE_FRAGE aus Dictionay FRAGEN
        frage_label.config(text=frage["Frage"]) #aktualisiert frage_label, indem der Teil Frage angezeigt wird
        GEWAEHLTE_ANTWORT.set(" ") #keine Vorauswahl einer Antwort im Radiobutton
        index = 0 
        for option in frage["Antwort-Optionen"]: #Loop durch Antwortmöglichkeiten
            auswahl_buttons[index].config(text=option, value=option) #und Text in Radiobutton aktualisiert
                        #text=option aktualisiert sichtbaren Text, value=setzt internen Wert, den der Button an
                        #GEWAEHLTE_ANTWORT gibt, wenn gewählt
            index += 1 #Index sorgt dafür, dass der richtige Radiobutton genutzt wird (0 bis 3)
        ZEIT_UEBRIG = 30 #Timer für neue Frage wieder auf 30 gesetzt
        timer_label.config(text=f"Zeit: {ZEIT_UEBRIG}") #Timer_Label in GUI visuell aktualisiert
        timer_starten() #startet Timer im Hintergrund (parallel via Thread)
    else:
        messagebox.showinfo("Fertig", "Du hast alle Fragen beantwortet!")

def timer_starten():
    """Timer für Zeit rückwärts zählen von 30. Läuft im separaten Thread um GUI nicht zu blockieren."""
    global TIMER_LAEUFT, TIMER_THREAD
    TIMER_LAEUFT = True
    if TIMER_THREAD and TIMER_THREAD.is_alive():
        return
    TIMER_THREAD = threading.Thread(target=timer_ablauf) #neuer Thread erstellt, der im Hintergrund andere
                                                        #die Funktion "timer_ablauf" ausführt
    TIMER_THREAD.daemon = True #sorgt dafür, dass der Thread automatisch beendet wird, wenn Hauptprogramm beendet wird
    TIMER_THREAD.start()

def timer_ablauf():
    """kümmert sich um das Herunterzählen der Zeit von 30 bis 0"""
    global ZEIT_UEBRIG, TIMER_LAEUFT, AKTUELLE_FRAGE
    while ZEIT_UEBRIG > 0 and TIMER_LAEUFT: #solange Zeit nicht abgelaufen und Timer nicht manuell gestoppt
        time.sleep(1) #wartet Thread eine Sekunde
        ZEIT_UEBRIG -= 1 #zieht dann eine Sekunde ab
        timer_label.config(text=f"Zeit: {ZEIT_UEBRIG}") #und aktualisiert Zeit im Text im Label
    if ZEIT_UEBRIG == 0: #wenn Zeit abgelaufen
        TIMER_LAEUFT = False #wird Timer deaktiviert
        messagebox.showinfo("Zeit abgelaufen", "Die Zeit ist um! Weiter zur nächsten Frage.")
        antwort_speichern() #Antwort wird gespeichert
        AKTUELLE_FRAGE += 1 #springt zur nächsten Frage
        frage_laden() #ruft Funktion auf, um neue Frage anzuzeigen & Timer neu zu laden

def antwort_speichern():
    """Speicherung der Antwort des Nutzers, wenn z.B. auf nächste Frage geklickt wird."""
    #global AKTUELLE_FRAGE
    ausgewaehlt = GEWAEHLTE_ANTWORT.get() #vom Nutzer ausgewählte Antwort in Variable "ausgewählt" gespeichert
    frage = FRAGEN[AKTUELLE_FRAGE] #holt sich aktuelle Frage aus Dictionary FRAGEN
    NUTZER_ANTWORTEN.append({ #neues Ergebnisobjekt zur Liste der Antworten hinzugefügt
        "Frage": frage["Frage"],
        "Gewählt": ausgewaehlt, #was Nutzer angeklickt hat
        "Richtig": frage["Antwort"]
    })

def naechste_frage():
    """Funktion für Klick auf Button "Nächste Frage". Prüft Antwort, speichert sie, beendet Timer, lädt nächste Frage"""
    global AKTUELLE_FRAGE, TIMER_LAEUFT
    if not GEWAEHLTE_ANTWORT.get().strip():#prüft, ob Nutzer etwas gewählt hat
        messagebox.showwarning("Keine Auswahl", "Bitte wähle eine Antwort aus.") #wenn nicht Ausgabe in Messagebox
        return
    TIMER_LAEUFT = False #Timer wird gestoppt
    antwort_speichern() #Antwort wird mithilfe der Funktion "antwort_speichern" gespeichert
    AKTUELLE_FRAGE += 1 #aktuelle Frage um 1 erhöht
    frage_laden() #nächste Frage geladen

def ergebnisse_speichern():
    """Funtion zum Speichern der Ergebnisse nach Klick auf "Ergebnisse speichern oder laden" Button"""
    dateipfad = filedialog.asksaveasfilename() #öffnet Datei-Dialog, Nutzer kann Speicherort und Dateiname auswählen
    with open(dateipfad, 'w', encoding="UTF-8") as datei:
        json.dump(NUTZER_ANTWORTEN, datei, indent=4) #Nutzer Antworten in json-Format gespeichert
    messagebox.showinfo("Gespeichert", f"Ergebnisse wurden gespeichert unter: {dateipfad}") #Info-Pop-up

def ergebnisse_laden():
    """Funktion zum Laden aus der gespeicherten Datei bei Klick auf "Ergebnisse speichern oder laden"-Button. """
    dateipfad = filedialog.askopenfilename() #öffnet Dateiauswahl-Dialogfenster
    with open(dateipfad, 'r', encoding="UTF-8") as datei: #öffnet Datei im Lesemodus
        ergebnisse = json.load(datei) #Datei eingelesen
    ergebnis_text = "\n\n".join([ #wandelt Datei in lesbaren Text, join verbindet alle mit zwei Zeilenumbrüchen
        f"Frage: {eintrag['Frage']}\nDeine Antwort: {eintrag['Gewählt']}\nRichtige Antwort: {eintrag['Richtig']}"
        for eintrag in ergebnisse
    ])
    messagebox.showinfo("Geladene Ergebnisse", ergebnis_text)

def ergebnisse_speichern_oder_laden():
    """Funktion um Auswahlmöglichkeit beim Ergebnisse speichern oder laden Button zu ermöglichen"""
    antwort = messagebox.askquestion("Ergebnisse speichern oder laden?",
                                     "Möchtest du die aktuellen Ergebnisse **speichern**?\n"
                                     "Wähle 'Nein' zum **Laden** einer gespeicherten Datei.")
        #öffnet Dialogfenster mit Ja/ Nein Abfrage, Rückgabewert ist ein string "yes", wenn Ja geklickt,
        #"no", wenn Nein geklickt wird
    if antwort == "yes": #wenn "Ja" ausgewählt, wird Speicher-Funktion aufgerufen
        ergebnisse_speichern()
    else: #ansonsten, die laden-Funktion
        ergebnisse_laden()

# GUI-Aufbau
fenster = tk.Tk()
fenster.title("Quiz-Anwendung")
fenster.geometry("500x400") #Fenster-Größe festgesetzt
fenster.resizable(False, False) #Fenster wird nicht angepasst, behält Größe auch bei Zeilenumbruch im frage_label bei

frage_label = tk.Label(fenster, text="", font=("Arial", 14), wraplength=500) #wraplength sorgt für Zeilenumbruch
                                                                            #wenn Text mehr als 500 Pixel
frage_label.pack(pady=20, padx=10)

GEWAEHLTE_ANTWORT = tk.StringVar() #gemeinsame Variable für Radiobuttons, wenn ein Button ausgewählt ändert sich value
GEWAEHLTE_ANTWORT.set(" ") #Keine Vorauswahl in den Radiobuttons
auswahl_buttons = []
for i in range(4): #erzeugt 4 Radiobuttons
    rb = tk.Radiobutton(fenster, text="", padx=20, variable=GEWAEHLTE_ANTWORT, value="", font=("Arial", 12))
    rb.pack(anchor="w")
    auswahl_buttons.append(rb) 

timer_label = tk.Label(fenster, text="Zeit: 30", font=("Arial", 12)) #Zeitlabel mit 30
timer_label.pack(pady=10)

naechste_button = tk.Button(fenster, text="Nächste Frage", command=naechste_frage) 
naechste_button.pack(pady=5)

speichern_button = tk.Button(fenster, text="Ergebnisse speichern oder laden", command=ergebnisse_speichern_oder_laden)
speichern_button.pack(pady=5)

frage_laden() #initialier Aufruf um erste Frage zu stellen

fenster.mainloop()
