#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  hello.py 
# Minimales wsgi-Skript
#
# Python 3 für Studium und Ausbildung
# Kap. 17
# Michael Weigend 22.11. 2021
#----------------------------------------------------                                     
from wsgiref.simple_server import make_server

def app(environ, start_response):                              #1
    start_response('200 OK', [('Content-Type', 'text/html')])  #2
    return [b'Hallo!']                                         #3


httpd = make_server("", 8000, app)
print('Serving on port 8000...')
httpd.serve_forever()
