#a) Definiere eine Variable text, die einen mehrzeiligen String speichert, welcher Sonderzeichen und 
# Unicode-Zeichen enthält. Verwende mindestens drei verschiedene Escape-Sequenzen und zwei Unicode-Zeichen 
# (z.B. ein Emoji und ein Zeichen aus einem anderen Schriftsystem).
# b) Zähle, wie oft ein bestimmtes Wort in text vorkommt. Das Wort soll als Eingabe über die Konsole gegeben 
# werden.
# c) Ersetze in text alle Vorkommen eines bestimmten Wortes (ebenfalls über die Konsole eingegeben) durch ein 
# anderes Wort (auch über die Konsole eingegeben) und gib den neuen Text aus.
# d) Speichere den modifizierten Text in einer Datei mit dem Namen modifizierter_text.txt unter Verwendung der
#  with-Anweisung.
# e) Dies eine Datei namens daten.json, die eine Liste von Dictionaries enthält, ein. Verwende das JSON-Modul,
#  um die Datei zu laden. Gib anschließend die Daten in der Konsole aus. 

import json

text = "Hallo!\nWillkommen zur Python-Übung.\n\nHier ein paar besondere Zeichen:\n" \
       "\t• Ein Emoji: \U0001F60A\n" \
       "\t• Ein japanisches Zeichen: \u5B66 (bedeutet 'lernen')\n" \
       "\t• Ein Anführungszeichen: \"Das ist ein Zitat.\"\n" \
       "\nViel Spaß beim Programmieren!\n#PythonRocks"
#t für tab: rückt ein
#print(text)

def wort_zaehlen(text, wort):
    anzahl = text.lower().count(wort.lower()) 
    print(f"Das Wort {wort} kommt {anzahl} mal im Text vor.")
    return anzahl

def ersetze_wort(text):
    zu_ersetzen = input("Welches Wort soll ersetzt werden: ")
    ersatz = input("Mit welchem Wort soll ersetzt werden: ")
    neuer_text = text.replace(zu_ersetzen, ersatz)
    print("Ersetzer Text:\n", neuer_text)
    return neuer_text

def speicher_neuen_text(text):
    with open ("modifizierter_text.txt", "w", encoding="utf-8") as datei:
        datei.write(text)
        print("Text wurde als 'modifizierter_text.txt' gespeichert.")

def json_datei(text):
    daten = {"inhalt":text}
    with open("daten.json", "w", encoding="utf-8") as datei:
        json.dump(daten, datei, ensure_ascii=False, indent=4)
        print("Text wurde in 'daten.json' als JSON gespeichert.")

aktueller_text = text

while True:
    print("1 - Wort zählen")
    print("2 - Wort ersetzen")
    print("3 - Text speichern")
    print("4 - Text speichern als json")
    print("5 - Aktuellen Text anzeigen")
    print("6 - Beenden")

    wahl = input("Deine Auswahl: ")

    if wahl == "1":
        wort = input("Welches Wort soll gezählt werden: ")
        wort_zaehlen(aktueller_text, wort)
    elif wahl == "2":
        aktueller_text = ersetze_wort(aktueller_text)
    elif wahl == "3":
        speicher_neuen_text(aktueller_text)
    elif wahl == "4":
        json_datei(aktueller_text)
    elif wahl == "5":
        print("\nAktueller Text:\n")
        print(aktueller_text)
    elif wahl == "0":
        print("Programm wird beendet.")
        break
    else:
        print("Ungültige Eingabe. Bitte wähle eine Zahl von 0 bis 5.")    

#Lösung Skript:
# text = "Hier ist ein Beispieltext mit einigen besonderen Zeichen: \nNeue Zeile, \tTabulator, \\Backslash, \u2764Herz Emoji, \U0001F600Grinsendes Gesicht."

# gesuchtes_wort = input("Bitte gib das Wort ein, nach dem gesucht werden soll: ")
# wortanzahl = text.count(gesuchtes_wort)
# print(f"Das Wort '{gesuchtes_wort}' kommt {wortanzahl} Mal vor.")

# zu_ersetzendes_wort = input("Bitte gib das Wort ein, das ersetzt werden soll: ")
# ersatzwort = input("Bitte gib das Ersatzwort ein: ")
# modifizierter_text = text.replace(zu_ersetzendes_wort, ersatzwort)
# print("Modifizierter Text:")
# print(modifizierter_text)

# with open('modifizierter_text.txt', 'w', encoding='utf-8') as datei:
#     datei.write(modifizierter_text)

# import json

# try:
#     with open('daten.json', 'r', encoding='utf-8') as datei:
#         daten = json.load(datei)
#         print("Inhalt der 'daten.json':")
#         print(daten)
# except FileNotFoundError:
#     print("Die Datei 'daten.json' wurde nicht gefunden.")