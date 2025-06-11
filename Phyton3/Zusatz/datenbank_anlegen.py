import sqlite3
verbindung = sqlite3.connect("uni.db") #Im Projektordner wird neue Datei mit dem Namen 'uni.db' angelegt.
#In dieser Datei wird neue Datenbank gespeichert. Das neu geschaffene Objekt verbindung repräsentiert diese Datenbank
c = verbindung.cursor() #neues Cursor-Objekt für den Zugriff auf die Datenbank erzeugt
befehl = """CREATE TABLE student(matnr INT, name VARCHAR(50))""" 
#Variable befehl erhält langen String mit einem SQL-Befehl. Hier wird ein langer String 
# (mit drei Anführungszeichen) verwendet, damit der SQL-Befehl in strukturierter Form mit 
# mehreren Zeilen aufgeschrieben werden kann.
c.execute #Der SQL-Befehl wird ausgeführt und eine neue Tabelle der Datenbank
#hinzugefügt. Wegen dieses Befehls kann das Programm nur einmal erfolgreich ausgeführt werden.

#neues Tupel mit Matrikelnummer und Name in die Tabelle student eingefügt:
c.execute("INSERT INTO student VALUES(21419, 'Jan');") 
c.execute("INSERT INTO student VALUES(27335, 'Kim');")
c.execute("INSERT INTO student VALUES(26112, 'Tina');")

verbindung.comit() #Alle Änderungen der Datenbank werden gespeicher
c.close() #cursor wird geschlossen und steht nun nicht mehr zur Verfügung
verbindung.close() #Verbindung zur Datenbank wird geschlossen
