class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color, size = 2):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill = fill_color, width = size)
    
class Cell:
    def __init__(self, window = None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    
    def draw(self, x1, y1, x2, y2, color = "black"):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        p1 = Point(self._x1, self._y1)
        p2 = Point(self._x2, self._y1)
        p3 = Point(self._x1, self._y2)
        p4 = Point(self._x2, self._y2)
        
        self._win.draw_line(Line(p1, p3), color)
        self._win.draw_line(Line(p1, p2), color)     
        self._win.draw_line(Line(p2, p4), color)
        self._win.draw_line(Line(p3, p4), color)
    
    def fill(self, color):
        p1 = Point(self._x1, self._y1)
        p2 = Point(self._x2, self._y1)
        p3 = Point(self._x1, self._y2)
        p4 = Point(self._x2, self._y2)
        
        self._win.draw_line(Line(p1, p3), color)
        self._win.draw_line(Line(p1, p2), color)     
        self._win.draw_line(Line(p2, p4), color)
        self._win.draw_line(Line(p3, p4), color)

        p5 = Point((self._x1 + self._x2)/2, self._y1)
        p6 = Point((self._x1 + self._x2)/2, self._y2)
        size = (self._x2 - self._x1)
        self._win.draw_line(Line(p5, p6), color, size)