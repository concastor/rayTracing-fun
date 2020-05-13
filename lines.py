from line import Line

#population class for lines
class Lines:
    def __init__(self, size, canvas, walls, x, y, rot):
        super().__init__()
        self.x = x
        self.y = y
        self.can = canvas
        self.size = size
        self.rotation = rot  #change this to rotate
        self.leftRotation = rot
        self.rotation_step = 360/size
        self.lines = []
        self.walls = walls #might be unnesccary to pass to each line
        self.FOV = int(self.size / 6)
        self.create_pop()

    def create_pop(self):
        if self.FOV is not None:
            for i in range(self.FOV):
                tempLine = Line(self.x, self.y, self.walls, self.rotation, self.can)
                self.lines.append(tempLine)
                self.rotation += self.rotation_step
        else:
            for i in range(self.size):
                tempLine = Line(self.x, self.y, self.walls, self.rotation, self.can)
                self.lines.append(tempLine)
                self.rotation += self.rotation_step


    def rotate_left(self):
        self.rotation += self.rotation_step
        self.lines[0].relocate(self.rotation)
        self.lines.insert(self.FOV, self.lines.pop(0))

    def rotate_right(self):
        self.leftRotation -= self.rotation_step
        self.lines[-1].relocate(self.leftRotation)
        self.lines.insert(0, self.lines.pop())

    def remove_lines(self):
        for i in self.lines:
            i.remove_line()

    def draw_lines(self, x, y):
        for i in self.lines:
            i.draw_line(x, y)

    def redraw_lines(self, x, y):
        self.x = x
        self.y = y
        for i in self.lines:
            i.redraw_line(x, y)
