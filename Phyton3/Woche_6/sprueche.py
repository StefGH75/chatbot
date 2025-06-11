class Spruch:
    """Modelliert einen Spruch"""
    def __init__(self, text, anlass):
        self.text = text
        self.anlass = anlass

class Sammlung:
    """Modelliert eine Sammlung von Sprüchen"""
    def __init__(self):
        self.sprueche= []
    
    def neu(self, text, anlass):
        texte = [spruch.text for spruch in self.sprueche]
        if text not in texte:
            neu = Spruch(text, anlass)
        
    def suche(self, anlass):
        ausgabe = ""
        for spruch in self.sprueche:
            if anlass == spruch.anlass:
                ausgabe += spruch.text + "\n"
        return ausgabe

    def anlaesse(self):
        return {spruch.anlass for spruch in self.sprueche}