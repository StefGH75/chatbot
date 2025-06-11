#! /sys/bin/env python3

#----------------------------------------------------
# Dateiname:  uhrzeit.py 
# Kleines wsgi-Skript, das die aktuelle Uhrzeit liefert.
#
# Python 3 für Sudium und Ausbildung
# Kap. 17
# Michael Weigend 22.11. 2021
#---------------------------------------------------- 
from time import localtime

HTML = '''<html>
<body>
<head>
    <title>Uhrzeit</title>
<head>
<h1>Die Uhrzeit</h1>
<p>
    Es ist {} Uhr {}.
</p>
</body>
</html>'''                                           #1

def uhrzeit():
    zeit = localtime()
    return HTML.format(zeit.tm_hour, zeit.tm_min)    #2


def application(environ, start_response):            #3
    if environ['PATH_INFO'] == '/uhrzeit':           #4
        status = '200 OK'                            #5
        content = uhrzeit()                          #6
    else:
        status = '404 NOT FOUND'                     #7       
        content = 'Seite nicht gefunden.'
    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length',
                         str(len(content)))]         #8
    start_response(status, response_headers)         #9
    return ( content.encode('utf8'), )                    #10

if __name__ == '__main__':                           #11
    from wsgiref.simple_server import make_server    #12
    port = 8000                                      #13
    httpd = make_server('', port, application)       #14
    print('Serving on port {}...'.format(port))
    httpd.serve_forever()                            #15

#1: Das ist ein HTML-Formatstring mit zwei Platzhaltern {}, die später durch
#Zahlen ersetzt werden. Er definiert die Webseite, die an den Client gesendet
#werden soll.
#2: Die Funktion ermittelt zunächst die lokale Uhrzeit als Zeittupel, formatiert
#dann den HTML-Formatstring, indem sie die Platzhalter durch Zahlen für die
#Stunde und die Minute ersetzt und gibt anschließend den kompletten HTML-
#Text zurück.
#3: Das Applikationsobjekt ist die Funktion application(). Der Name der Funktion
#wird in Zeile #13 dem HTTP-Server mitgeteilt.
#4: Der Dictionary-Eintrag environ['PATH_INFO'] ist die Pfadangabe des URLs,
#der vom Client an den HTTP-Server gesendet worden ist. Wenn dieser Pfad
#/uhrzeit lautet, wird in der folgenden if-Klausel dafür gesorgt, dass eine Webseite
#mit der Uhrzeit an den Client gesendet wird.
#5: Das HTTP-Paket, das später zurückgesendet wird, enthält auch eine
#Statusangabe. Der Status »200 OK« signalisiert, dass die Anfrage an den HTTP-
#Server ordnungsgemäß bearbeitet werden kann.
#6: Der Inhalt der Webseite wird durch einen Aufruf der Funktion uhrzeit()
#berechnet.
#7: Falls der URL der Anfrage des Clients an den HTTP-Server nicht mit /uhrzeit
#endet, wird eine Fehlermeldung erzeugt.
#8: Hier wird eine Liste von zwei Tupeln zusammengestellt, die die Daten für die
#Kopfzeile (Header) der Antwort an den Client spezifiziert: Typ und Länge des
#zurückgesendeten Inhalts. In diesem Fall wird ein HTML-Dokument zurückgegeben.
#9: Die Funktion, die im zweiten Argument übergeben worden ist, wird
#aufgerufen. Sie erzeugt den Kopf der Antwort an den Client. Das erste Argument
#des Aufrufs ist die Statusmeldung des HTTP-Servers, und das zweite Argument
#ist eine Liste aus zwei Tupeln, die Typ und Länge des Inhalts beschreiben.
#10: Die Funktion liefert eine Liste mit einem Bytestring mit der dynamisch 
# berechneten HTML-Seite.
#11: Nur wenn die Programmdatei direkt aufgerufen wird, wird der folgende
#Anweisungsblock ausgeführt. Dann wird ein HTTP-Server gestartet, der das
#Applikationsobjekt, die Funktion application(), verwendet. Wenn das Modul von
#einem anderen Programm importiert wird, wird dieser Block nicht ausgeführt.
#12: Der HTTP-Server soll Port 8000 verwenden.
#13: Hier wird ein HTTP-Server generiert und mit der Funktion application() als
#Applikationsobjekt verbunden.
#14: Der HTTP-Server wird gestartet.