class Geld:
    """Die Klasse modelliert einen Geldbetrag"""
    wechselkurs = {"USD": 0.8154,
                   "GBP": 1.1129,
                   "EUR": 1.0,
                   "JPY": 0.0079}
    
    def __init__(self, währung, betrag): #Objekt-Attribute erhahlten die Werte, die bei der Instanziierung als
                                            #Argumente übergeben worden sind
        self.währung = währung
        self.betrag = float(betrag)

    def Berechne_Euro(self):
        return self.betrag * self.wechselkurs[self.währung] #Methode gibt den Wert des Geld-Objekts in Euro zurück. Sie wird intern
                                                        #für Berechnungen verwendet.
    
    # def add(self, geld): # nimmt ein Geld-Objekt als Parameter, addiert den Wert dieses Geld-Objekts zum 
    #     #eigenen Wert und gibt ein neues Geld-Objekt mit der Summe zurück.
    #     a = self.Berechne_Euro() #beiden zu addierenden Geld-Beträge in Euro umgewandelt
    #     b = geld.Berechne_Euro()
    #     summe = (a + b)/self.wechselkurs[self.währung] #Geldbeträge in Eur addiert und dann in die Währungd des Objekts umgerechnet
    #     return Geld(self.währung, summe) #Durch Aufruf neues Geld-Objekt erzeugt, repräsentiert Summe
    
    def __add__(self, geld):
        a = self.Berechne_Euro()
        b = geld.Berechne_Euro()
        summe = (a + b)/self.wechselkurs[self.währung]
        return Geld(self.währung, summe)
    
    def __str__(self):
        return "{} {}".format(self.währung, round(self.betrag, 2))
    
if __name__ == "__main__":
    a = Geld("EUR", 10)
    b = Geld("USD", 1)
    print(a + b)

# a = Geld("EUR", 12)
# print(a.währung, a.betrag)

# b = a.add(Geld("USD", 1))
# print(b.währung, b.betrag)

# print(Geld.wechselkurs)

# a = 10
# a.__add__(2)
# print(a)