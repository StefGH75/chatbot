import pickle

liste = [1, 2, 3]
with open("liste.dat", "wb") as stream: #Im aktuellen Arbeitsverzeichnis wird eine Binärdatei zum Schreiben
                                        #geöffnet (Modus: wb). Weil in deinem Arbeitsverzeichnis (vermutlich)
                                        #noch keine Datei mit dem Namen liste.dat existiert, wird automatisch
                                        #eine neue Datei mit diesem Namen angelegt. Dabei wird ein Stream mit
                                      #dem Namen f erzeugt.
    pickle.dump(liste, stream) #Die Liste liste wird im Stream f gespeichert. Weil das Modul als Ganzes
                                #importiert worden ist, muss der Funktionsaufruf mit pickle beginnen. Mit
                                #dem Ende der with-Anweisung wird der Stream geschlossen und damit
                                #die Datei physisch gespeichert.
print(liste)