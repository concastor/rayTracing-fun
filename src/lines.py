from line import Line

#population class for lines
class Lines:
    def __init__(self, size, canvas, walls, x, y, rot):
        super().__init__()
        self.x = x
        self.y = y
        self.can = canvas
        self.size = size
        self.rotation = rot
        self.rotation_step = 360/size
        self.lines = []
        self.walls = walls #might be unnesccary to pass to each line
        self.FOV = int(self.size / 6)

        self.create_pop()
        
    def create_pop(self):
        for i in range(self.FOV):
            tempLine = Line(self.x, self.y, self.walls, self.rotation, self.can)
            self.lines.append(tempLine)
            self.rotation += self.rotation_step
            
    def remove_lines(self):
        for i in self.lines:
            i.remove_line()

    def draw_lines(self, x, y):
        for i in self.lines:
            i.draw_line(x, y)

    def redraw_lines(self, x, y):
        for i in self.lines:
            i.redraw_line(x, y)

    def get_distances(self):
        temp = []
        for i in self.lines:
            temp.append(i.distance)
        return temp