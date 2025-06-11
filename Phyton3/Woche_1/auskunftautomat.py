#print("Willkommen! Bitte stellen Sie ihre Frage.")
#frage = input("Frage: ")
#if "wann" in frage:
    #print("Vielen Dank für Ihre Frage zum Liefertermin.")
    #print("Carla hiflt Ihnen gern weiter.")
#elif "Rechnung" in frage:
 #   print("Vielen Dank für Ihre Frage zur Rechnung.")
 #   print("Tom hilft Ihnen gern weiter.")
#else:
#    print("Vielen Dank für Ihre Frage")
 #   print("Kim hilft Ihnen gern weiter.")


print("Willkommen! Bitte stellen Sie ihre Frage.")
frage = input("Frage: ")
if "Wann" in frage:
    thema = "zum Liefertermin"
    zuständig = "Carla"
elif "Rechnung" in frage:
    thema = "zur Rechnung"
    zuständig = "Tom"
else:
    thema = ""
    zuständig = "Kim"

print("Vielen Dank für Ihre Frage", thema)
print(zuständig, "hilft Ihnen gern weiter.")