#bremsweg = s
#geschwindigkeit = v
#bremsverzoegerung = a
#bremswegverzoegerung_trocken = 8
#bremswegverzoegerung_nass = 7

eingabe_geschwindigkeit = float(input("Geschwindigkeit in km/h: "))
eingabe_bremsweg = float(input("Bremsweg in m: "))
eingabe_bremswegverzoegerung = input ("Ist die Fahrbahn nass oder trocken? ")

v = eingabe_geschwindigkeit
a = eingabe_bremsweg
if eingabe_bremswegverzoegerung == "trocken":
    a = 8;
else:
    a = 7
v_ms = v / 3.6
bremsweg = v_ms ** 2/ (2 * a)
print("Die Bremsverzögerung ist: ", a)
print("Der Bremsweg ist: " ,round(bremsweg), "m")

