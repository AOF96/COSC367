from tkinter import *
from tkinter.ttk import * 

window = Tk()

inputTextFrame = Frame(window, relief=SUNKEN)
inputTextFrame.pack(side=TOP, fill=X, padx=9, pady=10)

text_input = StringVar()
text_input_label = Label(inputTextFrame, textvariable=text_input)
text_input_label.pack(side=LEFT)

clear_button = Button(inputTextFrame, text='Clear', command=lambda: clear_text())
clear_button.pack(side=RIGHT)

keyboard_levels = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

keyboard_frame_container = Frame(window)
keyboard_frame_container.pack(side="right", padx=10, pady=10)

keyBoardFrame = Frame(keyboard_frame_container, borderwidth=4, relief=RAISED)

for level in keyboard_levels:
    keyLine = Frame(keyBoardFrame)
    for char in level:
        char_button = Button(keyLine, text=char, width = 5, command=lambda x=char: addChar(x))
        char_button.pack(side=LEFT)
    keyLine.pack(side=TOP, padx=2, pady=2)
keyBoardFrame.pack()

def addChar(charToAdd):
    text_input.set(text_input.get() + charToAdd)
    
def clear_text():
    text_input.set("")

window.mainloop()