from urllib.request import urlopen
from re import findall

WDR = "https://www1.wdr.de/index.html" 
# f = urlopen(WDR) #Webseite des WDR heruntergeladen
# htmltext = f.read().decode() #Webseite als bytestring gelesen und mit der Methode decode in einen string überführt
# f.close

# liste = htmltext.split("Max:") #splitting mit "max:" als Trennstring. Es entsteht Liste mit drei Strings.
#                                 # zu Beginn des zweiten Strings(Index=1) und dritten Strings (Index=3) stehen
#                                 #gesuchte Zahlenwerte
# heute = liste[1].split("°")[0] #der zweite String(index=1) wird mit "°" als Trennstring gesplittet. Dabei entsteht
#                                 #neue Liste mit zwei Strings. Das erste Element(index=0) ist String mit Zahlenwert
#                                 #der vor ° steht. Das ist erwartete Höchsttemperatur für heute = wird heute zugewiesen
# morgen = liste[2].split("°")[0] #in gleicher Weise wird drittes Element von liste analysiert und die Höchst.
#                                 #temperatur von morgen ermittelt


with urlopen(WDR) as f:
    htmltext = f.read().decode()
heute, morgen = findall("Max: \d+", htmltext)

print("Wie warm wird es?")
# print("Höchsttemperatur heute: ", heute, "°C")
# print("Höchsttemperatur morgen: ", morgen, "°C")


print("Heute: " + heute + "°C")
print("Morgen: " + morgen + "°C")