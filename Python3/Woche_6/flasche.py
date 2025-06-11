class Flasche:
    """Modell einer Flasche"""
    def __init__(self):
        self.inhalt = 0
        self.max_inhalt = 1000
        self.geöffnet = False
    
    def öffnen(self):
        self.geöffnet = True

    def schließen(self):
        self.geöffnet = False

    def füllen(self, volumen):
        if self.geöffnet:
            if self.inhalt + volumen <= self.max_inhalt:
                self.inhalt += volumen
    
    def leeren(self):
        if self.geöffnet:
            self.inhalt = 0

a = Flasche()
print(a.max_inhalt)

a.öffnen()
a.füllen(100)
print(a.inhalt)

def __init__(self, fassungsvermögen):
    self.inhalt = 0
    self.max_inhalt = fassungsvermögen
    self.geöffnet = False

kleine_flashce = Flasche(200)