#Entwickle ein Python-Programm, das die folgenden Anforderungen erfüllt:
#a) Definiere eine Funktion namens temperatur_umrechner, die zwei Parameter akzeptiert: temperatur 
# und einheit. Der Parameter einheit soll optional sein und standardmäßig den Wert 'C' für Celsius haben. 
# Die Funktion soll die Temperatur von Celsius in Fahrenheit umrechnen, wenn einheit den Wert 'C' hat,
# und von Fahrenheit in Celsius, wenn einheit den Wert 'F' hat. Die Umrechnungsformeln lauten:
#  (C = (F - 32) * 5/9) und (F = C * 9/5 + 32).
#b) Verwende eine while-Schleife, um vom Benutzer wiederholt Temperaturen und optional die Einheiten 
# einzulesen, bis der Benutzer entscheidet, das Programm zu beenden. Gib für jede Eingabe die umgerechnete
#  Temperatur aus. Implementiere eine Möglichkeit für den Benutzer, das Programm durch Eingabe eines 
# bestimmten Wortes, zum Beispiel "ende", zu beenden.
#c) Stelle sicher, dass dein Programm Fehleingaben (wie z.B. nicht-numerische Temperaturwerte oder falsche
#  Einheitsangaben) elegant behandelt, indem du entsprechende Fehlermeldungen ausgibst und den Benutzer
#  zur erneuten Eingabe aufforderst. 

def temperatur_umrechner(temp, einheit="C"):
  if einheit == "C":
    return temp * 9/5 + 32
  elif einheit == "F":
    return (temp - 32) * 5/9
  else:
    return None

while True:
    eingabe = input("Temperatur mit Einheit oder ende zum Beenden:")
    
    if eingabe.lower() == "ende":
      break
    
    try:
      teile = eingabe.split()
      temp = float(teile[0])
      if len(teile) == 2:
        einheit = teile[1].upper()
      else:
        einheit = "C"
      umgerechnet = temperatur_umrechner(temp, einheit)
      if umgerechnet is not None:
        if einheit == "C":
          print(f"{temp} Grad Celsius sind {umgerechnet} Fahrenheit")
        else: 
          print(f"{temp} Fahrenheit sind {umgerechnet} Grad Celsius")
      else:
        print("Bitte gib eine gültige Einheit C oder F ein.")
    except ValueError:
      print("Bitte gib eine gültige Temperatur ein.")
    except Exception as e:
      print(f"Ein unerwarteter Fehler ist aufgetreten {e}")

#Lösung
#Funktion zur Umrechnung der Temperatur:
def temperatur_umrechner(temperatur, einheit='C'):
    if einheit == 'C': #wenn Einheit Celsius, rechne in Fahrenheit um
        return temperatur * 9/5 + 32
    elif einheit == 'F': #wenn Einheit in Fahrenheit, rechne in Celsius um
        return (temperatur - 32) * 5/9
    else:
        return None #wenn die Einheit ungültig ist, gib None zurück
    
#Hauptprogrammschleife, läuft so lange, bis Benutzer "ende" eingibt
while True:
    eingabe = input("Gib eine Temperatur mit Einheit ein (z.B. '35 C' oder '95 F'), oder 'ende' zum Beenden: ") #eingabe von benutzter einlesen
    
    if eingabe.lower() == 'ende': #wenn der Benutzer ende eingibt (egal ob groß oder klein), beende die Schleife
        break

    try:
        teile = eingabe.split() #Aufteilen der Eingabe in einzelne Teile (z.B. "35", "C")
        temp = float(teile[0]) #Versuch den ersten Teil in Zahl umzuwandeln
        if len(teile) == 2: #wenn zwei Teile vorhanden, verwende den zweiten als Einheit
            einheit = teile[1].upper() #z.B. c wird zu C
        else:
            einheit = 'C'  # Standardwert, wenn keine Einheit angegeben ist
        
        #Temperatur-Umrechnung durchführen:
        umgerechnet = temperatur_umrechner(temp, einheit)
        if umgerechnet is not None: #wenn das Ergebnis gültig ist, gib das umgerechnete Ergebnis aus
            if einheit == 'C':
                print(f"{temp} °C entspricht {umgerechnet} °F")
            else:
                print(f"{temp} °F entspricht {umgerechnet} °C")
        else:
            print("Bitte gib eine gültige Einheit ('C' oder 'F') ein.")

    except ValueError: #Fehlerbehandlung wenn keine gültige Zahl eingegeben
        print("Bitte gib eine gültige Zahl für die Temperatur ein.")
    except Exception as e: #Fehlerbehandlung für alle anderen unerwarteten Fehler
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")