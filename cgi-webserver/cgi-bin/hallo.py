#! /usr/bin/env python3

#----------------------------------------------------
# Dateiname:  hallo.py 
# CGI-Skript, das "Hallo" ausgibt
#
# Autor: Michael Weigend
# Python für Studium und Ausbildung
# Kapitel 17
# Letzte Änderung: 21.2.2022
#----------------------------------------------------
HTML = """Content-type: text/html; char-set=utf-8

<html>
  <body>
    Hallo!
  </body>
</html>"""                                              #1
    
print(HTML)
