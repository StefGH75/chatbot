# a) Importiere das Tkinter-Modul korrekt und initialisiere das Hauptfenster der Anwendung. Benenne das Fenster als "Mein GUI".
# b) Füge ein Label-Widget hinzu, das den Text "Willkommen zu deinem GUI!" in der Schriftart "Arial", Größe 16, in blauer Schrift auf gelbem Hintergrund anzeigt. Positioniere das Label zentral im Fenster.
# c) Erstelle eine Schaltfläche (Button), die beschriftet ist mit "Klick mich!". Wenn der Button geklickt wird, soll der Text des Labels zu "Button wurde geklickt!" geändert werden. Achte darauf, dass die Schaltfläche und das Label gut sichtbar und nicht übereinander angeordnet sind.
# d) Implementiere eine Funktion, die aufgerufen wird, wenn der Button geklickt wird und die den Text des Labels ändert. Verwende die Methode config des Label-Widgets, um den Text zu aktualisieren.
# e) Stelle sicher, dass das Fenster eine feste Größe hat und nicht vom Benutzer in der Größe verändert werden kann.
# f) Das Programm soll in einer Endlosschleife laufen, sodass das Fenster offen bleibt, bis der Benutzer es manuell schließt. 

from tkinter import *

def button_geklickt():
    label.config(text="Button wurde geklickt.")

fenster =Tk()
fenster.title("Meine GUI")
fenster.geometry("500x300")
fenster.resizable(False, False) #Verhindert das Ändern der Fenstergröße

label = Label(master=fenster, text="Willkommen zu deinem GUI!", font=("Arial", 16), fg="blue", bg="yellow")
label.pack(side=TOP, pady=20)

button_klicken = Button(master=fenster, text="Klick mich", command=button_geklickt, font=("Arial", 16))
button_klicken.pack(pady=5)

fenster=mainloop()