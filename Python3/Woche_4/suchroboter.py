from urllib.request import urlopen
from re import findall 

def finde_url(text: str):
    #return findall(r"https:?//+?[a-zA-Z0-9_.+-]+.html", text)
    return findall(r"https?://.+?.html", text)
def ausgabe(url:str, liste:list):
    if liste:
        print(f"Die Seite {url} enthält folgende URLs: ")
        for adresse in liste:
            print(adresse)
    else:
            print("Keine URL gefunden.")

while True:
    url = input("URL eingeben (oder Enter zum Beenden): ").strip()
    if not url:
        break

    try:
        f = urlopen(url)
        htmltext = f.read().decode()
        f.close
        liste = finde_url(htmltext)
        ausgabe(url, liste)
    except:
        print('Webseite konnte nicht geöffnet werden.')
print("Auf Wiedersehen")

#Lösung Skript:
# def urls_finden(webseite):
#     with urlopen(webseite) as f:
#         htmltext = f.read().decode()
#     reg = r'https?://.+?\.html'
#     url_liste = findall(reg, htmltext)
#     return set (url_liste)

# url = input("Webseite: ")
# try: 
#     urls = urls_finden(url)
#     print("Ich habe folgende URLs gefunden: ")
#     for url in urls:
#         print url
# except:
#     print("Ich konnte keine URLs finden.")
#     print("Prüfe bitte die Internetverbindung.")