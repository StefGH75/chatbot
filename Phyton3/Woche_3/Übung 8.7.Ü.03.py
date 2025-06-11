# a) Erstelle eine Liste mit den Namen von fünf Freunden.
# b) Speichere diese Liste in einer Datei mit dem Namen "freunde.txt" unter Verwendung des JSON-Formats.
# c) Lies die Liste aus der Datei "freunde.txt" und weise sie einer neuen Variablen zu.
# d) Füge der Liste in der Datei einen weiteren Namen hinzu, ohne die ursprüngliche Liste im Skript zu ändern.
# e) Fang mögliche Laufzeitfehler beim Öffnen, Schreiben und Lesen der Datei ab und gib eine benutzerfreundliche Fehlermeldung aus.
# f) Stelle sicher, dass die Datei in jedem Fall korrekt geschlossen wird, auch wenn Fehler auftreten. 

import json

freunde = ["Elisabeth", "Mailin", "Sandra", "Susanne", "Silke"]

with open("freunde.txt", "w") as datei:
    json.dump(freunde, datei, ensure_ascii=False, indent=4)

try:
    with open("freunde.txt", "r") as datei:
        geladene_liste = json.load(datei)
        print("Geladene Freunde Liste:", geladene_liste)
except Exception as e:
    print("Fehler beim Laden der Datei", e)

neuer_freund = input("Gib einen neuen Freund ein: ")
try:
    with open("freunde.txt", "r+") as datei:
        freunde = json.load(datei)
        freunde.append(neuer_freund)
        datei.seek(0)  # Zurück zum Anfang der Datei gehen
        json.dump(freunde, datei, indent=4)
        datei.truncate()  # Entfernt überschüssige Daten am Ende der Dateis
except Exception as e:
    print("Ein Fehler beim Aktualisieren der Liste ist aufgetreten", e)
    