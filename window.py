import tkinter as tk
import time
import random
from plate import Plate
from cell import Line
class Window:
    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__root.title = ("Continent Generator")
        self.parameter_frame = tk.Frame(self.__root)
        self.parameter_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        self._canvas = tk.Canvas(self.__root, bg="white", height=height, width=width)
        self._canvas.pack(fill = tk.BOTH, expand = 1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.start_button = tk.Button(self.parameter_frame, text="Start", command=self.plate_creation)
        self.start_button.grid(row=0, column=6, padx=5, pady=5)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
    
    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color = "black", size = 2):
        line.draw(self._canvas, fill_color, size)
    
    def plate_creation(self):
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        cols = canvas_width // 10
        rows = canvas_height // 10
        plate = Plate(self, cols, rows, 0, 5)
    
    
    