# Aufgabe: Fehler finden und vermeiden
# Du sollst eine Python-Funktion namens verbessere_quicksort schreiben, die den Quicksort-Algorithmus 
# implementiert und zusätzlich eine Verbesserung beinhaltet: Bevor die eigentliche Sortierung beginnt, soll 
# überprüft werden, ob die Liste bereits sortiert ist. Ist dies der Fall, gibt die Funktion die Liste direkt
#  zurück, ohne den Quicksort-Algorithmus durchzuführen. Diese Überprüfung soll durch eine Zusicherung (assert
# ) realisiert werden, die sicherstellt, dass die Funktion nur dann den Quicksort-Algorithmus ausführt, wenn
#  die Liste nicht bereits sortiert ist. Implementiere außerdem eine einfache Debugging-Ausgabe, die den
#  Zustand der Liste vor und nach der Sortierung in die Konsole schreibt, sofern die Umgebungsvariable DEBUG 
# auf True gesetzt ist.

import os
def ist_sortiert(s):
    return all(s[i] <= s[i+1] for i in range(len(s)-1))

def verbessere_quicksort(s):
    if ist_sortiert(s):
        return s #"Die Liste ist bereits sortiert."
    
    def quickssort(s):
        if len(s) <= 1:  #Abbruchbedingung: Liste mit 0 oder 1 Element ist schon sortiert
            return s

    debug = os.getenv('DEBUG', 'False') == 'True'

    if debug:
        print("Vor der Sortierung:", s)
    
    def quicksort(s):
        if len(s) <= 1:
            return s
        pivot = s[0]
        kleiner = [x for x in s[1:] if x < pivot]
        groesser_gleich = [x for x in s[1:] if x >= pivot]
        return quicksort(kleiner) + [pivot] + quicksort(groesser_gleich)
    
    sortierte_liste = quicksort(s)

    if debug:
        print("Nach der Sortierung:", sortierte_liste)
    
    return sortierte_liste