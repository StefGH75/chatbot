#Kosten für Reisegruppe mit Bus
kosten_bus = float(input("Wie teuer war der Bus: "))
kosten_hotel = float(input("Wie hoch waren die Kosten für das Hotel pro Person: "))
kosten_reisefuehrer = float(input("Wie hoch waren die Reiseführer-Kosten: "))
anzahl_teilnehmer = float(input("Wieviele Teilnehmer gab es: "))

gesamt_kosten = kosten_bus + kosten_hotel * anzahl_teilnehmer + kosten_reisefuehrer

print("Gesamtkosten: ", round(gesamt_kosten), "EUR")
print("Kosten pro Person: ", round(gesamt_kosten / anzahl_teilnehmer), "EUR")