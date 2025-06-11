def fak(n):
    if n == 0:          #Abbruch der Rekursion, denn 0! = 1
        return 1
    else:
        return n * fak(n - 1) #zunächst fak(n - 1) aufgerufen
    
eingabe= input("Natürliche Zahl: ") #der Variablen-Eingabe wird ein string mit einer Zahl übergeben
while eingabe: #solange der String eingabe nicht leer ist, wird der eingerückte Block ausgeführt (bei Enter=leer beendet)
    fakultaet = fak(int(eingabe)) #aus dem String wird eine ganze Zahl gewonnen. Mit dieser Zahl als argument 
                                #wird funktion fak() aufgerufen. Ergebnis wird Variablen fakultaet zugewiesen
    print("Fakultät von ", eingabe, ": ", fakultaet) #Ergebnis ausgegeben
    print()
    eingabe = input("Natürliche Zahl: ")