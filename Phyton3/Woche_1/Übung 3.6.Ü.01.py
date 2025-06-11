#a) Schreibe ein Python-Skript, das eine Liste von Ganzzahlen definiert und die Summe 
# sowie den Durchschnitt dieser Zahlen berechnet. Kommentiere jeden Schritt deines Skripts, 
# um zu erklären, was gemacht wird.

liste = (1, 3, 5, 7) # Eingabe
summe = liste[0] + liste[1] + liste[2] + liste[3] # Verarbeitung: die Einträge werden summiert
print(summe) # Ausgabe der Summe
durchschnitt = summe / len(liste) # Verarbeitung: der Durchschnitt wird aus der Summe und der Länge der Liste gebildet
print(durchschnitt) # Ausgabe des Durchschnitts

#einfacher:
liste = (1, 3, 5, 7)
summe = sum(liste)
print("Summe:", summe)

#b) Erstelle ein Python-Skript, das eine Zeichenkette (String) von einem Benutzer einliest 
# und anschließend prüft, ob es sich um eine Ganzzahl (int) oder eine Gleitkommazahl (float) handelt. Gib das Ergebnis aus und erkläre den Prozess in Kommentaren.
eingabe = input("Bitte gib eine Zahl an: ")
try: 
    int(eingabe)
    print("Die Eingabe ist eine Ganzzahl")
except ValueError:
    try:
        float(eingabe)
        print("Die Eingabe ist eine Dezimalzahl")
    except ValueError:
        print("Die Eingabe ist weder eine Ganzzahl noch eine Dezimalzahl")

#user_input = input("Gib eine Zahl ein: ")

#if user_input.isdigit():
#    print("Es ist eine ganze Zahl.")
#elif user_input.replace('.', '', 1).isdigit() and user_input.count('.') == 1:
#    print("Es ist eine Fließkommazahl.")
#else:
 #   print("Es ist keine Zahl.")

#c) Definiere ein Python-Skript, das ein einfaches Beispiel für das EVA-Prinzip demonstriert: 
# Es soll vom Benutzer zwei Zahlen einlesen (Eingabe), 
# diese multiplizieren (Verarbeitung) und das Ergebnis ausgeben (Ausgabe). 
# Kommentiere jeden Schritt im Skript.
zahl_1 = float(input("Bitte Zahl 1 eingeben: ")) # eingabe: aufforderung der Eingabe und Umwandlung von string in float, damit Berechnung möglich ist
zahl_2 = float(input("Bitte Zahl 2 eingeben: "))
ergebnis = zahl_1 * zahl_2 # Verarbeitung: Berechnung der Multiplikation
print("Das Ergebnis ist: ", ergebnis) # Ausgabe des Ergebnis

#d) Finde und korrigiere die Fehler im folgenden Python-Skript. Kommentiere, was falsch war
#  und wie du es behoben hast. 

#print("Willkommen zum Fehlerfindungs-Quiz!")
#zahl1 = input("Bitte gib eine Zahl ein: ")
#zahl2 = input("Bitte gib eine andere Zahl ein: ")
#ergebnis = zahl1 + zahl2
#print("Das Ergebnis der Addition ist: ", ergebnis)

print("Willkommen zum Fehlerfindungs-Quiz!")
zahl1 = int(input("Bitte gib eine Zahl ein: "))
zahl2 = int(input("Bitte gib eine andere Zahl ein: "))
ergebnis = zahl1 + zahl2
print("Das Ergebnis der Addition ist: ", ergebnis)
