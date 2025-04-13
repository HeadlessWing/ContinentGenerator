from window import *
from plate import *
from cell import *
def main():
    win = Window(1000, 1000)
    cell = Cell(win)

    cell.draw(3,3,503,503)
    print(cell._x1)
    print(cell._x2)
    cell.fill("green")
    #win._Window__canvas.create_line(250, 3, 250, 500, fill = "green", width = 500)
    
    win.wait_for_close()


if __name__ == "__main__":
    main()
