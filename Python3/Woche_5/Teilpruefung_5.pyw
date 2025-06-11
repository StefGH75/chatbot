#Autorin: Stefanie Millow
#Teilpruefung_5

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
aktuelle_frage = 0
gewaehlte_antwort = None
nutzer_antworten = []
zeit_übrig = 30
timer_thread = None
timer_läuft = False

def frage_laden():
    """Holt aktuelle Frage, setzt alles zurück, zeigt neue Antworten und startet Timer neu"""    
    global aktuelle_frage, gewaehlte_antwort, zeit_übrig, timer_läuft #als global definiert um auch auf 
                                                            #außerhalb definierte Werte zugegriffen werden kann
    if aktuelle_frage < len(FRAGEN): #prüft, ob es noch Fragen gibt (z.B. aktelle_frage=2, len(FRAGEN)== 4)
        frage = FRAGEN[aktuelle_frage] #holt aktuelle_frage aus Dictionay FRAGEN
        frage_label.config(text=frage["Frage"]) #aktualisiert frage_label, indem der Teil Frage angezeigt wird
        gewaehlte_antwort.set(" ") #keine Vorauswahl einer Antwort im Radiobutton
        index = 0 
        for option in frage["Antwort-Optionen"]: #Loop durch Antwortmöglichkeiten
            auswahl_buttons[index].config(text=option, value=option) #und Text in Radiobutton aktualisiert
                        #text=option aktualisiert sichtbaren Text, value=setzt internen Wert, den der Button an
                        #gewaehlte_antwort gibt, wenn gewählt
            index += 1 #Index sorgt dafür, dass der richtige Radiobutton genutzt wird (0 bis 3)
        zeit_übrig = 30 #Timer für neue Frage wieder auf 30 gesetzt
        timer_label.config(text=f"Zeit: {zeit_übrig}") #Timer_Label in GUI visuell aktualisiert
        timer_starten() #startet Timer im Hintergrund (parallel via Thread)
    else:
        messagebox.showinfo("Fertig", "Du hast alle Fragen beantwortet!")

def timer_starten():
    """Timer für Zeit rückwärts zählen von 30. Läuft im separaten Thread um GUI nicht zu blockieren."""
    global timer_läuft, timer_thread
    timer_läuft = True
    if timer_thread and timer_thread.is_alive():
        return
    timer_thread = threading.Thread(target=timer_ablauf) #neuer Thread erstellt, der im Hintergrund andere
                                                        #die Funktion "timer_ablauf" ausführt
    timer_thread.daemon = True #sorgt dafür, dass der Thread automatisch beendet wird, wenn Hauptprogramm beendet wird
    timer_thread.start()

def timer_ablauf():
    """kümmert sich um das Herunterzählen der Zeit von 30 bis 0"""
    global zeit_übrig, timer_läuft, aktuelle_frage
    while zeit_übrig > 0 and timer_läuft: #solange Zeit nicht abgelaufen und Timer nicht manuell gestoppt
        time.sleep(1) #wartet Thread eine Sekunde 
        zeit_übrig -= 1 #zieht dann eine Sekunde ab
        timer_label.config(text=f"Zeit: {zeit_übrig}") #und aktualisiert Zeit im Text im Label
    if zeit_übrig == 0: #wenn Zeit abgelaufen
        timer_läuft = False #wird Timer deaktiviert
        messagebox.showinfo("Zeit abgelaufen", "Die Zeit ist um! Weiter zur nächsten Frage.")
        antwort_speichern() #Antwort wird gespeichert
        aktuelle_frage += 1 #springt zur nächsten Frage
        frage_laden() #ruft Funktion auf, um neue Frage anzuzeigen & Timer neu zu laden

def antwort_speichern():
    """Speicherung der Antwort des Nutzers, wenn z.B. auf nächste Frage geklickt wird"""
    global aktuelle_frage
    ausgewaehlt = gewaehlte_antwort.get() #vom Nutzer ausgewählte Antwort in Variable "ausgewählt" gespeichert
    frage = FRAGEN[aktuelle_frage] #holt sich aktuelle Frage aus Dictionary FRAGEN
    nutzer_antworten.append({ #neues Ergebnisobjekt zur Liste der Antworten hinzugefügt
        "Frage": frage["Frage"],
        "Gewählt": ausgewaehlt, #was Nutzer angeklickt hat
        "Richtig": frage["Antwort"]
    })

