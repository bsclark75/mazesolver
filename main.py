from tkinter import Tk, BOTH, Canvas
from point import Point
from maze import Maze

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
    maze = Maze(Point(10,10),25,25,10,10,win)
    maze._break_entrance_and_exit()
    win.wait_for_close()


if __name__ == "__main__":
    main()
