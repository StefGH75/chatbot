from math import pi

def kuppel(hoehe:float, radius:float) -> float:
    'Volumen eines halben Rotationsellipsoiden' #Einzeiliger Docstring, der erklärt, was die Funktion macht.
    return 2/3 * pi * radius ** 2 * hoehe

def quader(laenge:float, breite:float, hoehe:float)-> float:
    'Volumen eines Quaders' #Einzeiliger Docstring, der erklärt, was die Funktion macht.
    return laenge * breite * hoehe

if __name__ =="__main__":
    print("Kuppel mit Radius 1 und Höhe 1", kuppel(1,1))
    print("Quader mit Seitenlängen 2, 3, 2: ", quader(2,3,2))