import tkinter as tk
from tkinter import *
from time import sleep
from orb import Orb
import random as rand

class Window:
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("RAY Tracing ON")
        self.window.geometry("1600x850")
        self.walls = []

        #function related to left frame of GUI
        self.leftFrame = Frame(self.window, width = 800)
        self.leftFrame.pack(side=LEFT)

        self.rayCan = Canvas(self.leftFrame, width = 800, height = 800)
        self.rayCan.pack()

        self.buttonFrame = Frame(self.leftFrame, bg='grey', width = 800)
        self.buttonFrame.pack(fill = X)
        
        self.Draw_walls()
        self.add_buttons()

        self.rayCan.bind('<Motion>', self.Mouse_move) #mouse move event
        self.window.bind('<a>', lambda x: self.Left_press()) #key press event
        self.window.bind('<d>', lambda y: self.Right_press()) #key press event

        #functions related to Right side of binder
        self.rightFrame = Frame(self.window, width = 800)
        self.rightFrame.pack(side=LEFT)

        self.wallCan = Canvas(self.rightFrame, width = 800, height = 800)
        self.wallCan.pack()

        self.orb = Orb(800/2, 800/2, self.rayCan, self.wallCan, self.window, self.walls)


    def add_buttons(self):
        explainLbl = Label(self.buttonFrame, bg = 'grey', text = "Select how many rays to emit")
        explainLbl.pack(side=LEFT, padx=10, pady = 10)

        thirtyB = Button(self.buttonFrame, text='30', width = 10, command=self.callback30 )
        thirtyB.pack(side=LEFT, padx=10, pady = 10)

        sixtyB = Button(self.buttonFrame, text='60', width = 10, command=self.callback60 )
        sixtyB.pack(side=LEFT, padx=10, pady = 10)

        ninteyB = Button(self.buttonFrame, text='90', width = 10, command=self.callback90 )
        ninteyB.pack(side=LEFT, padx=10, pady = 10)

        oneeightyB = Button(self.buttonFrame, text='180', width = 10, command=self.callback180)
        oneeightyB.pack(side=LEFT, padx=10, pady = 10)

        threesixB = Button(self.buttonFrame, text='360', width = 10, command=self.callback360)
        threesixB.pack(side=LEFT, padx=10, pady = 10)

        seventwentB = Button(self.buttonFrame, text='720', width = 10, command=self.callback720)
        seventwentB.pack(side=LEFT, padx=10, pady = 10)

    #functions for related buttons
    def callback30(self):
        self.orb.update_rays(30)
    
    def callback60(self):
        self.orb.update_rays(60)

    def callback90(self):
        self.orb.update_rays(90)

    def callback180(self):
        self.orb.update_rays(180)

    def callback360(self):
        self.orb.update_rays(360)

    def callback720(self):
        self.orb.update_rays(720)

    #event handlers
    def Mouse_move(self, event):
        self.window.after(15, self.orb.Redraw(event.x, event.y))

    def Left_press(self):
        self.orb.rotate_left()

    def Right_press(self):
        self.orb.rotate_right()

    def Draw_walls(self):
        #basic border walls
        self.create_border(-50,0,800,0)
        self.create_border(-50,800,850,800)
        self.create_border(800,850,800,-50)
        self.create_border(1,850,0,-50)

        for wall in range(5):
            points = []
            for point in range(4):
                points.append(rand.randint(0,800))
            self.create_border(points[0],points[1],points[2],points[2],)    
            
    def create_border(self, x1, y1, x2, y2):
        self.rayCan.create_line(x1, y1, x2, y2, width = 3)
        self.walls.append([x1, y1, x2, y2])


def main():
    win = Window()
    win.window.mainloop()


    
#run the fucntion
main()