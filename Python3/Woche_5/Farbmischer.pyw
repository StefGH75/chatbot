from tkinter import *

fenster = Tk()

def farbe():
    try:
        label.config(bg=entry.get())
    except Tk.TcLError:
        label.config(text="Ungültiger Farbcode", bg="white")

label = Label(fenster, width=25, height=8)

entry = Entry(fenster,font=("Arial", 12))
button = Button(fenster, font=("Arial", 12), text="Farbe zeigen", command=farbe)

label.pack()
entry.pack()
button.pack()

fenster.mainloop()

#Skript Lösung: 
# from tkinter import * 

# def farbe_zeigen(): 
#     label.config(bg=eingabe.get()) #1 
    
# # Widgets 
# fenster = Tk() 
# label = Label(master=fenster, width=25, height=8) 
# eingabe = Entry(master=fenster, width=8)

# button = Button(master=fenster, text='Farbe zeigen', command=farbe_zeigen)

# # Layout 
# label.pack() 
# eingabe.pack(side=LEFT) 
# button.pack(side=LEFT) 
# fenster.mainloop()