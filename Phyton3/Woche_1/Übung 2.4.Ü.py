# a)Erstelle eine Liste mit den Namen deiner 5 besten Freunde
freunde = ["Elisabeth", "Andrea", "Mailin", "Sandra", "Silke"]

# b) Füge der Liste zwei neue Namen hinzu, indem du die append() Methode verwendest.
freunde.append("Antje")
freunde.append("Susanne")
print(freunde)

# c) Entferne einen Namen aus der Liste mit der remove() Methode.
freunde.remove("Andrea")
freunde

# d) Erstelle ein Tupel, das drei verschiedene Ganzzahlen enthält.
ganzzahlen = (3, 7, 10)

#e) Konvertiere das Tupel in eine Liste und füge eine weitere Ganzzahl hinzu.
ganzzahlen_liste = list(ganzzahlen)
ganzzahlen_liste
ganzzahlen_liste.append(15)
ganzzahlen_liste

# f) Erstelle eine Menge mit mindestens drei deiner Lieblingsfrüchte.
fruechte = {"Äpfel", "Banane", "Himbeere"}

# g) Füge der Menge eine neue Frucht hinzu, die noch nicht in der Menge enthalten ist.
fruechte.add("Erdbeere")
fruechte

#h) Erstelle ein Dictionary, dass drei verschiedene Länder als Schlüssel und deren Hauptstädte als Werte enthält. 
geographie = {"Deutschland":"Berlin","Frankreich":"Paris", "Dänemark":"Kopenhagen"}
geographie