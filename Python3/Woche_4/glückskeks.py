from random import choice

TUE = ["Liebe", "Beachte", "Vergiss nicht", "Achte", "Schätze", "Respektiere", "Begrüße"]
DAS = ["das Leben", "deine Seele", "die Leidenschaft", "deine Freunde"]

wahl = "n" #Wahl bekommt einen Wert damit die Schleife mindestens einmal durchläuft
while wahl in "nN":
    glueckskeks = "{} {}!".format(choice(TUE), choice(DAS))
    print(glueckskeks)
    wahl = input("(N)euer Glückskeks (E)nde:")

print("Bis bald!")
input()