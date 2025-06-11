from PIL import Image

FILE = "SM_2.jpg"
im = Image.open(FILE) #image-Objekt wird erzeugt, modus hängt vom Dateityp ab, In diesem Fall RGB, da eine jpg-Datei verwendet wird
width, height = im.size #Höhe und Breite des Bildes werden in Pixeln ermittelt
for x in range(width): #in den beiden Schleifen werden alle Koordinaten durchlaufen, x durchläuft alle Zahlen von 0-width
    for y in range(height): #y alle Zahlen von 0 bis height
        pixel = im.getpixel((x, y)) #Pixel an der Position x, y gelesen (ein Tupel aus drei zahlen)
        if sum(pixel) < 350: #wenn die Helligkeit unter 350 liegt
            im.putpixel((x, y), (200, 0, 0)) #wird Pixel durch Tupel ersetzt, das einen dunkelroten Farbton entspricht
        else:
            im.putpixel((x, y), (200, 200, 255)) #ansonsten durch hellblauen Farbton
im.show() #Bidl wird in einem Viewer-Fenster auf Bildschirm gezeigt

# #effizientere Methode:
# from PIL import Image
# FILE = "SM_2.jpg"
# im = Image.open(FILE)
# list_im = list(im.getdata()) #aus Image-Objekt wird Liste von 3-Tupeln ezeugt, jedes Tupel repräsentiert ein Pixel
# list_new_im = [(200, 0, 0) if sum(pixel) < 350 else (200, 200, 255) for pixel in list_im] #mit dieser List
#         #Comprehension wird aus ursprünglicher Liste eine neue Liste. jedes Element ist entweder dunkelrot oder hellblau
# new_im = Image.new(mode=im.mode, size=im.size) #neues Image-Objekt erstellt (gleiche Größe und gleicher Modus)
# new_im.putdata(list_new_im) #neue Bilddaten werden in das neue image-Objekt eingefügt
# new_im.show() #Bild im Viewer-Fenster angezeigt