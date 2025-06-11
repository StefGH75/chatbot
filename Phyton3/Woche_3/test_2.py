def speichere_daten(studenten):
    try:
        with open('studentendaten.txt', 'w') as datei:
            for student in studenten:
                zeile = f"Name: {student[0]}, Matrikelnummer: {student[1]}, Studiengang: {student[2]}\n"
                datei.write(zeile)
    except IOError:
        print("Fehler beim Speichern der Datei.")


def lade_daten():
    try:
        studenten = []
        with open('studentendaten.txt', 'r') as datei:
            for zeile in datei:
                name, matrikelnummer, studiengang = zeile.strip().split(", ")
                student = {
                    "Name": name.split(": ")[1],
                    "Matrikelnummer": matrikelnummer.split(": ")[1],
                    "Studiengang": studiengang.split(": ")[1]
                }
                studenten.append(student)
        return studenten
    except IOError:
        print("Fehler beim Laden der Datei.")
        return []


# Beispiel für die Verwendung der Funktionen

studenten_daten = [
    ("Max Mustermann", "123456", "Informatik"),
    ("Erika Musterfrau", "654321", "Wirtschaftsinformatik")
]


speichere_daten(studenten_daten)
geladene_daten = lade_daten()
print(geladene_daten)


