#! /usr/bin/env python3
# #In der ersten Zeile steht eine Anweisung an das Betriebssystem, welcher
# Interpreter zur Ausführung des Skripts aufgerufen werden soll (Shebang-Zeile).
# Diese Zeile muss mit der Zeichenfolge #! beginnen (Shebang). Dahinter steht
# eine Angabe, welcher Interpreter verwendet werden soll. Wenn Deine Skripte auf
# einem Unix-Rechner laufen, sieht die erste Zeile Deiner CGI-Skripte in der Regel
# so aus wie bei diesem Beispiel. Hier wird der Unix-Befehl env verwendet, der den
# Pfad des Python-Interpreters liefert. Mit env kann das Python-Skript auch
# ausgeführt werden, wenn der genaue Pfad des Python-Interpreters nicht bekannt ist.
#In Windows wird die shebang-Zeile nicht interpretiert, man muss dafür sorgen, dass sie 
#ausgeführt wird
#----------------------------------------------------
# Dateiname:  uhrzeit.py 
# CGI-Skript, das html-Seite mit aktueller Uhrzeit ausgibt
#
# Autor: Michael Weigend
# Python für Studium und Ausbildung
# Kapitel 16
# Letzte Änderung: 21.2.2022
#----------------------------------------------------
print("Content-Type: text/html\n")

SCHABLONE = '''Content-type: text/html; char-set=utf-8

<html>
  <head>
     <title>Uhrzeit</title>
  </head>
  <body>
    <h2>Die aktuelle Uhrzeit </h2>
      Es ist {} Uhr {}.
  </body>
</html>'''                                          #1
    
from time import localtime
zeit = localtime()                                  #2
print(SCHABLONE.format(zeit.tm_hour, zeit.tm_min))  #3      
