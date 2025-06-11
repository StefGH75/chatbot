f = open("faust.txt", "r", encoding="utf-8") #Text wird aus dem Stream f gelesen 
text = f.read() #..und als string der Variablen text zugewiesen
f.close() #schließen, da nicht mit with open 
text = text.lower() #aus String wird neuer String aus kleinen Buchstaben und wieder dem Variablennamen text zugewiesen
for p in ".,:-?!;()_/[]": #es werden nach und nach Satzzeichen durch Leerzeichen ersetzt
    text = text.replace(p, "") #dabei jeweils ein neuer string immer wieder der gleichen Variable text zugewiesen
wortliste = text.split() #Text wird in eine Liste von Wörtern zerlegt, als Trennstring wird Leerraum zwischen Wörtern verwendet
wortmenge = set(wortliste) #Aus Wortliste wird eine Menge (ohne Duplikate) gebildet
print("Wörter insgesamt: ", len(wortliste))
print("Unterschiedliche Wörter: ", len(wortmenge))
print(list(wortmenge)[:50]) #aus der Menge wird eine Liste gebildet und aus dieser Liste eine neue liste mit den ersten 
                            #50 items erzeugt ausgegeben