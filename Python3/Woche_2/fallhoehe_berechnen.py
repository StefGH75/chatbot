#Um die Tiefe eines Brunnens abzuschätzen, kann man einen Stein hineinwerfen
#und die Sekunden bis zum Aufprall zählen. Je länger es dauert, bis der Stein die
#Wasseroberfläche erreicht, desto tiefer ist der Brunnen. Das folgende interaktive
#Programm fragt nach der Fallzeit und berechnet die Fallhöhe. Für die
#Berechnung wird eine Funktion definiert und aufgerufen. Die Funktion
#verwendet zur Berechnung der Fallhöhe s die folgende physikalische Formel:
#s000000000000 = 1/2g * t**2
#Dabei ist g die Erdbeschleunigung (g = 9,81 m/s²) und t die Fallzeit in Sekunden

def fallhoehe(t):   #Definition einer Funktion fallhoehe und einem Parameter mit Namen t (Fallzeit)
    g = 9.81        
    s = 0.5 * g * t ** 2 #Berechnung der Fallhöhe. In Formel wird t verwendet
    return s #Rückgabe des Ergebnisses von Fallhöhe s

zeit = float(input("Wie lange ist der Stein gefallen in s: "))
hoehe = fallhoehe(zeit) #Funktion fallhoehe wird aufgerufen, der Wert der Variablen zeit wird als 
                        #Argument übergeben. Der Wert, den die Funktion zurückgibt, wird der Variable hoehe zugewiesen
print("Fallhöhe: ", round(hoehe,2), "m2: ") #Text wird ausgegeben,Rundung auf zwei Dezimalstellen


def fallhoehe(t, g=9.81): # Für den zweiten Parameter g wird ein Default-Wert voreingestellt, womit der zweite Parameter optional wird
                        # und beim Aufruf weggelassen werden kann     
    s = 0.5 * g * t ** 2 #Berechnung der Fallhöhe. In Formel wird t verwendet
    return s #Rückgabe des Ergebnisses von Fallhöhe s

while True: #eine Endlosschleife wird definiert. kann mit str + c abgebrochen werden
    zeit = float(input("Wie lange ist der Stein gefallen in s: "))
    beschleunigung = input("g in m/s2: ")
    if beschleunigung: #es wird geprüft, ob str Zeichen enthält (nicht leer ist). dann True
        hoehe = fallhoehe(zeit, float(beschleunigung)) #Wenn Beschleunigung gefüllt, wird daraus Gleitkommazahl gemacht und die Funktion fallhoehe
                        #wird mit zwei Argumenten zeit und beschleunigung aufgerufen
    else: #else-Klausel wird durchgeführt, wenn nichts eingegeben wurde. dann wird Funktion fallhoehe mit nur einem Argument aufgerufen (g vorgegeben)
        hoehe = fallhoehe(zeit)
    print("Fallhöhe: ", round(hoehe,2), "m2: ") #Text wird ausgegeben,Rundung auf zwei Dezimalstellen


