from lines import Lines

class Orb:
    def __init__(self, x, y, C, W, walls):
        super().__init__()
        
        self.win = W
        self.can = C
        self.id = None
        self.x = x
        self.y = y
        self.r = 30 #radius of circle
        self.amount = 180  #default bvalue
        self.walls = walls
 
        self.lines = Lines(self.amount, self.can, self.walls, x ,y)

        self.DrawCircle()

    def DrawCircle(self):
        self.id = self.can.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = "black")
        self.lines.draw_lines(self.x, self.y)

    def Redraw(self, x, y):
        self.can.coords(self.id, x - self.r, y - self.r, x + self.r, y + self.r)
        self.lines.redraw_lines(x, y)

    def update_rays(self, x):
        self.can.delete(self.id)
        self.lines.remove_lines()
        self.amount = x
        self.lines = Lines(self.amount, self.can, self.walls, self.x ,self.y)
        self.DrawCircle()

        