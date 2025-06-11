with open("text.txt", "w") as stream:
    stream.write("Vierter Versuch")
    3/0 #Die ungültige Division durch 0 führt zu einem Laufzeitfehler. Öffne die Datei text.txt. 
        #Du stellst fest, dass sie nun den neuen Text enthält. Die Datei ist also vor dem Programmabbruch 
        # abgespeichert worden


#stream = open("text.txt", "w")
#try:
 #   stream.write("Zweiter Versuch")
#finally:
   # stream.close()