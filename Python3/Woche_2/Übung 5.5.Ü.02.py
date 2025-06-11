#Entwickle ein Python-Programm, das eine Funktion namens umrechner enthält, welche zwei Parameter akzeptiert:
#  betrag und waehrung, wobei waehrung einen optionalen Parameter darstellt, der standardmäßig auf "USD"
# gesetzt ist. Die Funktion soll den betrag von Euro in die angegebene Währung umrechnen. Verwende für die 
# Umrechnung folgende fiktive Wechselkurse: 1 Euro = 1,1 USD und 1 Euro = 0,9 GBP. Das Programm soll den 
# Benutzer auffordern, einen Betrag und eine Währung einzugeben, und dann das Ergebnis der Umrechnung ausgeben.
#  Implementiere zusätzlich eine Kontrollstruktur, die überprüft, ob die eingegebene Währung unterstützt wird,
#  und eine entsprechende Nachricht ausgibt, falls dies nicht der Fall ist. Verwende Schleifen, um den 
# Benutzer die Möglichkeit zu geben, mehrere Umrechnungen durchzuführen, bis er das Programm explizit beendet.

def umrechner(betrag, waehrung="USD"):
    if waehrung == "USD":
        return betrag * 1.1
    if waehrung == "GBP":
        return betrag * 0.9
    else:
        return None

while True: 
    betrag = float(input("Bitte gib einen Betrag in EUR ein, der umgerechnet werden soll: "))
    waehrung = input("Bitte gib eine Währung ein, in die umgerechnet werden soll (USD/GBP). Für USD drücke enter.").strip().upper()
    if waehrung == "":
       waehrung = "USD"

    if waehrung not in ["USD", "GBP", ""]:
        print("Die angegebene Währung wird nicht unterstützt.")
    else:
        ergebnis = umrechner(betrag, waehrung)
        if ergebnis is not None:
            print(f"Umrechnung: {ergebnis:.2f} {waehrung}")
        else:
            print("Es gab ein Problem mit der Währungsumrechnung.")

    weiter = input("Möchtest du weitere Umrechnung durchführen (ja/nein):").lower()
    if weiter != "ja":
        print("programm beendet.")
        break

        

