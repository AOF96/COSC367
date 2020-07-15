from tkinter import *
from tkinter.ttk import * 
window = Tk()

v_scrollbar = Scrollbar(window)
v_scrollbar.grid(row=0, column=1)
h_scrollbar = Scrollbar(window, orient=HORIZONTAL)
h_scrollbar.grid(row=1, column=0)


text_window = Text(window, width=24, height=10, yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
text_window.grid(row=0, column=0)
text_window.insert(INSERT, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

v_scrollbar.config(command=text_window.yview)
h_scrollbar.config(command=text_window.xview)

window.mainloop()