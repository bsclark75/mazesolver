from tkinter import Tk, BOTH, Canvas
from point import Point
from line import Line

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
    win = Window(800, 600)
    p1 = Point(10,10)
    p2 = Point(150,150)
    line1 = Line(p1,p2)
    win.draw_line(line1, 'black')
    win.wait_for_close()


if __name__ == "__main__":
    main()
