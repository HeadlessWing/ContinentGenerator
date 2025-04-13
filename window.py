import tkinter as tk
import time
import random

class Window:
    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__root.title = ("Continent Generator")
        self.parameter_frame = tk.Frame(self.__root)
        self.parameter_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        self.__canvas = tk.Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill = tk.BOTH, expand = 1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


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
        line.draw(self.__canvas, fill_color, size)
    
    
    