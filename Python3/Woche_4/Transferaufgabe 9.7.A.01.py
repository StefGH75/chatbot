#)a) Lese einen Text aus einer Datei, die Unicode-Zeichen enthält, und speichere den Text in einer Variablen. 
# Verwende dazu die with-Anweisung und stelle sicher, dass die Datei korrekt geschlossen wird.
# b) Verwende reguläre Ausdrücke, um alle Wörter im Text zu finden, die mit einem Großbuchstaben beginnen, und 
# speichere diese Wörter in einer Liste.
# c) Erstelle eine Funktion, die die Anzahl der Vorkommen jedes Wortes in der Liste aus b) zählt und diese in 
# einem Dictionary speichert.
# d) Speichere das Dictionary aus c) in einer JSON-Datei. Stelle sicher, dass Umlaute und Sonderzeichen korrekt
#  gespeichert werden.
# e) Lies die JSON-Datei, die du in d) erstellt hast, und gib den Inhalt in der Konsole aus. Verwende hierbei
#  die richtige Kodierung, um Umlaute und Sonderzeichen korrekt darzustellen. 

import re
import json

def text_lesen(dateiname):
    with open("datei.txt", "r", encoding="utf-8") as datei:
        return datei.read()

def finde_grossbuchstaben(text):
    return re.findall(r'[A-Z]+?', text)

def zaehlen(woerter):
    wort_zaehler = {}
    for wort in woerter:
        if wort in wort_zaehler:
            wort_zaehler[wort] += 1
        else:
            wort_zaehler[wort] = 1
    return wort_zaehler

def speichere_als_json(dictionary, dateiname):
    with open(dateiname, "w", encoding="utf-8") as datei:
        json.dump(dictionary, datei, ensure_ascii=False, indent=4)

def lese_json(dateiname):
    with open(dateiname, "r", encoding="utf-8") as datei:
        inhalt = json.load(datei)
        print(inhalt)

text = text_lesen("textdatei.txt")
wörter = finde_grossbuchstaben(text)
wort_zaehlen = zaehlen(wörter)
speichere_als_json(wort_zaehlen, "wort_zaehler.json")
lese_json("wort_zaehler.json")