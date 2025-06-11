#Entwickle ein Python-Programm, das die Rolle eines einfachen Quizspiels übernimmt.
# Das Spiel soll aus drei Fragen bestehen, die nacheinander gestellt werden. 
# Für jede Frage gibt es drei Antwortmöglichkeiten (a, b, c), von denen genau eine richtig ist.
# Nachdem der Spieler alle Fragen beantwortet hat, soll das Programm die Anzahl der richtig 
# beantworteten Fragen ausgeben und eine Rückmeldung geben. 
# Verwende für jede Frage eine if-elif-else-Struktur, um zu überprüfen, ob die Antwort 
# des Spielers richtig oder falsch ist. Nutze zudem eine while-Schleife, um sicherzustellen, 
# dass das Spiel nur fortgesetzt wird, wenn der Spieler eine gültige Antwort (a, b, oder c) 
# eingegeben hat. Wenn eine ungültige Eingabe erfolgt, soll der Spieler erneut zur Eingabe
# aufgefordert werden, bis eine gültige Antwort gegeben wird.

print("Quizspiel")

richtige_antworten = 0

antwort = input("Was ist die Hauptstadt von Frankreich?: "
"a) Madrid "
"b) Paris "
"c) Rom "
"Deine Antwort: ")

while antwort not in ["a", "b", "c"]:
    print("Das ist keine gültige Antworte. Bitte wähle a, b oder c")
    antwort = input("Was ist die Hauptstadt von Frankreich?: ")

if antwort =="b":
        print("Die Antwort ist korrekt")
        richtige_antworten +=1
else:
        print("Die Antwort ist nicht korrekt")

antwort = input("Wie viele Beine hat eine Spinne?: "
"a) 6 "
"b) 8 "
"c) 10: "
"Deine Antwort:" )

while antwort not in ["a", "b", "c"]:
    print("Das ist keine gültige Antworte. Bitte wähle a, b oder c")
    antwort = input("Wie viele Beine hat eine Spinne? : ")
if antwort =="b":
        print("Die Antwort ist korrekt")
        richtige_antworten +=1
else: 
        print("Die Antwort ist nicht korrekt")


antwort= input("Welche Farbe ergibt sich aus der Mischung von Blau und Gelb? "
"a) Grün "
"b) Lila "
"c) Orange: "
"Deine Antwort: ")

while antwort not in ["a", "b", "c"]:
    print("Das ist keine gültige Antworte. Bitte wähle a, b oder c")
    antwort = input("Welche Farbe ergibt sich aus der Mischung von Blau und Gelb?: ")

if antwort =="a":
         print("Die Antwort ist korrekt")
         richtige_antworten +=1
else: 
       print("Die Anwtort ist nicht korrekt")

print(f"Du hast {richtige_antworten} von 3 Fragen richtig beantwortet.")

#if richtige_antworten == 3:
 #   print("Du hast 3 richtige Antworten")
#elif richtige_antworten == 2:
#    print("Du hast 2 richtige Antworten")
#elif richtige_antworten == 1:
   # print("Du hast 1 richtige Antwort")
#else:
   # print("Schade. Du hast keine richtige Antwort. Probiere es noch einmal.")