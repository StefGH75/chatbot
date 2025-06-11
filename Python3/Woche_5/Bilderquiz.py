import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Quizdaten: [Bild-URL, richtige Antwort, [Antwort1, Antwort2, Antwort3]]
quiz_fragen = [
    [
        # Paris – Eiffelturm
        "https://www.juergen-reichmann.de/images/pics/1400000/1400249.jpg",
        "Paris",
        ["Paris", "London", "Rom"]
    ],
    [
        # Brandenburger Tor – Berlin
        "https://upload.wikimedia.org/wikipedia/commons/f/f7/Museumsinsel_Berlin_Juli_2021_1_%28cropped%29_b.jpg",
        "Berlin",
        ["Wien", "Berlin", "Prag"]
    ],
    [
        # London – Tower Bridge
        "https://upload.wikimedia.org/wikipedia/commons/6/67/London_Skyline_%28125508655%29.jpeg",
        "London",
        ["Madrid", "London", "Lissabon"]
    ]
]

class Bilderquiz:
    def __init__(self, master):
        self.master = master
        master.title("Städte-Bilderquiz")
        self.aktuelle_frage = 0
        self.antwort_buttons = []

        # GUI Elemente
        self.bild_label = tk.Label(master)
        self.bild_label.pack(pady=10)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        self.status_label = tk.Label(master, text="", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.zeige_frage()

    def zeige_frage(self):
        frage = quiz_fragen[self.aktuelle_frage]
        bild_url, richtige_antwort, antworten = frage

        # Bild aus dem Web laden
        headers = {'User-Agent': 'Mozilla/5.0'}  # Optional, aber sinnvoll bei manchen Servern
        response = requests.get(bild_url, headers=headers)
        img_data = response.content
        pil_img = Image.open(BytesIO(img_data))
        pil_img = pil_img.resize((400, 300))
        self.tk_img = ImageTk.PhotoImage(pil_img)  # <--- instanzweit speichern
        self.bild_label.config(image=self.tk_img)  # Bild setzen

        # Antwortbuttons
        for btn in self.antwort_buttons:
            btn.destroy()
        self.antwort_buttons.clear()

        for antwort in antworten:
            btn = tk.Button(self.button_frame, text=antwort, width=20, font=("Arial", 12),
                            command=lambda a=antwort: self.pruefe_antwort(a))
            btn.pack(pady=5)
            self.antwort_buttons.append(btn)

        self.status_label.config(text="", fg="black")

    def pruefe_antwort(self, ausgewaehlt):
        richtige = quiz_fragen[self.aktuelle_frage][1]
        for btn in self.antwort_buttons:
            if btn["text"] == richtige:
                btn.config(bg="lightgreen")
            elif btn["text"] == ausgewaehlt:
                btn.config(bg="salmon")
            else:
                btn.config(bg="SystemButtonFace")
    
        if ausgewaehlt == richtige:
            self.status_label.config(text="Richtig! 🎉", fg="green")
        else:
            self.status_label.config(text=f"Leider falsch. Richtige Antwort: {richtige}", fg="red")
        #"Weiter"-Button anzeigen
        weiter_button = tk.Button(self.master, text="Nächste Frage", command=self.naechste_frage)
        weiter_button.pack(pady=10)
        self.antwort_buttons.append(weiter_button)

    def naechste_frage(self):
        self.aktuelle_frage += 1
        if self.aktuelle_frage < len(quiz_fragen):
            for btn in self.antwort_buttons:
                btn.destroy()           
            self.zeige_frage()
        else:
            for btn in self.antwort_buttons:
                btn.destroy()
                self.status_label.config(text="Quiz beendet! 🎉", fg="blue")
                self.bild_label.config(image="")

# App starten
root = tk.Tk()
app = Bilderquiz(root)
root.mainloop()
