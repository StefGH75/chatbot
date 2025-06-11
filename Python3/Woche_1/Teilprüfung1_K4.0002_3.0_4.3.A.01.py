#Dateiname: Teilprüfung1_K4.0002_3.0_4.3A.01.py
#Autorin: Stefanie Millow
#Aufabe: Entwickle ein Python-Programm, das als Taschenrechner für einfache mathematische Operationen
#(Addition, Subtraktion, Multiplikation, Division) fungiert. Das Programm soll den Benutzer 
#zuerst fragen, welche Operation durchgeführt werden soll. Anschließend fragt es nach zwei 
#Zahlen, führt die gewählte Operation mit diesen Zahlen durch und gibt das Ergebnis aus. 
#Beachte dabei die korrekte Anwendung von Datentypen, die Implementierung von Kontrollstrukturen
#sowie die korrekte Verwendung von Kommentaren im Code. 

print("Taschenrechner:")

#Benutzer wird um Eingabe gewünschter Operation gebeten:
operation = input("Welche Operation soll durchgeführt werden: "
                 "Addition (A), Subtraktion (S), Multiplikation(M), Division (D)? "
                 "Bitte gib einen der jeweiligen Buchstaben A, S, M oder D an: ")

#Bis Buchstaben A, S, M oder D nicht angegeben wurde, wird nach gültiger Eingabe für Operation gebeten:
while operation not in ["A", "S", "M", "D"]:
        print("Fehler: Ungültige Eingabe.")
        operation = input("Bitte gib eine gültige Operation an (A, S, M, D): ")

#Benutzer wird um Eingabe der ersten Zahl gebeten sowie Schleife zur Prüfung gültiger Eingabe:
while True:
    try:
        zahl1 = float(input("Bitte nenne mir eine Zahl: ")) #str-Eingabe wird in Gleitkommazahl umgewandelt
        break #Falls die Eingabe gültig ist, wird die Schleife beendet
    except ValueError:
        print("Bitte gib eine gültige Zahl an.") #Fehlermeldung bei ungültiger Eingabe

#Benutzer wird um Eingabe der zweiten Zahl gebeten sowie Schleife zur Prüfung gültiger Eingabe:       
while True:
    try:
        zahl2 = float(input("Bitte nenne mir eine zweite Zahl: ")) #str-Eingabe wird in Gleitkommazahl umgewandelt
        break #Falls die Eingabe gültig ist, wird die Schleife beendet
    except ValueError:
        print("Das ist keine gültige Zahl") #Fehlermeldung bei ungültiger Eingabe

#Durchführung der Operationen und Ausgabe des Ergebnisses:
if operation == "A":
    ergebnis = zahl1 + zahl2 #Berechnung der Addition der Zahlen
    print("Das Ergebnis der Addition ist :", ergebnis) #Ausgabe des Ergebnisses

elif operation == "S":
    ergebnis = zahl1 - zahl2 #Berechnung der Subtraktion der Zahlen
    print("Das Ergebnis der Subtraktion ist: ", ergebnis) #Ausgabe des Ergebnisses

elif operation == "M":
    ergebnis = zahl1 * zahl2 
    print("Das Ergebnis Der Multiplikation ist: ", ergebnis) #Ausgabe des Ergebnisses

elif operation == "D":
    if zahl2 == 0: #Prüfung, ob zahl2 gleich 0 ist
        print("Fehler: da Teilung durch Null nicht möglich ist") #Ausgabe der Fehlermeldung
    else:
        ergebnis = zahl1 / zahl2 #Berechnung der Division der Zahlen
        print("Das Ergebnis Der Multiplikation ist: ", ergebnis) #Ausgabe des Ergebnisses
        
    
            
    


