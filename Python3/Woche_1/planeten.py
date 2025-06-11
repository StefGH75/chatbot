print("Zähle alle Planeten unseres Sonnensystems auf!")
planeten = {"Mars", "Erde", "Jupiter", "Saturn", "Uranus", "Venus", "Merkur"} # Menge mit den 8 Planeten
while planeten != set(): # Block wird solange wiedrholt, wie die Menge der planeten nicht leer ist (noch Elemente enthalten)
                                #len(planeten) > 2:
    planet = input("Planet: ")
    if planet in planeten:
        planeten = planeten - {planet} # wenn eingegene string planet in planeten enthalten ist, wird dieser aus Menge entfernt
        print("Richtig!")
    else:
        print("Sorry!", planet,"hatten wir schon oder", planet, "ist kein Planet")
    
print("Glückwunsch. Du hast alle Planeten aufgezählt")