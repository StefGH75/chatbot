#Entwickle ein Python-Programm, das eine Funktion namens berechne_durchschnitt definiert, welche eine 
# Liste von Zahlen als Parameter akzeptiert und den Durchschnittswert dieser Zahlen zurückgibt. Dein 
# Programm sollte folgende Anforderungen erfüllen:
# a) Definiere die Funktion berechne_durchschnitt, die eine Liste von Zahlen entgegennimmt. Die 
# Funktion soll den Durchschnitt dieser Zahlen berechnen und das Ergebnis zurückgeben.
# b) Verwende eine for-Schleife innerhalb der Funktion, um durch die Liste zu iterieren und die 
# Summe der Zahlen zu berechnen.
#c) Außerhalb der Funktion, definiere eine Liste von Zahlen und weise sie einer Variablen zu. 
# Verwende dann diese Liste als Argument, um die Funktion berechne_durchschnitt aufzurufen.
#d) Gib das Ergebnis des Funktionsaufrufs mit einer aussagekräftigen Nachricht mithilfe der 
# print()-Funktion aus.
# e) Stelle sicher, dass dein Programm auch mit einer leeren Liste umgehen kann, ohne einen Fehler 
# zu verursachen. In diesem Fall soll die Funktion None zurückgeben. 

def berechne_durchschnitt(zahlen): #Definition der Funktion, die eine Liste an Zahlen entgegennimmt
    if not zahlen: #überprüft, ob liste leer ist
        return None #bei leerer Liste, Rückgabe von none
    summe = 0 #Initialisierung der Summe
    for zahl in zahlen: #for-Schleife zur Summierung der Zahlen 
        summe += zahl
    durchschnitt = summe / len(zahlen) #Berechnung des Durchschnitts mithilfe der Summe und der Anzahl in der Liste zahlen
    return durchschnitt #gibt ergebnis des Durchschnitts aus

zahlen = [10, 20, 30, 40, 50] #Definition einer Liste von Zahlen außerhalb der Funktion
durchschnitt = berechne_durchschnitt(zahlen) #Funktionsaufruf mit der Liste
if durchschnitt is not None:
    print(f"Der Durchschnitt liegt bei: {durchschnitt}") #Ausgabe des Ergebnisses 
else: 
    print("Die Liste ist leer") #Ausgabe wenn Liste leer ist

leere_liste = []
durchschnitt_leer = berechne_durchschnitt(leere_liste)
if durchschnitt_leer is not None:
    print(f"Der Durchschnitt der leeren Liste liegt bei:{durchschnitt_leer}")
else: 
    print("Die Liste ist leer.")
