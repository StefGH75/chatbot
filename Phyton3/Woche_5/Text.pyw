from tkinter import Tk, Text, WORD

fenster = Tk()
text = Text(master=fenster, width=30, height=5, wrap =WORD, font=("Arial", 10)) #wrap=Zeilenumbruch nach letztem Wort
text.pack()
fenster.mainloop()