from tkinter import *
from tkinter.ttk import * 
master = Tk()
c = Canvas(master, width=500, height=500)
c.pack()
c.create_rectangle(50, 0, 100, 500, fill='blue')
c.create_rectangle(300, 0, 350, 500, fill='green')

master.mainloop()