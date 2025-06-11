#Autor: Stefanie Millow
#Entwickle ein Python-Skript, das folgende Funktionen ausführt: 
#a) Frage den Benutzer nach seiner aktuellen Stimmung (z.B. "glücklich", "traurig", "müde"). 
# Speichere die Eingabe in einer Variablen.
#b) Überprüfe die Eingabe des Benutzers. Wenn der Benutzer "glücklich" eingibt, soll das Programm
# ausgeben: "Es ist toll zu hören, dass du glücklich bist!". Wenn der Benutzer "traurig" eingibt, 
# soll das Programm ausgeben: "Es tut mir leid zu hören, dass du traurig bist. Ich hoffe, es geht 
# dir bald besser!". Bei der Eingabe von "müde" soll das Programm ausgeben: "Vielleicht solltest 
# du dich etwas ausruhen. Ruhe ist wichtig.". Für alle anderen Eingaben soll das Programm ausgeben:
#  "Interessant! Ich weiß nicht viel über diese Stimmung."
#c) Füge einen Kommentar über jede Kontrollstruktur hinzu, um zu erklären, was sie tut.
#d) Verwende eine while-Schleife, um den Benutzer zu fragen, ob er das Programm beenden möchte 
# ("Ja" oder "Nein"). Wenn der Benutzer "Nein" eingibt, wiederhole die Schritte a) bis c). 

while True:

    #Benutzer wird nach seiner Stimmung gefragt:
    stimmung = input("Wie ist deine aktuelle Stimmung? ").lower() #um groß/kleinschreibung zu ignorieren
    
    #Auswertung der Stimmung und jeweilige Ausgabe:
    if stimmung == "glücklich":
        print("Es ist toll zu hören, dass du glücklich bist!")

    elif stimmung == "traurig":
        print("Es tut mir leid zu hören, dass du traurig bist. Ich hoffe, es geht dir bald besser!")

    elif stimmung == "müde":
        print("Vielleicht solltest du dich etwas ausruhen. Ruhe ist wichtig.")

    else:
        print("Interessant! Ich weiß nicht viel über diese Stimmung.") #wenn es keine Übereinstimmung gibt

    #Benutzer wird gefragt, ob er das Programm beenden soll:
    frage = input("Möchtest du das Programm beenden 'Ja' oder 'Nein': ").lower() #Input vom Benutzer erbeten,ob beenden oder nicht

    if frage == "ja":
        print("Programm wird beendet. Tschüss!") 
        break #Schleife wird beendet, wenn der Benutzer Ja eingibt


#Lösung:
fortfahren = 'Nein'

while fortfahren.lower() != 'ja':
    # Schritt a: Eingabe der aktuellen Stimmung
    stimmung = input("Wie ist deine aktuelle Stimmung? (glücklich, traurig, müde): ")

    # Schritt b: Überprüfung der Eingabe und Ausgabe einer entsprechenden Nachricht

    if stimmung == 'glücklich':
        print("Es ist toll zu hören, dass du glücklich bist!")
    elif stimmung == 'traurig':
        print("Es tut mir leid zu hören, dass du traurig bist. Ich hoffe, es geht dir bald besser!")
    elif stimmung == 'müde':
        print("Vielleicht solltest du dich etwas ausruhen. Ruhe ist wichtig.")
    else:
        print("Interessant! Ich weiß nicht viel über diese Stimmung.")

    # Schritt d: Abfrage, ob das Programm beendet werden soll

    fortfahren = input("Möchtest du das Programm beenden? (Ja/Nein): ")