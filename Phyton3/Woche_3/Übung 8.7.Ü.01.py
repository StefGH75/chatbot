# a) Definiere eine Liste mit Namen einkaufsliste und fülle sie mit mindestens fünf verschiedenen 
# Lebensmitteln (als Strings).
# b) Schreibe eine Funktion einkauf_hinzufuegen, die ein neues Lebensmittel zur einkaufsliste hinzufügt. 
# Die Funktion soll überprüfen, ob das Lebensmittel bereits in der Liste vorhanden ist. Ist dies der Fall, 
# soll eine entsprechende Nachricht ausgegeben werden ("Lebensmittel bereits in der Liste!"), andernfalls 
# soll das Lebensmittel hinzugefügt werden.
# c) Nutze eine Schleife, um den Benutzer bis zu drei Mal nach neuen Lebensmitteln zu fragen, die zur Liste
#  hinzugefügt werden sollen. Verwende die Funktion einkauf_hinzufuegen für jeden Eingabewert.
# d) Speichere die endgültige einkaufsliste in einer Datei namens einkaufsliste.txt mithilfe der 
# with-Anweisung und dem write-Modus. Achte darauf, jedes Lebensmittel in einer neuen Zeile zu speichern.
# e) Fange mögliche Laufzeitfehler ab, die beim Öffnen, Schreiben oder Schließen der Datei auftreten können,
#  indem du try und except Blöcke verwendest.
# f) Lies die einkaufsliste.txt Datei und gib ihren Inhalt Zeile für Zeile in der Konsole aus. Verwende 
# dabei ebenfalls die with-Anweisung und den read-Modus.

einkaufsliste = ["Kartoffeln", "Brot", "Butter", "Marmelade", "Quark"]

def einkauf_hinzufuegen(lebensmittel):
    if lebensmittel in einkaufsliste:
        print("Lebensmittel bereits in der Liste!")
    else:
        einkaufsliste.append(lebensmittel)
        print(f"{lebensmittel} wurde zur Liste hinzugefügt.")

for i in range(3):
        lebensmittel_neu = input("Neues Lebensmittel: ")
        einkauf_hinzufuegen(lebensmittel_neu)

try:
    with open ("einkaufsliste.txt", "w") as datei:
        for lebensmittel in einkaufsliste: #iteriert über jedes Tupel in der Liste
            datei.write(f"{lebensmittel} \n") #schreibt 
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: ", e)

try:
    with open ("einkaufsliste.txt", "r") as datei:
        inhalt = datei.readlines()
        print("Einkaufsliste: ")
        for lebensmittel in inhalt: #liest Datei zeilenweise aus
            print(lebensmittel.strip())
except Exception as e:
        print(f"Ein Fehler ist aufgetreten beim Laden der Daten: {e}")
