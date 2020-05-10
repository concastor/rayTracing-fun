from lines import Lines

class Orb:
    def __init__(self, x, y, C, W, walls):
        super().__init__()
        
        self.win = W
        self.can = C
        self.id = None
        self.x = x
        self.y = y
        self.r = 30
        self.amount = 180
 

        # self.lines = Line(x, y, walls, 50, self.can)
        # self.lineb = Line(x, y, walls, 180, self.can)
        self.lines = Lines(self.amount, self.can, walls, x ,y)
        self.DrawCircle()

    def DrawCircle(self):
        self.id = self.can.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,fill = "black")
        self.lines
        self.lines.draw_lines(self.x, self.y)
        # self.lineb.draw_line(self.x, self.y)

    def Redraw(self, x, y):
        self.can.coords(self.id, x - self.r, y - self.r, x + self.r, y + self.r)
        self.lines.redraw_lines(x, y)
        # self.lineb.redraw_line(x, y)

        