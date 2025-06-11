#----------------------------------------------------
# Dateiname:  httpd.py 
# HTTP-Server, der CGI-Skripte verarbeiten kann.
# Die CGI-Skripte müssen in einem Unterverzeichnis des
# Verzeichnisses sein, in dem die Programmdatei des Servers ist.
# Dieses Unterverzeichnis hat den Namen cgi-bin.
#
# Python für Studium und Ausbildung
# Kap. 17
# Michael Weigend 17. 10. 2021
#----------------------------------------------------
# from http.server import HTTPServer, CGIHTTPRequestHandler

# handler_class = CGIHTTPRequestHandler
# handler_class.cgi_directories = ["/cgi-bin"]

# serveradresse = ("", 8000)
# server = HTTPServer(serveradresse, handler_class)
# server.serve_forever()

# from http.server import HTTPServer, CGIHTTPRequestHandler
# serveradresse =("", 8000)                             #1
# server=HTTPServer(serveradresse,
#                   CGIHTTPRequestHandler)              #2
# server.serve_forever()                                #3


from http.server import HTTPServer, CGIHTTPRequestHandler

handler = CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]

server = HTTPServer(("", 8000), handler)
print("Server läuft auf http://localhost:8000")
server.serve_forever()











                    
