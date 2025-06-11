from random import choice

def aufgabe(dictionary): #Funktion definiert, die kompletten Dialog bewerkstelligt, wird immer wieder aufgerufen
    vokabel = choice(list(dictionary.keys())) #aus der Liste der englischen Wörter (key) wird ein zufälliges Wort ausgewählt
    print("Nennen sie ein deutsches Wort für", vokabel + "!" )
    antwort = input("Deutsches Wort: ")
    if antwort not in dictionary[vokabel]: #Der Wert, der zu einem Schlüssel gehört, ist eine Liste von deutschen Wörtern
        print("Leider falsch") #wenn Antwort nicht in der Liste vorkommt, wird "Leider falsch" ausgegeben
        print(vokabel, "bedeutet: ", end='') #Schlüsselwort end=" " bewirkt, dass hinter der Ausgabe kein Zeilenumbruch erfolgt, sondern nur Leerzeichen (z.B. head bedeutet)
        for wort in dictionary[vokabel]: 
            print(wort, end='') #durch end="" alle Wörter der Liste werden hintereinander in der gleichen Zelle ausgegeben
            print()#Zeilenumbruch wird bewirkt
    else: 
        print("Richtig!")
        del dictionary[vokabel] #falls Spieler Vokabel gewusst hat, wird Item aus Dictionary gelöscht

dictionary = {'sun':['Sonne'],'key':['Taste', 'Schlüssel'],'head':['Kopf','Chef','Leiter']} #Wörterbuch definiert

while dictionary: #ein leeres Dictionary hat Wahreitswert False. Solange das nicht der Fall ist, wird dictionary übergeben
    aufgabe(dictionary)

print("Sie haben alle Vokabeln gelernt.")
eingabe= input() #hier wartet computer bis Enter gedrückt worden ist. Erst dann wird Ausführung beendet
    