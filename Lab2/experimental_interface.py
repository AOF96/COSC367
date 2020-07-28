from tkinter import *
from tkinter.ttk import * 
import csv
from csv import writer
import random
import time


window = Tk()

inputTextFrame = Frame(window)
inputTextFrame.pack(side=TOP, fill=X, padx=9, pady=10)

text_input = StringVar()
text_input_label = Label(inputTextFrame, textvariable=text_input)
text_input_label.pack(side=LEFT)
text_input.set("Press a key to begin!")


objective = []
keys = list("qwertyuiopasdfghjklzxcvbnm")
random.shuffle(keys)
chosenKeys = keys[0:5]
for i in range(6):
    random.shuffle(chosenKeys)
    objective += ''.join(str(e) for e in chosenKeys)



keyboard_frame_container = Frame(window)
keyboard_frame_container.pack(side="right", padx=10, pady=10)

keyBoardFrame = Frame(keyboard_frame_container, borderwidth=4, relief=RAISED)


def randomize_keyboard():
    '''Randomizes the locations of characters in the keyboard '''
    
    chars = list("qwertyuiopasdfghjklzxcvbnm")
    random.shuffle(chars)
    
    return [chars[0:10], chars[10:19], chars[19:26]]

def make_keyboard():
    '''Creates a new keyboard with randomized characters once the user has 
    selected the correct objective'''
    global keyBoardFrame
    global keys
    
    for key in keyBoardFrame.winfo_children():
            key.destroy()
    
    keyboard_levels = randomize_keyboard()        
    for level in keyboard_levels:
        keyLine = Frame(keyBoardFrame)
        for char in level:
            button_frame = Frame(keyLine, height=32, width=32)
            button_frame.pack_propagate(0)
            char_button = Button(button_frame, text=char, width = 5, command=lambda x=char: addChar(x))
            button_frame.pack(side=LEFT)
            char_button.pack(side=LEFT)
        keyLine.pack(side=TOP, padx=2, pady=2)
    keyBoardFrame.pack()

make_keyboard()

def log_result(file, element):
    '''Writes into a CSV file the time the user took to click on a objective letter'''    
    with open(file, 'a+', newline='') as write_object:
        csv_writer = writer(write_object)
        csv_writer.writerow(element)


index = 0
typee="dynamic"
start=None
counts = {}
results = []


def addChar(charToAdd):
    '''Sets the objective character on the screen and updates it once the user has
    clicked that character'''
    global index 
    global objective
    global text_input
    global dynamic
    global keys
    global start
    global results
    text_input.set(text_input.get() + charToAdd)
    
    if (start == None):
            text_input.set(objective[index])
            start = time.time()
            make_keyboard()
            
    if charToAdd == objective[index]:
        counts[charToAdd] = counts.get(charToAdd,0) + 1
        result = (["User", typee, charToAdd, counts.get(charToAdd), (time.time() - start) * 1000])
        log_result("experiment_" + typee + "_log.txt", result)
        start = time.time()
        if index == len(objective) -1:
            text_input.set("You made it to the end!")
            return
        index += 1
        text_input.set(objective[index])
        if typee == 'dynamic':
            make_keyboard()
    
#def display_target():
    #while n < 0:
    #for objective in target_letters:
        #text_input.set()
        
def main():
    global index
    global objective
    global text_input
    
    for i in range(0,2):
        index = 0
        text_input.set(objective[index])
        make_keyboard()
        index = 0

window.mainloop()