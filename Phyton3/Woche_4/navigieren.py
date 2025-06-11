import os

pfad = os.getcwd()

while pfad:
    print("Arbeitsverzeichnis: " + os.getcwd()) #Auf dem Display erscheint Arbeitsverzeichnis und dahinter vollständige Pfad
    print("Inhalt: ")
    for d in os.listdir(): #Liste der Dateien und Unterverzeichnisse wird durchlaufen
        print(d)
    pfad = input("Gewünschtes Verzeichnis: ")
    if os.path.exists(pfad): #falls gültiger Pfad, wird Verzeichnis mit diesem Pfad zum Arbeitsverzeichnis, siehe oben nochmal durchlaufen
        os.chdir(pfad)
    elif pfad:
        print("Ungültiger Pfad")
print("Auf Wiedersehen.")
input()
