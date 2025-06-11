ZEILE = "{:15}|{:10}" #Formatierungsstring mit zwei Platzhaltern, erste reserviert 15 Stellen, der zweite 10

def haeufigste_woerter(text, minlänge, anzahl):
    for ch in '${}<>.;:/?!"-_[]': #Satzzeichen
        text = text.replace(ch,' ') #werden durch Leerzeichen ersetzt
    wortliste = text.split() #der Text wird in Wörter zerteilt
    wortmenge = set(wortliste) #aus der Liste wird eine Menge aus Wörtern (ohne Duplikate) gewonnen
    haeufigkeiten = [(text.count(wort), wort) for wort in wortmenge if len(wort) >= minlänge]
    #eine Liste von Tupeln im Format (Häufigkeit, das Wort selbst) erstellt. In jedem Tupel kommt zuerst die Häufigkeit
    #(eine ganze Zahl), weil an später die Liste nach Häufigkeiten sortieren kann, Es werden nur Wörter aus 
    #der Wortmenge mit Länge größer oder gleich minlänge berücksichtigt
    haeufigkeiten.sort() #Liste nach Häufigkeiten aufsteigend sortiert
    haeufigkeiten.reverse() #Reihenfolge wird umgekehrt, also absteigend
    return haeufigkeiten[0:anzahl] #Liste bestehend aus den ersten Anzahl Tupeln der Liste zurückgegeben, Index 0 bis anzahl minus 1

def ausgabe(haeufigkeiten):
    print(ZEILE.format("Wort", "Vorkommen"))
    print(26*"-") #ausgegeben wird ein string aus 26 Minuszeichen (für die Tabelle)
    for vorkommen, wort in haeufigkeiten:
        print(ZEILE.format(wort, vorkommen))

dateiname = input("Dateiname: ")
minlaenge = int(input("Minimale Wortlänge: "))
anzahl = int(input("Länge der Tabelle: "))
f = open(dateiname, "r", encoding="utf-8")
text = f.read()
f.close
tabelle = haeufigste_woerter(text, minlaenge, anzahl)
ausgabe(tabelle)
input()
