#a) Lese eine Textdatei namens "tagebuch.txt", die in UTF-8 kodiert ist, und speichere den Inhalt in einer 
# Variablen. Verwende die with-answeisung und try-except-Blöcke, um Fehler beim Dateizugriff zu handhaben.
# b) Verwende eine Funktion, um alle Vorkommen eines bestimmten Wortes im Text zu zählen. Das Wort soll als 
# Parameter an die Funktion übergeben werden.
# c) Ersetze in dem Text alle Vorkommen des Wortes "traurig" durch "glücklich" und speichere das Ergebnis in
#  einer neuen Datei namens "tagebuch_neu.txt".
# d) Schreibe eine weitere Funktion, die den aktualisierten Text nimmt und eine Liste von Sätzen zurückgibt, 
# wobei jeder Satz ein Element der Liste ist. Verwende dazu eine geeignete String-Methode.
# e) Konvertiere die Liste von Sätzen in ein JSON-Format und speichere diese Daten in einer Datei namens 
# "tagebuch_saetze.json".
# Stelle sicher, dass dein Skript modular aufgebaut ist und du Import-Module für JSON-Funktionalitäten und 
# andere benötigte Funktionen verwendest. 

import json

#zählt wie oft ein bestimmtes Wort im Text vorkommt
def wort_zaehlen(text, wort):
    return text.lower().count(wort.lower()) 

#ersetzt ein Wort im Text durch ein anderes
def ersetze_wort(text, alt, neu):
    return text.replace(alt, neu)

#teilt den Text in Sätze auf
def teile_in_saetze(text):
    return text.split(" ")

#schreibt die Daten in eine json-datei
def json_format(dateiname, daten):
    with open("tagebuch_saetze.json", "w", encoding="utf-8") as datei:
        json.dump(daten, datei, ensure_ascii=False, indent=4)

try:
    with open("tagebuch.txt", "w+", encoding="utf-8") as datei:
        datei.write("Das ist ein Beispiel Tagebuch Eintrag. Liebes Tagebuch. Ich bin heute traurig.")
        datei.seek(0) #Cursor an den Anfang setzen
        inhalt = datei.read()       
except Exception as e:
    print("Fehler: ", e)
else:
    wort_vorkommen = wort_zaehlen(inhalt,"Tagebuch")
    print(f"Das Wort Tagebuch kommt {wort_vorkommen} mal vor.")

    aktualisierter_text = ersetze_wort(inhalt, "traurig", "glücklich")

    with open("tagebuch_neu.txt", "w", encoding="utf-8") as neue_datei:
        neue_datei.write(aktualisierter_text)

    saetze = teile_in_saetze(aktualisierter_text)
    json_format("tagebuch_satze.json", saetze)
