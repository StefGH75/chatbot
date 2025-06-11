from tkinter import *
from time import *
from _thread import start_new_thread

fenster = Tk()
 
label_ausgabe = Label(fenster, bg="blue", fg="white", width=16, height=2)

def run():
    while go: #solange globale Variante go den Wert True hat, wird folgende Schleife ausgeführt
        zeit = round(time() - startzeit, 3) #von aktuellen unix-Zeit wird Startzeit abgezogen, Ergebnis
        #ist Anzahl Sekunden seit Klick, Ergebnis auf drei Stellen nach Komma gerundet und zeit zugewiesen
        label_ausgabe.config(text=str(zeit) + "Sekunden", width=16, height=2) #label wird neu konfiguriert
        #enthält Text als string, der aus zwei Teilen zusammengesetzt wird:Sekundenzahl und strink "Sekunden"
        sleep(0.001) #der Thread, in dem die funktion ausgeführt wird, wartet für eine Millisekunde

def start():
    global startzeit, go #Variablen start und go werden als global definiert, nur so können ihre Werte
    #innerhalb der Funktion geändert werden
    startzeit = time() #startzeit wird auf unix-Zeit gesetzt
    go = True
    start_new_thread(run, ()) #run wird im eigenen Thread gestartet

def stopp():
    global go
    go = False #Der Wert der globalen Variablen go wird auf False gesetzt. Das be-wirkt, dass die 
    #Ausführung der Funktion run() beendet wird (while-Schleife wird verlassen)

def reset():
    label_ausgabe.config(text="0.000 Sekunden", width=16, height=2)

button_start = Button(fenster, text="Start", command=start)
button_stopp = Button(fenster, text="Stopp", command=stopp)
button_reset = Button(fenster, text="Reset", command=reset)

label_ausgabe.pack()
button_start.pack(side=LEFT, anchor=W)
button_stopp.pack(side=LEFT, anchor=W)
button_reset.pack(side=LEFT, anchor=W)

fenster.mainloop()