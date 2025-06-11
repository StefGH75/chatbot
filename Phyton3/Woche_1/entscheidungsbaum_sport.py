sonne = input("Scheint die Sonne ja/nein: ")
if sonne == "ja":
    luftfeuchtigkeit = input("Ist die Luftfeuchtigkeit hoch: ")
    if luftfeuchtigkeit == "ja":
        print("Kein Sport")
    else:
        print("Sport")
else:
    regen = input("Regnet es: ")
    if regen == "ja":
        wind = input("Ist es windig: ")
        if wind == "ja":
            print("Kein Sport")
        else:
            print("Sport")
    else:
        print("Sport")