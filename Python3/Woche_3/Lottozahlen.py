from random import choice

lottozahlen = list(range(1,50)) #Liste mit den zahlen 1 bis 49 erzeugt
gezogen = [] #leere Liste gezogen wird definiert, soll mit Lottozahlen gefüllt werden
for i in range(6): #der Block wird 6mal wiederholt
    zahl = choice(lottozahlen) #eine zufällige Zahl wird aus den (verbleibenden) lottozahlen ausgewählt
    lottozahlen.remove(zahl) #die gezogene Zahl wird aus der Liste entfernt
    gezogen.append(zahl) #die gezogene Zahl wird an die Liste gezogen angehängt

gezogen.sort() #die gezogene liste wird sortiert
print("Ziehung der Lottozahlen: ")
for z in gezogen:
    print(z, end=" ") #end bewirkt, dass sie in einer Reihe ausgegeben werden