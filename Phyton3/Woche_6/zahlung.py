from geld import Geld

class Zahlung(Geld): #Klasse Zahlung wird von der Basisklasse Geld abgeleite
    """Die Klasse modelliert eine Zahlung mit Datum"""
    def __init__(self, währung, betrag, zeitpunkt): #Hier wird die Initialisierungsmethode der Basisklasse 
        #Geld aufgerufen. Die Attribute währung und betrag werden als Argumente weitergereicht.
        Geld.__init__(self, währung, betrag)
        self.zeitpunkt = zeitpunkt #zeitpunkt wird mit einem Wert belegt, z. B. einem String, der von der 
                                    #Funktion asctime() aus dem Modul time geliefert wird.

    def __str__(self):
        return "{} {} Datum: {}".format(self.währung, round(self.betrag, 2), self.zeitpunkt)
    #es wird ein String konstruiert, der ein Zahlung-Objekt darstellt. Er enthält drei variable Teile: 
    # Währung, Betrag und den Zeitpunkt der Zahlung. Dieser String wird zurückgegeben.
    
if __name__ == "__main__": #dient nur zum Testen, if-Klausel nur ausgeführt, wenn Programmdatei direkt aufgerufen
    from time import asctime
    a = Zahlung("EUR", 10, asctime())
    b = Geld("USD", 1)
    print(a)
    print(a+b)
