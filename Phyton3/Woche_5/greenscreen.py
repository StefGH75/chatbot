from PIL import Image
BACKGROUND_FILE = "landschaft.jpg"
PERSON_FILE = "person.jpg"
F = 0.9 #Faktor, der angibt, wie grün ein Pixel sein muss, damit es als ausgeblendeter Bereich gewertet wird. Je
#größer F ist, desto größer muss der Wert des grünen Farbkanals gegenüber den anderen Farbkanälen sein
im_background = Image.open(BACKGROUND_FILE) #Hintergrundbild geladen
im_person = Image.open(PERSON_FILE) 
list_person = list(im_person.getdata()) #aus Image-Objekt werden zeilenweise die Pixel ausgelesen und eine lange Liste aus 3-Tupeln gewonnen
list_mask = [0 if g > F *(r + b) else 255 for r, g, b in list_person] #list comprehension beschreibt eine Liste
#aus Zahlen, die entweder 0 oder 255 sind. Aus Pixeln des Bilds mit Person vor dem grünen Hintegrund werden hier
#die Pixel der Maske ermittelt. Wenn das Pixel des Personenbildes grün ist, wird Pixel der Maske schwarz, sonst
#wird es weiß
im_mask = Image.new(mode="L", size=im_person.size) #es wird ein ganzes schwarz-weiß Bild erstellt, gleichen Maße
im_mask.putdata(list_mask) #in das Bild werden die Daten (0-255) aus liste_mask eingefügt
im_background.paste(im_person, box=(100,10), mask=im_mask) #mithilfe der Maske wird Bild in Landschaftsbild 
#eingefügt. Die obere linke Ecke des eingefügten Bilds ist an Position (100,10) in der Geometrie des Landschafts
#bildes
im_background.show()