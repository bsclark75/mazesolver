from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.widget = Tk()
        self.widget.title = "Maze Solver"
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.width = width
        self.height = height

    def redraw(self):
        self.widget.update_idletasks()
        self.widget.update()

    def wait_for_close(self):
        pass