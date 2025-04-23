import random
from cell import Cell, TerrainType
import math
import statistics
from color import rgb_to_hex
class Plate:
    def __init__(self, window, size_w, size_h, lat, planet_size = 5, seed = None):
        self._win = window
        self._num_cols = int(size_w)
        self._num_rows = int(size_h)
        self._lat = lat
        self.planet_size = planet_size
        self._cells = []
        self._speed_frame = 1
        self._speed = 10
        self._cell_size = 10
        self.seed = seed
        self.direction = random.randint(1,4)
        if seed == None:
                self.seed = random.seed(seed)
        self.create_cells()
        self.raise_plate()

    
    def create_cells(self):
        self._cells = [[Cell(self._win) for j in range(self._num_rows)] for i in range(self._num_cols)]
        outside = Cell()
        outside.up = outside
        outside.left = outside
        outside.right = outside
        outside.down = outside
        outside.elevation = -150
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                current = self._cells[i][j]
                if i > 0 :
                    current.left = self._cells[i-1][j]
                else:
                    current.left = outside
                if j > 0:
                    current.up = self._cells[i][j-1]
                else:
                    current.up = outside
                if i < self._num_cols - 1:
                    current.right = self._cells[i+1][j]
                else:
                    current.right = outside
                if j < self._num_rows - 1:
                    current.down = self._cells[i][j+1]
                else:
                    current.down = outside
                self._draw_cell(i , j)
        self._win.redraw()

    def _draw_cell(self, i, j, color = "blue"):
        if self._win is None:
            return
        x1 = i*  self._cell_size
        y1 = j * self._cell_size
        x2 = x1 + self._cell_size
        y2 = y1 + self._cell_size
        self._cells[i][j].draw(x1, y1, x2, y2, color)
        self._speed = float('inf')
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        if self._speed_frame % self._speed == 0:
            self._win.redraw()
            self._speed_frame = 1
        else:
            self._speed_frame += 1
    
    def raise_plate(self):
        length = self._num_cols // 1.25
        start_l = int((self._num_cols - length) // 2)
        end_l = int(self._num_cols - start_l)
        height = self._num_rows // 1.25
        start_h = int((self._num_rows - height) // 2)
        end_h = int(self._num_rows - start_h)
        #self._speed = 10000

        for i in range(start_l, end_l):
            for j in range(start_h, end_h):
                current = self._cells[i][j]
                current.elevation = 50
        self.hotspot(5)
        
        for k in range(30):
            self.randomize_elevation()
            self.smooth_elevation()
            self.highspot(start_h, end_h, start_l, end_l)
            
            self.move_hotspots()
            #self.draw_terrain()
            self.draw_elevation()
            self._win.redraw()
        
    
    def highspot(self, start_h, end_h, start_l, end_l):
        i1 = random.randint(int(start_l/2), int(end_l/2) - 1)
        i2 = random.randint(int(start_l/2), int(end_l/2) - 1)
        
        j1 = random.randint(int(start_h/2), int(end_h/2) - 1)
        j2 = random.randint(int(start_h/2), int(end_h/2) - 1)
        i = i1+i2
        j = j1+j2
        current = self._cells[i][j]
        current.elevation += 150

        #if direction <= 2:

            #length = random.randint(self._num_cols//4)
        #destination = 

    def hotspot(self, number):
        for k in range (number):
            i = random.randint(0, self._num_cols - 1)
            j = random.randint(0, self._num_rows - 1)
            current = self._cells[i][j]
            current.elevation += 500
            current.hot_spot = 5

    def randomize_elevation(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                current = self._cells[i][j]
                current.elevation += random.randint(-50, 50)
    
    def smooth_elevation(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                current = self._cells[i][j]
                neighbor_elevation = [current.up.elevation, current.right.elevation, current.down.elevation, current.left.elevation]
                mean = statistics.mean(neighbor_elevation)
                current.elevation = (current.elevation + mean)/2
    
    def move_hotspots(self):
        visited_list = []
        hot_spot_growth = 1.05
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                current = self._cells[i][j]
                if current.hot_spot > 0 and current not in visited_list:
                    strength = random.randint(0,500)
                    if strength <  20:
                        current.explode_r(current.hot_spot)
                        current.hot_spot = 2
                    else:
                        match self.direction:
                            case 1:
                                current.up.left.elevation += strength
                                current.left.elevation += .5 * strength
                                current.up.elevation += .5 * strength
                                current.up.left.hot_spot = current.hot_spot * hot_spot_growth
                                current.hot_spot = 0
                            case 2:
                                current.left.down.elevation += strength
                                current.left.down.hot_spot = current.hot_spot * hot_spot_growth
                                current.left.elevation += .5 * strength
                                current.down.elevation += .5 * strength
                                current.hot_spot = 0
                                visited_list.append(current.left.down)
                            case 3:
                                current.down.right.elevation += strength
                                current.down.right.hot_spot = current.hot_spot * hot_spot_growth
                                current.right.elevation += .5 * strength
                                current.down.elevation += .5 * strength
                                current.hot_spot = 0
                                visited_list.append(current.down.right)
                            case 4:
                                current.right.up.elevation += strength
                                current.right.up.hot_spot = current.hot_spot * hot_spot_growth
                                current.right.elevation += .5 * strength
                                current.up.elevation += .5 * strength
                                current.hot_spot = 0
                            
                    self._cells[0][0].up.elevation = -150
                    

                
    def draw_elevation(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                current = self._cells[i][j]
                neighbor_terrain = [current.up.terrain, current.right.terrain, current.down.terrain, current.left.terrain]
                if TerrainType.OCEAN in neighbor_terrain:
                    if current.elevation <= 0:
                        current.terrain = TerrainType.OCEAN
                        blue = min(255, int(255+current.elevation))
                        if blue < 50:
                            blue = 50
                        color = rgb_to_hex((0, 0, blue ))
                    current.elevation -= 10
                if current.elevation > 0:
                    current.terrain = TerrainType.PLAINS
                if current.terrain != TerrainType.OCEAN:
                    hc = max(0, min(200, int(current.elevation)))
                    hcg = min(255, hc+50)
                    color = rgb_to_hex((hc,hcg,hc))
                self._draw_cell(i , j, color)
    def draw_terrain(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                current = self._cells[i][j]
                neighbor_terrain = [current.up.terrain, current.right.terrain, current.down.terrain, current.left.terrain]
                if TerrainType.OCEAN in neighbor_terrain:
                    if current.elevation <= 0:
                        current.terrain = TerrainType.OCEAN
                        blue = min(255, int(255+current.elevation))
                        if blue < 50:
                            blue = 50
                        color = rgb_to_hex((0, 0, blue ))
                    current.elevation -= 10
                if 0 < current.elevation < 75:
                    current.terrain = TerrainType.PLAINS
                    color = "green"
                if 75 <= current.elevation < 150:
                    current.terrain = TerrainType.FOREST
                    color = "dark green"
                if current.elevation >= 150:
                    current.terrain = TerrainType.MOUNTAIN
                    color = "dark gray"
                if current.terrain == TerrainType.DESERT:
                    color = "sand"
                if current.terrain == TerrainType.SWAMP:
                    color = "obsidian"
            #if current.terrain == TerrainType.
   
                self._draw_cell(i , j, color)





    


        
    



    