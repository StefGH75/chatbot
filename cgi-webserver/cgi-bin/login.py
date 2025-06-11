#! /usr/bin/env python3                            

#----------------------------------------------------
# Dateiname:  login.py 
# CGI-Skript, das eine Anfrage mit Variablen
# bearbeitet
#
# Autor: Michael Weigend
# Python für Studium und Ausbildung
# Kapitel 16
# Letzte Änderung: 21.2.2022
#----------------------------------------------------
# import cgi

#!/usr/bin/env python3
import os
from urllib.parse import parse_qs

HTML = '''<html>
  <head>
    <title> Begrüßung </title>
  </head>
  <body>
    <h3>Herzlich willkommen, {}!</h3>
  </body>
</html>'''

# CGI-Header mit Leerzeile danach!
print("Content-Type: text/html; charset=utf-8\n")

# Query-Parameter auslesen
query_string = os.environ.get("QUERY_STRING", "")
params = parse_qs(query_string)
name = params.get("name", ["Gast"])[0]

print(HTML.format(name))

