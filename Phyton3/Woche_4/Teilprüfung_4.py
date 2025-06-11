#Teilprüfung 4
#Autorin: Stefanie Millow

import re
import json

#h) Beispiel Textdatei:
beispiel_feedbacks= (
"Der Service am 12.03.2025 war exzellent! Vielen Dank!\n"
"Servicio excelente el 10.04.2025, muy rápido.\n"
"Great service on 10.04.2025!\n"
"Wirklich exzellent betreut worden am 12.03.2025.\n"
"Service parfait le 18.03.2025, merci!\n"
"Exzellent!\n"
"Ich bin mit dem Service vom 10.04.2025 sehr zufrieden.\n")

with open("feedback.txt", "w", encoding="utf-8") as datei: #speichert Beispieltext in der angegeben Datei und schließt automatisch sobald with-Block verlassen
        datei.write(beispiel_feedbacks)

print(f"Die Beispieldatei feedback.txt wurde erstellt.\U0001F4BE") #mit emoji Diskette für Datei gespeichert

try:
    #a) Datei lesen mit with-Anweisung:
    with open("feedback.txt", "r", encoding="utf-8") as datei: #Datei zum Lesen geöffnet, UTF-8 wegen möglicher Sonderzeichen
        text = datei.read() #ganze Datei als string eingelesen
        print(f"Die Datei wurde erfolgreich gelesen.\u2705") #mit emoji checkmark/erledigt

    #b) Datumsangaben im Format DD.MM.YYYY extrahieren & in Variable datumsliste gespeichert
    datumsliste = re.findall(r"\d{2}\.\d{2}\.\d{4}", text) #d{2}=zwei Ziffern, d{4}= 4 Ziffern für Jahr

    #c) Anzahl der Vorkommen jedes Datums
    datum_zaehler = {} #Zähler auf Null setzen
    for datum in datumsliste:
        if datum in datum_zaehler:
            datum_zaehler[datum] += 1 #Wenn das Datum schon existiert, Wert erhöhen
        else:
            datum_zaehler[datum] = 1 #Wenn noch nicht vorhanden, mit 1 starten

    print("\U0001F4C5:", datum_zaehler) #Ausgabe inklusive emoji für Kalender

    # d) Kommentare mit dem Wort "exzellent" finden
    zeilen = text.splitlines() #Zerlegt den Text an Zeilenumbrüchen (\n)
    exzellente_kommentare = [] #Leere Liste zur Sammlung passender Zeilen

    for zeile in zeilen:
        if re.search(r"\bexzellent\b", zeile, re.IGNORECASE): #re.search prüft, ob das Wort "exzellent" in der Zeile vorkommt
                                                              #b steht für Wortgrenze, damit nur alleinstehend "exzellent" gesucht wird
                                                              #ignorecase: sucht nach Klein- und Großbuchstaben
            exzellente_kommentare.append(zeile) #passende Zeile zur Liste hinzufügen
    print("Kommentare, die 'exzellent' enthalten: ", exzellente_kommentare) #Ausgabe der entsprechenden Kommentare zur Prüfung

    #e) zwei JSON-Dateien schreiben:
    with open("datums_vorkommen.json", "w", encoding="utf-8") as datei:
        json.dump(datum_zaehler, datei, ensure_ascii=False, indent=4) #ensure_ascii=False sorgt für korrekte Darstellung von Umlauten
                                                                      #indent=4 macht die JSON-Datei lesbarer (Einrückung)

    with open("exzellente_feedbacks.json", "w", encoding="utf-8") as datei:
        json.dump(exzellente_kommentare, datei, ensure_ascii=False, indent=4)

    print(f"Die JSON-Dateien wurden erfolgreich verarbeitet und gespeichert.\u2705") #Ausgabe inklusive emoji checkmark/erledigt

except FileNotFoundError: #Fehler, falls die Datei nicht existiert (z. B. Tippfehler im Dateinamen)
    print(f"Fehler: Die Datei wurde nicht gefunden.\u274C") #mit emoji Rotes Kreuz/Fehler
except IOError as e: #Fehler bei Dateioperationen, z. B. Schreibprobleme oder fehlende Rechte
    print(f"Ein Input/Output-Fehler ist aufgetreten:\u274C {e}") #mit emoji Rotes Kreuz/Fehler
except Exception as e: #Allgemeine Fehlerbehandlung für alle anderen (unerwarteten) Fehler
    print(f"Ein unerwarteter Fehler ist aufgetreten:\u274C {e}") #mit emoji Rotes Kreuz/Fehler