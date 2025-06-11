def ziffern(t:str): #Funktion Ziffern wird definiert mit Argument t
    return sum(1 for zeichen in t if zeichen.isdigit()) #für jedes Zeichen in t, dass eine Ziffer ist,
                                                        # wird eine 1 gezählt und die Summe ausgegeben
print(ziffern("heute ist der 24.03.2035"))  #Beispiel-Aufruf

#Lösung aus Skript:

def ziffern(text:str):
    anzahl = 0
    for buchstabe in text:
        if buchstabe in "0123456789":
            anzahl +=1
    return anzahl
    
print(ziffern("heute ist der 24.03.2035"))