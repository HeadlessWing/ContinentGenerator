import random
class Plate:
    def __init__(self, window, size, lat, planet_size = 5):
        self._win = window
        self._size = size
        self._lat = lat
        self.planet_size = planet_size
        
        