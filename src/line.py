import math

class Line:
    def __init__(self, xs, ys, walls, r, Can):
        super().__init__()
        self.id = None
        self.canvas = Can
        self.xstart = xs
        self.ystart = ys
        self.walls = walls

        self.distance = 0

        #end points
        self.px = None
        self.py = None
        self.r = r
        
        self.angle = 90 + r
        if self.r == 0 or self.r == 180:
            self.slope = None
        else:
            self.slope = math.tan(math.radians(self.angle))
            self.b = self.ystart - (self.slope*self.xstart)


    #find where the lines collide
    def find_end(self):
        mini = math.inf
        for wall in self.walls:
            #first line
            x1 = wall[0]
            y1 = wall[1]
            x2 = wall[2]
            y2 = wall[3]
            
            if self.slope is None:
                x4 = self.xstart
                y4 = self.ystart + 10
                
            else:
                x4 = 0
                y4 = self.ystart - (self.slope*self.xstart) #has to refind the b location
                
            x3 = self.xstart
            y3 = self.ystart
            

            den = (x1 - x2)* (y3 - y4) - (y1 - y2)*(x3 - x4)
            if den != 0:
                t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3-x4)) /den
                u = ((x1 - x2)*(y1 - y3) - (y1 - y2)*(x1-x3)) /den

                px = math.inf
                py = math.inf
                
                #check if lines are going left or right
                if 0 <= self.r < 180 :
                    if 0< t < 1 and 0 > u:
                        px = x1 + t*(x2 - x1)
                        py = y1 + t*(y2 - y1)
                else:
                    if 0< t < 1 and 0 < u:
                        px = x1 + t*(x2 - x1)
                        py = y1 + t*(y2 - y1)
                
                #calculate distance between points
                distance = math.sqrt(((self.xstart - px) ** 2) + ((self.ystart - py) ** 2))

                #check if its the smallest
                if distance < mini:
                    self.px = px
                    self.py = py
                    mini = distance
                    self.distance = int(mini) / 2 
                    if self.distance > 400: self.distance = 400


    def draw_line(self, x, y):
        self.xstart = x
        self.ystart = y
        self.find_end()
        self.id = self.canvas.create_line(self.xstart,self.ystart, self.px, self.py)

    def redraw_line(self, x, y):
        self.xstart = x
        self.ystart = y
        self.find_end()
        self.canvas.coords(self.id, x,y,self.px, self.py)

    def remove_line(self):
        self.canvas.delete(self.id)

    