from tkinter import *
from _csv import writer
import time
import random

class Screen(object):
    def __init__(self, dist, width):
        """Object constructor initialising all attributes."""
        self.master = Tk()
        self.count = 0
        self.repetitions = 4
        self.width = 700
        self.height = 700
        self.center = self.width / 2
        self.randomDistances = random.sample(dist, len(dist))
        self.randomWidths = random.sample(width, len(width))
        self.started = False
        self.green = 1
        self.widths =[]
        self.distances =[]
        

    def initiate(self):
        """Initiates lines of a random width and height."""
        self.c = Canvas(self.master, width=self.width, height=self.height)
        self.c.pack()
        for distance in self.randomDistances:
            self.distances += [distance] * self.repetitions
        for width in self.randomWidths:
            self.widths += [width] * self.repetitions
        self.createLines()


    def createLines(self):
        """Creates new lines of a random width and height once the user has 
        clicked the correct position on the screen"""
        total = self.distances[self.count] + self.widths[self.count]
        margin = (self.width - total) / 2
        left = margin+self.widths[self.count]
        rightTop = margin+self.distances[self.count]
        right = margin+self.widths[self.count]+self.distances[self.count]
        if self.started == False:
            self.time = time.time()
            self.c.create_rectangle(margin, 0, left,self.height, tag="left", fill="green", outline="green")
            self.c.create_rectangle(rightTop, 0, right,self.height, tag="right", fill="blue", outline="blue")
            self.c.tag_bind("left", "<ButtonPress-1>", self.leftClick)
            self.c.tag_bind("right", "<ButtonPress-1>",  self.rightClick)
        else:
            self.c.coords("left", margin, 0,left, self.height)
            self.c.coords("right", rightTop, 0, right, self.height)

    
    def leftClick(self, dummy):
        """Function that gets called once the user has clicked the left line and 
        logs time if it's green"""
        self.started = True
        if self.count >= len(self.distances) -1:
            print("You made it to the end! Check your result on the new generated file 'result.txt'")
            self.master.destroy()
            return
        if self.green == 1:
            self.recordTime()
            self.count +=1
            self.green = 0
            self.c.itemconfigure("left", fill="blue", outline='blue')
            self.c.itemconfigure("right", fill="green", outline='green')
            self.createLines()
            
            return
        else:
            return
    
    
    def rightClick(self, dummy):
        """Function that gets called once the user has clicked the right line and 
        logs time if it's green"""        
        self.started = True
        self.recordTime()
        if self.count >= len(self.distances) -1:
            print("You made it to the end! Check your result on the new generated file 'result.txt'")
            self.master.destroy()
            return
        if self.green == 0:
            self.c.itemconfigure("right", fill="blue", outline='blue')
            self.c.itemconfigure("left", fill="green",outline='green')
            self.green = 1
            self.count +=1
            self.createLines()
            
            return
        else:
            return

    
    def recordTime(self):
        """Records the time the user takes to reach a target and saves it into a 
        generated file called result.txt"""
        log = ["User", self.distances[self.count], self.widths[self.count],  self.count % self.repetitions, time.time() - self.time]
        self.time = time.time()
        with open("result.txt", 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(log)


dist = [64, 128, 256, 512]
width = [4, 8, 16, 32]
board = Screen(dist,width)
board.initiate()
board.master.mainloop()
