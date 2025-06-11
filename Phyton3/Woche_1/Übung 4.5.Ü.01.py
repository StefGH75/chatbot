#Autorin: Stefanie Millow
#Aufgabe: Entwickle ein Python-Programm, das die folgenden Anforderungen erfüllt: 
#a) Das Programm soll zuerst den Benutzer bitten, eine ganze Zahl einzugeben. Verwende dafür die Funktion 
# input() und wandle die Eingabe in eine ganze Zahl um. 
#b) Überprüfe anschließend, ob die eingegebene Zahl kleiner als 10, gleich 10 oder größer als 10 ist. 
# Verwende dafür eine Kombination aus if, elif und else Anweisungen. 
#c) Für jede der drei Bedingungen soll das Programm eine entsprechende Nachricht ausgeben: 
#Wenn die Zahl kleiner als 10 ist, soll ausgegeben werden: "Die Zahl ist kleiner als 10." 
#Wenn die Zahl gleich 10 ist, soll ausgegeben werden: "Die Zahl ist genau 10." 
#Wenn die Zahl größer als 10 ist, soll ausgegeben werden: "Die Zahl ist größer als 10." 
#d) Am Ende soll das Programm eine Liste von Zahlen von 1 bis zur eingegebenen Zahl (inklusive) mithilfe 
# einer for-Schleife ausgeben. Jede Zahl soll in einer neuen Zeile angezeigt werden. Verwende Kommentare im 
# Code, um die einzelnen Schritte zu erläutern. 

zahl = int(input("Bitte eine Zahl eingeben: ")) #Benutzer wird um Eingabe gebeten und Eingabe wird in ganze Zahl umgewandelt

if zahl < 10: #Schleife: wenn die Zahl kleiner 0 ist
    print("Die Zahl ist kleiner als 10") #dann Ausgabe

elif zahl == 10: #Schleife: wenn die Zahl gleich 0 ist
    print("Die Zahl ist genau 10") #dann Ausgabe

else: #wenn ersten beiden Bedingungen nicht zutreffen
    print("Die Zahl ist größer als 10") #dann Ausgabe

print("Hier sind die Zahlen von 1 bis", zahl, ":") #Hinweis zur Ausgabe
for i in range(1, zahl + 1): #Start einer Schleife, die bei jedem Durchlauf Zahl (i) nimmt. 
                            #Die range-Funktion erzeugt Folge von Zahlen beginnend mit 1 bis eins vor zahl + 1
    print(i) # bei jedem Durchlauf wird der aktuelle Wert von i in eine rneuen Zeile ausgegeben

#Lösung zusätzlich, wenn Zahl negativ:
# Schritt 1: Benutzer nach einer ganzen Zahl fragen
num_input = input("Bitte geben Sie eine ganze Zahl ein: ")

# Umwandeln der Eingabe in eine ganze Zahl
num = int(num_input)

# Schritt 2: Überprüfen, ob die Zahl kleiner als, gleich 10 oder größer als 10 ist
if num == 10:
    print("Die Zahl ist genau 10.")
elif num < 10:
    print("Die Zahl ist kleiner als 10.")
else:
    print("Die Zahl ist größer als 10.")

# Schritt 3: Entscheiden, ob wir vorwärts oder rückwärts zählen
# Wenn die Zahl kleiner als 1 ist, zählen wir rückwärts
stride = 1  # Standardmäßig vorwärts zählen
if num < 1:
    stride = -1  # Rückwärts zählen, wenn die Zahl kleiner als 1 ist

# Schritt 4: Liste der Zahlen von 1 bis zur eingegebenen Zahl ausgeben
output_str = ""

# Verwenden der range-Funktion für das Zählen, basierend auf der Richtung (vorwärts oder rückwärts)
if stride == 1:
    for i in range(1, num + 1, stride):
        output_str += str(i)
        if i != num:
            output_str += "\n"
else:
    for i in range(1, num - 1, stride):
        output_str += str(i)
        if i != num - 1:
            output_str += "\n"

# Ausgabe der Zahlen als eine Liste
print(output_str)
