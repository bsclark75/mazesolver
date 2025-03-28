from tkinter import Tk, BOTH, Canvas
from point import Point
from line import Line
from cell import Cell

class Window:
    def __init__(self, width, height):
        self.widget = Tk()
        self.widget.title("Maze Solver")
        self.canvas = Canvas(self.widget)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.width = width
        self.height = height
        self.widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.widget.update_idletasks()
        self.widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        self.widget.quit()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


def main():
    cells = []
    win = Window(800, 600)
    for i in range(10):
        p1 = Point(i *10, 10)
        p2 = Point(10 * (i + 1), 20)
        cells.append(Cell(win, p1, p2))
    for cell in cells:
        cell.draw()
    for i in range(len(cells) - 1):
        cells[i].draw_move(cells[i+1])
    win.wait_for_close()


if __name__ == "__main__":
    main()
