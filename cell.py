from enum import Enum
import random

class TerrainType(Enum):
    OCEAN = "ocean"
    PLAINS = "plains"
    SWAMP = "swamp"
    DESERT = "desert"
    FOREST = "forest"
    MOUNTAIN = "mountain"

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
        self.up = None
        self.right = None
        self.down = None
        self.left = None
        self.elevation = -50
        self.hot_spot = 0
        self.terrain = TerrainType.OCEAN
        self._win = window

    def explode_r(self, strength):
        reduction = 4
        base = 50
        max = 150
        self.elevation += (strength * base) % max 
        self.up.elevation += strength * base/2 % max
        self.down.elevation += strength * base/2 % max
        self.left.elevation += strength * base/2 % max
        self.right.elevation += strength * base/2 % max
        if strength > 5:
            self.up.explode_r(strength/reduction)
            self.down.explode_r(strength/reduction)
            self.left.explode_r(strength/reduction)
            self.right.explode_r(strength/reduction)

    def draw(self, x1, y1, x2, y2, color = "blue"):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        p1 = Point(self._x1, self._y1)
        p2 = Point(self._x2, self._y1)
        p3 = Point(self._x1, self._y2)
        p4 = Point(self._x2, self._y2)

        self._win._canvas.create_rectangle(x1, y1, x2, y2, fill = color, outline = color)