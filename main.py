import tkinter as tk
from tkinter import *
from time import sleep
from orb import Orb

class Window:
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("RAY Tracing ON")
        self.window.geometry("800x800")
        self.walls = []

        self.can = Canvas(self.window, width = 800, height = 800)
        self.can.pack()

        self.Draw_walls()
        #event binder
        self.window.bind('<Motion>', self.Mouse_move) #mouse move


        self.orb = Orb(800 / 2, 800 / 2, self.can, self.window , self.walls)

    def Mouse_move(self, event):
        self.window.after(30, self.orb.Redraw(event.x, event.y) )

    def Draw_walls(self):
        #basic border walls
        self.can.create_line(0,0,800,0)
        self.can.create_line(0,800,800,800)
        self.can.create_line(800,800,800,0)
        self.can.create_line(0,800,0,0)

        self.can.create_line(150,60,500,700)
        # self.can.create_line(80,30,700,200)
        
        self.walls.append([0,0,800,0])
        self.walls.append([0,800,800,800])
        self.walls.append([800,800,800,0])
        self.walls.append([0,800,0,0])

        self.walls.append([150,60,500,700])
        # self.walls.append([80,30,700,200])


def main():
    win = Window()
    win.window.mainloop()


    
#run the fucntion
main()