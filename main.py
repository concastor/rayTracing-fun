import tkinter as tk
from tkinter import *
from time import sleep
from orb import Orb

class Window:
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("RAY Tracing ON")
        self.window.geometry("800x850")
        self.walls = []

        #create canvas for drawing
        self.can = Canvas(self.window, width = 800, height = 800)
        self.can.pack()
        
        #create button frames and buttons
        self.buttonFrame = Frame(self.window, bg='grey', width = 800)
        self.buttonFrame.pack(fill = X)
        
        self.Draw_walls()
        self.orb = Orb(800 / 2, 800 / 2, self.can, self.window , self.walls)

        #add the bottom buttons
        self.add_buttons()

    

        #event binder
        self.can.bind('<Motion>', self.Mouse_move) #mouse move event



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

    def Mouse_move(self, event):
        self.window.after(15, self.orb.Redraw(event.x, event.y))

    def Draw_walls(self):
        #basic border walls
        self.can.create_line(0,0,800,0)
        self.can.create_line(0,800,800,800)
        self.can.create_line(800,800,800,0)
        self.can.create_line(0,800,0,0)

        self.can.create_line(150,60,500,700)
        self.can.create_line(80,30,700,200)
        
        self.walls.append([0,0,800,0])
        self.walls.append([0,800,800,800])
        self.walls.append([800,800,800,0])
        self.walls.append([0,800,0,0])

        self.walls.append([150,60,500,700])
        self.walls.append([80,30,700,200])


def main():
    win = Window()
    win.window.mainloop()


    
#run the fucntion
main()