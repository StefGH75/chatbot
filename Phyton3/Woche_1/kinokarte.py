print ("Willkommen im Kino! Bitte geben Sie ihr Alter an")
alter = int(input("Alter: "))
if alter < 18:
    print("Dein Ticket kostet 5,00€")
else:
    print("Dein Ticket kostet 8,50€")
print("Viel Spaß!")