def naechste_frage():
    """Funktion für Klick auf Button "Nächste Frage". Prüft Antwort, speichert sie, beendet Timer, lädt nächste Frage"""
    global aktuelle_frage, timer_läuft
    if not gewaehlte_antwort.get().strip():#prüft, ob Nutzer etwas gewählt hat
        messagebox.showwarning("Keine Auswahl", "Bitte wähle eine Antwort aus.") #wenn nicht Ausgabe in Messagebox
        return
    timer_läuft = False #Timer wird gestoppt
    antwort_speichern() #Antwort wird mithilfe der Funktion "antwort_speichern" gespeichert
    aktuelle_frage += 1 #aktuelle Frage um 1 erhöht
    frage_laden() #nächste Frage geladen

def ergebnisse_speichern():
    """Funtion zum Speichern der Ergebnisse nach Klick auf "Ergebnisse speichern" Button"""
    dateipfad = filedialog.asksaveasfilename() #öffnet Datei-Dialog, Nutzer kann Speicherort und Dateiname auswählen
    with open(dateipfad, 'w') as datei:
        json.dump(nutzer_antworten, datei, indent=4) #Nutzer Antworten in json-Format gespeichert
    messagebox.showinfo("Gespeichert", f"Ergebnisse wurden gespeichert unter: {dateipfad}") #Info-Pop-up

def ergebnisse_laden():
    """Funktion zum Laden aus der gespeicherten Datei bei Klick auf "Ergebnisse laden"-Button. """
    dateipfad = filedialog.askopenfilename() #öffnet Dateiauswahl-Dialogfenster
    with open(dateipfad, 'r') as datei: #öffnet Datei im Lesemodus
        ergebnisse = json.load(datei) #Datei eingelesen
    ergebnis_text = "\n\n".join([ #wandelt Datei in lesbaren Text, join verbindet alle mit zwei Zeilenumbrüchen
        f"Frage: {eintrag['Frage']}\nDeine Antwort: {eintrag['Gewählt']}\nRichtige Antwort: {eintrag['Richtig']}"
        for eintrag in ergebnisse
    ])
    messagebox.showinfo("Geladene Ergebnisse", ergebnis_text)

# GUI-Aufbau
fenster = tk.Tk()
fenster.title("Quiz-Anwendung")
fenster.geometry("500x400") #Fenster-Größe festgesetzt
fenster.resizable(False, False) #Fenster wird nicht angepasst, behält Größe auch bei Zeilenumbruch im frage_label bei

frage_label = tk.Label(fenster, text="", font=("Arial", 14), wraplength=500) #wraplength sorgt für Zeilenumbruch
                                                                            #wenn Text mehr als 500 Pixel
frage_label.pack(pady=20, padx=10)

gewaehlte_antwort = tk.StringVar() #gemeinsame Variable für Radiobuttons, wenn ein Button ausgewählt ändert sich value
gewaehlte_antwort.set(" ") #Keine Vorauswahl in den Radiobuttons
auswahl_buttons = []
for i in range(4): #erzeugt 4 Radiobuttons
    rb = tk.Radiobutton(fenster, text="", padx=20, variable=gewaehlte_antwort, value="", font=("Arial", 12))
    rb.pack(anchor="w")
    auswahl_buttons.append(rb) 

timer_label = tk.Label(fenster, text="Zeit: 30", font=("Arial", 12)) #Zeitlabel mit 30
timer_label.pack(pady=10)

naechste_button = tk.Button(fenster, text="Nächste Frage", command=naechste_frage) 
naechste_button.pack(pady=5)

speichern_button = tk.Button(fenster, text="Ergebnisse speichern", command=ergebnisse_speichern)
speichern_button.pack(pady=5)

laden_button = tk.Button(fenster, text="Ergebnisse laden", command=ergebnisse_laden)
laden_button.pack(pady=5)

frage_laden() #initialier Aufruf um erste Frage zu stellen

fenster.mainloop()