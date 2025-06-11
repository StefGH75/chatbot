from random import choice
#Textschablone, langer String mit Platzhaltern
STORY = '''Am Morgen ging {sie} mit ihrem {gegenstand} über den {ort}. "Ach", dachte {sie}, "wie gut, 
dass ich den {gegenstand} dabeihabe. Ohne {gegenstand} käme ich mir irgendwie unvollständig vor."'''
ORTE = ["Prinzipalmarkt", "Domplatz"] #Liste von orten, die später zufällig ausgewählt werden
sie = input("Weiblicher Vorname: " ) #Benutzer gibt Wörter ein
gegenstand = input("Gegenstand(männlich): ")
story = STORY.format(sie=sie, gegenstand=gegenstand, ort = choice(ORTE)) #es wird ein neuer string gebildet, indem
#in Textschablone die Platzhalter durch Wörter ersetzt werden, der neue string Variable story zugewiesen
print(story)