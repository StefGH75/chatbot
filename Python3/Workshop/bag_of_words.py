def bow(satz, vokabular): 

    woerter = satz.lower().split() # Satz in Kleinbuchstaben umgewandelt und in Wörter aufgeteilt

    bow = [0] * len(vokabular) # dictonary mit 0 initialisiert mit enstprechender Anzahl Einträgen 
    #bow = {wort: 0 for wort in vokabular}

    for i, wort in enumerate(vokabular): # jedes Wort wird durchlaufen und markiert
                                        #enumerate erzeugt ein Tuple (Index, Element) für jedes Wort in der Liste (vokabular)
                                        #i ist der Index des aktuellen Worts in der Liste, wort ist das tatsächliche Wort an dieser Stelle
                                        # statt enumerate: Durchlaufe das Vokabular manuell mit Index
                                        #for i in range(len(vokabular)):
                                        #wort = vokabular[i]
                                        #if wort in woerter:
                                        #bow[i] = 1
        if wort in woerter:
            bow[i] = 1  # Wenn das Wort vorkommt, setze auf 1
    #for wort in vokabular:
        #if wort in satz:
            #bow[vokabular.index[wort)]] = 1

    return bow  

#Beispiel:
vokabular = ["hallo", "wie", "mein", "gehts", "name", "ist", "schlecht", "dir"]

while True:
    satz = input("Gib einen Satz ein oder 'Beenden': ")
    if satz.lower() == "beenden":
        break
    bow = bow(satz, vokabular)
    print("Bag-of-Words für Satz: ", bow)




#satz1 = "hallo wie gehts dir"
#satz2 = "mein name ist cornelius" 

#bow1 = bow(satz1, vokabular)
#bow2 = bow(satz2, vokabular)

#print("Bag-of-Words für Satz 1:", bow1)
#print("Bag-of-Words für Satz 2:", bow2)


	
