import math

class Line:
    def __init__(self, xs, ys, walls, r, Can):
        super().__init__()
        self.id = None
        self.canvas = Can
        self.xstart = xs
        self.ystart = ys
        self.walls = walls

        #end points
        self.px = None
        self.py = None
        self.r = r
        self.slope = math.tan(math.radians(90 - r))
        self.b = self.ystart - (self.slope*self.xstart)

    #find where the lines collide
    #TODO make sure that it picks the closet line for collisoins
    def find_end(self):
        for wall in self.walls:
            #first line
            x1 = wall[0]
            y1 = wall[1]
            x2 = wall[2]
            y2 = wall[3]

            #second line
            # if 0 < self.r < 180 :
            #     x3 = 0
            #     y3 = self.ystart - (self.slope*self.xstart) #has to refind the b location
            #     x4 = self.xstart
            #     y4 = self.ystart

            # else:
            x4 = 0
            y4 = self.ystart - (self.slope*self.xstart) #has to refind the b location
            x3 = self.xstart
            y3 = self.ystart
            

            den = (x1 - x2)* (y3 - y4) - (y1 - y2)*(x3 - x4)
            if den != 0:
                t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3-x4)) /den
                u = ((x1 - x2)*(y1 - y3) - (y1 - y2)*(x1-x3)) /den
                # print(t)
                # print(u)
                
                #check if lines are going left or right
                if 0 < self.r < 180 :
                    if 0< t < 1 and 0 > u:
                        self.px = x1 + t*(x2 - x1)
                        self.py = y1 + t*(y2 - y1)
                else:
                    if 0< t < 1 and 0 < u:
                        self.px = x1 + t*(x2 - x1)
                        self.py = y1 + t*(y2 - y1)
            
                


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


# def test():
#     test = Line(10, 10, [], 60, 10)
#     print(test.slope)
#     print(test.b)
#     print("")
#     test.find_end()
#     test.draw_line()

# test()

    