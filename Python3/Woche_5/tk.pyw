from tkinter import Tk, Label
fenster = Tk()
fenster.title("Meine GUI")
label = Label(master=fenster, text="Guten Morgen!", font=("Courier", 20), fg="blue", height=2, width=20) #Hier wird ein Objekt vom Typ Label definiert. Das Label wird dem Tk-Objekt zugeordnet und 
                                                    #zeigt den Text "Guten Morgen!" an. 
label.pack() #Das Layout wird festgelegt. Dazu wird die Methode pack() aufgerufen. Alle Widget-Objekte besitzen diese Methode. Der Aufruf sorgt 
            #dafür, dass das Widget in das Master-Widget eingefügt wird
fenster.mainloop()

