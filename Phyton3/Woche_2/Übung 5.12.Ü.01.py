#Entwickle eine Python-Funktion namens filtere_gerade_zahlen, die eine Liste von Zahlen als Argument 
# nimmt und mithilfe der filter()-Funktion alle geraden Zahlen aus dieser Liste zurückgibt. Verwende 
# eine Lambda-Funktion, um zu bestimmen, ob eine Zahl gerade ist. Die Funktion soll die gefilterten 
# Zahlen als Liste zurückgeben. Teste deine Funktion mit einer Liste von Zahlen und gib das Ergebnis 
# mit der print()-Funktion aus. Verwende für deine Tests die Liste [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] und 
# stelle sicher, dass deine Funktion korrekt implementiert ist, indem du das Ergebnis überprüfst. 

def filtere_gerade_zahlen(zahlen):
    gerade_zahlen = list(filter(lambda zahl: zahl % 2 == 0, zahlen)) #Lambda prüft, ob der Rest bei Division durch 
                                                               # 2 gleich 0 ist (also gerade Zahl)
    return gerade_zahlen

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

gefilterte_gerade_zahlen = filtere_gerade_zahlen(liste)
print(gefilterte_gerade_zahlen)