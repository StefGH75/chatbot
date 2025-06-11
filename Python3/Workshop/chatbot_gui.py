"""
Autorin: Stefanie Millow
chatbot_gui.py
Chatbot Graphical User Interface (GUI) für Kommunikation mit dem
Chatbot in Kombination mit dem Chatbot Trainer (chatbot_trainer.py)
Das Training erfolgt mit Hilfe der Datei: ChatbotTraining.csv

"""

import tkinter as tk
from tkinter import scrolledtext
import random
from chatbot_trainer import trainiere_chatbot

#Komponenten aus dem Training laden:
trained_components = trainiere_chatbot()
model = trained_components["model"]
preprocess = trained_components["preprocess"]
text_to_features = trained_components["text_to_features"]
vocab = trained_components["vocab"]
label_encoder = trained_components["label_encoder"]
tag_to_response = trained_components["tag_to_response"]

#GUI aufbauen:

#Hauptfenster erstellen:
fenster = tk.Tk()
fenster.title("Chatbot GUI")
fenster.geometry("500x500")

#Chat-Bereich erstellen:
chat_area = scrolledtext.ScrolledText(fenster, wrap=tk.WORD)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state=tk.DISABLED)

#User-Eingabe erstellen:
user_entry = tk.Entry(fenster)
user_entry.pack(padx=10, pady=5, fill=tk.X)

def antwort_generieren(user_input):
    """Definition zur Generierung der Antwort auf Basis der Nutzereingabe"""
    user_processed = preprocess(user_input)
    #Bag of Words Vektor erstellen:
    user_vector = [1 if word in user_processed else 0 for word in vocab]
    #geht vocab durch: 1 wenn Wort in Eingabe vorkommt, sonst 0

    #falls die Eingabe weniger als 1 Treffer in der dict hat:
    if sum(user_vector) < 1:
        return "I'm sorry, I didn't understand that"

    #Vorhersage mit ML-Modell:

    #vortrainiertes Modell genutzt:
    prediction = model.predict([user_vector])
    #vorhergesagter Klassenindex in sprechenden Tag zurückübersetzt:
    predicted_class = label_encoder.inverse_transform(prediction)
    #Zugriff auf das erste Element in der Liste:
    predicted_tag = predicted_class[0]
    #wenn eingabe weniger als 1 Treffer hat, dann wird Meldung ausgegeben:
    antworten = tag_to_response.get(predicted_tag, ["I'm sorry, I didn't understand that"])
    #zufällige Antwort aus der Liste ausgegeben:
    return random.choice(antworten)

def senden(_event=None):
    """Definition zum Senden der Antwort"""

    #Texteingabe holen und prüfen:
    frage = user_entry.get()
    if frage.strip() == "": #wenn Feld leer ist(nur Leerzeichen)
        return #tue nichts

    antwort = antwort_generieren(frage)

    #Chatverlauf aktualisieren:

    #Aktivierung Textfeld:
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"Du: {frage}\n") #Benutzerfrage einfügen
    chat_area.insert(tk.END, f"Bot: {antwort}\n\n") #Bot-Antwort einfügen
    chat_area.config(state=tk.DISABLED) #sperrt Textfeld (nicht editierbar)
    chat_area.yview(tk.END) #scrollt automatisch zum letzten Eintrag

    user_entry.delete(0, tk.END) #leert Eingabefeld für nächste Eingabe

#Send Button:
send_button = tk.Button(fenster, text="Senden", command=senden)
send_button.pack(padx=10, pady=5)

#Nachricht senden auch über Eingabe-Taste (return) ermöglichen:
fenster.bind("<Return>", senden)

fenster.mainloop()
