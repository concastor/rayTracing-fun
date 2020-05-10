from line import Line

#population class for lines
class Lines:
    def __init__(self, size, canvas, walls, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.can = canvas
        self.size = size
        self.rotation = 0
        self.rotation_step = 360/size
        self.lines = []
        self.walls = walls #might be unnesccary to pass to each line
        self.create_pop()

    def create_pop(self):
        for i in range(self.size):
            tempLine = Line(self.x, self.y, self.walls, self.rotation, self.can)
            self.lines.append(tempLine)
            self.rotation += self.rotation_step
            


    def draw_lines(self, x, y):
        for i in self.lines:
            i.draw_line(x, y)

    def redraw_lines(self, x, y):
        for i in self.lines:
            i.redraw_line(x, y)
