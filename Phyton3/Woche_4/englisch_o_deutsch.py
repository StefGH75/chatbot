
ENGLISCH = (" the ", " of ", " to ", " and ", " a ") #Liste mit den häufigsten Wörtern, Leerzeichen vor und nach
DEUTSCH = (" die ", " der ", " und ", " zu ", " den " ) #Wort, damit sie einzeln gezählt werden (nicht to in tollkühn)

def zaehle(text:str, haeufige_woerter:list): #Funktion ermittelt wie häufig typische Wörter einer Sprache 
    n = 0                                      #im string text vorkommen 
    for wort in haeufige_woerter:
        n += text.count(wort)
        return n                               #und gibt Zahl zurück 

text = ""  #Variable text bekommt einen Wert, damit die Schleife wenigstens einmal durchlaufen kann
while len(text) < 50:
    text = input("Text (mindestens 50 Zeichen): ")

n_englisch = zaehle(text, ENGLISCH) 
n_deutsch = zaehle(text, DEUTSCH)
if n_englisch > n_deutsch:
    sprache = "Englisch"
elif n_deutsch > n_englisch:
    sprache = "Deutsch"
else: 
    sprache = "Unbekannt"
print()

print(f"Im Text erkenne ich {n_deutsch} typische deutsche Wörter und {n_englisch} typische englische Wörter. Sprache: {sprache}") 