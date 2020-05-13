from lines import Lines

class Orb:
    def __init__(self, x, y, C,C2, W, walls):
        super().__init__()
        
        self.win = W
        self.rayCan = C
        self.wallCan = C2
        self.id = None
        self.x = x
        self.y = y
        self.rotation = 360
        self.r = 10 #radius of circle
        self.amount = 180  #default bvalue
        self.walls = walls
 
        self.lines = Lines(self.amount, self.rayCan, self.walls, x ,y, self.rotation)

        self.DrawCircle()

    def rotate_left(self):
        self.lines.rotate_left()

        

    def rotate_right(self):
        self.lines.rotate_right()
        # self.lines = Lines(self.amount, self.rayCan, self.walls, self.x , self.y, self.rotation)

    def DrawCircle(self):
        self.id = self.rayCan.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = "black")
        self.lines.draw_lines(self.x, self.y)
        self.wallCan.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = "black")

    def Redraw(self, x, y):
        self.x = x
        self.y = y
        self.rayCan.coords(self.id, x - self.r, y - self.r, x + self.r, y + self.r)
        self.lines.redraw_lines(x, y)

    def update_rays(self, x):
        self.rayCan.delete(self.id)
        self.lines.remove_lines()
        self.amount = x
        self.lines = Lines(self.amount, self.rayCan, self.walls, self.x , self.y, self.rotation)
        self.DrawCircle()

        