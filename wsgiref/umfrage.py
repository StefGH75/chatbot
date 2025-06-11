#! /usr/bin/env python3                            

#----------------------------------------------------
# Dateiname:  umfrage.py 
# WSGI-Skript, das eine Abstimmung organisiert
#
# Python 3 für Studium und Ausbildung
# Kap. 17
# Michael Weigend 19.11.2021
#----------------------------------------------------
import pickle
from urllib.parse import parse_qs

PATH = 'poll.data'

VOTE = '''
<html>
<head>
  <title> Umfrage </title>
</head>
<body>
<h2>Sind Studiengeb&uuml;hren sinnvoll?</h2>
Was ist Ihre Meinung? <br/>
<form method="post" action="/evaluate">
<input type="radio" name="poll" value="ja"/> Ja<br/>
<input type="radio" name="poll" value="nein"/> Nein<br/>
<input type="radio" name="poll" value="jein" checked="checked"/> Wei&szlig; nicht<br/><br/>
<input type="submit" value="Meinung abgeben"/>
</form>
</body>
</html>'''

RESULT = '''
<html>
  <head>
    <title>Ergebnis</title>
  </head>
  <body>
    <h2>Zwischenergebnis</h2>
    Frage: Sind Studiengeb&uuml;hren sinnvoll?<br/>
    Ja: {}<br/>
    Nein: {}<br/>
    Wei&szlig; nicht: {}<br/>
  </body>
</html>'''


def evaluate(environ):
    try:
        with open(PATH, 'rb') as f:
            d = pickle.load(f)
    except:
        d = {'ja': 0, 'nein': 0, 'jein': 0}

    try:
        length = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        length = 0

    body = environ['wsgi.input'].read(length).decode()
    params = parse_qs(body)
    p = params.get('poll', ['jein'])[0]

    if p in d:
        d[p] += 1

    with open(PATH, 'wb') as f:
        pickle.dump(d, f)

    return RESULT.format(d['ja'], d['nein'], d['jein'])


def application(environ, start_response):
    path = environ.get('PATH_INFO', '/')

    if path == '/poll':
        status = '200 OK'
        content = VOTE
    elif path == '/evaluate':
        status = '200 OK'
        content = evaluate(environ)
    else:
        status = '404 NOT FOUND'
        content = 'Seite nicht gefunden.'

    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(content)))
    ]
    start_response(status, response_headers)
    return [content.encode('utf8')]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    port = 8000
    httpd = make_server('', port, application)
    print(f"Serving on port {port}...")
    httpd.serve_forever()