from tkinter import *
from random import choice, randint
from _thread import start_new_thread
from time import sleep

class Zahl:
    def __init__(self, app): #Initialisierungsmethode übergibt als zweites Argument das App-Objekt, wird benötigt
        #um auf den Schläger und auf das Canvas zuzugreifen. jede Bewegung einer Zahl auf Canvas ist Canvas Operation
        self.app = app
        self.canvas = app.canvas
        self.schlaeger = app.schlaeger
        self.wert = 0
        self.id = self.canvas.create_text(0, 0, text="")
        self.aktiv = False 
    
    def starten(self):
            self.aktiv = True
            start_new_thread(self.run, ())

    def run(self): #run() wird in einem eigenen Thread ausgeführt. Das ist schon deshalb notwendig, weil sich
        #gleichzeitig (parallel) mehrere Zahlen über den Canvas bewegen sollen. Außerdem enthält die Definition 
        #von run() eine Endlosschleife.
        c = self.canvas #kleiner Kniff: Es wird für self.canvas ein neuer Name c als Abkürzung eingeführt. 
        #Das macht den folgenden Programmtext kürzer und besser lesbar. Denn self.canvas wird oft verwendet.
        while self.app.spiel_laueft:
        #while True: #um Programm möglichst kurz und einfach zu halten, wird hier eine Endlosschleife verwendet. 
            #Das funktioniert, weil die Methode run() in einem eigenen Thread ausgeführt wird
            x, y = randint(10, 290), -10 #fallende Zahl eine Startposition auf dem Canvas festgelegt.
            #x-Koordinate (waagerecht) ist eine Zufallszahl, die y-Koordinate ist immer -10. Damit ist die 
            # Zahl zu Beginn oberhalb des sichtbaren Bereichs des Canvas. Sie ist also zu Beginn unsichtbar.
            self.wert = randint(-10, 10) #Zahlenwert des Zahl-Objekts (die Zahl, die man sieht) ist eine ganze
            #Zufallszahl zwischen -10 und +10.
            c.itemconfigure(self.id, text=str(self.wert)) 
            c.coords(self.id, x, y) #Zahl wird auf dem Canvas an die festgelegte Position gebracht
            x1, y1, x2, y2 = c.coords(self.schlaeger.id) #Koordinaten des Schlägers auf dem Canvas ermittelt.
            hit = self.id in c.find_overlapping(x1, y1, x2, y2) #Variable hit erhält  Wahrheitswert True
            #wenn die Zahl den Schläger berührt, und sonst False.
            sleep(randint(0,30)/10)
            while y < 200 and self.app.spiel_laueft: #Solange die Zahl noch nicht unten angekommen ist und nicht den 
                #Schläger berührt, wandert sie nach unten
                sleep(0.05)
                x, y = c.coords(self.id)
                c.move(self.id, 0, 5)
                x1, y1, x2, y2 = c.coords(self.schlaeger.id)
                hit = self.id in c.find_overlapping(x1, y1, x2, y2)
                if hit:
                    self.app.punkte += self.wert
                    self.app.punkte_label.config(text=f"Punkte: {self.app.punkte}")
                    break
        c.itemconfigure(self.id, text="")

class Schlaeger:
    def __init__(self, canvas):
        self.canvas = canvas #Schläger-Objekt braucht den Zugriff auf den Canvas; denn der Schläger ist ein 
        #kleines Rechteck, das vom Canvas-Objekt gezeichnet wird
        self.id = canvas.create_rectangle(10, 185, 40, 190)

    def links(self):
        self.canvas.move(self.id, -20, 0) #Schläger wird auf dem Canvas um 20 Pixel nach links bewegt. 
        #(Die x-Koordinate ändert sich um -20. Die y-Koordinate ändert sich nicht.)

    def rechts(self):
        self.canvas.move(self.id, 20, 0)

class App():
    def __init__(self):
        self.punkte = 0
        self.spiel_laueft = False
        self.fenster = Tk()
        self.fenster.title("Zahlensammler")
        self.punkte_label = Label(self.fenster, text="Punkte: 0")
        self.timer_label = Label(self.fenster, text="Zeit: 10")
        self.ende_label = Label(self.fenster, text="", fg="red")
        self.canvas = Canvas(self.fenster, width=300, height=200)
        
        self.schlaeger = Schlaeger(self.canvas)
        self.zahlen = [Zahl(self) for _ in range(12)] 
                #for i in range(12): #12 anonyme Zahl-Objekte erzeugt. Sie benötigen keinen Namen, weil nicht auf sie 
            #zugegriffen wird. Sie laufen komplett selbstständig und brauchen von außen nicht gesteuert zu 
            # werden.
           # Zahl(self)
     
        self.b_start = Button(master=self.fenster, text="Start", command=self.starten)
        self.b_links = Button(master=self.fenster, text ="<-", command=self.schlaeger.links)
        self.b_rechts = Button(master=self.fenster, text ="->", command=self.schlaeger.rechts)
        self.punkte_label.pack()
        self.timer_label.pack(padx=10)
        self.ende_label.pack(padx=10)
        self.canvas.pack()
        self.b_start.pack(padx=5, pady=5, side=LEFT)
        self.b_links.pack(padx=5, pady=5, side=LEFT)
        self.b_rechts.pack(padx=5, pady=5, side=LEFT)
        self.fenster.mainloop()

    def starten(self):
        self.punkte = 0
        self.spiel_laueft = True
        self.punkte_label.config(text="Punkte: 0")
        self.ende_label.config(text="")
        self.timer_label.config(text="Zeit: 10")

        # Starte Zahlen
        for z in self.zahlen:
            z.starten()

        # Starte Countdown
        self.fenster.after(100, self.countdown, 10)

    def countdown(self, sekunden):
        if sekunden > 0 and self.spiel_laueft:
            self.timer_label.config(text=f"Zeit: {sekunden}")
            self.fenster.after(1000, self.countdown, sekunden - 1)
        else:
            self.spiel_laueft = False
            self.timer_label.config(text="Zeit: 0")
            self.ende_label.config(text="Spielende")

App()

