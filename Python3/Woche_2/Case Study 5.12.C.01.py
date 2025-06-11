#Entwickle ein Python-Programm, das eine Datenanalyse für ein fiktives Unternehmen durchführt, welches 
# verschiedene Produkte verkauft. Deine Aufgabe besteht darin, eine Reihe von Funktionen zu erstellen,
#  die verschiedene Analysen ermöglichen. Das Programm soll folgende Funktionen beinhalten:
# Liste an Produkten: Laptop, 999,00€, Smartphone, 599,00€, Kopfhörer, 149,00€, Smartwatch, 249,00€, 
# Tablet, 399,00€, E-Book-Reader, 129,00€, Fitness-Tracker, 79,00€, Bluetoothlautsprecher, 89,00€,
# Powerbank, 39,00€, Webcam, 59,00€
#a) Eine Funktion durchschnittspreis, die den Durchschnittspreis aus einer Liste von Produkt-Preisen
#  berechnet. Die Funktion nimmt eine Liste von Preisen als Argument und gibt den Durchschnittspreis zurück.
#b) Eine Funktion produkt_filter, die eine Liste von Produktnamen und einen Buchstaben als Argumente 
# nimmt und alle Produkte zurückgibt, die mit diesem Buchstaben beginnen, unter Verwendung der 
# filter()-Funktion.
#c) Eine rekursive Funktion max_preis, die den höchsten Preis in einer Liste von Preisen findet. 
# Wenn die Liste leer ist, soll die Funktion None zurückgeben.
#d) Eine Funktion preis_mit_steuer, die den Preis eines Produkts inklusive Mehrwertsteuer berechnet. 
# Die Funktion nimmt zwei Argumente: den Preis ohne Steuer und den Steuersatz (als optionalen Parameter
#  mit einem Default-Wert von 19%).
#e) Eine Lambda-Funktion, die zusammen mit der map()-Funktion verwendet wird, um die Preise einer Liste
#  von Produkten um einen bestimmten Prozentsatz zu erhöhen. Die Prozentsatzerhöhung soll als Argument 
# übergeben werden.
#f) Eine Funktion drucke_produktliste, die eine Liste von Produktnamen schön formatiert auf der Konsole
#  ausgibt. Verwende die print()-Funktion, um jedes Produkt in einer neuen Zeile auszugeben. 

def durchschnittspreis(preise):
    if not preise:
        return None
    else:
        return sum(preise) / len(preise)

def produktfilter(produktname, buchstabe):
    return list(filter(lambda produkt: produkt.startswith(buchstabe), produktname))

def max_preis(liste):
    if not liste:
        return None #Rückgabe None wenn Liste leer ist
    if len(liste) == 1:
        return liste[0] #Nur ein Element > das ist das Maximum
    else:
        max_rest = max_preis(liste[1:]) #rekursiver Aufruf mit dem Rest der Liste
        return liste[0] if liste[0] > max_rest else max_rest #Vergleich aktuelles Element mit Rest

def preis_mit_steuer(preis, steuersatz=0.19):
    return preis + (preis * steuersatz)

def preise_erhoehen(preise, prozentsatzerhoehung):
    return list(map(lambda preis: preis + preis * prozentsatzerhoehung, preise))

def drucke_produktliste(produkte):
    for produkt in produkte:
        print(produkt)

preise = [10, 20, 30, 40, 50]
produkte = ["Apfel", "Banane", "Zitrone", "Orange"]
erhoehung = 0.10  # 10%

print("Durchschnittspreis:", durchschnittspreis(preise))
print("Produkte mit 'B':", produktfilter(produkte, 'B'))
print("Maximaler Preis:", max_preis(preise))
print("Preis mit Steuer:", preis_mit_steuer(100))
print("Preise erhöht:", preise_erhoehen(preise, erhoehung))
drucke_produktliste(produkte)