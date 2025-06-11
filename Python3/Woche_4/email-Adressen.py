from urllib.request import urlopen
from re import findall

# def finde_adressen(text:str):
#     for p in ".,:-?!;()_/[]": #es werden nach und nach Satzzeichen durch Leerzeichen ersetzt
#         text = text.replace(p, "") #dabei jeweils ein neuer string immer wieder der gleichen Variable text zugewiesen
#     wortliste = text.split() 
#     wortmenge = set(wortliste)
#     adressen = []

#     for wort in wortmenge:
#         if "@" in wort and "." in wort:
#             adressen.append(wort)
#     return adressen

def finde_adressen(text: str):
    return findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

def ausgabe(url:str, liste:list):
    if liste:
        print(f"Die Seite {url} enthält folgende Email-Adressen: ")
        for adresse in liste:
            print(adresse)
    else:
            print("Keine Email-Adresse gefunden.")

while True:
    url = input("URL eingeben (oder Enter zum Beenden): ").strip()
    if not url:
        break

    try:
        f = urlopen(url)
        htmltext = f.read().decode()
        f.close
        liste = finde_adressen(htmltext)
        ausgabe(url, liste)
    except:
        print('Webseite konnte nicht geöffnet werden.')
print("Auf Wiedersehen")


