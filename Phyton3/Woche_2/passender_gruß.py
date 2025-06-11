#Übung 3: Passender Gruß
#Schreibe ein Programm, das zur aktuellen Uhrzeit passend grüßt. Morgens erfolgt die Begrüßung mit 
# „Guten Morgen“, mittags mit „Guten Tag“, und abends wird „Guten Abend“ gesagt

import time
zeit = time.localtime()
stunde = zeit.tm_hour
if stunde < 12:
    gruß = "Guten Morgen"
elif stunde == 12:
    gruß = "Guten Tag"
else: 
    gruß = "Guten Abend"
print(gruß)
